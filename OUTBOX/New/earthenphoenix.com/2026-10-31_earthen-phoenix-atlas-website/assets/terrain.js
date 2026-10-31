/* THE EARTHEN ATLAS — terrain engine.
   Tension is drawn as elevation. The logo's own bands are the elevation key:
   yellow / orange / red = peaks of tension, brown = settling, green = grounded.
   Each session is a "mode": a different way of bringing the ground level. */
(() => {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const KEY = ['#5f7d45', '#8f5c34', '#c4432f', '#e5842f', '#f3bd47'];          // grounded → peak, on dark
  const KEYP = ['#4b6a35', '#7a4a2a', '#b3392a', '#cf6a22', '#c98d14'];         // same key, on paper
  const SNOW = ['#5f7d45', '#7f8e4f', '#8f6a45', '#b9a487', '#f1e9dc'];          // zen: real mountains
  const HERB = ['#3d5a2f', '#5f7d45', '#83a052', '#b9b65e', '#e8d483'];          // herbs: an infusion
  const NIGHT = ['#2f3b3a', '#3e4b47', '#56605a', '#7a7f74', '#a7a493'];         // astro: a dark horizon
  const clamp = (x, a, b) => x < a ? a : x > b ? b : x;
  const ease = x => x * x * (3 - 2 * x);
  const g = (u, v, cu, cv, s) => { const du = (u - cu) / s, dv = (v - cv) / s; return Math.exp(-(du * du + dv * dv)); };
  const KNOTS = [[.3, .22, .085, .5, 'L. shoulder'], [.7, .21, .085, .46, 'R. shoulder'], [.5, .38, .075, .32, 'Mid-back'], [.41, .72, .1, .38, 'Low back'], [.6, .74, .1, .4, ''], [.2, .5, .07, .2, ''], [.8, .52, .07, .24, '']];
  const back = (u, v) => .15 * Math.exp(-(((u - .5) / .3) ** 2)) * (.55 + .45 * Math.sin(Math.PI * clamp(v * 1.1, 0, 1))) - .05 * Math.exp(-(((u - .5) / .035) ** 2));

  // stylised sun-sign star patterns (u, v in the sky above the horizon)
  const SIGNS = {
    Aries: [[.3, .3], [.45, .22], [.6, .26], [.7, .38]], Taurus: [[.25, .2], [.4, .32], [.5, .38], [.62, .3], [.75, .18], [.52, .5]],
    Gemini: [[.35, .15], [.35, .5], [.6, .15], [.6, .5], [.35, .3], [.6, .3]], Cancer: [[.5, .2], [.5, .38], [.35, .52], [.66, .52]],
    Leo: [[.3, .4], [.4, .28], [.52, .25], [.6, .34], [.55, .48], [.72, .5]], Virgo: [[.25, .22], [.38, .3], [.5, .26], [.6, .38], [.52, .52], [.72, .46]],
    Libra: [[.3, .45], [.5, .2], [.7, .45], [.4, .45], [.6, .45]], Scorpio: [[.22, .2], [.32, .3], [.44, .34], [.55, .42], [.64, .52], [.76, .48], [.8, .38]],
    Sagittarius: [[.3, .5], [.45, .38], [.6, .26], [.72, .18], [.62, .4], [.48, .22]], Capricorn: [[.25, .25], [.5, .5], [.75, .25], [.5, .3]],
    Aquarius: [[.22, .3], [.35, .22], [.48, .3], [.6, .22], [.74, .3], [.48, .45]], Pisces: [[.2, .45], [.35, .3], [.5, .22], [.65, .3], [.8, .45], [.5, .45]]
  };

  const all = [];
  class Terrain {
    constructor(el) {
      this.el = el; this.mode = el.dataset.terrain; this.paper = el.classList.contains('on-paper');
      this.mini = el.classList.contains('mini');
      this.c = document.createElement('canvas'); this.c.setAttribute('aria-hidden', 'true'); el.prepend(this.c); this.x = this.c.getContext('2d');
      this.read = document.getElementById(el.dataset.read || '') || el.querySelector('.read');
      this.k = KNOTS.map(([u, v, s, a, n]) => ({ u, v, s, a, a0: a, n }));
      this.dents = []; this.parts = []; this.t = 0; this.sp = 0; this.p = { pressure: 'light', depth: 2, reiki: 'on', vessel: 'tea', sign: 'Scorpio' };
      this.add = new Set(); this.ptr = null; this.turb = 1; this.stars = Array.from({ length: 70 }, () => [Math.random(), Math.random() * .62, Math.random()]);
      this.init(); this.size(); this.vis = false;
      new ResizeObserver(() => { this.size(); this.draw(); }).observe(el);
      new IntersectionObserver(es => { this.vis = es[0].isIntersecting; }, { rootMargin: '80px' }).observe(el);
      const pt = e => { const r = this.c.getBoundingClientRect(); return this.unproj(e.clientX - r.left, e.clientY - r.top); };
      el.addEventListener('pointerdown', e => { const q = pt(e); this.ptr = q; this.tap && this.tap(q.u, q.v); if (RM) this.draw(); });
      el.addEventListener('pointermove', e => { const q = pt(e); if (this.ptr || this.mode === 'zen') { const d = this.ptr ? Math.hypot(q.u - this.ptr.u, q.v - this.ptr.v) : 0; this.turb = clamp(this.turb + d * 1.5, 0, 1); } if (this.ptr) { this.ptr = q; this.drag && this.drag(q.u, q.v); } });
      ['pointerup', 'pointerleave', 'pointercancel'].forEach(t => el.addEventListener(t, () => { this.ptr = null; }));
      if (RM) { for (let i = 0; i < 160; i++) this.step(1 / 30); this.draw(); }
      all.push(this); el.terrain = this;
    }
    size() {
      const r = this.el.getBoundingClientRect(), d = Math.min(devicePixelRatio || 1, this.mini ? 1.5 : 2);
      this.w = Math.max(10, r.width); this.h = Math.max(10, r.height);
      this.c.width = Math.round(this.w * d); this.c.height = Math.round(this.h * d); this.x.setTransform(d, 0, 0, d, 0, 0);
      this.cols = Math.round(clamp(this.w / (this.mini ? 9 : 11), 28, 96)); this.rows = Math.round(clamp(this.h / (this.mini ? 13 : 15), 12, 34));
      // [top, depth, amplitude, width] of the projection, per mode
      const [t, d2, a, w] = { hero: [.34, .6, .72, 1.08], astro: [.66, .3, .2, .9], ground: [.12, .82, .8, 1.12] }[this.mode] || [.3, .6, .52, .9];
      this.top = this.h * t; this.dep = this.h * d2; this.amp = this.h * a * (this.mode === 'hero' && this.w < 700 ? .75 : 1); this.W = this.w * w;
      if (this.mode === 'ground') this.rows = Math.round(clamp(this.h / 12, 8, 14));
    }
    proj(u, v, h) { const f = .7 + .3 * v, sx = this.sx || 1; return [this.w / 2 + (u - .5) * this.W * f * sx, this.top + v * this.dep - h * this.amp * (.55 + .45 * v)]; }
    unproj(x, y) { const v = clamp((y - this.top) / this.dep, 0, 1), f = .7 + .3 * v; return { u: clamp((x - this.w / 2) / (this.W * f * (this.sx || 1)) + .5, 0, 1), v }; }
    base(u, v) {
      if (this.mode === 'zen') {
        const far = (1 - v) ** 1.7, ridge = .55 + .3 * Math.sin(u * 7.1 + 1) + .18 * Math.sin(u * 17.3) + .1 * Math.sin(u * 31 + 2);
        const river = .5 + .16 * Math.sin(v * 5.2 + .4); return far * ridge * .95 + .03 * Math.sin(u * 9 + v * 4) - .06 * Math.exp(-(((u - river) / .03) ** 2)) * v;
      }
      if (this.mode === 'astro') return .05 + .05 * Math.sin(u * 6 + 1) + .03 * Math.sin(u * 15);
      if (this.mode === 'yoga' || this.mode === 'herbs') return .02;
      return back(u, v);
    }
    H(u, v) {
      let h = this.base(u, v);
      if (this.useKnots !== false) { const ks = this.ks ?? 1; for (const k of this.k) h += k.a * ks * g(u, v, k.u, k.v, k.s); }
      for (const d of this.dents) h -= d.d * d.f * g(u, v, d.u, d.v, d.s);
      return h + (this.extra ? this.extra(u, v) : 0);
    }
    tension() { let a = 0, b = 0; for (const k of this.k) { a += k.a; b += k.a0; } return a / b; }
    say(s) { if (this.read && this.read.textContent !== s) this.read.textContent = s; }
    relax(k, r, dt) { k.a = Math.max(k.a0 * .08, k.a - k.a * r * dt); }
    regrow(r, dt) { for (const k of this.k) k.a += (k.a0 - k.a) * r * dt; }
    dent(u, v, d, s, life, grow) { this.dents.push({ u, v, d, s, s0: s, life, age: 0, f: 0, grow: grow || 0 }); }
    stepDents(dt) {
      for (const d of this.dents) { d.age += dt; const x = d.age / d.life; d.f = x < .25 ? ease(x / .25) : 1 - ease(clamp((x - .25) / .75, 0, 1)); d.s = d.s0 + d.grow * Math.min(1, x * 1.6); }
      this.dents = this.dents.filter(d => d.age < d.life);
    }
    init() {   // the mode's own hooks (tap, extra, over, under...) become this terrain's methods
      const M = MODES[this.mode] || MODES.hero;
      for (const [k, f] of Object.entries(M)) if (k !== 'init' && k !== 'step') this[k] = f;
      M.init.call(this);
    }
    step(dt) { this.t += dt; this.stepDents(dt); (MODES[this.mode] || MODES.hero).step.call(this, dt); }
    color(u, v, h) {
      if (this.mode === 'zen') return clamp(Math.floor(h / .18), 0, 4);
      if (this.mode === 'yoga' || this.mode === 'herbs') return clamp(Math.floor(Math.abs(h - .02) / .035), 0, 4);
      if (this.mode === 'astro') return clamp(Math.floor(h / .04), 0, 4);
      return clamp(Math.floor((h - this.base(u, v) + .02) / .085), 0, 4);
    }
    draw() {
      const x = this.x, C = this.cols, R = this.rows, pal = this.mode === 'zen' ? SNOW : this.mode === 'herbs' ? HERB : this.mode === 'astro' ? NIGHT : this.paper ? KEYP : KEY;
      const bg = getComputedStyle(this.el).getPropertyValue('--fill').trim() || (this.paper ? '#efe7da' : '#1a1612');
      x.clearRect(0, 0, this.w, this.h);
      if (this.under) this.under(x);
      const lw = this.mini ? 1 : this.w < 500 ? 1.1 : 1.4, pts = new Array(C + 1), cs = new Array(C + 1);
      for (let r = 0; r < R; r++) {
        const v = r / (R - 1);
        for (let c = 0; c <= C; c++) { const u = c / C, h = this.H(u, v); pts[c] = this.proj(u, v, h); cs[c] = this.color(u, v, h); }
        x.beginPath(); x.moveTo(pts[0][0], pts[0][1]); for (let c = 1; c <= C; c++) x.lineTo(pts[c][0], pts[c][1]);
        x.lineTo(pts[C][0], this.h + 4); x.lineTo(pts[0][0], this.h + 4); x.closePath(); x.fillStyle = bg; x.fill();
        x.lineWidth = lw * (.7 + .5 * v); x.lineJoin = 'round';
        for (let b = 0; b < 5; b++) {
          let open = false; x.beginPath();
          for (let c = 0; c < C; c++) {
            if (Math.max(cs[c], cs[c + 1]) === b) { if (!open) { x.moveTo(pts[c][0], pts[c][1]); open = true; } x.lineTo(pts[c + 1][0], pts[c + 1][1]); } else open = false;
          }
          x.strokeStyle = pal[b]; x.globalAlpha = .45 + .55 * v; x.stroke();
        }
        x.globalAlpha = 1;
      }
      if (this.over) this.over(x);
    }
    labels(x) {   // cartographic labels on the knots
      if (this.mini || this.w < 420) return;
      x.font = '500 10px "Martian Mono", ui-monospace, monospace'; x.textAlign = 'left';
      for (const k of this.k) {
        if (!k.n) continue; const [px, py] = this.proj(k.u, k.v, this.H(k.u, k.v)), tl = Math.round(k.a / k.a0 * 100);
        x.strokeStyle = x.fillStyle = this.paper ? 'rgba(30,26,22,.75)' : 'rgba(239,231,218,.8)'; x.lineWidth = 1;
        x.beginPath(); x.moveTo(px, py - 4); x.lineTo(px + 14, py - 26); x.lineTo(px + 22, py - 26); x.stroke();
        x.beginPath(); x.arc(px, py - 2, 2.2, 0, 7); x.fill();
        x.fillText(k.n.toUpperCase() + '  ' + tl + '%', px + 26, py - 23);
      }
    }
    glow(x, u, v, lift, r, col) {
      const [px, py] = this.proj(u, v, this.H(u, v)), y = py - lift;
      const gr = x.createRadialGradient(px, y, 0, px, y, r); gr.addColorStop(0, col); gr.addColorStop(1, 'rgba(0,0,0,0)');
      x.fillStyle = gr; x.beginPath(); x.arc(px, y, r, 0, 7); x.fill(); return [px, y, py];
    }
  }

  const MODES = {
    // HOME: a long stroke travels the back; peaks cool to ground, then slowly return. Scrolling grounds it further.
    hero: {
      init() { this.sv = -1; },
      step(dt) {
        const T = 16, ph = (this.t % T) / T;
        this.sv = ph > .14 && ph < .56 ? 1 - (ph - .14) / .42 : -1;
        for (const k of this.k) { if (this.sv >= 0 && Math.abs(k.v - this.sv) < .13) this.relax(k, 1.5, dt); }
        if (ph > .66) this.regrow(1, dt);
        this.ks = 1 - .85 * this.sp;   // scrolling away grounds the view, without touching the session itself
        this.say('TENSION ' + String(Math.round(this.tension() * this.ks * 100)).padStart(2, '0') + '%  ·  ' + (this.sv >= 0 ? 'A LONG STROKE PASSES' : ph > .66 ? 'EVERYDAY TENSION RETURNS' : ph < .14 ? 'HELD IN THE SHOULDERS' : 'GROUNDED'));
      },
      extra(u, v) { return this.sv >= 0 ? .035 * Math.exp(-(((v - this.sv) / .03) ** 2)) * Math.exp(-(((u - .5) / .34) ** 2)) * this.ks : 0; }
    },
    swedish: {
      init() { this.sv = 1; this.dir = -1; this.n = 1; },
      step(dt) {
        const ts = this.add.has('still') ? .55 : 1, sp = .19 * ts, med = this.p.pressure === 'medium';
        this.sv += this.dir * sp * dt; if (this.sv < .04 || this.sv > .98) { this.dir *= -1; this.n++; this.sv = clamp(this.sv, .04, .98); }
        for (const k of this.k) if (Math.abs(k.v - this.sv) < .12) this.relax(k, med ? .9 : .45, dt);
        if (this.ptr) for (const k of this.k) if (g(k.u, k.v, this.ptr.u, this.ptr.v, .14) > .3) this.relax(k, 1.6, dt);
        this.regrow(.05, dt);
        this.say('STROKE ' + this.n + '  ·  ' + (med ? 'MEDIUM' : 'LIGHT') + ' PRESSURE  ·  TENSION ' + Math.round(this.tension() * 100) + '%');
      },
      extra(u, v) {
        const med = this.p.pressure === 'medium';
        let e = (med ? .045 : .03) * Math.exp(-(((v - this.sv) / .035) ** 2)) * Math.exp(-(((u - .5) / .3) ** 2));
        if (this.ptr) e += .04 * g(u, v, this.ptr.u, this.ptr.v, .06);
        if (this.add.has('sound')) { const d = Math.hypot(u - .5, (v - .38) * .8); e += .016 * Math.sin(d * 46 - this.t * 4) * Math.exp(-d * 3); }
        return e;
      },
      under() { if (this.add.has('breath')) { const b = 1 + .07 * Math.sin(this.t * Math.PI * 2 / 8); this.amp = this.h * .52 * b; } else this.amp = this.h * .52; },
      over(x) { this.labels(x); if (!this.mini) this.glow(x, .5, clamp(this.sv, 0, 1), 6, this.w * .09, this.paper ? 'rgba(207,106,34,.22)' : 'rgba(243,189,71,.2)'); }
    },
    deep: {
      init() { this.ki = 0; },
      step(dt) {
        const D = [.1, .17, .26][this.p.depth] || .26, ph = (this.t % 8) / 8, press = .5 + .5 * Math.cos(2 * Math.PI * ph);
        const k = this.k[this.ki]; this.press = press; this.out = Math.sin(2 * Math.PI * ph) > 0;
        this.dents = [{ u: k.u + .01, v: k.v + .01, d: D * press, s: [.065, .052, .042][this.p.depth] || .042, f: 1, age: 0, life: 9 }];
        this.relax(k, .09 * press * (this.p.depth + 1), dt); for (const o of this.k) if (o !== k) o.a += (o.a0 - o.a) * .015 * dt;
        if (k.a < k.a0 * .3) { this.ki = (this.ki + 1) % 5; }
        this.say((this.out ? 'BREATHE OUT · SINKING' : 'BREATHE IN · EASING') + '  ·  ' + (k.n || 'Knot').toUpperCase() + ' ' + Math.round(k.a / k.a0 * 100) + '%');
      },
      over(x) {
        this.labels(x); const k = this.k[this.ki], [px, py] = this.proj(k.u, k.v, this.H(k.u, k.v));
        x.strokeStyle = this.paper ? '#1e1a16' : '#efe7da'; x.lineWidth = 1.2; x.setLineDash([3, 4]); x.beginPath(); x.moveTo(px, py - 70 + this.press * 30); x.lineTo(px, py - 6); x.stroke(); x.setLineDash([]);
        x.beginPath(); x.arc(px, py - 70 + this.press * 30, 4, 0, 7); x.fillStyle = '#e5842f'; x.fill();
      }
    },
    thai: {
      init() { this.beat = -1; this.sx = 1; },
      step(dt) {
        const T = 11, t = this.t % T;
        if (t < 6.4) { const b = Math.floor(t / .8); if (b !== this.beat) { this.beat = b; const v = .96 - (b >> 1) * .1, u = b % 2 ? .6 : .4; this.dent(u, v, .14, .055, .7); this.lastP = [u, v]; } this.sx += (1 - this.sx) * 3 * dt; for (const k of this.k) if (k.v > .55) this.relax(k, .2, dt); }
        else { this.beat = -1; const s = (t - 6.4) / 4.6; this.sx = 1 + .17 * Math.sin(Math.PI * s); for (const k of this.k) this.relax(k, .25, dt); }
        if (t < .1) for (const k of this.k) k.a = k.a0;
        this.say(t < 6.4 ? 'PRESS ' + (Math.floor(t / .8) + 1) + ' OF 8  ·  ON THE BEAT, FEET TO HIPS' : 'STRETCH  ·  DRAWN LONG');
      },
      tap(u, v) { this.dent(u, v, .15, .055, .8); },
      over(x) { if (this.dents.length && !this.mini) for (const d of this.dents) this.glow(x, d.u, d.v, 0, 40 * d.f, this.paper ? 'rgba(179,57,42,.25)' : 'rgba(229,132,47,.3)'); }
    },
    lymph: {
      init() {
        this.paths = [[[.04, .66], [.18, .42], [.3, .2], [.5, .08]], [[.96, .66], [.82, .42], [.7, .2], [.5, .08]], [[.4, 1], [.42, .78], [.33, .45], [.5, .08]], [[.6, 1], [.58, .78], [.67, .45], [.5, .08]], [[.5, -.02], [.5, .08]]];
        this.sw = .14; this.parts = Array.from({ length: this.mini ? 26 : 54 }, () => ({ p: Math.floor(Math.random() * 5), s: Math.random() }));
        for (const k of this.k) { k.a0 *= .45; k.a = k.a0; }
      },
      at(path, s) { const P = this.paths[path], n = P.length - 1, i = Math.min(n - 1, Math.floor(s * n)), f = s * n - i; return [P[i][0] + (P[i + 1][0] - P[i][0]) * f, P[i][1] + (P[i + 1][1] - P[i][1]) * f]; },
      step(dt) {
        for (const q of this.parts) { q.s += dt * (q.p === 4 ? .5 : .16); if (q.s >= 1) { q.s = 0; q.p = Math.floor(Math.random() * 5); this.sw = Math.max(.02, this.sw - .0035); } }
        if (this.sw <= .021) this.sw = .14;   // drained: the loop begins again
        this.say('SWELLING ' + Math.round(this.sw / .14 * 100) + '%  ·  FLOWING TOWARD THE COLLARBONE');
      },
      extra(u, v) { return this.sw * g(u, v, .5, .62, .42); },
      over(x) {
        x.strokeStyle = this.paper ? 'rgba(30,26,22,.28)' : 'rgba(239,231,218,.25)'; x.lineWidth = 1; x.setLineDash([2, 5]);
        for (let p = 0; p < 5; p++) { x.beginPath(); for (let i = 0; i <= 30; i++) { const [u, v] = MODES.lymph.at.call(this, p, i / 30), [px, py] = this.proj(u, clamp(v, 0, 1), this.H(u, clamp(v, 0, 1))); i ? x.lineTo(px, py) : x.moveTo(px, py); } x.stroke(); }
        x.setLineDash([]); x.fillStyle = this.paper ? '#3d6b7a' : '#a9d2d6';
        for (const q of this.parts) { const [u, v] = MODES.lymph.at.call(this, q.p, q.s), vv = clamp(v, 0, 1), [px, py] = this.proj(u, vv, this.H(u, vv)); x.globalAlpha = .4 + .6 * Math.sin(Math.PI * q.s); x.beginPath(); x.arc(px, py - 2, this.mini ? 1.6 : 2.3, 0, 7); x.fill(); }
        x.globalAlpha = 1; const [cx, cy] = this.proj(.5, .08, this.H(.5, .08)); x.strokeStyle = this.paper ? '#3d6b7a' : '#a9d2d6'; x.beginPath(); x.arc(cx, cy - 2, 6 + 2 * Math.sin(this.t * 3), 0, 7); x.stroke();
        if (!this.mini && this.w > 420) { x.font = '500 10px "Martian Mono", monospace'; x.fillStyle = x.strokeStyle; x.fillText('COLLARBONE', cx + 14, cy - 8); }
      }
    },
    sarga: {
      init() { this.i = -1; this.prints = []; },
      step(dt) {
        const T = 1.5, n = 8, cyc = this.t % (T * (n + 3)), i = Math.floor(cyc / T);
        if (i !== this.i) { this.i = i; if (i < n) this.stepAt(i % 2 ? .55 : .45, .86 - i * .09); if (i === n + 2) { for (const k of this.k) k.a = k.a0; this.prints = []; } }
        for (const p of this.prints) p.age += dt; this.prints = this.prints.filter(p => p.age < 6);
        this.say(this.i < n ? 'STEP ' + (this.i + 1) + '  ·  WEIGHT HELD BY THE STRAP  ·  DEEP INTO THE FASCIA' : 'REST  ·  THE GROUND SETTLES');
      },
      stepAt(u, v) { this.dent(u, v, .3, .035, 2.6, .07); this.prints.push({ u, v, age: 0, l: u < .5 }); for (const k of this.k) if (g(k.u, k.v, u, v, .2) > .2) k.a *= .62; },
      tap(u, v) { this.stepAt(u, v); },
      over(x) {
        if (this.mini) return; x.strokeStyle = this.paper ? '#1e1a16' : '#efe7da'; x.lineWidth = 1.2;
        for (const p of this.prints) {
          const [px, py] = this.proj(p.u, p.v, this.H(p.u, p.v) + .02), a = Math.max(0, 1 - p.age / 6); x.globalAlpha = a;
          x.beginPath(); x.ellipse(px, py, 7, 13, p.l ? -.15 : .15, 0, 7); x.stroke();
          for (let t = 0; t < 5; t++) { x.beginPath(); x.arc(px - 6 + t * 3 * (p.l ? 1 : 1), py - 17 + Math.abs(t - 1.5) * 1.3, 1.5, 0, 7); x.stroke(); }
        }
        x.globalAlpha = 1;
      }
    },
    reiki: {
      init() { this.hu = .5; this.hv = .22; this.pi = 0; this.bal = .3; },
      step(dt) {
        if (!this.manual) { const s = Math.floor(this.t / 6) % 3; if (s !== this.pi) { this.pi = s; [this.hu, this.hv] = [[.5, .22], [.5, .46], [.5, .72]][s]; } }
        const near = this.p.reiki === 'near', ks = this.k, m = ks.reduce((a, k) => a + k.a, 0) / ks.length;
        for (const k of ks) { const w = g(k.u, k.v, this.hu, this.hv, .25); k.a += (m * .55 - k.a) * dt * (.12 + (near ? .12 : .32) * w); }
        const sd = Math.sqrt(ks.reduce((a, k) => a + (k.a - m) ** 2, 0) / ks.length);
        if (sd < .012 && m < .12) for (const k of ks) k.a = k.a0;
        this.say((near ? 'HANDS NEAR THE BODY' : 'HANDS RESTING ON') + '  ·  BALANCE ' + Math.round(100 - sd / m * 100) + '%');
      },
      tap(u, v) { this.manual = true; this.hu = u; this.hv = v; clearTimeout(this.mt); this.mt = setTimeout(() => this.manual = false, 9000); },
      extra(u, v) { return this.p.reiki === 'on' ? .02 * g(u, v, this.hu, this.hv, .12) : 0; },
      over(x) {
        const near = this.p.reiki === 'near', lift = near ? (this.mini ? 18 : 46) : 4;
        const [px, y, py] = this.glow(x, this.hu, this.hv, lift, this.w * (this.mini ? .13 : .11), this.paper ? 'rgba(207,106,34,.28)' : 'rgba(243,189,71,.28)');
        x.strokeStyle = this.paper ? '#1e1a16' : '#efe7da'; x.lineWidth = 1.3;
        const sc = this.mini ? .6 : 1;
        for (const s of [-1, 1]) { x.beginPath(); x.ellipse(px + s * 16 * sc, y, 9 * sc, 15 * sc, s * .25, 0, 7); x.stroke(); }
        if (near) { x.setLineDash([2, 4]); x.beginPath(); x.moveTo(px, y + 16 * sc); x.lineTo(px, py); x.stroke(); x.setLineDash([]); }
      }
    },
    yoga: {
      init() { this.useKnots = false; },
      step(dt) { const t = this.t % 15; this.flow = t < 8; this.say(this.flow ? 'VINYASA  ·  MOVING WITH THE BREATH' : 'YIN  ·  HOLD ' + Math.floor(t - 8 + 1) + 's'); this.mix = this.flow ? Math.min(1, t / 1.2) * Math.min(1, (8 - t) / 1.2) : 0; },
      tap() { this.t = Math.floor(this.t / 15) * 15 + 15; },
      extra(u, v) {
        const t = this.t, f = this.mix || 0;
        const flow = .1 * Math.sin(u * 9 - t * 2.6 + v * 3) * Math.sin(v * 5.5 + t * 1.3) + .05 * Math.sin(u * 3 + t * 1.8);
        const yin = .035 * (.5 + .5 * Math.sin(t * Math.PI * 2 / 6)) * Math.exp(-(((u - .5) / .35) ** 2) - (((v - .5) / .5) ** 2));
        return f * flow + (1 - f) * yin;
      }
    },
    zen: {
      init() { this.useKnots = false; this.turb = 1; this.drops = Array.from({ length: this.mini ? 14 : 30 }, () => Math.random()); },
      step(dt) { this.turb = Math.max(.04, this.turb - dt * .045); for (let i = 0; i < this.drops.length; i++) { this.drops[i] += dt * (.05 + .25 * this.turb); if (this.drops[i] > 1) this.drops[i] -= 1; } this.say('THE RIVER  ·  ' + (this.turb > .66 ? 'RUSHING' : this.turb > .3 ? 'SLOWING' : 'STILL') + '  ·  STAY A WHILE'); },
      extra(u, v) { const r = .5 + .16 * Math.sin(v * 5.2 + .4), w = Math.exp(-(((u - r) / .05) ** 2)) * v; return w * this.turb * .025 * Math.sin(u * 60 + this.t * 7) * Math.sin(v * 30 - this.t * 4); },
      over(x) {
        x.fillStyle = this.paper ? '#3d6b7a' : '#a9d2d6';
        for (const s of this.drops) { const v = s, u = .5 + .16 * Math.sin(v * 5.2 + .4) + .008 * Math.sin(s * 80), [px, py] = this.proj(u, v, this.H(u, v)); x.globalAlpha = .3 + .6 * v; x.beginPath(); x.arc(px, py - 1, .8 + v * 1.8, 0, 7); x.fill(); }
        x.globalAlpha = 1;
      }
    },
    astro: {
      init() { this.useKnots = false; this.drawn = 0; this.last = ''; },
      step(dt) { if (this.p.sign !== this.last) { this.last = this.p.sign; this.drawn = 0; } this.drawn = Math.min(1, this.drawn + dt * .45); },
      under(x) {
        for (const [u, v, s] of this.stars) { x.globalAlpha = .25 + .35 * (.5 + .5 * Math.sin(this.t * (1 + s) + s * 9)); x.fillStyle = '#efe7da'; x.fillRect(u * this.w, v * this.h, 1.2, 1.2); }
        const P = SIGNS[this.p.sign] || SIGNS.Aries, n = P.length, d = this.drawn * (n - 1);
        x.globalAlpha = 1; x.strokeStyle = 'rgba(243,189,71,.75)'; x.lineWidth = 1.2; x.beginPath();
        for (let i = 0; i < n; i++) { const [px, py] = [P[i][0] * this.w, P[i][1] * this.h]; if (i === 0) x.moveTo(px, py); else if (i <= d + 1) { const f = clamp(d - (i - 1), 0, 1), [qx, qy] = [P[i - 1][0] * this.w, P[i - 1][1] * this.h]; x.lineTo(qx + (px - qx) * f, qy + (py - qy) * f); } }
        x.stroke();
        for (const [u, v] of P) { const gr = x.createRadialGradient(u * this.w, v * this.h, 0, u * this.w, v * this.h, 12); gr.addColorStop(0, 'rgba(243,189,71,.9)'); gr.addColorStop(1, 'rgba(243,189,71,0)'); x.fillStyle = gr; x.beginPath(); x.arc(u * this.w, v * this.h, 12, 0, 7); x.fill(); x.fillStyle = '#fff6df'; x.beginPath(); x.arc(u * this.w, v * this.h, 2, 0, 7); x.fill(); }
        if (!this.mini) { x.font = '500 11px "Martian Mono", monospace'; x.fillStyle = 'rgba(239,231,218,.8)'; x.fillText(this.p.sign.toUpperCase() + '  ·  STYLISED', 18, 26); }
      }
    },
    herbs: {
      init() { this.useKnots = false; this.drops = []; this.next = 0; this.rx = 0; },
      step(dt) {
        const kind = this.p.vessel; this.next -= dt;
        if (this.next <= 0) { if (kind === 'tincture') { this.drops.push({ u: .5 + (Math.random() - .5) * .16, v: .45 + (Math.random() - .5) * .16, age: 0, a: .2, k: 40 }); this.next = 1.4; } else if (kind === 'tea') { this.drops.push({ u: .5, v: .5, age: 0, a: .16, k: 16 }); this.next = 2.6; } else this.next = 9; }
        for (const d of this.drops) d.age += dt; this.drops = this.drops.filter(d => d.age < 7);
        this.rx += dt * .12; if (this.rx > 1) this.rx = 0;
        this.say(kind === 'tea' ? 'TEA  ·  STEEPING SLOWLY, SPREADING WIDE' : kind === 'tincture' ? 'TINCTURE  ·  A FEW DROPS AT A TIME' : 'ROLLIE  ·  ROLLED ON, WHERE YOU NEED IT');
      },
      tap(u, v) { this.drops.push({ u, v, age: 0, a: .2, k: 30 }); },
      extra(u, v) {
        let e = 0; for (const d of this.drops) { const r = Math.hypot(u - d.u, (v - d.v) * .8), front = d.age * (d.k > 20 ? .16 : .07); e += d.a * Math.exp(-d.age * .3) * Math.cos((r - front) * d.k) * Math.exp(-(((r - front) / .09) ** 2)); }
        if (this.p.vessel === 'rollie') { const ru = .15 + .7 * this.rx, rv = .35 + .3 * Math.sin(this.rx * 6); e += .16 * Math.exp(-(((u - ru) ** 2 + (v - rv) ** 2) / .003)); for (let i = 1; i < 30; i++) { const s = this.rx - i * .01; if (s < 0) break; const tu = .15 + .7 * s, tv = .35 + .3 * Math.sin(s * 6); e += .05 * (1 - i / 30) * Math.exp(-(((u - tu) ** 2 + (v - tv) ** 2) / .0012)); } }
        return e;
      }
    }
  };
  // FOOTER: ground level. What is left of the terrain only breathes.
  MODES.ground = {
    init() { for (const k of this.k) { k.a0 *= .16; k.a = k.a0; } },
    step() { const b = .5 + .5 * Math.sin(this.t * Math.PI * 2 / 7); for (const k of this.k) k.a = k.a0 * (.6 + .4 * b); }
  };

  document.querySelectorAll('[data-terrain]').forEach(el => new Terrain(el));
  let last = performance.now();
  function loop(now) {
    const dt = Math.min(.05, (now - last) / 1000); last = now;
    for (const t of all) if (t.vis && !document.hidden) { t.step(dt); t.draw(); }
    requestAnimationFrame(loop);
  }
  if (!RM) requestAnimationFrame(loop);
  // controls: <button data-set="pressure:medium">, <button data-add="sound">, <input data-range="depth">
  document.addEventListener('click', e => {
    const b = e.target.closest('[data-set],[data-add],[data-act]'); if (!b) return;
    const T = (document.getElementById(b.closest('[data-for]')?.dataset.for || '') || {}).terrain; if (!T) return;
    if (b.dataset.set) { const [k, v] = b.dataset.set.split(':'); T.p[k] = v; b.parentElement.querySelectorAll('[data-set]').forEach(o => o.setAttribute('aria-pressed', o === b)); }
    if (b.dataset.add) { const on = !T.add.has(b.dataset.add); on ? T.add.add(b.dataset.add) : T.add.delete(b.dataset.add); b.setAttribute('aria-pressed', on); }
    if (b.dataset.act === 'tap' && T.tap) T.tap(.35 + Math.random() * .3, .3 + Math.random() * .45);
    if (RM) { for (let i = 0; i < 40; i++) T.step(1 / 30); T.draw(); }
  });
  document.addEventListener('input', e => {
    const r = e.target.closest('[data-range]'); if (!r) return; const T = (document.getElementById(r.closest('[data-for]')?.dataset.for || '') || {}).terrain; if (!T) return;
    T.p[r.dataset.range] = +r.value; if (RM) { for (let i = 0; i < 40; i++) T.step(1 / 30); T.draw(); }
  });
  window.EPAtlas = { all, SIGNS };
})();
