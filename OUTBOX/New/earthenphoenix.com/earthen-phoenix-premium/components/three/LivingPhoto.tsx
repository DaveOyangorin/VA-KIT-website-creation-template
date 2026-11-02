'use client';
import { useEffect, useRef } from 'react';
import type { ServiceKey } from '@/lib/content';
import type { ImageName } from '@/lib/images';
import { asset } from '@/lib/site';
import { CARD_FS, CARD_VS, LINES_FS, LINES_VS, PHOTO_FS, PHOTO_VS, POINTS_FS, POINTS_VS } from '@/lib/gl/shaders';

/**
 * The living photograph: a session page's hero photo, lifted onto a curved 3D surface that acts out the session.
 * Reiki warms and lifts under hovering hands; Swedish glides an oil sheen down the length; lymph flows to the node;
 * deep tissue sinks in slowly; Thai presses on a beat; Sarga ripples under each footstep; the mountain breathes mist;
 * yoga breathes; readings turn the room to night under a turning zodiac wheel with three cards turning over; herbalism
 * steams while leaves fall. The cursor tilts the surface (and on the readings page, moves the lens of light).
 *
 * Decoration only: the <img> underneath stays the real hero (LCP, alt text, fallback). No WebGL -> nothing changes.
 * Rendering stops when the hero is off-screen, the tab is hidden or the visitor presses pause.
 */
const MODE: Record<ServiceKey, number> = { reiki: 0, swedish: 1, lymph: 2, deep: 3, thai: 4, sarga: 5, zen: 6, yoga: 7, astro: 8, herbs: 9 };
const COUNT: Record<ServiceKey, number> = { reiki: 260, swedish: 150, lymph: 640, deep: 300, thai: 320, sarga: 360, zen: 170, yoga: 380, astro: 1900, herbs: 70 };
const NX = 96, NY = 60, FOV = Math.PI / 6;

type M4 = Float32Array;
const mul = (a: M4, b: M4) => {
  const o = new Float32Array(16);
  for (let c = 0; c < 4; c++) for (let r = 0; r < 4; r++) {
    let s = 0;
    for (let k = 0; k < 4; k++) s += a[k * 4 + r] * b[c * 4 + k];
    o[c * 4 + r] = s;
  }
  return o;
};
const I = () => new Float32Array([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]);
const T = (x: number, y: number, z: number) => { const m = I(); m[12] = x; m[13] = y; m[14] = z; return m; };
const S = (s: number) => { const m = I(); m[0] = m[5] = m[10] = s; return m; };
const RX = (a: number) => { const m = I(), c = Math.cos(a), s = Math.sin(a); m[5] = c; m[6] = s; m[9] = -s; m[10] = c; return m; };
const RY = (a: number) => { const m = I(), c = Math.cos(a), s = Math.sin(a); m[0] = c; m[2] = -s; m[8] = s; m[10] = c; return m; };
const RZ = (a: number) => { const m = I(), c = Math.cos(a), s = Math.sin(a); m[0] = c; m[1] = s; m[4] = -s; m[5] = c; return m; };
const persp = (fovy: number, asp: number, n: number, f: number) => {
  const t = 1 / Math.tan(fovy / 2), m = new Float32Array(16);
  m[0] = t / asp; m[5] = t; m[10] = (f + n) / (n - f); m[11] = -1; m[14] = (2 * f * n) / (n - f);
  return m;
};
const rnd = (n: number) => { const x = Math.sin(n * 12.9898) * 43758.5453; return x - Math.floor(x); };
const ease = (x: number) => (x <= 0 ? 0 : x >= 1 ? 1 : x * x * (3 - 2 * x));

/* Three made-up star patterns for the readings sky (decorative, not real constellations): points, then edges. */
const SKY: [number, number][][] = [
  [[0.3, 0.83], [0.33, 0.87], [0.37, 0.85], [0.4, 0.89], [0.38, 0.81], [0.34, 0.8]],
  [[0.87, 0.8], [0.9, 0.84], [0.94, 0.82], [0.92, 0.88], [0.97, 0.9]],
  [[0.44, 0.08], [0.47, 0.13], [0.52, 0.11], [0.55, 0.15], [0.5, 0.05]],
];
const EDGES: [number, number][][] = [[[0, 1], [1, 2], [2, 3], [2, 4], [4, 5], [5, 0]], [[0, 1], [1, 2], [1, 3], [3, 4]], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]]];

function compile(gl: WebGLRenderingContext, vs: string, fs: string, defs = '') {
  const p = gl.createProgram()!;
  for (const [type, src] of [[gl.VERTEX_SHADER, defs + vs], [gl.FRAGMENT_SHADER, fs]] as const) {
    const s = gl.createShader(type)!;
    gl.shaderSource(s, src);
    gl.compileShader(s);
    if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s) || 'shader');
    gl.attachShader(p, s);
  }
  gl.linkProgram(p);
  if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p) || 'link');
  const u: Record<string, WebGLUniformLocation | null> = {};
  const n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
  for (let i = 0; i < n; i++) { const name = gl.getActiveUniform(p, i)!.name.replace('[0]', ''); u[name] = gl.getUniformLocation(p, name); }
  return { p, u };
}

/* The hero photo for the texture. In a sandboxed preview the page's own <img> can't be uploaded to WebGL
   (cross-origin), so there is an inline copy of the same photo shipped as a script (public/tex/<name>.js). */
const whenLoaded = (img: HTMLImageElement) =>
  img.complete && img.naturalWidth ? Promise.resolve(img) : new Promise<HTMLImageElement>((r) => img.addEventListener('load', () => r(img), { once: true }));
function inlineCopy(name: ImageName) {
  const w = window as unknown as { __EPTEX?: Record<string, string> };
  return new Promise<HTMLImageElement>((res, rej) => {
    const use = () => { const im = new Image(); im.onload = () => res(im); im.onerror = rej; im.src = w.__EPTEX![name]; };
    if (w.__EPTEX?.[name]) return use();
    const s = document.createElement('script');
    s.src = asset(`/tex/${name}.js`);
    s.onload = use; s.onerror = rej;
    document.head.appendChild(s);
  });
}

export default function LivingPhoto({ k, img, pos = '50% 50%', paused = false }: { k: ServiceKey; img: ImageName; pos?: string; paused?: boolean }) {
  const ref = useRef<HTMLCanvasElement>(null);
  const pausedRef = useRef(paused);
  const kick = useRef<() => void>(() => {});
  useEffect(() => { pausedRef.current = paused; kick.current(); }, [paused]);

  useEffect(() => {
    const cv = ref.current!;
    const photo = cv.parentElement!.querySelector('img');
    const gl = cv.getContext('webgl', { antialias: true, alpha: false, powerPreference: 'high-performance' });
    if (!gl || !photo) return;
    const mode = MODE[k];
    let dead = false, raf = 0;
    const stats = ((window as unknown as { __lp?: Record<string, unknown> }).__lp = { k, state: 'init', frames: 0, fps: 0, tex: '' });

    let progs: { photo: ReturnType<typeof compile>; pts: ReturnType<typeof compile>; lines: ReturnType<typeof compile>; card: ReturnType<typeof compile> };
    try {
      const vtf = (gl.getParameter(gl.MAX_VERTEX_TEXTURE_IMAGE_UNITS) as number) > 0;
      progs = {
        photo: compile(gl, PHOTO_VS, PHOTO_FS, vtf ? '#define VTF\n' : ''),
        pts: compile(gl, POINTS_VS, POINTS_FS),
        lines: compile(gl, LINES_VS, LINES_FS),
        card: compile(gl, CARD_VS, CARD_FS),
      };
    } catch (e) {
      stats.state = 'shader-error: ' + String(e).slice(0, 300);
      return;
    }

    /* geometry */
    const grid = new Float32Array((NX + 1) * (NY + 1) * 2);
    for (let y = 0, i = 0; y <= NY; y++) for (let x = 0; x <= NX; x++) { grid[i++] = x / NX; grid[i++] = y / NY; }
    const idx = new Uint16Array(NX * NY * 6);
    for (let y = 0, i = 0; y < NY; y++) for (let x = 0; x < NX; x++) {
      const a = y * (NX + 1) + x, b = a + 1, c = a + NX + 1, d = c + 1;
      idx.set([a, b, d, a, d, c], i); i += 6;
    }
    const buf = (data: BufferSource, target: number = gl.ARRAY_BUFFER) => { const b = gl.createBuffer(); gl.bindBuffer(target, b); gl.bufferData(target, data, gl.STATIC_DRAW); return b; };
    const gridBuf = buf(grid), idxBuf = buf(idx, gl.ELEMENT_ARRAY_BUFFER);

    const portrait = () => cv.clientWidth < cv.clientHeight * 0.9;
    // where the session plays out: right of the words on wide screens, above them on phones
    const focus = () => (portrait() ? { x: 0.58, y: 0.8, s: 0.62 } : { x: 0.73, y: 0.52, s: 1 });
    const deck = () => (portrait() ? { x: 0.62, y: 0.8, h: 0.27, gap: 0.14 } : { x: 0.8, y: 0.53, h: 0.5, gap: 0.075 });
    const place = (p: [number, number], f = focus()) => [f.x + (p[0] - 0.73) * f.s, f.y + (p[1] - 0.52) * f.s] as [number, number];

    let n = COUNT[k];
    const ptsBuf = gl.createBuffer();
    const linesBuf = gl.createBuffer();
    let lineCount = 0;
    const buildPoints = () => {
      const extra = mode === 8 ? SKY.flat().length : 0;
      const a = new Float32Array((n + extra) * 4);
      for (let i = 0; i < n * 4; i++) a[i] = Math.random();
      if (mode === 8) {
        let j = n * 4;
        for (const [x, y] of SKY.flat()) { a.set([x, y, 0, 2], j); j += 4; }
        const L: number[] = [], total = EDGES.flat().length;
        let o = 0;
        SKY.forEach((s, si) => EDGES[si].forEach(([u, v]) => {
          const [x0, y0] = s[u], [x1, y1] = s[v];
          L.push(x0, y0, o / total, x1, y1, (o + 1) / total); o++;
        }));
        gl.bindBuffer(gl.ARRAY_BUFFER, linesBuf); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(L), gl.STATIC_DRAW);
        lineCount = L.length / 3;
      }
      gl.bindBuffer(gl.ARRAY_BUFFER, ptsBuf); gl.bufferData(gl.ARRAY_BUFFER, a, gl.STATIC_DRAW);
    };
    const cardBuf = buf(new Float32Array([-0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5]));

    /* texture */
    const tex = gl.createTexture();
    let texW = 1, texH = 1, haveTex = false;
    const [px, py] = pos.split(' ').map((v) => parseFloat(v) / 100);
    const upload = (src: HTMLImageElement) => {
      gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, true);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, src);
      for (const [p, v] of [[gl.TEXTURE_MIN_FILTER, gl.LINEAR], [gl.TEXTURE_MAG_FILTER, gl.LINEAR], [gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE], [gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE]]) gl.texParameteri(gl.TEXTURE_2D, p, v);
      texW = src.naturalWidth; texH = src.naturalHeight;
      haveTex = true;
      stats.tex = src === photo ? 'direct' : 'inline';
      kick.current();
    };
    whenLoaded(photo)
      .then((im) => { if (dead) return; try { upload(im); } catch { return inlineCopy(img).then((c) => { if (!dead) upload(c); }); } })
      .catch(() => { stats.state = 'no-texture'; });

    /* size */
    let dpr = Math.min(window.devicePixelRatio || 1, portrait() ? 1.5 : 1.75);
    let W = 1, H = 1;
    const resize = () => {
      W = Math.max(1, Math.round(cv.clientWidth * dpr)); H = Math.max(1, Math.round(cv.clientHeight * dpr));
      if (cv.width !== W || cv.height !== H) { cv.width = W; cv.height = H; buildPoints(); }
      kick.current();
    };
    const ro = new ResizeObserver(resize);
    ro.observe(cv);

    /* input */
    const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
    const ptr = { x: 0.5, y: 0.5, at: -1e9 };
    const onMove = (e: PointerEvent) => {
      const r = cv.getBoundingClientRect();
      if (e.clientY > r.bottom || e.clientY < r.top) return;
      ptr.x = (e.clientX - r.left) / r.width; ptr.y = 1 - (e.clientY - r.top) / r.height; ptr.at = performance.now();
    };
    window.addEventListener('pointermove', onMove, { passive: true });

    let inView = true;
    const io = new IntersectionObserver(([e]) => { inView = e.isIntersecting; kick.current(); });
    io.observe(cv);
    const onVis = () => kick.current();
    document.addEventListener('visibilitychange', onVis);
    const onLost = (e: Event) => { e.preventDefault(); dead = true; cancelAnimationFrame(raf); cv.style.opacity = '0'; };
    cv.addEventListener('webglcontextlost', onLost);

    /* per-session points of action, in plane space (x, y, strength or age) */
    const P = new Float32Array(12);
    const action = (t: number) => {
      const f = focus(), q = (x: number, y: number) => place([x, y], f);
      P.fill(0);
      if (mode === 0) {          // two hands hovering head to heart to belly and back
        for (let i = 0; i < 2; i++) {
          const a = t * 0.22 + i * 2.2;
          const [x, y] = q(0.73 + 0.15 * Math.sin(a), 0.52 + 0.11 * Math.sin(a * 2));
          P.set([x, y, 0.75 + 0.25 * Math.sin(t * 1.3 + i)], i * 3);
        }
      } else if (mode === 1) {   // the glide crosses every 7s; an oil drop lands every 3.5s
        P[0] = ((t / 7) % 1) * 1.4 - 0.2;
        const c = Math.floor(t / 3.5), [x, y] = q(0.6 + rnd(c) * 0.3, 0.4 + rnd(c + 9) * 0.3);
        P.set([x, y, t - c * 3.5], 3);
      } else if (mode === 2) {
        const [x, y] = q(0.8, 0.72);
        P.set([x, y, 0.5 + 0.5 * Math.sin(t * 1.6)], 0);
      } else if (mode === 3) {   // pressure sinks in and releases at three spots in turn
        const spots: [number, number][] = [[0.62, 0.45], [0.76, 0.56], [0.88, 0.43]];
        spots.forEach((s, i) => {
          const ph = (((t / 3.4 - i) % 3) + 3) % 3;
          const [x, y] = q(...s);
          P.set([x, y, ph < 1 ? Math.sin(Math.PI * ph) ** 2 : 0], i * 3);
        });
      } else if (mode === 4) {   // left, right, left, right
        const [lx, ly] = q(0.65, 0.5), [rx, ry] = q(0.84, 0.52);
        P.set([lx, ly, t % 1.8, rx, ry, (t + 0.9) % 1.8], 0);
      } else if (mode === 5) {   // footsteps walking along the back, alternating feet
        const n0 = Math.floor(t / 1.2);
        for (let j = n0 - 3; j <= n0; j++) {
          const m = ((j % 8) + 8) % 8, [x, y] = q(0.5 + m * 0.06, 0.48 + (j % 2 ? 0.045 : -0.045));
          P.set([x, y, j < 0 ? -1 : t - j * 1.2], (((j % 4) + 4) % 4) * 3);
        }
      } else if (mode === 6) {   // the sun climbs over 24s
        const u = (t % 24) / 24;
        P.set([0.8, 0.55 + 0.3 * Math.sin(u * Math.PI), 1], 0);
      } else if (mode === 7) {   // four counts in, four counts out
        const [x, y] = q(0.73, 0.52);
        P.set([x, y, 0.5 - 0.5 * Math.cos((t / 8) * Math.PI * 2)], 0);
      } else if (mode === 8) {
        const d = deck();
        P.set([d.x, d.y, portrait() ? 0.42 : 0.6], 9);
      }
      return P;
    };

    /* time and camera */
    let t = 0, last = performance.now(), shown = false, slow = 0, frames = 0;
    const tilt = { x: 0, y: 0 }, lens = { x: 0.7, y: 0.5 };
    const section = cv.closest('section') ?? cv;

    const frame = (now: number) => {
      raf = 0;
      const running = !pausedRef.current && inView && !document.hidden;
      const dt = Math.min(0.05, (now - last) / 1000);
      last = now;
      if (running) t += dt;
      if (running && frames < 120) { frames++; slow += dt > 0.034 ? 1 : 0; if (frames === 120 && slow > 50 && dpr > 1) { dpr = 1; n = Math.round(n * 0.55); resize(); } }
      stats.frames++;
      if (!haveTex) { if (running) raf = requestAnimationFrame(frame); return; }

      const asp = W / H;
      const r = section.getBoundingClientRect();
      const pr = Math.max(0, Math.min(1, -r.top / Math.max(1, r.height)));
      const live = fine && now - ptr.at < 4000;
      const tx = live ? -(ptr.y - 0.5) * 0.08 : Math.sin(t * 0.17) * 0.025;
      const ty = live ? (ptr.x - 0.5) * 0.12 : Math.sin(t * 0.23) * 0.04;
      tilt.x += (tx - tilt.x) * 0.06; tilt.y += (ty - tilt.y) * 0.06;
      const auto = mode === 8 ? { x: 0.5 + 0.2 * Math.sin(t * 0.27), y: 0.5 + 0.2 * Math.sin(t * 0.19) } : { x: 0.5, y: 0.5 };
      const lt = live && mode === 8 ? { x: ptr.x, y: ptr.y } : auto;
      lens.x += (lt.x - lens.x) * 0.08; lens.y += (lt.y - lens.y) * 0.08;

      const D = 1 / Math.tan(FOV / 2);
      const proj = persp(FOV, asp, 0.1, 50);
      const PV = mul(proj, T(0, 0, -(D + pr * 0.8)));
      const Mdl = mul(RX(tilt.x + pr * 0.22), RY(tilt.y));
      const sizeX = 2 * asp * 1.1, sizeY = 2 * 1.1;
      const pa = sizeX / sizeY, ta = texW / texH;
      const cover = pa > ta ? [1, ta / pa, 0, 0] : [pa / ta, 1, 0, 0];
      cover[2] = (1 - cover[0]) * px; cover[3] = (1 - cover[1]) * (1 - py);
      const Pt = action(t);

      gl.viewport(0, 0, W, H);
      gl.disable(gl.DEPTH_TEST);
      gl.disable(gl.BLEND);

      const common = (u: Record<string, WebGLUniformLocation | null>) => {
        gl.uniformMatrix4fv(u.uPV, false, PV); gl.uniformMatrix4fv(u.uM, false, Mdl);
        if (u.uSize) gl.uniform2f(u.uSize, sizeX, sizeY);
        if (u.uT) gl.uniform1f(u.uT, t);
        if (u.uMode) gl.uniform1f(u.uMode, mode);
        if (u.uAsp) gl.uniform1f(u.uAsp, pa);
        if (u.uP) gl.uniform3fv(u.uP, Pt);
      };
      const attr = (p: WebGLProgram, name: string, b: WebGLBuffer | null, size: number) => {
        const l = gl.getAttribLocation(p, name);
        gl.bindBuffer(gl.ARRAY_BUFFER, b); gl.enableVertexAttribArray(l); gl.vertexAttribPointer(l, size, gl.FLOAT, false, 0, 0);
        return l;
      };

      // the photograph
      { const { p, u } = progs.photo; gl.useProgram(p); common(u);
        gl.uniform1f(u.uBend, 0.12); gl.uniform1f(u.uRelief, mode === 6 ? 0.06 : 0.03);
        gl.uniform4fv(u.uCover, cover); gl.uniform2f(u.uLens, lens.x, lens.y);
        gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, tex); gl.uniform1i(u.uTex, 0);
        const l = attr(p, 'aPos', gridBuf, 2);
        gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, idxBuf);
        gl.drawElements(gl.TRIANGLES, idx.length, gl.UNSIGNED_SHORT, 0);
        gl.disableVertexAttribArray(l); }

      gl.enable(gl.BLEND);
      gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);

      // what moves in it
      { const { p, u } = progs.pts; gl.useProgram(p); common(u);
        gl.uniform1f(u.uPx, (proj[5] * H) / 2);
        const l = attr(p, 'aS', ptsBuf, 4);
        gl.drawArrays(gl.POINTS, 0, n + (mode === 8 ? SKY.flat().length : 0));
        gl.disableVertexAttribArray(l); }

      if (mode === 8) {
        // the constellations draw themselves in, hold, and fade (16s)
        const c = (t % 16) / 16;
        { const { p, u } = progs.lines; gl.useProgram(p); common(u);
          gl.uniform1f(u.uProg, ease(c / 0.45)); gl.uniform1f(u.uFade, c < 0.85 ? 1 : 1 - ease((c - 0.85) / 0.15));
          const l = attr(p, 'aL', linesBuf, 3);
          gl.drawArrays(gl.LINES, 0, lineCount);
          gl.disableVertexAttribArray(l); }
        // three cards, dealt face down, turned over one by one (sun, moon, star), then gathered back (14s)
        { const { p, u } = progs.card; gl.useProgram(p); common(u);
          const l = attr(p, 'aQ', cardBuf, 2);
          const d = deck(), cyc = t % 14;
          for (let i = 0; i < 3; i++) {
            const turn = ease((cyc - 1.6 - i * 1.3) / 1.1) * (1 - ease((cyc - 11 - i * 0.25) / 0.9));
            const [x, y] = [d.x + (i - 1) * d.gap, d.y - 0.01 + Math.sin(t * 0.8 + i * 2) * 0.01];
            const deal = ease((t - 0.3 - i * 0.25) / 0.9);
            const C = mul(mul(mul(T((x - 0.5) * sizeX, (y - 0.5) * sizeY - (1 - deal) * 0.6, 0.35 + i * 0.01 + turn * 0.12), RY(Math.PI * (1 - turn))), RZ((i - 1) * -0.12)), S(d.h));
            gl.uniformMatrix4fv(u.uC, false, C);
            gl.uniform1f(u.uSym, i); gl.uniform1f(u.uA, deal); gl.uniform1f(u.uLit, 0.82 + 0.18 * Math.abs(Math.cos(Math.PI * (1 - turn))));
            gl.drawArrays(gl.TRIANGLES, 0, 6);
          }
          gl.disableVertexAttribArray(l); }
      }

      if (!shown) { shown = true; cv.style.opacity = '1'; stats.state = 'running'; }
      stats.fps = dt ? Math.round(1 / dt) : 0;
      if (running) raf = requestAnimationFrame(frame);
    };
    kick.current = () => { if (!dead && !raf) { last = performance.now(); raf = requestAnimationFrame(frame); } };
    resize();

    return () => {
      dead = true; cancelAnimationFrame(raf); kick.current = () => {};
      ro.disconnect(); io.disconnect();
      window.removeEventListener('pointermove', onMove);
      document.removeEventListener('visibilitychange', onVis);
      cv.removeEventListener('webglcontextlost', onLost);
      gl.getExtension('WEBGL_lose_context')?.loseContext();
    };
  }, [k, img, pos]);

  return <canvas ref={ref} aria-hidden className="absolute inset-0 h-full w-full opacity-0 transition-opacity duration-[1400ms] ease-out" />;
}
