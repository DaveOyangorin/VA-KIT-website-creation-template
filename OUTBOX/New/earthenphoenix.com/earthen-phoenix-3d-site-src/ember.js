/*
 * Earthen Phoenix: the ember engine shared by every page.
 * One cloud of glowing particles on a fixed canvas. Each <section data-shape="..."> names the
 * shape the embers take while it is on screen; scrolling between sections reshapes them.
 * Text, menus and entrances work without WebGL; the canvas is only decoration.
 */
import * as THREE from 'three';

const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const small = () => innerWidth <= 900;
gsap.registerPlugin(ScrollTrigger);

/* ---------- chrome: header, menu, entrances ---------- */
const header = document.querySelector('.hdr');
ScrollTrigger.create({ start: 30, onUpdate: (s) => header.classList.toggle('solid', s.scroll() > 30) });
header.classList.toggle('solid', scrollY > 30);

const menuBtn = document.querySelector('.menu-btn'), menu = document.getElementById('menu');
const setMenu = (open) => {
  document.documentElement.classList.toggle('menu-open', open);
  menuBtn.setAttribute('aria-expanded', String(open));
  menu.hidden = !open;
  if (open) menu.querySelector('a')?.focus();
};
menuBtn.addEventListener('click', () => setMenu(menuBtn.getAttribute('aria-expanded') !== 'true'));
menu.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });
addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { setMenu(false); menuBtn.focus(); } });
addEventListener('resize', () => { if (!small() && !menu.hidden) setMenu(false); });

const sections = [...document.querySelectorAll('main > section')];
const dots = [...document.querySelectorAll('.progress a')];
sections.forEach((s, i) => ScrollTrigger.create({ trigger: s, start: 'top 55%', end: 'bottom 55%', onToggle: (e) => e.isActive && dots.forEach((d, j) => d.classList.toggle('on', i === j)) }));

if (reduce) {
  gsap.set('.rv', { opacity: 1, y: 0 });
} else {
  const first = sections[0];
  gsap.from(first.querySelectorAll('h1 .ln > span'), { yPercent: 110, duration: 1.4, ease: 'expo.out', stagger: .12, delay: .3 });
  gsap.to(first.querySelectorAll('.rv'), { opacity: 1, y: 0, duration: 1.2, ease: 'expo.out', stagger: .08, delay: .6 });
  sections.slice(1).forEach((s) => {
    gsap.to(s.querySelectorAll('.rv'), { opacity: 1, y: 0, duration: 1.1, ease: 'expo.out', stagger: .07,
      scrollTrigger: { trigger: s, start: 'top 72%', toggleActions: 'play none none reverse' } });
  });
  document.querySelectorAll('.photo').forEach((p) => gsap.fromTo(p, { clipPath: 'inset(18% 18% 18% 18% round 28px)' }, { clipPath: 'inset(0% 0% 0% 0% round 22px)', ease: 'none',
    scrollTrigger: { trigger: p, start: 'top 95%', end: 'top 40%', scrub: true } }));
}

/* ---------- shapes: each returns [x, y, z, shade] ---------- */
let seed = 11;
const R = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
const TAU = Math.PI * 2;
const ball = (r) => { const a = R() * TAU, b = Math.acos(2 * R() - 1), q = r * Math.cbrt(R()); return [q * Math.sin(b) * Math.cos(a), q * Math.cos(b), q * Math.sin(b) * Math.sin(a)]; };
const LAYER_Y = [1, .5, 0, -.5, -1];

const GEN = {
  phoenix() {                   // the logo's bird: raised wings, crest, a tail of flame
    const k = R();
    if (k < .52) {
      const s = R() < .5 ? -1 : 1, fea = R() < .82;
      let u = R(); if (fea) u = (Math.floor(u * 26) + .5) / 26;
      const ex = s * (.16 + 2.1 * u), ey = .5 + 1.6 * u - .45 * u * u, a = .12 + .8 * u, L = .45 + Math.pow(u, .8);
      const v = fea ? Math.pow(R(), .85) : R() * .3, j = (R() - .5) * .025 * (1 - v);
      return [ex + s * Math.sin(a) * L * v + j, ey - Math.cos(a) * L * v + j, -.35 * u * u - .12 * v + (R() - .5) * .05, .25 + .75 * u * (1 - .45 * v)];
    }
    if (k < .58) { const [x, y, z] = ball(1); return [x * .15, .2 + y * .5, z * .13, .75]; }
    if (k < .64) {
      const q = R();
      if (q < .45) { const [x, y, z] = ball(.1); return [x, .9 + y, z, .95]; }
      if (q < .58) { const t = R(); return [.08 + .14 * t, .9 - .05 * t, 0, .95]; }
      const c = Math.floor(R() * 3), t = R();
      return [-.04 - (.18 + c * .05) * t, .96 + (.32 - c * .06) * t + .08 * Math.sin(t * 3), (R() - .5) * .02, 1];
    }
    if (k < .92) {
      const j = Math.floor(R() * 7) - 3, t = Math.pow(R(), .8);
      return [j * .2 * t + .18 * Math.sin(t * 4.2 + j) * t + j * .12 * t * t * t + (R() - .5) * .07 * (1 - .5 * t), -.25 - 1.75 * t, .15 * Math.sin(t * 3 + j * 1.3), .7 - .65 * t];
    }
    return [(R() - .5) * 5.4, (R() - .5) * 4.6, (R() - .5) * 2, R() * .6];
  },
  reiki() {                     // energy held near, never touching
    const k = R();
    if (k < .58) { const a = R() * TAU, y = 1 - 2 * R(), r = Math.sqrt(1 - y * y), d = 1.05 + (R() - .5) * .08; return [Math.cos(a) * r * d, y * d, Math.sin(a) * r * d, .35 + .4 * (y * .5 + .5)]; }
    if (k < .74) { const [x, y, z] = ball(.42); return [x, y, z, 1]; }
    const a = R() * TAU, b = Math.acos(2 * R() - 1), r = 1.18 + Math.abs((R() + R() + R()) / 3 - .5) * 1.4;
    return [r * Math.sin(b) * Math.cos(a), r * Math.cos(b), r * Math.sin(b) * Math.sin(a), k < .9 ? .5 : .2];
  },
  swedish() {                   // long, slow strokes
    const n = 13, j = Math.floor(R() * n), x = -2.8 + 5.6 * (R() + R() + R()) / 3;
    const y = (j - (n - 1) / 2) * .13 + .42 * Math.sin(x * .85 + j * .33) * (.65 + .35 * Math.cos(j * .7));
    return [x, y + (R() - .5) * .02, .5 * Math.cos(x * .7 + j * .45) + (j - n / 2) * .03, j / (n - 1)];
  },
  lymph() {                     // streams that flow in to one node
    const k = R(), N = [0, .7, 0];
    if (k < .78) {
      const j = Math.floor(R() * 11), a = -Math.PI * .1 - j / 10 * Math.PI * 1.2, t = R();
      const sx = Math.cos(a) * 2.4, sy = Math.sin(a) * 1.9 + .2, bow = .35 * Math.sin(Math.PI * t) * (j % 2 ? 1 : -1);
      const x = sx + (N[0] - sx) * t, y = sy + (N[1] - sy) * t, dx = N[0] - sx, dy = N[1] - sy, l = Math.hypot(dx, dy);
      return [x - dy / l * bow + (R() - .5) * .03, y + dx / l * bow + (R() - .5) * .03, (R() - .5) * .25 * (1 - t), .2 + .7 * t];
    }
    if (k < .9) { const [x, y, z] = ball(.24); return [x, N[1] + y, z, 1]; }
    const [x, y, z] = ball(.6); return [x, N[1] + y, z, .55];
  },
  deep() {                      // layers, pressed on a beat
    const i = Math.floor(R() * 5);
    let x = R() * 3.2 - 1.6, z = R() * 2 - 1;
    if (i % 2) z = Math.round(z * 7) / 7 + .03 * Math.sin(x * 6 + i);
    else if (i === 2) x = Math.round(x * 9) / 9 + .03 * Math.sin(z * 6);
    return [x, LAYER_Y[i] + (R() - .5) * .02, z, 1 - i / 4];
  },
  thai() {                      // a woven sheet: pressed in rhythm, then drawn long
    let x = R() * 4 - 2, z = R() * 2.4 - 1.2;
    if (R() < .5) x = Math.round(x * 3.5) / 3.5; else z = Math.round(z * 5) / 5;
    return [x, .18 * Math.sin(x * 2) * Math.cos(z * 2) + (R() - .5) * .015, z, (x + 2) / 4];
  },
  sarga() {                     // full weight into one point, a strap overhead
    const k = R();
    if (k < .86) { const z = Math.round((R() * 4 - 2) * 9) / 9, x = R() * 4 - 2, r2 = x * x + z * z;
      const y = -.7 - 1.05 * Math.exp(-r2 / .42) + .05 * Math.sin(Math.sqrt(r2) * 9) * Math.exp(-r2 * .5);
      return [x, y, z, Math.min(1, .15 + (-.7 - y) * .9)]; }
    if (k < .93) return [(R() - .5) * 1.8, 1.55 + (R() - .5) * .03, (R() - .5) * .03, .9];
    const s = R() < .5 ? -1 : 1, t = R();
    return [s * (.62 - .45 * t), 1.55 - 1.1 * t, 0, .7];
  },
  zen() {                       // peaks, a river, a few stars
    const k = R();
    const P = [[-1.7, -.6, 1.5, .55], [-.5, -.9, 1.95, .5], [.8, -.7, 1.45, .6], [2.0, -.5, 1.05, .5], [-2.7, -.3, .8, .5]];
    const h = (x, z) => P.reduce((s, [px, pz, ph, w]) => s + ph * Math.exp(-((x - px) ** 2 + (z - pz) ** 2) / w), 0) + .12 * Math.sin(x * 3.1 + z * 2) * Math.sin(x * 1.7 - z * 2.3);
    if (k < .82) { const x = R() * 6 - 3, z = Math.round((R() * 3 - 1.5) * 10) / 10, y = Math.max(0, h(x, z)); return [x, y - 1, z, Math.min(1, y / 1.7)]; }
    if (k < .97) { const x = R() * 6 - 3; return [x, -.98, .75 + .25 * Math.sin(x * 1.3) + (R() - .5) * .06, 2]; }
    const a = R() * Math.PI, rr = 3.2 + R() * .8; return [Math.cos(a) * rr, -1 + Math.sin(a) * rr * .8, -2 - R() * 1.5, .95];
  },
  yoga() {                      // flow, then hold: one unbroken line of breath
    const k = R(), t = R() * TAU, d = 1 + Math.sin(t) ** 2;
    if (k < .85) { const r = .07 * Math.sqrt(R()), a = R() * TAU;
      return [2.1 * Math.cos(t) / d + r * Math.cos(a), 1.5 * Math.sin(t) * Math.cos(t) / d + r * Math.sin(a), .45 * Math.sin(t) + (R() - .5) * .05, .5 + .5 * Math.cos(t)]; }
    const [x, y, z] = ball(2.6); return [x, y * .7, z * .5, .3];
  },
  astro() {                     // a zodiac ring, a star pattern, three cards
    const k = R();
    if (k < .3) { const a = R() * TAU, r = 1.72 + (R() - .5) * .03; return [Math.cos(a) * r, Math.sin(a) * r, 0, .7]; }
    if (k < .4) { const a = Math.floor(R() * 12) / 12 * TAU, r = 1.55 + R() * .3; return [Math.cos(a) * r, Math.sin(a) * r, 0, .95]; }
    if (k < .55) { const S = [[-.9, .95], [-.45, 1.15], [0, 1.05], [.4, 1.25], [.85, 1.0], [1.1, .7], [-1.15, .55]];
      const i = Math.floor(R() * (S.length - 1)), t = R() < .3 ? 0 : R(), [ax, ay] = S[i], [bx, by] = S[i + 1];
      return t === 0 ? [ax + (R() - .5) * .05, ay + (R() - .5) * .05, 0, 1] : [ax + (bx - ax) * t, ay + (by - ay) * t, 0, .45]; }
    if (k < .92) { const c = Math.floor(R() * 3) - 1, w = .36, h = .58;
      let u = R() * 2 - 1, v = R() * 2 - 1; if (R() < .7) { if (R() < .5) u = Math.sign(u); else v = Math.sign(v); }
      const rot = -c * .22, px = u * w, py = v * h;
      return [c * .82 + px * Math.cos(rot) - py * Math.sin(rot), -.35 + px * Math.sin(rot) + py * Math.cos(rot) - Math.abs(c) * .08, c * .1, .35 + .3 * (v * .5 + .5)]; }
    const [x, y, z] = ball(2.4); return [x, y, z * .4 - .6, .9];
  },
  herbs() {                     // a sprig, leaf by leaf, and a dropper's slow drops
    const k = R(), stem = (t) => [.25 * Math.sin(t * 2.2), -1.9 + 3.6 * t, 0];
    if (k < .14) { const t = R(), [x, y, z] = stem(t); return [x + (R() - .5) * .025, y, z, .3]; }
    if (k < .9) {
      const i = Math.floor(R() * 9), s = i % 2 ? 1 : -1, t0 = .12 + i * .095, [bx, by] = stem(t0);
      const L = .95 - i * .06, a = s * (.95 - i * .04), u = R(), half = .22 * Math.sin(Math.PI * u) * L;
      const edge = R() < .6, w = edge ? (R() < .5 ? 1 : -1) * half : (R() < .3 ? 0 : (R() * 2 - 1) * half);
      const lx = u * L, ly = w, ca = Math.cos(a), sa = Math.sin(a);
      return [bx + lx * sa - ly * ca * s, by + lx * ca * .6 + ly * sa * s * .6 + u * .2, (R() - .5) * .04 + .15 * u * s, .25 + .7 * u];
    }
    const [x, y, z] = ball(.07); return [1.6 + x, -1.6 + Math.floor(R() * 6) * .53 + y * (1 + Math.max(0, y) * 6), z, 1.6];
  },
  bottle() {                    // the shelf: an amber dropper bottle
    const k = R();
    const prof = (y) => y < -1.3 ? .55 + .15 * Math.sqrt(Math.max(0, 1 - ((y + 1.3) / .1) ** 2)) : y < .2 ? .7 : y < .55 ? .7 - .45 * ((y - .2) / .35) : y < .9 ? .25 : y < 1.0 ? .3 : .21 * Math.sqrt(Math.max(0, 1 - ((y - 1.3) / .4) ** 2)) + .02;
    if (k < .8) { const y = -1.4 + R() * 3.1, a = R() * TAU, r = prof(y); const cap = y > .9; return [Math.cos(a) * r, y, Math.sin(a) * r, cap ? .2 : .45 + .3 * Math.max(0, Math.cos(a - 1))]; }
    if (k < .95) { const y = -1.35 + R() * 1.1, a = R() * TAU, r = .62 * Math.sqrt(R()); return [Math.cos(a) * r, y, Math.sin(a) * r, 1]; }
    const [x, y, z] = ball(2.4); return [x, y, z * .5, .5];
  },
  field() {                     // a slow drift of embers behind long reading
    return [(R() - .5) * 14, (R() - .5) * 7, -6 + R() * 7.5, R()];
  },
};
/* colours (lo, hi), motion, size, brightness, how the shape sits by default */
const LOOK = {
  phoenix: { lo: [.82, .22, .12], hi: [.98, .72, .25], anim: 0, sz: 1, al: .5, sc: .74, rx: .05, ry: -.22 },
  reiki:   { lo: [.92, .45, .18], hi: [1, .85, .55], anim: 1, sz: 1, al: .5, sc: 1, rx: .2, ry: .3 },
  swedish: { lo: [.92, .6, .52], hi: [.93, .46, .18], anim: 2, sz: .9, al: .55, sc: .6, rx: .35, ry: -.35 },
  lymph:   { lo: [.92, .55, .4], hi: [1, .86, .6], anim: 7, sz: .95, al: .5, sc: .78, rx: .1, ry: -.25 },
  deep:    { lo: [.8, .22, .14], hi: [.96, .7, .26], anim: 3, sz: .9, al: .5, sc: .72, rx: .42, ry: .45 },
  thai:    { lo: [.36, .62, .32], hi: [.97, .72, .28], anim: 8, sz: .9, al: .55, sc: .72, rx: .55, ry: -.4 },
  sarga:   { lo: [.62, .34, .22], hi: [.95, .55, .22], anim: 4, sz: .9, al: .5, sc: .78, rx: .5, ry: -.5 },
  zen:     { lo: [.3, .5, .28], hi: [.9, .93, .82], anim: 5, sz: .85, al: .55, sc: .55, rx: .28, ry: .2 },
  yoga:    { lo: [.92, .55, .45], hi: [.98, .74, .3], anim: 9, sz: .95, al: .5, sc: .72, rx: .25, ry: .3 },
  astro:   { lo: [.9, .5, .3], hi: [1, .9, .7], anim: 10, sz: .95, al: .5, sc: .8, rx: .1, ry: -.2 },
  herbs:   { lo: [.3, .55, .28], hi: [.78, .9, .55], anim: 11, sz: .95, al: .55, sc: .72, rx: .05, ry: -.3 },
  bottle:  { lo: [.7, .32, .1], hi: [1, .78, .42], anim: 1, sz: .95, al: .5, sc: .82, rx: .12, ry: 0 },
  field:   { lo: [.75, .25, .12], hi: [.98, .7, .3], anim: 6, sz: 1.5, al: .3, sc: 1, rx: 0, ry: 0 },
};
/* where the shape sits for a section: x, y, camera distance, scale factor */
const POSE = {
  right: { x: 1.62, y: -.05, z: 8, k: 1 },
  left: { x: -1.62, y: 0, z: 8, k: 1, flip: true },
  'left-near': { x: -1.5, y: 0, z: 7.2, k: 1.08, flip: true },
  'right-near': { x: 1.5, y: 0, z: 7.2, k: 1.08 },
  top: { x: 0, y: 1.12, z: 8.6, k: .62 },
  bg: { x: 0, y: 0, z: 7, k: 1 },
};

/* ---------- renderer ---------- */
const canvas = document.getElementById('stage');
let renderer;
try { renderer = new THREE.WebGLRenderer({ canvas, antialias: false, alpha: false, powerPreference: 'high-performance' }); }
catch (e) { canvas.remove(); throw e; }
const PR = Math.min(devicePixelRatio, 2);
renderer.setPixelRatio(PR);
renderer.setClearColor(0x000000, 1);
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100);
camera.position.z = 8;

const chapters = sections.map((s) => ({ shape: s.dataset.shape in GEN ? s.dataset.shape : 'field', pose: POSE[s.dataset.pose] ? s.dataset.pose : 'bg', el: s }));
const used = [...new Set(chapters.map((c) => c.shape))].slice(0, 7);
chapters.forEach((c) => { c.slot = Math.max(0, used.indexOf(c.shape)); });

const N = small() ? 11000 : 20000;
const geo = new THREE.BufferGeometry();
const shades = [new Float32Array(N * 4), new Float32Array(N * 4)];
let first;
used.forEach((name, si) => {
  const pos = new Float32Array(N * 3);
  for (let i = 0; i < N; i++) { const [x, y, z, s] = GEN[name](); pos[i * 3] = x; pos[i * 3 + 1] = y; pos[i * 3 + 2] = z; shades[si >> 2][i * 4 + (si & 3)] = s; }
  const at = new THREE.BufferAttribute(pos, 3);
  if (!si) first = at;
  geo.setAttribute(si ? 'p' + si : 'position', at);
});
for (let si = used.length; si < 7; si++) geo.setAttribute('p' + si, first);
geo.setAttribute('sh0', new THREE.BufferAttribute(shades[0], 4));
geo.setAttribute('sh1', new THREE.BufferAttribute(shades[1], 4));
const rnd = new Float32Array(N * 4); for (let i = 0; i < rnd.length; i++) rnd[i] = R();
geo.setAttribute('rnd', new THREE.BufferAttribute(rnd, 4));

const pad = (f) => Array.from({ length: 7 }, (_, i) => f(LOOK[used[Math.min(i, used.length - 1)]]));
const sel = (name, type) => [0, 1, 2, 3, 4, 5].map((i) => `if (k < ${i}.5) return ${name}[${i}];`).join(' ') + ` return ${name}[6];`;
const mat = new THREE.ShaderMaterial({
  transparent: true, depthWrite: false, depthTest: false, blending: THREE.AdditiveBlending,
  uniforms: {
    uA: { value: 0 }, uB: { value: 0 }, uF: { value: 0 }, uT: { value: 0 }, uIdle: { value: reduce ? 0 : 1 },
    uBeat: { value: 0 }, uIntro: { value: reduce ? 1 : 0 }, uSize: { value: 30 * PR },
    uLo: { value: pad((l) => new THREE.Vector3(...l.lo)) }, uHi: { value: pad((l) => new THREE.Vector3(...l.hi)) },
    uAnim: { value: pad((l) => l.anim) }, uSz: { value: pad((l) => l.sz) }, uAl: { value: pad((l) => l.al) },
  },
  vertexShader: /* glsl */`
    attribute vec3 p1, p2, p3, p4, p5, p6;
    attribute vec4 sh0, sh1, rnd;
    uniform float uA, uB, uF, uT, uIdle, uBeat, uIntro, uSize;
    uniform vec3 uLo[7], uHi[7];
    uniform float uAnim[7], uSz[7], uAl[7];
    varying vec3 vC; varying float vA;
    vec3 P(float k) { if (k < .5) return position; if (k < 1.5) return p1; if (k < 2.5) return p2; if (k < 3.5) return p3; if (k < 4.5) return p4; if (k < 5.5) return p5; return p6; }
    float SH(float k) { if (k < .5) return sh0.x; if (k < 1.5) return sh0.y; if (k < 2.5) return sh0.z; if (k < 3.5) return sh0.w; if (k < 4.5) return sh1.x; if (k < 5.5) return sh1.y; return sh1.z; }
    vec3 LO(float k) { ${sel('uLo')} }
    vec3 HI(float k) { ${sel('uHi')} }
    float AN(float k) { ${sel('uAnim')} }
    float SZ(float k) { ${sel('uSz')} }
    float AL(float k) { ${sel('uAl')} }
    vec3 COL(float k, float s) {
      if (s > 1.9) return vec3(.62, .82, .92);                 // water: the river
      if (s > 1.5) return vec3(.95, .82, .45);                 // a dropper's drop
      vec3 c = mix(LO(k), HI(k), clamp(s, 0., 1.));
      return mix(c, vec3(1., .93, .8), smoothstep(.88, 1., s) * .6);
    }
    vec3 rotY(vec3 p, float a) { return vec3(p.x * cos(a) - p.z * sin(a), p.y, p.x * sin(a) + p.z * cos(a)); }
    vec3 anim(float k, vec3 p) {
      float id = AN(k), t = uT * uIdle;
      if (id < .5) {                                 // phoenix: wings beat, the tail flickers
        float w = smoothstep(.2, 2.3, abs(p.x));
        p.y += sin(t * 1.2) * .13 * w * w; p.z += sin(t * 1.2 + .6) * .08 * w;
        p.x += sin(p.y * 3. + t * 2.4 + rnd.x * 2.) * .07 * smoothstep(-.3, -1.9, p.y) * (1. - w);
      } else if (id < 1.5) {                         // breathe and turn
        p = rotY(p, t * .15) * (1. + .04 * sin(t * 1.1));
      } else if (id < 2.5) {                         // strokes travel along
        p.y += .13 * sin(p.x * 1.3 - t * 1.1); p.z += .08 * cos(p.x * 1.1 - t * .8);
      } else if (id < 3.5) {                         // pressed on a beat
        p.y *= 1. - .3 * uBeat;
      } else if (id < 4.5) {                         // the step settles and lifts
        if (p.y < .4) p.y -= .22 * exp(-dot(p.xz, p.xz) / .42) * (sin(t * .8) * .5 + .5);
      } else if (id < 5.5) {
      } else if (id < 6.5) {                         // embers rise and wrap round
        p.y = mod(p.y + t * (.05 + .1 * rnd.x) + 3.5, 7.) - 3.5; p.x += sin(t * .3 + rnd.y * 6.28) * .15;
      } else if (id < 7.5) {                         // lymph: everything drifts in to the node
        vec3 n = vec3(0., .7, 0.);
        if (length(p - n) > .7) p = n + (p - n) * (1. - .22 * fract(t * .18 + rnd.x));
      } else if (id < 8.5) {                         // Thai: press on the beat, then draw long
        p.y *= 1. - .55 * uBeat; p.x *= 1. + .16 * (sin(t * .45) * .5 + .5);
      } else if (id < 9.5) {                         // yoga: flow, then hold
        p = rotY(p, t * .25 + .5 * sin(t * .25));
      } else if (id < 10.5) {                        // the zodiac ring turns
        if (length(p.xy) > 1.45 && abs(p.z) < .1) { float a = t * .06; p.xy = vec2(p.x * cos(a) - p.y * sin(a), p.x * sin(a) + p.y * cos(a)); }
      } else {                                       // herbs: the sprig sways, drops fall
        if (p.x > 1.45) p.y = 1.6 - mod(1.6 - p.y + t * .45, 3.2);
        else p.x += sin(t * .7) * .08 * (p.y + 2.) / 4.;
      }
      return p;
    }
    void main() {
      float f = clamp((uF - rnd.x * .35) / .65, 0., 1.); f = f * f * (3. - 2. * f);
      vec3 p = mix(anim(uA, P(uA)), anim(uB, P(uB)), f);
      float sw = sin(3.14159 * f);
      p += vec3(sin(p.y * 1.7 + uT * .7 + rnd.y * 6.28), cos(p.x * 1.5 - uT * .6 + rnd.z * 6.28), sin(p.z * 1.9 + rnd.x * 6.28)) * .55 * sw;
      float g = smoothstep(rnd.w * .55, rnd.w * .55 + .45, uIntro);
      p = mix(vec3((rnd.x - .5) * 7., -3.4 + rnd.y * 1.2, (rnd.z - .5) * 3.), p, g);
      vec4 mv = modelViewMatrix * vec4(p, 1.);
      gl_Position = projectionMatrix * mv;
      gl_PointSize = uSize * mix(SZ(uA), SZ(uB), f) * (.5 + rnd.z * .9) / -mv.z;
      vC = mix(COL(uA, SH(uA)), COL(uB, SH(uB)), f);
      vA = mix(AL(uA), AL(uB), f) * (.7 + .3 * sin(uT * 2. * uIdle + rnd.y * 40.)) * (.35 + .65 * g);
    }`,
  fragmentShader: /* glsl */`
    varying vec3 vC; varying float vA;
    void main() {
      float r = length(gl_PointCoord - .5);
      if (r > .5) discard;
      float a = smoothstep(.5, 0., r); a *= a;
      gl_FragColor = vec4(vC * a * vA, 1.);
    }`,
});
const wrap = new THREE.Group(); scene.add(wrap);
const cloud = new THREE.Points(geo, mat); cloud.frustumCulled = false; wrap.add(cloud);

/* ---------- labels beside the pressed layers (sections with data-labels) ---------- */
const labelBox = document.getElementById('labels');
const labelSets = chapters.map((c) => (c.el.dataset.labels || '').split(';').filter(Boolean).map((l) => {
  const [t, s] = l.split('|'); const d = document.createElement('div'); d.innerHTML = `${s ? `<span>${s}</span>` : ''}${t}`; labelBox.appendChild(d); return d;
}));

/* ---------- scroll story: each section's arrival is one scrubbed tween ---------- */
const key = (c, i) => {
  const L = LOOK[c.shape], P = POSE[c.pose], f = P.flip ? -1 : 1;
  return { x: P.x, y: P.y, z: P.z, sc: L.sc * P.k, rx: L.rx, ry: L.ry * f + (i % 2 ? .15 : 0), m: i };
};
const K = chapters.map(key);
const S = { ...K[0] };
for (let i = 1; i < K.length; i++) {
  gsap.fromTo(S, { ...K[i - 1] }, { ...K[i], ease: 'power2.inOut', immediateRender: false,
    scrollTrigger: { trigger: chapters[i].el, start: 'top bottom', end: 'top 30%', scrub: reduce ? true : 1.2 } });
}

const ptr = { x: 0, y: 0, tx: 0, ty: 0 };
const glow = document.querySelector('.glow');
addEventListener('pointermove', (e) => { ptr.tx = e.clientX / innerWidth - .5; ptr.ty = e.clientY / innerHeight - .5;
  glow.style.setProperty('--gx', e.clientX / innerWidth * 100 + '%'); glow.style.setProperty('--gy', e.clientY / innerHeight * 100 + '%'); }, { passive: true });

function resize() { renderer.setSize(innerWidth, innerHeight, false); camera.aspect = innerWidth / innerHeight; camera.updateProjectionMatrix(); }
addEventListener('resize', resize); resize();

const intro = { v: reduce ? 1 : 0 };
if (!reduce) gsap.to(intro, { v: 1, duration: 3, ease: 'power3.out', delay: .1 });

const clock = new THREE.Clock(), v3 = new THREE.Vector3();
let running = true;
document.addEventListener('visibilitychange', () => { running = !document.hidden; if (running) requestAnimationFrame(frame); });

function frame() {
  if (!running) return;
  const t = clock.getElapsedTime(), m = small(), idle = reduce ? 0 : 1;
  ptr.x += (ptr.tx - ptr.x) * .05; ptr.y += (ptr.ty - ptr.y) * .05;

  const i = Math.max(0, Math.min(Math.floor(S.m), K.length - 1)), f = Math.min(1, Math.max(0, S.m - i));
  const ca = chapters[i], cb = chapters[Math.min(i + 1, K.length - 1)];
  const U = mat.uniforms;
  U.uA.value = ca.slot; U.uB.value = cb.slot; U.uF.value = ca.slot === cb.slot ? 0 : f;
  U.uT.value = t; U.uIntro.value = intro.v;
  const beat = idle ? Math.pow(Math.max(0, Math.sin(t * 2.2)), 4) : 0;
  U.uBeat.value = beat;

  const bgW = (ca.pose === 'bg' ? 1 - f : 0) + (cb.pose === 'bg' && cb !== ca ? f : 0);
  const x = m ? 0 : S.x, y = m ? Math.min(1.55, S.y * .5 + 1.25 * (1 - bgW)) : S.y;
  const sc = S.sc * (m ? .44 + .56 * bgW : 1);
  wrap.position.set(x, y + Math.sin(t * .7) * .05 * idle, 0);
  wrap.rotation.set(S.rx + ptr.y * .2 * idle, S.ry + ptr.x * .3 * idle + Math.sin(t * .3) * .05 * idle, 0);
  wrap.scale.setScalar(sc);
  camera.position.z = S.z * (m ? 1.15 : 1);
  renderer.render(scene, camera);

  wrap.updateMatrixWorld();
  labelSets.forEach((els, ci) => {
    const show = m ? 0 : Math.max(0, 1 - Math.abs(S.m - ci) * 2.4);
    els.forEach((el, k) => {
      if (show <= 0) { el.style.opacity = 0; return; }
      v3.set(-1.75, LAYER_Y[k] * (1 - .3 * beat), 0).applyMatrix4(wrap.matrixWorld).project(camera);
      el.style.transform = `translate(calc(${(v3.x * .5 + .5) * innerWidth}px - 100%), ${(-v3.y * .5 + .5) * innerHeight - 9}px)`;
      el.style.opacity = show;
    });
  });
  requestAnimationFrame(frame);
}
requestAnimationFrame(frame);
window.__ep3d = { ok: true, N, shapes: used };
