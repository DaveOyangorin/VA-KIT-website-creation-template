/* EMBER SWARM — one field of embers that takes the shape of each Earthen Phoenix service.
   A body lying face down (seen from above) is made of ~1000 embers. Each technique is shown as HEAT:
   where the hands, forearm or feet work, embers glow; where nothing touches, they stay ash.
     swedish  two hands draw long strokes; light or medium; sound / meditation / breathwork add-ons
     deep     one slow point sinks deeper on every out-breath; embers swell with depth
     thai     palm presses on a beat from feet to hips, then the legs are drawn long in a stretch
     lymph    flow travels from hands, feet and head toward the nodes and the collarbone
     sarga    bare footprints stamped step by step up the back, heat spreading deep around them
     reiki    hands hover on or just above; warmth gathers and then evens out across the whole body
   Other shapes: yoga (a figure that flows, then holds), zen (mountains and a river that slows),
   astro (the stars of your sun sign), herbs (a cup, roller or dropper filling with herbs),
   phoenix (the hero: ash rises into the phoenix from the logo, and settles back as you scroll),
   sparks (embers drifting up behind the final call to action).
   Everything pauses off screen and in background tabs; reduced motion draws one still frame. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window, TAU = Math.PI * 2;
  function cl(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  function sine(x) { return -(Math.cos(Math.PI * cl(x)) - 1) / 2; }
  function breath(t) { return .5 - .5 * Math.cos(t / 8000 * TAU); }
  function rnd(s) { return function () { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }; }

  // colour ramps: 0 ember (ash → clay → ember → white heat), 1 herb green, 2 water
  var RAMPS = [[[0, [70, 61, 54]], [.35, [134, 58, 34]], [.6, [196, 83, 45]], [.8, [242, 163, 58]], [1, [255, 241, 214]]],
               [[0, [56, 64, 50]], [.5, [112, 140, 94]], [1, [220, 238, 204]]],
               [[0, [48, 62, 60]], [.5, [126, 162, 158]], [1, [236, 247, 243]]]];
  var LUT = RAMPS.map(function (st) {
    var out = [];
    for (var i = 0; i < 64; i++) {
      var v = i / 63, j = 1; while (j < st.length - 1 && st[j][0] < v) j++;
      var a = st[j - 1], b = st[j], f = cl((v - a[0]) / (b[0] - a[0]));
      out.push('rgb(' + [0, 1, 2].map(function (c) { return Math.round(a[1][c] + (b[1][c] - a[1][c]) * f); }).join(',') + ')');
    }
    return out;
  });

  // ---------- the body, face down, seen from above (virtual 600 x 420, head on the left) ----------
  var BODY = null;
  function body() {
    if (BODY) return BODY;
    var c = document.createElement('canvas'); c.width = 600; c.height = 420; var g = c.getContext('2d');
    g.fillStyle = g.strokeStyle = '#000'; g.lineCap = 'round'; g.lineJoin = 'round';
    g.beginPath(); g.ellipse(70, 210, 27, 23, 0, 0, TAU); g.fill();
    g.fillRect(90, 197, 26, 26);
    var top = [[112, 147], [150, 137], [200, 150], [240, 159], [276, 151], [306, 153]], pts = top.concat(top.slice().reverse().map(function (p) { return [p[0], 420 - p[1]]; }));
    g.beginPath(); g.moveTo(pts[0][0], pts[0][1]); for (var i = 1; i < pts.length; i++) g.lineTo(pts[i][0], pts[i][1]); g.closePath(); g.fill();
    [[[124, 137], [200, 123], [286, 129]], [[124, 283], [200, 297], [286, 291]]].forEach(function (a) { g.lineWidth = 21; g.beginPath(); g.moveTo(a[0][0], a[0][1]); g.lineTo(a[1][0], a[1][1]); g.lineTo(a[2][0], a[2][1]); g.stroke(); g.beginPath(); g.ellipse(300, a[2][1], 14, 10, 0, 0, TAU); g.fill(); });
    [[184, 236]].forEach(function () {});
    [[300, 184, 420, 180, 546, 187], [300, 236, 420, 240, 546, 233]].forEach(function (l) {
      g.lineWidth = 42; g.beginPath(); g.moveTo(l[0], l[1]); g.lineTo(l[2], l[3]); g.stroke();
      g.lineWidth = 30; g.beginPath(); g.moveTo(l[2], l[3]); g.lineTo(l[4], l[5]); g.stroke();
      g.beginPath(); g.ellipse(562, l[5], 11, 14, 0, 0, TAU); g.fill();
    });
    var d = g.getImageData(0, 0, 600, 420).data, r = rnd(9), bx = [], by = [], reg = [];
    for (var y = 3; y < 420; y += 7) for (var x = 3; x < 600; x += 7) {
      if (d[(y * 600 + x) * 4 + 3] < 128) continue;
      bx.push(x + (r() - .5) * 2.4); by.push(y + (r() - .5) * 2.4);
      reg.push(x < 96 ? 'head' : x > 302 ? 'leg' : (y < 147 || y > 273) ? 'arm' : 'torso');
    }
    BODY = { x: bx, y: by, r: reg, n: bx.length };
    return BODY;
  }

  // a polyline you can travel along at constant speed
  function path(pts) {
    var len = [0]; for (var i = 1; i < pts.length; i++) len.push(len[i - 1] + Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]));
    var L = len[len.length - 1];
    return { L: L, at: function (u) { var d = cl(u) * L, j = 1; while (j < len.length - 1 && len[j] < d) j++; var f = (d - len[j - 1]) / Math.max(1e-6, len[j] - len[j - 1]); return [pts[j - 1][0] + (pts[j][0] - pts[j - 1][0]) * f, pts[j - 1][1] + (pts[j][1] - pts[j - 1][1]) * f]; } };
  }

  // ---------- the engine ----------
  function Swarm(box, o) {
    o = o || {}; var S = this;
    S.box = box; S.free = !!o.free; S.VW = 600; S.VH = 420; S.N = o.N || 1400;
    var cv = document.createElement('canvas'); cv.setAttribute('aria-hidden', 'true'); box.insertBefore(cv, box.firstChild); S.cv = cv; S.ctx = cv.getContext('2d');
    ['x', 'y', 'vx', 'vy', 'tx', 'ty', 'h', 'a', 'ta', 'sz', 'tsz'].forEach(function (k) { S[k] = new Float32Array(S.N); });
    S.tone = new Uint8Array(S.N); S.base = 2.3; S.k = .06; S.damp = .8; S.t = 0; S.labelEl = box.querySelector('.label'); S.pointer = null;
    S.size(); var r = rnd(3);
    for (var i = 0; i < S.N; i++) { S.x[i] = S.tx[i] = r() * S.VW; S.y[i] = S.ty[i] = S.VH - 4 - r() * 18; S.a[i] = S.ta[i] = .15; S.sz[i] = S.tsz[i] = .7; }
    var visible = false, raf = 0, prev = 0;
    function loop(now) { raf = 0; if (!visible || document.hidden) return; var dt = prev ? Math.min(50, now - prev) : 16.7; prev = now; S.frame(now, dt); raf = requestAnimationFrame(loop); }
    S.kick = function () { if (!raf && !reduce && visible && !document.hidden) { prev = 0; raf = requestAnimationFrame(loop); } };
    if (!reduce) {
      if (hasIO) new IntersectionObserver(function (es) { es.forEach(function (e) { visible = e.isIntersecting; S.kick(); }); }, { rootMargin: '100px' }).observe(box);
      else { visible = true; S.kick(); }
      document.addEventListener('visibilitychange', S.kick);
    }
    addEventListener('resize', function () { clearTimeout(S.rt); S.rt = setTimeout(function () { S.size(); if (S.mode && S.mode.resize) S.mode.resize(); if (reduce) S.still(); }, 160); });
    box.addEventListener('pointermove', function (e) { S.pointer = S.pt(e); S.pointer.down = e.buttons > 0 || e.pointerType === 'mouse'; S.pointer.t = performance.now(); if (S.mode && S.mode.move) S.mode.move(S.pointer, e); });
    box.addEventListener('pointerleave', function () { S.pointer = null; });
    box.addEventListener('click', function (e) { if (S.mode && S.mode.tap) { S.mode.tap(S.pt(e)); if (reduce) S.still(); } });
  }
  Swarm.prototype.size = function () {
    var r = this.box.getBoundingClientRect(); this.dpr = Math.min(2, window.devicePixelRatio || 1); this.W = Math.max(60, r.width); this.H = Math.max(60, r.height);
    if (this.free) { this.VW = this.W; this.VH = this.H; this.s = 1; this.ox = this.oy = 0; this.rot = false; this.vw = [0, 0, this.W, this.H]; }
    else {
      var v = (this.mode && this.mode.view) || [0, 0, 600, 420];
      this.rot = !!(this.mode && this.mode.kind === 'body' && this.H / this.W > .85);   // a tall frame: lay the body head-up
      if (this.rot) { v = [8, 84, 604, 252]; this.s = Math.min(this.W / v[3], this.H / v[2]); this.ox = (this.W - v[3] * this.s) / 2; this.oy = (this.H - v[2] * this.s) / 2; }
      else { this.s = Math.min(this.W / v[2], this.H / v[3]); this.ox = (this.W - v[2] * this.s) / 2; this.oy = (this.H - v[3] * this.s) / 2; }
      this.vw = v;
    }
    this.cv.width = Math.round(this.W * this.dpr); this.cv.height = Math.round(this.H * this.dpr);
  };
  Swarm.prototype.pt = function (e) {
    var r = this.cv.getBoundingClientRect(), sx = e.clientX - r.left, sy = e.clientY - r.top, v = this.vw;
    return this.rot ? { x: (sy - this.oy) / this.s + v[0], y: v[1] + v[3] - (sx - this.ox) / this.s } : { x: (sx - this.ox) / this.s + v[0], y: (sy - this.oy) / this.s + v[1] };
  };
  Swarm.prototype.xf = function () {
    var d = this.dpr, s = this.s, v = this.vw;
    if (this.rot) this.ctx.setTransform(0, d * s, -d * s, 0, d * (this.ox + (v[1] + v[3]) * s), d * (this.oy - v[0] * s));
    else this.ctx.setTransform(d * s, 0, 0, d * s, d * (this.ox - v[0] * s), d * (this.oy - v[1] * s));
  };
  Swarm.prototype.label = function (txt) {
    var el = this.labelEl; if (!el || el.dataset.t === txt) return; el.dataset.t = txt;
    if (reduce) { el.textContent = txt; return; }
    el.classList.add('fade'); clearTimeout(el._t); el._t = setTimeout(function () { el.textContent = txt; el.classList.remove('fade'); }, 380);
  };
  Swarm.prototype.dormant = function (from) {   // embers not needed by a shape rest as ash along the floor
    var r = rnd(17 + from);
    for (var i = from; i < this.N; i++) { this.tx[i] = r() * this.VW; this.ty[i] = this.VH - 4 - r() * 16; this.ta[i] = .14; this.tsz[i] = .6; this.tone[i] = 0; }
  };
  Swarm.prototype.set = function (name, params) {
    var make = MODES[name]; if (!make) return;
    var prevKind = this.mode && this.mode.kind;
    this.name = name; this.mode = make(this, params || {}, prevKind); this.size();
    if (reduce) this.still(); else this.kick();
  };
  Swarm.prototype.still = function () {   // reduced motion: let the shape settle, then draw it once
    var t = 9000;
    for (var n = 0; n < 160; n++) { t += 16.7; this.mode.step(t, 16.7, true); this.physics(16.7, true); }
    this.draw(t);
  };
  Swarm.prototype.physics = function (dt, snap) {
    var k = dt / 16.7, kk = this.k * k, dp = Math.pow(this.damp, k);
    for (var i = 0; i < this.N; i++) {
      if (snap) { this.x[i] = this.tx[i]; this.y[i] = this.ty[i]; this.a[i] = this.ta[i]; this.sz[i] = this.tsz[i]; continue; }
      this.vx[i] = (this.vx[i] + (this.tx[i] - this.x[i]) * kk) * dp; this.vy[i] = (this.vy[i] + (this.ty[i] - this.y[i]) * kk) * dp;
      this.x[i] += this.vx[i] * k; this.y[i] += this.vy[i] * k;
      this.a[i] += (this.ta[i] - this.a[i]) * .07 * k; this.sz[i] += (this.tsz[i] - this.sz[i]) * .1 * k;
    }
  };
  Swarm.prototype.draw = function (t) {
    var c = this.ctx, i, h, r;
    c.setTransform(1, 0, 0, 1, 0, 0); c.clearRect(0, 0, this.cv.width, this.cv.height);
    this.xf();
    if (this.mode && this.mode.under) this.mode.under(c, t);
    for (i = 0; i < this.N; i++) {
      if (this.a[i] < .02) continue; h = cl(this.h[i]); r = this.base * (.55 + .85 * h) * this.sz[i];
      c.globalAlpha = cl(this.a[i]); c.fillStyle = LUT[this.tone[i]][h * 63 | 0]; c.beginPath(); c.arc(this.x[i], this.y[i], r, 0, TAU); c.fill();
    }
    c.globalCompositeOperation = 'lighter';
    for (i = 0; i < this.N; i++) {
      h = this.h[i]; if (h < .5 || this.a[i] < .1) continue; r = this.base * (.55 + .85 * h) * this.sz[i] * 2.8;
      c.globalAlpha = cl(this.a[i]) * (h - .5) * .45; c.fillStyle = LUT[this.tone[i]][cl(h) * 63 | 0]; c.beginPath(); c.arc(this.x[i], this.y[i], r, 0, TAU); c.fill();
    }
    c.globalCompositeOperation = 'source-over'; c.globalAlpha = 1;
    if (this.mode && this.mode.over) this.mode.over(c, t);
  };
  Swarm.prototype.frame = function (t, dt) { this.t = t; if (this.mode) this.mode.step(t, dt, false); this.physics(dt, false); this.draw(t); };

  // ---------- body techniques ----------
  function bodyMode(S, prevKind) {
    var B = body(); S.B = B.n; S.k = .06; S.damp = .8; S.base = 2.3;
    for (var i = 0; i < B.n; i++) { S.tx[i] = B.x[i]; S.ty[i] = B.y[i]; S.ta[i] = 1; S.tsz[i] = 1; S.tone[i] = 0; }
    S.dormant(B.n);
    if (prevKind !== 'body') for (i = 0; i < B.n; i++) S.h[i] = .05;
    return B;
  }
  function heat(S, B, cx, cy, R, amt, szAdd) {   // add warmth around a point, falling off to its edge
    var R2 = R * R;
    for (var i = 0; i < B.n; i++) { var dx = B.x[i] - cx, dy = B.y[i] - cy, d2 = dx * dx + dy * dy; if (d2 > R2) continue; var f = 1 - Math.sqrt(d2) / R; S.h[i] = Math.min(1.05, S.h[i] + amt * f); if (szAdd) S.tsz[i] = Math.max(S.tsz[i], 1 + szAdd * f); }
  }
  function cool(S, B, rate, k, floor) { for (var i = 0; i < B.n; i++) { S.h[i] += ((floor || .05) - S.h[i]) * rate * k; S.tsz[i] += (1 - S.tsz[i]) * .03 * k; } }
  function visitor(S, B, k) {   // the visitor's own touch warms the body too
    var p = S.pointer; if (p && p.down && performance.now() - p.t < 120) heat(S, B, p.x, p.y, 20, .05 * k);
  }
  function palm(c, x, y, a, rx) { var g = c.createRadialGradient(x, y, 0, x, y, rx || 26); g.addColorStop(0, 'rgba(255,236,200,' + (.55 * a) + ')'); g.addColorStop(1, 'rgba(255,236,200,0)'); c.fillStyle = g; c.beginPath(); c.ellipse(x, y, (rx || 26), (rx || 26) * .7, 0, 0, TAU); c.fill(); }

  var MODES = {};

  MODES.swedish = function (S, p, prev) {
    var B = bodyMode(S, prev), medium = !!p.medium, add = p.add || {}, ph = 0, rings = [], lastRing = 0;
    var P = path([[296, 197], [250, 193], [200, 191], [150, 187], [120, 178], [112, 160], [138, 149], [190, 160], [240, 168], [290, 172], [300, 188], [296, 197]]);
    var m = { kind: 'body', hands: [], step: function (t, dt) {
      var k = dt / 16.7, sp = add.still ? .68 : 1; ph += dt / 8000 * sp;
      var a = P.at(ph % 1), b = [a[0], 420 - a[1]]; m.hands = [a, b];
      [a, b].forEach(function (q) { heat(S, B, q[0], q[1], medium ? 30 : 22, (medium ? .07 : .045) * k, medium ? .5 : 0); });
      if (add.sound && t - lastRing > 2600) { rings.push(t); lastRing = t; }
      rings = rings.filter(function (r0) { return t - r0 < 4000; });
      rings.forEach(function (r0) { var rad = (t - r0) / 4000 * 520; for (var i = 0; i < B.n; i++) { var d = Math.hypot(B.x[i] - 70, B.y[i] - 210); if (Math.abs(d - rad) < 10) S.h[i] += .025 * k; } });
      var br = add.breath ? breath(t) : 0; if (add.breath) for (var i = 0; i < B.n; i++) if (B.r[i] === 'torso') S.tsz[i] = Math.max(S.tsz[i], 1 + .5 * br);
      cool(S, B, .012, k); visitor(S, B, k);
      S.label(add.breath ? (Math.sin(t / 8000 * TAU) > 0 ? 'Breathe in' : 'And out') : medium ? 'Medium pressure · long strokes' : 'Light pressure · long strokes');
    }, over: function (c, t) {
      m.hands.forEach(function (q) { palm(c, q[0], q[1], 1, medium ? 30 : 24); });
      rings.forEach(function (r0) { var u = (t - r0) / 4000; c.strokeStyle = 'rgba(255,236,200,' + (.4 * (1 - u)) + ')'; c.lineWidth = 1.2; c.beginPath(); c.arc(70, 210, u * 520, 0, TAU); c.stroke(); });
      if (add.still) { c.fillStyle = 'rgba(21,17,14,.28)'; c.fillRect(-200, -200, 1000, 820); }
    } };
    return m;
  };

  MODES.deep = function (S, p, prev) {
    var B = bodyMode(S, prev), level = p.level == null ? 1 : p.level, tool = [0, 0], push = 0;
    var P = path([[292, 192], [240, 190], [190, 188], [150, 184], [128, 170], [150, 158], [190, 168], [230, 176]]);
    return { kind: 'body', step: function (t, dt) {
      var k = dt / 16.7, q = (t % 8000) / 8000, u = (t / 26000) % 2; u = u > 1 ? 2 - u : u;
      tool = P.at(u); push = q < .5 ? sine(q * 2) : 1 - sine((q - .5) * 2);
      heat(S, B, tool[0], tool[1], 12 + 6 * level, (.05 + .05 * level) * push * k, (.6 + .7 * level) * push);
      cool(S, B, .006, k); visitor(S, B, k);
      S.label(q < .5 ? 'Exhale · sink in' : 'Inhale · ease off');
    }, over: function (c) {
      for (var i = 0; i <= level; i++) { var rr = (22 + i * 10) * (1 - .45 * push); c.strokeStyle = 'rgba(255,226,176,' + (.5 - i * .12) + ')'; c.lineWidth = 1.2; c.beginPath(); c.arc(tool[0], tool[1], rr, 0, TAU); c.stroke(); }
      palm(c, tool[0], tool[1], .9, 16);
    } };
  };

  MODES.thai = function (S, p, prev) {
    var B = bodyMode(S, prev), beat = -1, rings = [], t0 = null, stretch = 0, BEAT = 560, NB = 14, CYC = NB * BEAT + 3200;
    var spots = []; for (var j = 0; j < 7; j++) { var x = 548 - j * 38; spots.push([x, 186 + (x > 300 ? 0 : 0)]); spots.push([x, 234]); }
    return { kind: 'body', step: function (t, dt) {
      var k = dt / 16.7, e; if (t0 === null) t0 = t; e = (t - t0) % CYC;
      if (e < NB * BEAT) {
        var b = Math.floor(e / BEAT); stretch += (0 - stretch) * .08 * k;
        if (b !== beat) { beat = b; var s = spots[b % spots.length]; heat(S, B, s[0], s[1], 24, .9, .9); rings.push({ x: s[0], y: s[1], t: t }); }
        S.label('Rhythmic compressions');
      } else { stretch += (1 - stretch) * .05 * k; for (var i = 0; i < B.n; i++) if (B.r[i] === 'leg') S.h[i] += (.42 * stretch - S.h[i]) * .05 * k; S.label('Full-body stretching'); }
      for (i = 0; i < B.n; i++) {
        if (B.r[i] !== 'leg') continue; var f = (B.x[i] - 300) / 250, side = B.y[i] < 210 ? -1 : 1;
        S.tx[i] = B.x[i] + stretch * f * 24; S.ty[i] = B.y[i] + stretch * side * f * 26;
      }
      cool(S, B, .007, k); visitor(S, B, k);
      rings = rings.filter(function (r) { return t - r.t < 900; });
    }, over: function (c, t) {
      rings.forEach(function (r) { var u = (t - r.t) / 900; c.strokeStyle = 'rgba(255,226,176,' + (.8 * (1 - u)) + ')'; c.lineWidth = 1.6; c.beginPath(); c.arc(r.x, r.y, 10 + u * 34, 0, TAU); c.stroke(); });
      var b = beat % NB; for (var i = 0; i < NB; i++) { c.fillStyle = i === b ? '#f2a33a' : 'rgba(243,236,226,.2)'; c.beginPath(); c.arc(300 - NB * 6 + i * 12, 402, i === b ? 3.6 : 2.4, 0, TAU); c.fill(); }
    }, tap: function (q) { heat(S, B, q.x, q.y, 17, .6, .5); rings.push({ x: q.x, y: q.y, t: S.t || performance.now() }); } };
  };

  MODES.lymph = function (S, p, prev) {
    var B = bodyMode(S, prev), T = [112, 210], flow = [], r = rnd(5);
    var V = [[[555, 187], [420, 182], [312, 188], [250, 200], [160, 205], T], [[555, 233], [420, 238], [312, 232], [250, 220], [160, 215], T],
             [[298, 129], [200, 124], [138, 143], T], [[298, 291], [200, 296], [138, 277], T], [[48, 210], [86, 210], T]].map(path);
    var NODES = [[138, 143], [138, 277], [306, 192], [306, 228], [92, 210]];
    for (var i = 0; i < 70; i++) flow.push({ v: i % V.length, u: r() });
    return { kind: 'body', step: function (t, dt) {
      var k = dt / 16.7;
      flow.forEach(function (f) { f.u += .0026 * k * (.6 + .4 * (f.v + 1) / V.length); if (f.u > 1) { f.u = 0; f.v = Math.floor(r() * V.length); } var q = V[f.v].at(f.u); f.x = q[0]; f.y = q[1]; heat(S, B, q[0], q[1], 9, .022 * k); });
      NODES.forEach(function (n, j) { heat(S, B, n[0], n[1], 12, .014 * k * (.5 + .5 * Math.sin(t * .003 + j))); });
      cool(S, B, .02, k); visitor(S, B, k);
      S.label('Flow, toward the heart');
    }, over: function (c) {
      c.strokeStyle = 'rgba(167,191,174,.22)'; c.lineWidth = 1; V.forEach(function (v) { c.beginPath(); for (var i = 0; i <= 30; i++) { var q = v.at(i / 30); if (i) c.lineTo(q[0], q[1]); else c.moveTo(q[0], q[1]); } c.stroke(); });
      c.fillStyle = 'rgba(214,236,222,.9)'; flow.forEach(function (f) { if (f.x == null) return; c.beginPath(); c.arc(f.x, f.y, 1.8, 0, TAU); c.fill(); });
    } };
  };

  MODES.sarga = function (S, p, prev) {
    var B = bodyMode(S, prev), stamps = [], last = -1, t0 = null, STEP = 1100, N = 7, CYC = N * STEP + 2600;
    function foot(x, y, side) {   // heel, ball and toes, pointing toward the head
      return [[x, y, 9, 8], [x - 24, y + side * 1, 12, 10], [x - 39, y - 6, 3.4, 3.4], [x - 41, y, 3.6, 3.6], [x - 40, y + 6, 3.4, 3.4], [x - 36, y + 11 * side, 3, 3]];
    }
    function stamp(x, y, side, t) {
      var parts = foot(x, y, side);
      for (var i = 0; i < B.n; i++) for (var j = 0; j < parts.length; j++) { var q = parts[j], dx = (B.x[i] - q[0]) / (q[2] + 2), dy = (B.y[i] - q[1]) / (q[3] + 2); if (dx * dx + dy * dy < 1) { S.h[i] = 1; S.tsz[i] = 2; break; } }
      heat(S, B, x - 16, y, 34, .16, .5); stamps.push({ parts: parts, t: t });
    }
    return { kind: 'body', step: function (t, dt) {
      var k = dt / 16.7; if (t0 === null) t0 = t; var e = (t - t0) % CYC, n = Math.floor(e / STEP);
      if (n < N && n !== last) { last = n; var side = n % 2 ? 1 : -1; stamp(304 - n * 30, 210 + side * 14, side, t); }
      if (n >= N) last = -1;
      stamps = stamps.filter(function (s) { return t - s.t < 2400; });
      cool(S, B, .0045, k);
      S.label('Barefoot, step by step, deep into the fascia');
    }, over: function (c, t) {
      stamps.forEach(function (s) { var a = 1 - (t - s.t) / 2400; c.strokeStyle = 'rgba(255,226,176,' + (.55 * a) + ')'; c.lineWidth = 1; s.parts.forEach(function (q) { c.beginPath(); c.ellipse(q[0], q[1], q[2] + 3, q[3] + 3, 0, 0, TAU); c.stroke(); }); });
    }, tap: function (q) { stamp(q.x + 16, q.y, 1, S.t || performance.now()); } };
  };

  MODES.reiki = function (S, p, prev) {
    var B = bodyMode(S, prev), near = !!p.near, POS = [[70, 'Head'], [150, 'Shoulders'], [222, 'Heart, from behind'], [282, 'Lower back'], [430, 'Knees'], [548, 'Feet']], idx = 1, hx = 150, picked = -1e9, moved = 0, sparks = [], r = rnd(2);
    var m = { kind: 'body', step: function (t, dt, snap) {
      var k = dt / 16.7;
      if (!snap && t - picked > 14000 && t - moved > 6500) { idx = (idx + 1) % POS.length; moved = t; }
      hx += (POS[idx][0] - hx) * (snap ? 1 : .03 * k);
      var settled = 1 - cl(Math.abs(POS[idx][0] - hx) / 50);
      [190, 230].forEach(function (y) { heat(S, B, hx, y, 34, (near ? .005 : .01) * settled * k); });
      var mean = 0, i; for (i = 0; i < B.n; i++) mean += S.h[i]; mean /= B.n;
      for (i = 0; i < B.n; i++) S.h[i] += (Math.min(.42, mean + .002) - S.h[i]) * .006 * k;   // warmth evens out across the whole body
      if (!snap && settled > .5 && r() < .35) sparks.push({ x: hx + (r() - .5) * 60, y: 200 + (r() - .5) * 50, vy: -.4 - r() * .5, t: t });
      sparks = sparks.filter(function (s) { s.y += s.vy * k; return t - s.t < 2200; });
      S.label(POS[idx][1] + (near ? ' · hands just above' : ' · hands resting on'));
    }, over: function (c, t) {
      var lift = near ? 16 : 0;
      [190, 230].forEach(function (y) { c.fillStyle = 'rgba(0,0,0,' + (near ? .18 : .3) + ')'; c.beginPath(); c.ellipse(hx + 3, y + 3, 24, 14, 0, 0, TAU); c.fill(); palm(c, hx - lift * .4, y - lift, 1, 26); c.strokeStyle = 'rgba(255,236,200,.5)'; c.lineWidth = 1; c.beginPath(); c.ellipse(hx - lift * .4, y - lift, 22, 13, 0, 0, TAU); c.stroke(); });
      sparks.forEach(function (s) { var a = 1 - (t - s.t) / 2200; c.fillStyle = 'rgba(255,214,160,' + a + ')'; c.beginPath(); c.arc(s.x, s.y, 1.6, 0, TAU); c.fill(); });
    }, tap: function (q) { var best = 0; POS.forEach(function (v, i) { if (Math.abs(v[0] - q.x) < Math.abs(POS[best][0] - q.x)) best = i; }); idx = best; picked = S.t || performance.now(); } };
    return m;
  };

  // ---------- yoga: embers ride the bones of a figure that flows, then holds ----------
  MODES.yoga = function (S, p) {
    S.k = .2; S.damp = .62; S.base = 2.1;
    var POSES = {
      mountain: { F: [300, 340], K: [300, 286], H: [300, 232], S: [300, 142], E: [306, 188], W: [308, 230], C: [300, 112] },
      reach:    { F: [300, 340], K: [300, 286], H: [300, 232], S: [300, 142], E: [298, 96], W: [296, 54], C: [304, 112] },
      fold:     { F: [300, 340], K: [300, 286], H: [296, 232], S: [328, 300], E: [324, 326], W: [318, 340], C: [338, 322] },
      plank:    { F: [182, 338], K: [226, 320], H: [270, 300], S: [380, 270], E: [380, 305], W: [380, 340], C: [404, 258] },
      updog:    { F: [182, 338], K: [228, 336], H: [276, 330], S: [372, 264], E: [376, 302], W: [378, 340], C: [392, 242] },
      downdog:  { F: [222, 340], K: [242, 290], H: [262, 238], S: [330, 300], E: [352, 320], W: [374, 340], C: [342, 318] },
      child:    { F: [214, 340], K: [272, 340], H: [226, 318], S: [318, 328], E: [362, 338], W: [404, 340], C: [338, 330] }
    };
    var SEQ = [['reach', 900, 300], ['fold', 1000, 300], ['plank', 1000, 300], ['updog', 900, 300], ['downdog', 1000, 700], ['child', 2200, 0]];
    var BONES = [['H', 'S', 15], ['S', 'E', 6], ['E', 'W', 5], ['H', 'K', 10], ['K', 'F', 7]], M = 760, own = [], r = rnd(11), cur = clone(POSES.mountain), from, seg = 0, state = 'flow', t0 = null, prevP = null;
    function clone(o) { var c = {}; for (var k in o) c[k] = o[k].slice(); return c; }
    var tot = 0; BONES.forEach(function (b) { tot += b[2] * 60; }); tot += 18 * 40;
    for (var i = 0; i < M; i++) {
      var pick = r() * tot, bi = -1, acc = 0; for (var j = 0; j < BONES.length; j++) { acc += BONES[j][2] * 60; if (pick < acc) { bi = j; break; } }
      own.push({ b: bi, u: r(), v: (r() * 2 - 1), ang: r() * TAU, rr: Math.sqrt(r()) });
    }
    for (i = 0; i < M; i++) { S.ta[i] = 1; S.tsz[i] = 1; S.tone[i] = 0; } S.dormant(M);
    function begin(t) { state = 'flow'; seg = 0; from = clone(cur); t0 = t; }
    var m = { kind: 'yoga', view: [130, 30, 340, 330], step: function (t, dt, snap) {
      var k = dt / 16.7;
      if (t0 === null) begin(t);
      if (snap) { cur = clone(POSES.child); state = 'hold'; }
      else if (state === 'flow') {
        var s = SEQ[seg], e = t - t0, f = Math.min(1, e / s[1]), to = POSES[s[0]];
        for (var key in cur) { cur[key][0] = from[key][0] + (to[key][0] - from[key][0]) * sine(f); cur[key][1] = from[key][1] + (to[key][1] - from[key][1]) * sine(f); }
        if (e > s[1] + s[2]) { if (seg === SEQ.length - 1) { state = 'hold'; t0 = t; } else { seg++; from = clone(cur); t0 = t; } }
      } else if (state === 'hold' && t - t0 > 9000) { from = clone(cur); var back = t; state = 'rise'; t0 = back; }
      else if (state === 'rise') { var g = Math.min(1, (t - t0) / 1200); for (key in cur) { cur[key][0] = from[key][0] + (POSES.mountain[key][0] - from[key][0]) * sine(g); cur[key][1] = from[key][1] + (POSES.mountain[key][1] - from[key][1]) * sine(g); } if (g >= 1) begin(t); }
      var speed = 0; if (prevP) for (key in cur) speed += Math.hypot(cur[key][0] - prevP[key][0], cur[key][1] - prevP[key][1]); prevP = clone(cur);
      var br = state === 'hold' ? breath(t - t0) : 0, heatT = state === 'hold' ? .18 + .22 * br : cl(.3 + speed * .06);
      for (i = 0; i < M; i++) {
        var o = own[i], hx, hy;
        if (o.b < 0) { hx = cur.C[0] + Math.cos(o.ang) * 17 * o.rr; hy = cur.C[1] + Math.sin(o.ang) * 17 * o.rr; }
        else { var b = BONES[o.b], A = cur[b[0]], Bp = cur[b[1]], dx = Bp[0] - A[0], dy = Bp[1] - A[1], L = Math.hypot(dx, dy) || 1; hx = A[0] + dx * o.u - dy / L * o.v * b[2] * .5; hy = A[1] + dy * o.u + dx / L * o.v * b[2] * .5; }
        S.tx[i] = hx; S.ty[i] = hy - (state === 'hold' ? br * 2 * (1 - o.u) : 0);
        S.h[i] += (heatT * (.7 + .3 * Math.sin(i)) - S.h[i]) * .08 * k;
      }
      S.label(state === 'hold' ? 'Yin · hold, and breathe' : 'Vinyasa · flow');
    }, under: function (c) { c.strokeStyle = 'rgba(243,236,226,.14)'; c.lineWidth = 1; c.beginPath(); c.moveTo(120, 346); c.lineTo(480, 346); c.stroke(); },
      tap: function () { if (state === 'hold') { from = clone(cur); state = 'rise'; t0 = S.t || performance.now(); } } };
    return m;
  };

  // ---------- zen mountain: ridges of cool embers, a river that slows the longer you stay ----------
  MODES.zen = function (S) {
    S.k = .08; S.damp = .76; S.base = 2;
    var r = rnd(41), n = 0, calm = 0, RIV = 420, riv = [], lastMove = null, ph = [r() * TAU, r() * TAU, r() * TAU, r() * TAU];
    function ridge(x, i) { return [150, 196, 238][i] - [70, 56, 40][i] * (.5 + .3 * Math.sin(x / 600 * 5 + ph[i]) + .14 * Math.sin(x / 600 * 13 + ph[3] * i) + .06 * Math.sin(x / 600 * 31 + i)); }
    for (var i = 0; i < 3; i++) for (var x = 6; x < 594; x += 5.2) {
      var y = ridge(x, i); S.tx[n] = x; S.ty[n] = y; S.h[n] = [.18, .28, .4][i]; S.ta[n] = [.55, .75, 1][i]; S.tsz[n] = .9; S.tone[n] = 0; n++;
      for (var f = 0; f < 3 && n < 960; f++) if (r() < .6) { S.tx[n] = x + r() * 4; S.ty[n] = y + 5 + Math.pow(r(), 1.6) * (90 - i * 20); S.h[n] = [.12, .18, .26][i] * (.6 + .4 * r()); S.ta[n] = [.4, .55, .8][i]; S.tsz[n] = .75; S.tone[n] = 0; n++; }
    }
    for (i = 0; i < 46; i++) { var a = r() * TAU, rr = Math.sqrt(r()) * 24; S.tx[n] = 462 + Math.cos(a) * rr; S.ty[n] = 98 + Math.sin(a) * rr; S.h[n] = .55 + .4 * r(); S.ta[n] = .9; S.tsz[n] = .8; S.tone[n] = 0; n++; }
    var R0 = n; for (i = 0; i < RIV && n < S.N; i++, n++) { riv.push({ i: n, u: r(), v: r() * 2 - 1 }); S.tone[n] = 2; S.ta[n] = 1; S.tsz[n] = .9; }
    S.dormant(n);
    function bez(a, b, c, d, u) { var m = 1 - u; return m * m * m * a + 3 * m * m * u * b + 3 * m * u * u * c + u * u * u * d; }
    function rv(u) { return [bez(372, 470, 80, 230, u), bez(236, 300, 340, 430, u)]; }
    return { kind: 'zen', view: [0, 40, 600, 380], step: function (t, dt, snap) {
      var k = dt / 16.7; calm = snap ? 1 : Math.min(1, calm + dt / 15000);
      var sp = (1 - calm) * .0045 + .0006;
      riv.forEach(function (q) {
        if (!snap) { q.u += sp * k * (.4 + q.u); if (q.u > 1) { q.u = 0; q.v = r() * 2 - 1; S.x[q.i] = rv(0)[0]; S.y[q.i] = rv(0)[1]; } }
        var c = rv(q.u), c2 = rv(Math.min(1, q.u + .01)), an = Math.atan2(c2[1] - c[1], c2[0] - c[0]) + Math.PI / 2, w = 3 + 60 * q.u * q.u;
        S.tx[q.i] = c[0] + Math.cos(an) * w * q.v; S.ty[q.i] = c[1] + Math.sin(an) * w * q.v;
        S.h[q.i] = .25 + .55 * (1 - calm) * Math.abs(Math.sin(q.u * 30 + t * .004 * (1 - calm) + q.v * 3));
      });
      S.k = .08 + .3 * (1 - calm);
      S.label(calm < .35 ? 'Rushing' : calm < .8 ? 'Slowing' : 'Still enough to rest');
    }, move: function (q, e) {
      if (lastMove) { var v = Math.hypot(e.clientX - lastMove[0], e.clientY - lastMove[1]) / Math.max(8, e.timeStamp - lastMove[2]); if (v > 1) calm = Math.max(0, calm - .03 * v); }
      lastMove = [e.clientX, e.clientY, e.timeStamp];
    } };
  };

  // ---------- astrology: the stars of your sun sign ----------
  var SIGNS = [   // stylised star patterns in a 0..1 box: [stars], [lines as index pairs]
    ['Aries', [[.12, .58], [.46, .44], [.7, .4], [.86, .5]], [[0, 1], [1, 2], [2, 3]]],
    ['Taurus', [[.5, .55], [.42, .48], [.38, .4], [.47, .63], [.57, .6], [.14, .22], [.84, .3]], [[2, 1], [1, 0], [0, 3], [3, 4], [2, 5], [4, 6]]],
    ['Gemini', [[.25, .15], [.3, .45], [.32, .8], [.62, .12], [.66, .44], [.7, .82], [.3, .45]], [[0, 1], [1, 2], [3, 4], [4, 5], [0, 3], [1, 4]]],
    ['Cancer', [[.5, .45], [.45, .2], [.22, .82], [.78, .78], [.52, .55]], [[1, 0], [0, 4], [4, 2], [4, 3]]],
    ['Leo', [[.2, .3], [.28, .18], [.4, .2], [.42, .36], [.32, .5], [.62, .55], [.85, .62], [.7, .4]], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3]]],
    ['Virgo', [[.15, .3], [.3, .35], [.44, .45], [.56, .4], [.7, .3], [.5, .65], [.62, .82], [.82, .55]], [[0, 1], [1, 2], [2, 3], [3, 4], [2, 5], [5, 6], [3, 7]]],
    ['Libra', [[.5, .2], [.3, .45], [.7, .45], [.25, .75], [.75, .78]], [[0, 1], [0, 2], [1, 2], [1, 3], [2, 4]]],
    ['Scorpio', [[.1, .25], [.18, .35], [.28, .42], [.38, .5], [.48, .62], [.55, .76], [.68, .82], [.8, .74], [.84, .6]], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8]]],
    ['Sagittarius', [[.3, .55], [.42, .45], [.55, .5], [.6, .35], [.72, .42], [.5, .72], [.38, .7]], [[0, 1], [1, 2], [2, 3], [3, 4], [2, 5], [5, 6], [6, 0]]],
    ['Capricorn', [[.15, .3], [.3, .55], [.5, .75], [.75, .65], [.88, .35], [.6, .45]], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]]],
    ['Aquarius', [[.12, .4], [.28, .32], [.42, .42], [.56, .35], [.66, .55], [.8, .48], [.88, .7]], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]],
    ['Pisces', [[.12, .2], [.2, .35], [.34, .55], [.5, .7], [.66, .6], [.8, .5], [.9, .4], [.82, .3]], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 5]]]
  ];
  var CUSP = [[1, 20, 10], [2, 19, 11], [3, 21, 0], [4, 20, 1], [5, 21, 2], [6, 21, 3], [7, 23, 4], [8, 23, 5], [9, 23, 6], [10, 23, 7], [11, 22, 8], [12, 22, 9]];   // [month, first day, sign that starts then]
  function signOf(mo, d) { var c = CUSP[mo - 1]; return d < c[1] ? (c[2] + 11) % 12 : c[2]; }
  MODES.astro = function (S, p) {
    S.k = .05; S.damp = .82; S.base = 2;
    var sg = SIGNS[p.sign == null ? signOf(new Date().getMonth() + 1, new Date().getDate()) : p.sign], r = rnd(13), n = 0, t0 = null, stars = sg[1].map(function (q) { return [110 + q[0] * 380, 50 + q[1] * 300]; });
    stars.forEach(function (st, si) { for (var j = 0; j < 22; j++) { var a = r() * TAU, rr = Math.pow(r(), 2) * 9; S.tx[n] = st[0] + Math.cos(a) * rr; S.ty[n] = st[1] + Math.sin(a) * rr; S.h[n] = .7 + .3 * (1 - rr / 9); S.ta[n] = 1; S.tsz[n] = 1.1; S.tone[n] = 0; n++; } });
    var F = n; for (; n < S.N; n++) { S.tx[n] = r() * 600; S.ty[n] = r() * 400; S.h[n] = .08 + r() * .3; S.ta[n] = .25 + r() * .5; S.tsz[n] = .4 + r() * .5; S.tone[n] = 0; }
    S.label(sg[0]);
    return { kind: 'astro', step: function (t, dt, snap) { if (t0 === null) t0 = t; if (snap) t0 = t - 9000; for (var i = F; i < S.N; i += 7) S.tsz[i] = .4 + .4 * (.5 + .5 * Math.sin(t * .002 + i)); },
      over: function (c, t) { var g = cl((t - t0 - 600) / 2400); c.strokeStyle = 'rgba(255,226,176,.55)'; c.lineWidth = 1.1; sg[2].forEach(function (l, i) { var f = cl(g * sg[2].length - i); if (f <= 0) return; var a = stars[l[0]], b = stars[l[1]]; c.beginPath(); c.moveTo(a[0], a[1]); c.lineTo(a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f); c.stroke(); }); } };
  };

  // ---------- herbs: a vessel fills with herbs, from the bottom up ----------
  var VESSEL = {};
  function vessel(kind) {
    if (VESSEL[kind]) return VESSEL[kind];
    var c = document.createElement('canvas'); c.width = 600; c.height = 420; var g = c.getContext('2d'), outline = new Path2D();
    if (kind === 'tea') { outline.moveTo(196, 200); outline.lineTo(404, 200); outline.bezierCurveTo(404, 300, 360, 340, 300, 340); outline.bezierCurveTo(240, 340, 196, 300, 196, 200); outline.moveTo(404, 226); outline.bezierCurveTo(456, 226, 456, 290, 392, 292); outline.moveTo(170, 352); outline.bezierCurveTo(230, 372, 370, 372, 430, 352); }
    else if (kind === 'rollie') { outline.roundRect ? outline.roundRect(262, 150, 76, 196, 18) : outline.rect(262, 150, 76, 196); outline.moveTo(278, 150); outline.lineTo(278, 108); outline.lineTo(322, 108); outline.lineTo(322, 150); outline.moveTo(312, 346); outline.arc(300, 352, 12, 0, TAU); }
    else { outline.moveTo(276, 206); outline.lineTo(276, 186); outline.lineTo(324, 186); outline.lineTo(324, 206); outline.bezierCurveTo(360, 214, 364, 236, 364, 260); outline.lineTo(364, 330); outline.quadraticCurveTo(364, 346, 348, 346); outline.lineTo(252, 346); outline.quadraticCurveTo(236, 346, 236, 330); outline.lineTo(236, 260); outline.bezierCurveTo(236, 236, 240, 214, 276, 206); outline.moveTo(290, 186); outline.lineTo(290, 150); outline.quadraticCurveTo(300, 104, 310, 150); outline.lineTo(310, 186); }
    g.fillStyle = '#000';
    if (kind === 'tea') { g.beginPath(); g.moveTo(200, 214); g.lineTo(400, 214); g.bezierCurveTo(398, 300, 358, 334, 300, 334); g.bezierCurveTo(242, 334, 202, 300, 200, 214); g.fill(); }
    else if (kind === 'rollie') { g.fillRect(268, 176, 64, 164); }
    else { g.beginPath(); g.moveTo(242, 262); g.bezierCurveTo(242, 236, 250, 222, 280, 214); g.lineTo(320, 214); g.bezierCurveTo(350, 222, 358, 236, 358, 262); g.lineTo(358, 328); g.quadraticCurveTo(358, 340, 346, 340); g.lineTo(254, 340); g.quadraticCurveTo(242, 340, 242, 328); g.fill(); }
    var d = g.getImageData(0, 0, 600, 420).data, pts = [], r = rnd(21);
    for (var y = 2; y < 420; y += 6) for (var x = 2; x < 600; x += 6) if (d[(y * 600 + x) * 4 + 3] > 128) pts.push([x + (r() - .5) * 2, y + (r() - .5) * 2]);
    pts.sort(function (a, b) { return b[1] - a[1]; });
    return (VESSEL[kind] = { pts: pts, outline: outline });
  }
  MODES.herbs = function (S, p) {
    S.k = .07; S.damp = .78; S.base = 2.4;
    var kind = p.kind || 'tea', V = vessel(kind), n = V.pts.length, r = rnd(31), t0 = null, rel = new Uint8Array(n);
    var tone = kind === 'tea' ? 1 : 0, hv = kind === 'tea' ? .55 : kind === 'rollie' ? .72 : .5;
    for (var i = 0; i < n; i++) { S.tx[i] = 300 + (r() - .5) * 30; S.ty[i] = 20; S.ta[i] = 0; S.tone[i] = tone; S.h[i] = hv * (.6 + .4 * r()); S.tsz[i] = 1; }
    S.dormant(n);
    S.label(kind === 'tea' ? 'Teas' : kind === 'rollie' ? 'Rollies' : 'Tinctures');
    return { kind: 'herbs', step: function (t, dt, snap) {
      if (t0 === null) t0 = t;
      var due = snap ? n : Math.floor((t - t0) / 3.2);
      for (var i = 0; i < Math.min(n, due); i++) if (!rel[i]) { rel[i] = 1; S.x[i] = 300 + (r() - .5) * 16; S.y[i] = 30 + r() * 10; S.vx[i] = S.vy[i] = 0; S.tx[i] = V.pts[i][0]; S.ty[i] = V.pts[i][1]; S.ta[i] = 1; S.a[i] = .9; }
    }, over: function (c) { c.strokeStyle = 'rgba(243,236,226,.8)'; c.lineWidth = 2; c.lineCap = 'round'; c.stroke(V.outline); } };
  };

  // ---------- the hero: ash → phoenix → ash ----------
  MODES.phoenix = function (S) {
    var P = window.EP_PHOENIX || [], n = Math.min(P.length, S.N), r = rnd(5), ign = [], t0 = null, cx, cy, sc;
    S.base = 1.7; S.k = .03; S.damp = .86;
    function layout() { var wide = S.W > 900; cx = S.W * (wide ? .76 : .5); cy = S.H * (wide ? .36 : .3); sc = Math.min(S.W * (wide ? .3 : .44), S.H * .3); S.base = Math.max(1.2, sc / 150); }
    layout();
    for (var i = 0; i < n; i++) { S.x[i] = r() * S.W; S.y[i] = S.H - r() * 30; S.h[i] = 0; S.a[i] = .5; ign.push(200 + (1 - (P[i][1] + 1) / 2) * 1200 + r() * 900); }
    S.dormant(n); for (i = n; i < S.N; i++) S.ta[i] = 0;
    return { kind: 'phoenix', resize: layout, step: function (t, dt, snap) {
      var k = dt / 16.7, prog = cl(window.scrollY / (S.H * .85)), pt = S.pointer;
      if (t0 === null) t0 = t; var e = snap ? 99999 : t - t0;
      for (var i = 0; i < n; i++) {
        var lit = e > ign[i], fx = cx + P[i][0] * sc, fy = cy + P[i][1] * sc;
        if (!snap) { var wing = Math.max(0, Math.abs(P[i][0]) - .16), flap = Math.sin(t * .0017); fy -= flap * wing * wing * sc * .7; fx -= (P[i][0] > 0 ? 1 : -1) * Math.max(0, flap) * wing * sc * .1; }   // the wings beat, slowly
        var flick = .55 + .3 * Math.sin(t * .006 + i * 1.7) * Math.sin(t * .0023 + i);
        var gx = (i * 97 % 1000) / 1000 * S.W, gy = S.H - 6 - (i % 7) * 3;   // its place in the ash
        var ground = snap ? 0 : prog;
        S.tx[i] = lit ? fx + (gx - fx) * ground + Math.sin(t * .001 + i) * 2 : gx; S.ty[i] = lit ? fy + (gy - fy) * ground + Math.cos(t * .0013 + i) * 2 : gy;
        var target = lit ? (snap ? .75 : flick) * (1 - ground * .9) : .02;
        S.h[i] += (target - S.h[i]) * (lit && S.h[i] < .3 ? .2 : .05) * k; S.ta[i] = lit ? 1 : .35; S.tsz[i] = 1;
        if (pt && !snap) { var dx = S.x[i] - pt.x, dy = S.y[i] - pt.y, d2 = dx * dx + dy * dy; if (d2 < 6400) { var f = 1 - Math.sqrt(d2) / 80; S.h[i] = Math.min(1, S.h[i] + .08 * f); S.vx[i] += dx * .01 * f; S.vy[i] += dy * .01 * f; } }
      }
    } };
  };
  MODES.sparks = function (S) {
    var r = rnd(8), n = Math.min(S.N, 180); S.base = 1.6; S.k = 0; S.damp = 1;
    for (var i = 0; i < n; i++) { S.x[i] = r() * S.W; S.y[i] = S.H * r(); S.h[i] = r(); S.ta[i] = S.a[i] = 1; S.tsz[i] = S.sz[i] = .6 + r(); }
    for (i = n; i < S.N; i++) S.ta[i] = S.a[i] = 0;
    return { kind: 'sparks', step: function (t, dt, snap) {
      var k = dt / 16.7;
      for (var i = 0; i < n; i++) {
        if (!snap) { S.y[i] -= (.35 + S.sz[i] * .35) * k; S.x[i] += Math.sin(t * .001 + i) * .3 * k; S.h[i] -= .0018 * k; }
        if (S.y[i] < -10 || S.h[i] < .05) { S.y[i] = S.H + 5; S.x[i] = r() * S.W; S.h[i] = .7 + r() * .3; }
        S.tx[i] = S.x[i]; S.ty[i] = S.y[i]; S.a[i] = cl(S.h[i] * 1.4);
      }
    } };
  };

  // ---------- wiring ----------
  window.EPswarm = { Swarm: Swarm, signOf: signOf, SIGNS: SIGNS };
  var LABEL = { swedish: 'Swedish', deep: 'Deep tissue', thai: 'Thai', lymph: 'Lymphatic', sarga: 'Sarga', reiki: 'Reiki', yoga: 'Yoga', zen: 'Zen mountain', astro: 'Astrology', herbs: 'Herbs' };

  document.querySelectorAll('[data-hero]').forEach(function (el) { var S = new Swarm(el, { free: true, N: (window.EP_PHOENIX || []).length || 1200 }); S.set('phoenix'); });
  document.querySelectorAll('[data-sparks]').forEach(function (el) { var S = new Swarm(el, { free: true, N: +(el.dataset.n || 180) }); S.set('sparks'); });

  document.querySelectorAll('[data-swarm]').forEach(function (el) {
    var S = new Swarm(el, { N: 1400 }), mode = el.dataset.swarm, params = {};
    if (mode === 'index') {   // one kiln for the whole list: each row shows its own technique
      var rows = document.querySelectorAll('.list a[data-tech]'), first = rows[0] ? rows[0].dataset.tech : 'swedish';
      function show(a) { rows.forEach(function (o) { o.classList.toggle('on', o === a); }); S.set(a.dataset.tech, a.dataset.tech === 'herbs' ? { kind: 'tea' } : {}); }
      rows.forEach(function (a) { a.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') show(a); }); a.addEventListener('focus', function () { show(a); }); });
      if (hasIO && matchMedia('(max-width: 900px)').matches) { var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) show(e.target); }); }, { rootMargin: '-55% 0px -40% 0px' }); rows.forEach(function (a) { io.observe(a); }); }
      if (rows[0]) show(rows[0]); else S.set(first);
      return;
    }
    S.set(mode, params);
    function group(sel, fn) { var bs = document.querySelectorAll(sel); bs.forEach(function (b) { b.addEventListener('click', function () { bs.forEach(function (o) { o.setAttribute('aria-pressed', String(o === b)); }); fn(b); }); }); }
    if (mode === 'swedish') {
      group('[data-pressure]', function (b) { params.medium = b.dataset.pressure === 'medium'; S.set('swedish', params); });
      document.querySelectorAll('[data-addon]').forEach(function (b) { b.addEventListener('click', function () { params.add = params.add || {}; var k = b.dataset.addon; params.add[k] = !params.add[k]; b.setAttribute('aria-pressed', String(params.add[k])); S.set('swedish', params); }); });
    }
    if (mode === 'reiki') group('[data-reiki]', function (b) { S.set('reiki', { near: b.dataset.reiki === 'near' }); });
    if (mode === 'deep') { var d = document.getElementById('depth'), o = document.getElementById('depthOut'); if (d) d.addEventListener('input', function () { o.textContent = ['Firm', 'Deep', 'Deeper'][+d.value]; S.set('deep', { level: +d.value }); }); }
    if (mode === 'herbs') group('[data-vessel]', function (b) { S.set('herbs', { kind: b.dataset.vessel }); });
    if (mode === 'astro') {
      var mo = document.getElementById('month'), dy = document.getElementById('day'), out = document.getElementById('signOut');
      function days() { var n = new Date(2024, +mo.value, 0).getDate(), cur = dy.value; dy.innerHTML = ''; for (var i = 1; i <= n; i++) dy.add(new Option(i, i)); dy.value = Math.min(+cur || 1, n); }
      function pick() { var s = signOf(+mo.value, +dy.value); S.set('astro', { sign: s }); out.textContent = 'Your sun sign: ' + SIGNS[s][0] + '. A reading explores your whole birth chart.'; }
      if (mo) { mo.value = new Date().getMonth() + 1; days(); dy.value = new Date().getDate(); mo.addEventListener('change', function () { days(); pick(); }); dy.addEventListener('change', pick); pick(); }
    }
  });
})();
