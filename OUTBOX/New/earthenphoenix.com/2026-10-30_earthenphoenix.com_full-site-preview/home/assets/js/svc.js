/* Earthen Phoenix: one signature animation per service, each drawn from what the session physically does.
   reiki    hands move on or just above a clothed body; warmth gathers and evens out (balance)
   swedish  long effleurage strokes leave a warm oil sheen; light or medium pressure; sound, meditation, breathwork add-ons
   deep     a forearm sinks through skin, fascia and muscle on the exhale and eases on the inhale; knots smooth out
   thai     palm-walking compressions in rhythm, then a held leg stretch and knee-to-chest
   lymph    six steps of the firming treatment, told by scroll: brush, flow, wrap, towel, head & neck, cream
   sarga    a bare foot glides along the back while the strap takes the weight; tangled fascia lines straighten
   zen      a mountain river that slows from rushing to still while you stay with it
   finder   the logo's banded circle as a depth gauge: how much pressure each session uses
   Every stage runs only while on screen, pauses in background tabs and draws a still, final frame for reduced motion. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;
  var TAU = Math.PI * 2;
  function sine(x) { x = Math.max(0, Math.min(1, x)); return -(Math.cos(Math.PI * x) - 1) / 2; }
  function smooth(x) { x = Math.max(0, Math.min(1, x)); return x * x * (3 - 2 * x); }
  function breath(t) { return .5 - .5 * Math.cos(t / 8000 * TAU); }   // 4 s in, 4 s out, the same breath used across the site
  function seeded(s) { return function () { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }; }
  function gauss(d, w) { return Math.exp(-(d / w) * (d / w)); }
  function caption(el, txt) {
    if (!el || el.dataset.t === txt) return; el.dataset.t = txt;
    if (reduce) { el.textContent = txt; return; }
    el.classList.add('fade'); clearTimeout(el._t); el._t = setTimeout(function () { el.textContent = txt; el.classList.remove('fade'); }, 450);
  }
  function pressGroup(sel, cb) {   // segmented buttons: one pressed at a time
    var bs = document.querySelectorAll(sel);
    bs.forEach(function (b) { b.addEventListener('click', function () { bs.forEach(function (o) { o.setAttribute('aria-pressed', String(o === b)); }); cb(b); }); });
  }

  // a canvas that fits its box, with a virtual scene of VW x VH units letterboxed inside it
  function Stage(box, VW, VH, api) {
    var cv = document.createElement('canvas'); cv.setAttribute('aria-hidden', 'true'); box.insertBefore(cv, box.firstChild);
    var ctx = cv.getContext('2d'), S = { box: box, cv: cv, ctx: ctx, VW: VW, VH: VH, t: 0 };
    function size() {
      var r = box.getBoundingClientRect(); S.dpr = Math.min(2, window.devicePixelRatio || 1); S.W = Math.max(50, r.width); S.H = Math.max(50, r.height);
      cv.width = Math.round(S.W * S.dpr); cv.height = Math.round(S.H * S.dpr);
      S.s = Math.min(S.W / VW, S.H / VH); S.ox = (S.W - VW * S.s) / 2; S.oy = (S.H - VH * S.s) / 2;
      S.L = -S.ox / S.s; S.R = (S.W - S.ox) / S.s; S.T = -S.oy / S.s; S.B = (S.H - S.oy) / S.s;
    }
    S.full = function () { ctx.setTransform(S.dpr, 0, 0, S.dpr, 0, 0); };
    S.scene = function () { ctx.setTransform(S.dpr * S.s, 0, 0, S.dpr * S.s, S.dpr * S.ox, S.dpr * S.oy); };
    S.pt = function (e) { var r = cv.getBoundingClientRect(); return [(e.clientX - r.left - S.ox) / S.s, (e.clientY - r.top - S.oy) / S.s]; };
    var visible = false, raf = 0, prev = 0;
    function still() { (api.still || api.frame)(S, 6000, 16.7); }
    function loop(now) {
      raf = 0; if (!visible || document.hidden) return;
      var dt = prev ? Math.min(50, now - prev) : 16.7; prev = now; S.t = now; api.frame(S, now, dt); raf = requestAnimationFrame(loop);
    }
    function start() { if (!raf && !reduce && visible && !document.hidden) { prev = 0; raf = requestAnimationFrame(loop); } }
    S.redraw = function () { if (reduce) still(); };
    size(); if (api.init) api.init(S);
    if (reduce) still();
    else {
      if (hasIO) new IntersectionObserver(function (es) { es.forEach(function (e) { visible = e.isIntersecting; start(); }); }, { rootMargin: '80px' }).observe(box);
      else { visible = true; start(); }
      document.addEventListener('visibilitychange', start);
    }
    addEventListener('resize', function () { clearTimeout(S.rt); S.rt = setTimeout(function () { size(); if (api.resize) api.resize(S); if (reduce) still(); }, 150); });
    return S;
  }
  function bg(S, c) { S.full(); S.ctx.fillStyle = c; S.ctx.fillRect(0, 0, S.W, S.H); S.scene(); }
  function line(ctx, pts) { ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]); for (var i = 1; i < pts.length; i++) ctx.lineTo(pts[i][0], pts[i][1]); }
  function smoothPath(ctx, pts, close) {   // a curve through the midpoints, so hand-placed points read as a soft outline
    ctx.beginPath(); ctx.moveTo(pts[0][0], pts[0][1]);
    for (var i = 1; i < pts.length - 1; i++) { var mx = (pts[i][0] + pts[i + 1][0]) / 2, my = (pts[i][1] + pts[i + 1][1]) / 2; ctx.quadraticCurveTo(pts[i][0], pts[i][1], mx, my); }
    ctx.lineTo(pts[pts.length - 1][0], pts[pts.length - 1][1]); if (close) ctx.closePath();
  }
  function sampler(pts, n) {   // evenly spaced points along a Catmull-Rom curve, for things that travel a path
    var out = [], i, k;
    for (i = 0; i < pts.length - 1; i++) {
      var p0 = pts[Math.max(0, i - 1)], p1 = pts[i], p2 = pts[i + 1], p3 = pts[Math.min(pts.length - 1, i + 2)];
      for (k = 0; k < 24; k++) {
        var t = k / 24, t2 = t * t, t3 = t2 * t;
        out.push([.5 * (2 * p1[0] + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3),
                  .5 * (2 * p1[1] + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)]);
      }
    }
    out.push(pts[pts.length - 1]);
    var len = [0]; for (i = 1; i < out.length; i++) len.push(len[i - 1] + Math.hypot(out[i][0] - out[i - 1][0], out[i][1] - out[i - 1][1]));
    var L = len[len.length - 1];
    return { L: L, at: function (u) {
      var d = Math.max(0, Math.min(1, u)) * L, lo = 0, hi = len.length - 1;
      while (hi - lo > 1) { var m = (lo + hi) >> 1; if (len[m] < d) lo = m; else hi = m; }
      var f = (d - len[lo]) / Math.max(1e-6, len[hi] - len[lo]);
      return [out[lo][0] + (out[hi][0] - out[lo][0]) * f, out[lo][1] + (out[hi][1] - out[lo][1]) * f];
    } };
  }

  var sig = {};

  // ---------- REIKI: on or near the clothed body ----------
  sig.reiki = function (box) {
    var cap = box.querySelector('.cap');
    var C = [[182, 314], [215, 302], [262, 284], [322, 277], [382, 285], [442, 289], [502, 283], [562, 293], [622, 301], [682, 307], [708, 300], [720, 268], [736, 268], [744, 300], [748, 330]];
    function surf(x) {
      if (x < 182) { var dx = x - 150; return dx > -30 ? 300 - Math.sqrt(Math.max(0, 900 - dx * dx)) : 330; }
      for (var i = 1; i < C.length; i++) if (x <= C[i][0]) { var a = C[i - 1], b = C[i], f = smooth((x - a[0]) / (b[0] - a[0])); return a[1] + (b[1] - a[1]) * f; }
      return 330;
    }
    var POS = [[150, 'Head'], [305, 'Heart'], [432, 'Belly'], [522, 'Hips'], [626, 'Knees'], [724, 'Feet']];
    var N = 64, X0 = 110, X1 = 760, E = new Float32Array(N), parts = [], idx = 1, near = false, hx = 305, hy = 200, vx = 0, vy = 0, lastPick = -1e9, lastMove = 0, rand = seeded(7);
    function setPos(i, t) { idx = i; lastMove = t; caption(cap, POS[i][1] + (near ? ' · hands just above' : ' · hands resting on')); }
    function draw(S, t, dt) {
      var ctx = S.ctx, k = dt / 16.7, i;
      bg(S, '#24180f');
      var glow = ctx.createRadialGradient(120, 90, 10, 120, 90, 420); glow.addColorStop(0, 'rgba(255,190,120,.22)'); glow.addColorStop(1, 'rgba(255,190,120,0)');
      ctx.fillStyle = glow; ctx.fillRect(S.L, S.T, S.R - S.L, S.B - S.T);
      // candle, as in her session photos
      ctx.fillStyle = '#e9d8bd'; ctx.fillRect(108, 104, 22, 46);
      var fl = 1 + (reduce ? 0 : .08 * Math.sin(t * .013) + .05 * Math.sin(t * .031));
      ctx.fillStyle = 'rgba(255,214,150,.95)'; ctx.beginPath(); ctx.ellipse(119, 92, 5, 11 * fl, 0, 0, TAU); ctx.fill();
      // table
      ctx.fillStyle = '#4a3426'; ctx.fillRect(90, 330, 660, 12); ctx.fillRect(120, 342, 10, 128); ctx.fillRect(712, 342, 10, 128);
      // head, then the drape over the clothed body
      ctx.fillStyle = '#b98763'; ctx.beginPath(); ctx.arc(150, 300, 30, 0, TAU); ctx.fill();
      ctx.fillStyle = '#3b281c'; ctx.beginPath(); ctx.arc(146, 304, 30, Math.PI * .55, Math.PI * 1.25); ctx.fill();
      var body = C.map(function (p) { return [p[0], p[1] - 4]; }); body.unshift([182, 330]); body.push([748, 330]);
      smoothPath(ctx, body, true); ctx.fillStyle = '#efe2cf'; ctx.fill();
      ctx.strokeStyle = 'rgba(122,90,64,.25)'; ctx.lineWidth = 3; ctx.lineCap = 'round';
      [[300, 290, 330, 325], [470, 292, 452, 326], [600, 300, 640, 326]].forEach(function (f) { ctx.beginPath(); ctx.moveTo(f[0], f[1]); ctx.quadraticCurveTo((f[0] + f[2]) / 2 + 8, (f[1] + f[3]) / 2, f[2], f[3]); ctx.stroke(); });
      // hands follow their position slowly, with weight
      if (!reduce && t - lastPick > 15000 && t - lastMove > 6500) setPos((idx + 1) % POS.length, t);
      var tx = POS[idx][0], ty = surf(tx) - (near ? 40 : 8) - 9;
      vx += (tx - hx) * .006 * k; vy += (ty - hy) * .01 * k; vx *= Math.pow(.86, k); vy *= Math.pow(.84, k); hx += vx * k; hy += vy * k;
      if (reduce) { hx = tx; hy = ty; }
      var settle = Math.max(0, 1 - Math.hypot(tx - hx, ty - hy) / 60);
      // warmth gathers under the hands and evens out along the body: balance
      for (i = 0; i < N; i++) { var x = X0 + (X1 - X0) * i / (N - 1); E[i] += settle * .012 * k * (gauss(x - hx, 70)) * (near ? .8 : 1); }
      var nE = new Float32Array(N); for (i = 0; i < N; i++) { var a = E[Math.max(0, i - 1)], b = E[Math.min(N - 1, i + 1)]; nE[i] = Math.min(1, E[i] + ((a + b) / 2 - E[i]) * .09 * k) * Math.pow(.9985, k); }
      E = nE; if (reduce) for (i = 0; i < N; i++) E[i] = .55;
      ctx.globalCompositeOperation = 'lighter';
      for (i = 0; i < N; i += 2) {
        if (E[i] < .02) continue; var gx = X0 + (X1 - X0) * i / (N - 1), gy = surf(gx) + 6, g = ctx.createRadialGradient(gx, gy, 0, gx, gy, 46);
        g.addColorStop(0, 'rgba(255,170,90,' + (E[i] * .32).toFixed(3) + ')'); g.addColorStop(1, 'rgba(255,170,90,0)'); ctx.fillStyle = g; ctx.fillRect(gx - 46, gy - 46, 92, 92);
      }
      // light motes fall from the palms and spread along the body
      if (!reduce && settle > .3) for (i = 0; i < 2; i++) parts.push({ x: hx + (rand() - .5) * 70, y: hy + 10, vy: .5 + rand() * .8, vx: 0, life: 1, on: false });
      if (parts.length > 260) parts.splice(0, parts.length - 260);
      for (i = parts.length - 1; i >= 0; i--) {
        var p = parts[i];
        if (!p.on) { p.y += p.vy * k; if (p.y >= surf(p.x) - 2) { p.on = true; p.vx = (rand() - .5) * 1.4; } }
        else { p.x += p.vx * k; p.y = surf(p.x) - 2; p.vx *= .99; p.life -= .006 * k; }
        if (p.life <= 0) { parts.splice(i, 1); continue; }
        ctx.fillStyle = 'rgba(255,222,170,' + (p.life * .8).toFixed(3) + ')'; ctx.beginPath(); ctx.arc(p.x, p.y, 1.8, 0, TAU); ctx.fill();
      }
      ctx.globalCompositeOperation = 'source-over';
      // two hands, forearms coming down from above
      [-30, 30].forEach(function (o) {
        var px = hx + o, py = hy;
        ctx.strokeStyle = 'rgba(169,122,90,.85)'; ctx.lineWidth = 13; ctx.lineCap = 'round';
        ctx.beginPath(); ctx.moveTo(px + o * 4.5, S.T - 30); ctx.quadraticCurveTo(px + o * 2.2, py - 60, px + o * .3, py - 6); ctx.stroke();
        ctx.fillStyle = '#c99a78'; ctx.beginPath(); ctx.ellipse(px, py, 30, 10, o > 0 ? .08 : -.08, 0, TAU); ctx.fill();
        var hg = ctx.createRadialGradient(px, py + 10, 0, px, py + 10, 38); hg.addColorStop(0, 'rgba(255,214,160,' + (.35 * settle).toFixed(3) + ')'); hg.addColorStop(1, 'rgba(255,214,160,0)');
        ctx.fillStyle = hg; ctx.fillRect(px - 40, py - 28, 80, 76);
      });
    }
    var S = Stage(box, 800, 500, { frame: draw, still: function (S) { draw(S, 6000, 16.7); } });
    setPos(1, 0);
    box.addEventListener('click', function (e) {
      var p = S.pt(e), best = 0; POS.forEach(function (q, i) { if (Math.abs(q[0] - p[0]) < Math.abs(POS[best][0] - p[0])) best = i; });
      lastPick = performance.now(); setPos(best, lastPick); S.redraw();
    });
    pressGroup('[data-reiki]', function (b) { near = b.dataset.reiki === 'near'; setPos(idx, lastMove); S.redraw(); });
  };

  // ---------- SWEDISH: long strokes, warm oil ----------
  sig.swedish = function (box) {
    var cap = box.querySelector('.cap'), medium = false, add = { sound: false, breath: false, still: false };
    var R = [[40, 64], [120, 94], [188, 122], [198, 172], [172, 232], [142, 330], [150, 410], [178, 500]];
    var stroke = sampler([[38, 470], [44, 330], [50, 200], [72, 142], [160, 124], [186, 170], [162, 262], [146, 360], [120, 450], [38, 470]].map(function (p) { return [400 + p[0], p[1]]; }));
    var trail = [], user = null, userT = -1e9, phase = 0, rings = [], lastRing = 0;
    function torso(ctx, sc) {
      var pts = [], i; for (i = R.length - 1; i >= 0; i--) pts.push([400 - R[i][0] * sc, R[i][1]]); for (i = 0; i < R.length; i++) pts.push([400 + R[i][0] * sc, R[i][1]]);
      smoothPath(ctx, pts, true);
    }
    function draw(S, t, dt) {
      var ctx = S.ctx, b = breath(t), sc = add.breath ? 1 + .028 * b : 1, speed = add.still ? .68 : 1, i;
      bg(S, '#2a1c14');
      var g = ctx.createRadialGradient(400, 250, 40, 400, 250, 520); g.addColorStop(0, 'rgba(240,190,140,.16)'); g.addColorStop(1, 'rgba(240,190,140,0)');
      ctx.fillStyle = g; ctx.fillRect(S.L, S.T, S.R - S.L, S.B - S.T);
      ctx.fillStyle = '#3a2a20'; ctx.beginPath(); ctx.ellipse(400, 26, 52, 58, 0, 0, TAU); ctx.fill();
      var skin = ctx.createLinearGradient(220, 0, 580, 0); skin.addColorStop(0, '#c08e6a'); skin.addColorStop(.5, '#dcb08d'); skin.addColorStop(1, '#c08e6a');
      torso(ctx, sc); ctx.fillStyle = skin; ctx.fill();
      ctx.save(); torso(ctx, sc); ctx.clip();
      ctx.strokeStyle = 'rgba(150,100,70,.35)'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(400, 80); ctx.lineTo(400, 500); ctx.stroke();
      ctx.lineWidth = 2; [[1], [-1]].forEach(function (s) { ctx.beginPath(); ctx.moveTo(400 + s[0] * 40, 150); ctx.quadraticCurveTo(400 + s[0] * 120, 140, 400 + s[0] * 110, 250); ctx.stroke(); });
      // the hands travel one long stroke per breath: up the back on the in-breath, round the shoulders and down the sides on the out-breath
      phase += dt / 8000 * speed; var auto = performance.now() - userT > 2200;
      if (auto && !reduce) {
        var p = stroke.at(phase % 1);
        trail.push({ x: p[0], y: p[1], t: t }); trail.push({ x: 800 - p[0], y: p[1], t: t, m: 1 });
      }
      var life = 5200, w = medium ? 32 : 18;
      while (trail.length && t - trail[0].t > life) trail.shift();
      if (reduce) { trail = []; for (i = 0; i <= 120; i++) { var q = stroke.at(i / 120); trail.push({ x: q[0], y: q[1], t: t - 2000 }); trail.push({ x: 800 - q[0], y: q[1], t: t - 2000, m: 1 }); } }
      if (medium) {   // medium pressure: a soft press shadow under the sheen
        ctx.globalCompositeOperation = 'multiply';
        for (i = 2; i < trail.length; i++) { var a0 = trail[i - 2], a1 = trail[i]; if (a1.t - a0.t > 100 || Math.hypot(a1.x - a0.x, a1.y - a0.y) > 40) continue;
          ctx.strokeStyle = 'rgba(150,90,60,' + (.07 * (1 - (t - a1.t) / life)).toFixed(3) + ')'; ctx.lineWidth = w + 10; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(a0.x, a0.y + 3); ctx.lineTo(a1.x, a1.y + 3); ctx.stroke(); }
      }
      ctx.globalCompositeOperation = 'lighter';
      for (i = 2; i < trail.length; i++) {
        var c0 = trail[i - 2], c1 = trail[i]; if (c1.t - c0.t > 100 || Math.hypot(c1.x - c0.x, c1.y - c0.y) > 40) continue;
        var age = (t - c1.t) / life, al = Math.pow(1 - age, 1.6);
        ctx.strokeStyle = medium ? 'rgba(255,170,90,' + (.06 * al).toFixed(3) + ')' : 'rgba(255,224,170,' + (.05 * al).toFixed(3) + ')';
        ctx.lineWidth = w; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(c0.x, c0.y); ctx.lineTo(c1.x, c1.y); ctx.stroke();
      }
      ctx.globalCompositeOperation = 'source-over'; ctx.restore();
      // hands
      if (!reduce) {
        var hp = auto ? stroke.at(phase % 1) : null;
        var hands = hp ? [hp, [800 - hp[0], hp[1]]] : (user ? [user] : []);
        hands.forEach(function (h) { var hg = ctx.createRadialGradient(h[0], h[1], 0, h[0], h[1], 30); hg.addColorStop(0, 'rgba(255,232,200,.55)'); hg.addColorStop(1, 'rgba(255,232,200,0)'); ctx.fillStyle = hg; ctx.fillRect(h[0] - 30, h[1] - 30, 60, 60); });
      }
      // add-ons
      if (add.sound) {
        if (t - lastRing > 2600 || reduce) { rings.push(t); lastRing = t; if (reduce) rings = [t - 600, t - 1800]; }
        rings = rings.filter(function (r0) { return t - r0 < 4400; });
        rings.forEach(function (r0) { var u = (t - r0) / 4400; ctx.strokeStyle = 'rgba(250,230,200,' + (.55 * (1 - u)).toFixed(3) + ')'; ctx.lineWidth = 1.5; ctx.beginPath(); ctx.ellipse(400, 30, 40 + u * 380, 30 + u * 280, 0, 0, TAU); ctx.stroke(); });
      }
      if (add.still) {
        S.full(); var v = ctx.createRadialGradient(S.W / 2, S.H / 2, S.H * .3, S.W / 2, S.H / 2, S.W * .75); v.addColorStop(0, 'rgba(20,12,8,0)'); v.addColorStop(1, 'rgba(20,12,8,.55)'); ctx.fillStyle = v; ctx.fillRect(0, 0, S.W, S.H); S.scene();
      }
      var msg = add.breath ? (b > .5 ? (Math.sin(t / 8000 * TAU) > 0 ? 'Breathe in' : 'And out') : (Math.sin(t / 8000 * TAU) > 0 ? 'Breathe in' : 'And out')) : (medium ? 'Medium pressure · long strokes' : 'Light pressure · long strokes');
      caption(cap, msg);
    }
    var S = Stage(box, 800, 500, { frame: draw });
    function userAt(e) { var p = S.pt(e); user = p; userT = performance.now(); trail.push({ x: p[0], y: p[1], t: S.t || performance.now() }); }
    box.addEventListener('pointerdown', function (e) { userAt(e); box.dataset.drag = '1'; });
    box.addEventListener('pointermove', function (e) { if (box.dataset.drag) userAt(e); });
    ['pointerup', 'pointerleave', 'pointercancel'].forEach(function (n) { box.addEventListener(n, function () { delete box.dataset.drag; user = null; }); });
    pressGroup('[data-pressure]', function (b) { medium = b.dataset.pressure === 'medium'; S.redraw(); });
    document.querySelectorAll('[data-addon]').forEach(function (b) { b.addEventListener('click', function () { var k = b.dataset.addon; add[k] = !add[k]; b.setAttribute('aria-pressed', String(add[k])); S.redraw(); }); });
  };

  // ---------- DEEP TISSUE: layers, with the breath ----------
  sig.deep = function (box) {
    var cap = box.querySelector('.cap'), level = 1, D = [80, 170, 290], NB = 48, rows = [], rand = seeded(23), releasedAt = 0;
    var Y = [120, 150, 186, 330, 470], NAMES = ['Skin', 'Fascia', 'Muscle', 'Deep muscle'];
    function initRows() {
      rows = [];
      for (var y = 200; y <= 320; y += 15) rows.push({ y: y, deep: false });
      for (y = 346; y <= 458; y += 16) rows.push({ y: y, deep: true });
      rows.forEach(function (r, j) {
        r.T = new Float32Array(NB); r.T0 = new Float32Array(NB); r.ph = rand() * TAU;
        [230 + rand() * 60, 400 + rand() * 50, 560 + rand() * 60].forEach(function (kx) { for (var i = 0; i < NB; i++) { var x = i / (NB - 1) * 800; r.T0[i] = Math.min(1, r.T0[i] + gauss(x - kx, 55 + rand() * 20)); } });
        r.T.set(r.T0);
      });
    }
    initRows();
    function draw(S, t, dt) {
      var ctx = S.ctx, k = dt / 16.7, i, j, x;
      var p = (t % 8000) / 8000, d = reduce ? D[level] : D[level] * (p < .5 ? .3 + .7 * sine(p * 2) : 1 - .7 * sine((p - .5) * 2)), sinking = p < .5;
      var tx = reduce ? 400 : 400 + 230 * Math.sin(t * .00021);
      function disp(xx, yb) { return Math.max(0, d * gauss(xx - tx, 90) * Math.max(0, 1 - (yb - 120) / 560)); }
      bg(S, '#1e140e');
      var cols = ['#e2b48f', '#efdcc4', '#a5533b', '#7b3425', '#55251a'];
      for (j = 0; j < 5; j++) {   // each layer is painted over the one above it; every boundary dips under the forearm
        ctx.beginPath(); ctx.moveTo(S.L, S.B);
        for (x = S.L; x <= S.R + 8; x += 8) { var yb = j < 4 ? Y[j] : 470; ctx.lineTo(x, yb + disp(x, yb)); }
        ctx.lineTo(S.R, S.B); ctx.closePath(); ctx.fillStyle = cols[j]; ctx.fill();
      }
      // fascia: a fine web
      ctx.strokeStyle = 'rgba(160,110,80,.35)'; ctx.lineWidth = 1;
      for (x = Math.floor(S.L / 22) * 22; x < S.R; x += 22) { ctx.beginPath(); ctx.moveTo(x, 152 + disp(x, 152)); ctx.lineTo(x + 18, 184 + disp(x + 18, 184)); ctx.moveTo(x + 18, 152 + disp(x + 18, 152)); ctx.lineTo(x, 184 + disp(x, 184)); ctx.stroke(); }
      // muscle fibres: knotted where tension is held, long and easy where it has let go
      var reach = 120 + d * 1.08, total = 0;
      rows.forEach(function (r, ri) {
        for (i = 0; i < NB; i++) {
          var bx = i / (NB - 1) * 800;
          if (!reduce && sinking && r.y < reach) r.T[i] = Math.max(0, r.T[i] - .0065 * k * gauss(bx - tx, 70));
          if (reduce) r.T[i] = r.y < reach ? r.T0[i] * .15 : r.T0[i];
          total += r.T[i];
        }
        ctx.strokeStyle = r.deep ? 'rgba(240,170,140,.32)' : 'rgba(255,200,170,.4)'; ctx.lineWidth = 1.6; ctx.beginPath();
        for (x = S.L; x <= S.R; x += 5) {
          var bi = Math.max(0, Math.min(NB - 1, Math.round(x / 800 * (NB - 1)))), T = r.T[bi];
          var y = r.y + disp(x, r.y) + T * 7 * Math.sin(x * .34 + r.ph) * Math.sin(x * .05 + ri) + (1 - T) * 1.6 * Math.sin(x * .025 + r.ph + t * .0004);
          if (x === S.L) ctx.moveTo(x, y); else ctx.lineTo(x, y);
        }
        ctx.stroke();
      });
      // the forearm, coming in from the upper right
      var tipY = 120 + d - 26;
      ctx.lineCap = 'round'; ctx.strokeStyle = 'rgba(0,0,0,.25)'; ctx.lineWidth = 70; ctx.beginPath(); ctx.moveTo(tx + 214, S.T - 60); ctx.lineTo(tx + 6, tipY + 6); ctx.stroke();
      ctx.strokeStyle = '#c99a78'; ctx.lineWidth = 62; ctx.beginPath(); ctx.moveTo(tx + 210, S.T - 60); ctx.lineTo(tx, tipY); ctx.stroke();
      ctx.strokeStyle = 'rgba(255,230,200,.25)'; ctx.lineWidth = 6; ctx.beginPath(); ctx.moveTo(tx + 226, S.T - 60); ctx.lineTo(tx + 22, tipY - 18); ctx.stroke();
      // labels
      ctx.font = '700 12px Figtree, system-ui, sans-serif'; ctx.textAlign = 'right'; ctx.fillStyle = 'rgba(43,29,20,.7)';
      ctx.fillText(NAMES[0].toUpperCase(), S.R - 16, 140); ctx.fillText(NAMES[1].toUpperCase(), S.R - 16, 172);
      ctx.fillStyle = 'rgba(250,236,220,.75)'; ctx.fillText(NAMES[2].toUpperCase(), S.R - 16, 262); ctx.fillText(NAMES[3].toUpperCase(), S.R - 16, 404);
      ctx.textAlign = 'left';
      var mean = total / (rows.length * NB);
      if (!reduce && mean < .06 && !releasedAt) releasedAt = t;
      if (releasedAt && t - releasedAt > 7000) { rows.forEach(function (r) { for (i = 0; i < NB; i++) r.T[i] += (r.T0[i] - r.T[i]) * .004 * k; }); if (mean > .3) releasedAt = 0; }
      caption(cap, reduce ? 'Pressure you choose, with the breath' : releasedAt ? 'Let go. Stretch ideas to take home.' : sinking ? 'Exhale · sink in' : 'Inhale · ease off');
    }
    var S = Stage(box, 800, 500, { frame: draw });
    var inp = document.getElementById('depth'), out = document.getElementById('depthOut'), LBL = ['Firm', 'Deep', 'Deeper'];
    if (inp) inp.addEventListener('input', function () { level = +inp.value; out.textContent = LBL[level]; releasedAt = 0; S.redraw(); });
  };

  // ---------- THAI: rhythmic compressions, then stretching ----------
  sig.thai = function (box) {
    var cap = box.querySelector('.cap'), rings = [], beat = -1, t0 = null;
    var HIP = [414, 388], L1 = 116, L2 = 112;
    var PH = [['walk', 7200], ['raise', 1600], ['hold', 2800], ['lower', 1400], ['knee', 1600], ['hold2', 2400], ['back', 1400]], TOTAL = PH.reduce(function (a, p) { return a + p[1]; }, 0);
    var REST = [0, .05], RAISE = [-1.2, 0], KNEE = [-2.2, 1.95];
    function legPts(a1, a2) { var k = [HIP[0] + Math.cos(a1) * L1, HIP[1] + Math.sin(a1) * L1], an = [k[0] + Math.cos(a1 + a2) * L2, k[1] + Math.sin(a1 + a2) * L2]; return [HIP, k, an]; }
    function lerp(a, b, f) { return [a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f]; }
    function limb(ctx, pts, w) { ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.strokeStyle = 'rgba(43,29,20,.55)'; ctx.lineWidth = w + 4; line(ctx, pts); ctx.stroke(); ctx.strokeStyle = '#efe2cf'; ctx.lineWidth = w; line(ctx, pts); ctx.stroke(); }
    function palm(ctx, x, y, a) { var g = ctx.createRadialGradient(x, y, 0, x, y, 26); g.addColorStop(0, 'rgba(255,214,160,' + (.75 * a).toFixed(3) + ')'); g.addColorStop(1, 'rgba(255,214,160,0)'); ctx.fillStyle = g; ctx.fillRect(x - 26, y - 26, 52, 52); ctx.fillStyle = 'rgba(201,154,120,' + a.toFixed(3) + ')'; ctx.beginPath(); ctx.ellipse(x, y - 12, 15, 7, 0, 0, TAU); ctx.fill(); }
    function draw(S, t, dt) {
      var ctx = S.ctx, i;
      if (t0 === null) t0 = t;
      var e = reduce ? PH[0][1] + PH[1][1] + 1000 : (t - t0) % TOTAL, ph = 0; while (e > PH[ph][1]) { e -= PH[ph][1]; ph++; }
      var f = e / PH[ph][1], name = PH[ph][0], ang = REST;
      if (name === 'raise') ang = lerp(REST, RAISE, sine(f)); else if (name === 'hold') ang = RAISE; else if (name === 'lower') ang = lerp(RAISE, REST, sine(f));
      else if (name === 'knee') ang = lerp(REST, KNEE, sine(f)); else if (name === 'hold2') ang = KNEE; else if (name === 'back') ang = lerp(KNEE, REST, sine(f));
      bg(S, '#2b1e16'); ctx.translate(0, -140);
      ctx.fillStyle = 'rgba(250,236,220,.05)'; ctx.fillRect(S.L, 418, S.R - S.L, S.B + 140 - 418);
      ctx.fillStyle = '#56613f'; ctx.beginPath(); ctx.roundRect ? ctx.roundRect(70, 404, 660, 16, 8) : ctx.rect(70, 404, 660, 16); ctx.fill();
      // receiver, lying on the mat
      limb(ctx, [[186, 384], [412, 388]], 50); limb(ctx, [[204, 398], [372, 402]], 16);
      ctx.fillStyle = '#b98763'; ctx.beginPath(); ctx.arc(152, 374, 24, 0, TAU); ctx.fill(); ctx.fillStyle = '#3b281c'; ctx.beginPath(); ctx.arc(150, 378, 24, Math.PI * .5, Math.PI * 1.3); ctx.fill();
      var rest = [[414, 392], [530, 395], [640, 396]]; limb(ctx, rest, 30); limb(ctx, [[640, 396], [652, 372]], 14);
      var leg = legPts(ang[0], ang[1]), sh = Math.atan2(leg[2][1] - leg[1][1], leg[2][0] - leg[1][0]) - Math.PI / 2;
      // the stretch shows as warmth along the back of the thigh
      if (name === 'hold' || name === 'raise' || name === 'lower') {
        var a = name === 'hold' ? 1 : name === 'raise' ? f : 1 - f;
        ctx.strokeStyle = 'rgba(232,132,78,' + (.55 * a).toFixed(3) + ')'; ctx.lineWidth = 40; ctx.lineCap = 'round'; line(ctx, [leg[0], leg[1]]); ctx.stroke();
      }
      limb(ctx, leg, 30); limb(ctx, [leg[2], [leg[2][0] + Math.cos(sh) * 24, leg[2][1] + Math.sin(sh) * 24]], 14);
      // palms: walking compressions in rhythm, or holding the stretch
      if (name === 'walk') {
        var BEAT = 600, b = Math.floor(e / BEAT), bf = (e % BEAT) / BEAT, u = (b % 12) / 11, uu = u < .5 ? 1 - u * 2 : (u - .5) * 2;
        var onRest = b % 2 === 0, src = onRest ? rest : leg, pt = lerp(src[0], src[2], .15 + .85 * uu), press = Math.sin(Math.PI * Math.min(1, bf * 1.6));
        if (b !== beat && !reduce) { beat = b; rings.push({ x: pt[0], y: pt[1] - 6, t: t }); }
        palm(ctx, pt[0], pt[1] - 4 + press * 4, 1); palm(ctx, lerp(src[0], src[2], .15 + .85 * Math.max(0, uu - .12))[0] - 20, lerp(src[0], src[2], .15 + .85 * Math.max(0, uu - .12))[1] - 6, .55);
        caption(cap, 'Rhythmic compressions');
      } else if (name === 'knee' || name === 'hold2' || name === 'back') { palm(ctx, leg[1][0], leg[1][1] - 6, 1); palm(ctx, leg[2][0] + 6, leg[2][1] - 4, .8); caption(cap, 'Knee to chest · breathe'); }
      else { palm(ctx, leg[2][0] + 8, leg[2][1] + 6, 1); palm(ctx, 470, 392, .8); caption(cap, 'Full-body stretching'); }
      if (reduce) caption(cap, 'Stretching and rhythmic compressions');
      rings = rings.filter(function (r) { return t - r.t < 1100; });
      rings.forEach(function (r) { var u = (t - r.t) / 1100; ctx.strokeStyle = 'rgba(244,191,150,' + (.8 * (1 - u)).toFixed(3) + ')'; ctx.lineWidth = 2; ctx.beginPath(); ctx.ellipse(r.x, r.y, 12 + u * 46, 5 + u * 14, 0, 0, TAU); ctx.stroke(); });
      // rhythm strip
      for (i = 0; i < 12; i++) { var lit = name === 'walk' && (beat % 12) === i; ctx.fillStyle = lit ? '#e07a3c' : 'rgba(250,236,220,.22)'; ctx.beginPath(); ctx.arc(400 - 11 * 14 / 2 + i * 14, 468, lit ? 4.5 : 3, 0, TAU); ctx.fill(); }
    }
    var S = Stage(box, 800, 345, { frame: draw });
    box.addEventListener('click', function (e) { var p = S.pt(e); rings.push({ x: p[0], y: p[1] + 140, t: S.t || performance.now() }); });
  };

  // ---------- LYMPHATIC FIRMING: six steps, told by scroll ----------
  sig.lymph = function (box) {
    var T = [205, 118], active = 0, alpha = [1, 0, 0, 0, 0, 0], parts = [], rand = seeded(5);
    var V = [[[120, 292], [128, 210], [150, 142], [185, 122], T], [[280, 292], [272, 210], [250, 142], [222, 120], T],
             [[170, 470], [174, 380], [182, 296], [192, 230], [198, 170], T], [[230, 470], [226, 380], [218, 296], [206, 230], [202, 170], T],
             [[180, 56], [184, 98], [195, 112], T], [[220, 56], [216, 98], [210, 112], T]].map(function (p) { return sampler(p); });
    var NODES = [[150, 142], [250, 142], [182, 296], [218, 296], [184, 98], [216, 98]];
    function figure(ctx) {
      ctx.beginPath(); ctx.arc(200, 62, 30, 0, TAU);
      ctx.moveTo(150, 120); ctx.quadraticCurveTo(200, 104, 250, 120); ctx.quadraticCurveTo(244, 190, 236, 240); ctx.quadraticCurveTo(250, 270, 244, 296); ctx.lineTo(156, 296); ctx.quadraticCurveTo(150, 270, 164, 240); ctx.quadraticCurveTo(156, 190, 150, 120); ctx.closePath();
      ctx.rect(190, 86, 20, 26);
    }
    function limbs(ctx, w) {
      ctx.lineCap = 'round'; ctx.lineWidth = w;
      [[[152, 128], [130, 210], [120, 292]], [[248, 128], [270, 210], [280, 292]], [[180, 292], [174, 380], [170, 472]], [[220, 292], [226, 380], [230, 472]]].forEach(function (p) { line(ctx, p); ctx.stroke(); });
    }
    var steps = document.querySelectorAll('.steps li');
    if (hasIO && steps.length) {
      var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { active = +e.target.dataset.step; steps.forEach(function (s) { s.classList.toggle('on', s === e.target); }); } }); }, { rootMargin: '-45% 0px -45% 0px' });
      steps.forEach(function (s) { io.observe(s); });
    }
    function draw(S, t, dt) {
      var ctx = S.ctx, k = dt / 16.7, i, m;
      for (m = 0; m < 6; m++) alpha[m] += ((m === active ? 1 : 0) - alpha[m]) * (reduce ? 1 : .05 * k);
      bg(S, '#2a1c14');
      // body
      ctx.fillStyle = '#efe2cf'; ctx.strokeStyle = '#efe2cf'; ctx.beginPath(); figure(ctx); ctx.fill(); limbs(ctx, 26);
      // vessels and nodes
      ctx.strokeStyle = 'rgba(86,97,63,.55)'; ctx.lineWidth = 1.6; V.forEach(function (v) { ctx.beginPath(); for (i = 0; i <= 40; i++) { var p = v.at(i / 40); if (i) ctx.lineTo(p[0], p[1]); else ctx.moveTo(p[0], p[1]); } ctx.stroke(); });
      NODES.forEach(function (n, j) { var pulse = alpha[1] * (.5 + .5 * Math.sin(t * .004 + j)); ctx.fillStyle = 'rgba(86,97,63,' + (.5 + .4 * pulse).toFixed(3) + ')'; ctx.beginPath(); ctx.arc(n[0], n[1], 3.6 + 2.5 * pulse, 0, TAU); ctx.fill(); });
      // 1 dry brushing: a brush sweeps each path toward the heart
      if (alpha[0] > .01) {
        var bi = Math.floor(t / 1600) % 4, bu = (t % 1600) / 1600, bp = V[bi].at(reduce ? .6 : sine(bu) * .92);
        ctx.globalAlpha = alpha[0];
        for (i = 0; i < 4; i++) { ctx.strokeStyle = 'rgba(181,80,31,.22)'; ctx.lineWidth = 10; ctx.beginPath(); for (var s = 0; s <= 20; s++) { var q = V[i].at(s / 20 * (i === bi ? sine(bu) * .92 : .92)); if (s) ctx.lineTo(q[0], q[1]); else ctx.moveTo(q[0], q[1]); } ctx.stroke(); }
        ctx.fillStyle = '#6e4a2c'; ctx.beginPath(); ctx.ellipse(bp[0], bp[1], 15, 9, 0, 0, TAU); ctx.fill();
        ctx.strokeStyle = '#d9bf9f'; ctx.lineWidth = 1.4; for (i = -12; i <= 12; i += 4) { ctx.beginPath(); ctx.moveTo(bp[0] + i, bp[1] + 6); ctx.lineTo(bp[0] + i * 1.1, bp[1] + 13); ctx.stroke(); }
        ctx.globalAlpha = 1;
      }
      // 2 lymphatic massage: flow along every vessel, toward the collarbone
      if (alpha[1] > .01 || alpha[4] > .01) {
        if (!reduce && parts.length < 140) for (i = 0; i < 2; i++) { var vi = alpha[4] > .5 ? 4 + Math.floor(rand() * 2) : Math.floor(rand() * 6); parts.push({ v: vi, u: 0 }); }
        if (reduce && !parts.length) for (i = 0; i < 60; i++) parts.push({ v: i % 6, u: (i * .137) % 1 });
        ctx.fillStyle = '#56613f';
        for (i = parts.length - 1; i >= 0; i--) {
          var pp = parts[i]; if (!reduce) pp.u += .0035 * k * (alpha[4] > .5 ? 1.6 : 1); if (pp.u >= 1) { parts.splice(i, 1); continue; }
          var pq = V[pp.v].at(pp.u), a2 = Math.max(alpha[1], pp.v >= 4 ? alpha[4] : 0);
          ctx.globalAlpha = a2 * Math.sin(Math.PI * pp.u); ctx.beginPath(); ctx.arc(pq[0], pq[1], 2.4, 0, TAU); ctx.fill();
        }
        ctx.globalAlpha = 1;
      }
      // 3 heated wrap, 4 hot towel: warm bands wind on, then fade under steam
      // wrap bands and the cream's sheen are painted on a layer, then cut to the body's shape
      var wrapA = Math.max(alpha[2], alpha[3] * .5), o = null;
      if (wrapA > .01 || alpha[5] > .01) {
        var off = S.off || (S.off = document.createElement('canvas')); if (off.width !== S.cv.width || off.height !== S.cv.height) { off.width = S.cv.width; off.height = S.cv.height; }
        o = off.getContext('2d'); o.setTransform(1, 0, 0, 1, 0, 0); o.clearRect(0, 0, off.width, off.height); o.setTransform(S.dpr * S.s, 0, 0, S.dpr * S.s, S.dpr * S.ox, S.dpr * S.oy);
      }
      if (wrapA > .01) {
        var prog = reduce ? 1 : Math.min(1, ((t / 1000) % 9) / 5);
        o.lineCap = 'butt'; o.lineWidth = 27; o.strokeStyle = 'rgba(201,135,92,' + (.5 * wrapA).toFixed(3) + ')';
        for (i = 0; i < 16; i++) { var yb = 476 - i * 24, pi = Math.max(0, Math.min(1, prog * 16 - i)); if (pi <= 0) continue; o.beginPath(); o.moveTo(100, yb + 10); o.lineTo(100 + 200 * pi, yb + 10 - 20 * pi); o.stroke(); }
      }
      if (alpha[5] > .01) {
        var sx2 = reduce ? 200 : -140 + ((t % 2600) / 2600) * 680, sg = o.createLinearGradient(sx2 - 110, 0, sx2 + 110, 0);
        sg.addColorStop(0, 'rgba(255,255,255,0)'); sg.addColorStop(.5, 'rgba(255,250,236,' + (.9 * alpha[5]).toFixed(3) + ')'); sg.addColorStop(1, 'rgba(255,255,255,0)');
        o.fillStyle = 'rgba(255,236,206,' + (.28 * alpha[5]).toFixed(3) + ')'; o.fillRect(0, 0, 400, 500); o.fillStyle = sg; o.fillRect(0, 0, 400, 500);
        for (i = 0; i < 10; i++) { var spx = 120 + ((i * 53) % 160), spy = 80 + ((i * 97) % 380), tw = .5 + .5 * Math.sin(t * .006 + i * 2); o.fillStyle = 'rgba(255,255,255,' + (alpha[5] * tw * .8).toFixed(3) + ')'; o.beginPath(); o.arc(spx, spy, 1.6, 0, TAU); o.fill(); }
      }
      if (o) {
        var mk = S.mask || (S.mask = document.createElement('canvas')); if (mk.width !== off.width || mk.height !== off.height) { mk.width = off.width; mk.height = off.height; }
        var m = mk.getContext('2d'); m.setTransform(1, 0, 0, 1, 0, 0); m.clearRect(0, 0, mk.width, mk.height); m.setTransform(S.dpr * S.s, 0, 0, S.dpr * S.s, S.dpr * S.ox, S.dpr * S.oy);
        m.fillStyle = m.strokeStyle = '#000'; m.beginPath(); figure(m); m.fill(); limbs(m, 26);
        o.setTransform(1, 0, 0, 1, 0, 0); o.globalCompositeOperation = 'destination-in'; o.drawImage(mk, 0, 0); o.globalCompositeOperation = 'source-over';
        ctx.setTransform(1, 0, 0, 1, 0, 0); ctx.drawImage(S.off, 0, 0); S.scene();
      }
      if (wrapA > .01) { var wg = ctx.createRadialGradient(200, 300, 20, 200, 300, 260); wg.addColorStop(0, 'rgba(255,150,80,' + (.22 * wrapA).toFixed(3) + ')'); wg.addColorStop(1, 'rgba(255,150,80,0)'); ctx.fillStyle = wg; ctx.fillRect(0, 0, 400, 500); }
      if (alpha[3] > .01) {
        ctx.strokeStyle = 'rgba(255,250,240,' + (.8 * alpha[3]).toFixed(3) + ')'; ctx.lineWidth = 3; ctx.lineCap = 'round';
        for (i = 0; i < 9; i++) {
          var sx = 140 + i * 15, rise = reduce ? .5 : ((t / 2600 + i * .37) % 1);
          ctx.globalAlpha = Math.sin(Math.PI * rise); ctx.beginPath();
          for (var sy = 0; sy <= 60; sy += 4) { var yy = 300 - rise * 160 - sy; ctx.lineTo(sx + Math.sin((yy + t * .05) * .06 + i) * 6, yy); }
          ctx.stroke();
        }
        ctx.globalAlpha = 1;
      }
      // 5 head & neck: two palms at the sides of the neck
      if (alpha[4] > .01) {
        [[168, 100], [232, 100]].forEach(function (h, j) {
          var o = reduce ? 0 : Math.sin(t * .002 + j * Math.PI) * 4, g = ctx.createRadialGradient(h[0], h[1] + o, 0, h[0], h[1] + o, 26);
          g.addColorStop(0, 'rgba(255,214,160,' + (.75 * alpha[4]).toFixed(3) + ')'); g.addColorStop(1, 'rgba(255,214,160,0)'); ctx.fillStyle = g; ctx.fillRect(h[0] - 26, h[1] + o - 26, 52, 52);
        });
      }
    }
    Stage(box, 400, 500, { frame: draw, still: function (S) { alpha = [0, 1, 0, 0, 0, 0]; active = 1; draw(S, 6000, 16.7); } });
  };

  // ---------- SARGA: bare foot, fabric strap, fascia ----------
  sig.sarga = function (box) {
    var cap = box.querySelector('.cap'), NC = 72, X0 = 130, X1 = 690, rel = new Float32Array(NC), noise = [], rand = seeded(31), fx = 300, fv = 0, target = null, dragT = -1e9, doneAt = 0;
    for (var j = 0; j < 5; j++) { noise.push([]); for (var i = 0; i < NC; i++) noise[j].push((rand() - .5) * 2); }
    var B = [[110, 440], [150, 416], [210, 408], [300, 416], [380, 414], [470, 396], [540, 410], [620, 426], [700, 432]];
    function surf(x) { for (var i = 1; i < B.length; i++) if (x <= B[i][0]) { var a = B[i - 1], b = B[i], f = smooth((x - a[0]) / (b[0] - a[0])); return a[1] + (b[1] - a[1]) * f; } return 448; }
    function draw(S, t, dt) {
      var ctx = S.ctx, k = dt / 16.7, i;
      if (reduce) { fx = 420; for (i = 0; i < NC; i++) rel[i] = X0 + (X1 - X0) * i / (NC - 1) < 470 ? 1 : 0; }
      else {
        var tgt = (performance.now() - dragT < 2500 && target !== null) ? target : 410 + 230 * Math.sin(t * .00016);
        fv += (tgt - fx) * .004 * k; fv *= Math.pow(.88, k); fx += fv * k;
      }
      var press = 12;
      function sy(x) { return surf(x) + press * gauss(x - fx, 46); }
      bg(S, '#271a12');
      var g = ctx.createLinearGradient(0, 0, 0, 500); g.addColorStop(0, 'rgba(240,200,150,.12)'); g.addColorStop(1, 'rgba(240,200,150,0)'); ctx.fillStyle = g; ctx.fillRect(S.L, S.T, S.R - S.L, S.B - S.T);
      // overhead bar and strap
      ctx.strokeStyle = '#8a5a34'; ctx.lineWidth = 9; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(150, 46); ctx.lineTo(650, 46); ctx.stroke();
      ctx.strokeStyle = 'rgba(138,90,52,.6)'; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(170, S.T); ctx.lineTo(170, 46); ctx.moveTo(630, S.T); ctx.lineTo(630, 46); ctx.stroke();
      var hip = [fx + 70, 236], sh = [fx + 60, 134], hd = [fx + 66, 104], handL = [fx + 36, 76], handR = [fx + 88, 76];
      var anchor = Math.max(220, Math.min(580, fx + 62));
      ctx.strokeStyle = '#d9bf9f'; ctx.lineWidth = 7; ctx.beginPath(); ctx.moveTo(anchor - 14, 50); ctx.lineTo(handL[0], handL[1]); ctx.moveTo(anchor + 14, 50); ctx.lineTo(handR[0], handR[1]); ctx.stroke();
      // floor, mat, receiver lying face down
      ctx.fillStyle = '#56613f'; ctx.fillRect(90, 466, 640, 10);
      ctx.fillStyle = '#b98763'; ctx.beginPath(); ctx.arc(126, 440, 26, 0, TAU); ctx.fill();
      ctx.beginPath(); ctx.moveTo(140, 466); for (var x = 140; x <= 704; x += 6) ctx.lineTo(x, sy(x)); ctx.lineTo(704, 466); ctx.closePath(); ctx.fillStyle = '#d8ab88'; ctx.fill();
      // fascia lines just under the surface: tangled where untouched, long and parallel where the foot has passed
      var mean = 0;
      for (i = 0; i < NC; i++) { var cx = X0 + (X1 - X0) * i / (NC - 1); if (!reduce) rel[i] = Math.min(1, rel[i] + .0042 * k * gauss(cx - fx, 42)); mean += rel[i]; }
      mean /= NC;
      for (j = 0; j < 5; j++) {
        ctx.beginPath();
        for (i = 0; i < NC; i++) { var xx = X0 + (X1 - X0) * i / (NC - 1), r = rel[i], yy = sy(xx) + 7 + j * 4 + (1 - r) * 5.5 * noise[j][i]; if (i) ctx.lineTo(xx, yy); else ctx.moveTo(xx, yy); }
        ctx.strokeStyle = 'rgba(122,52,30,.55)'; ctx.lineWidth = 1.3; ctx.stroke();
      }
      ctx.strokeStyle = 'rgba(122,52,30,.5)'; ctx.lineWidth = 1.1;
      for (i = 0; i < NC - 1; i += 2) { var x1 = X0 + (X1 - X0) * i / (NC - 1), r1 = 1 - rel[i]; if (r1 < .05) continue; ctx.globalAlpha = r1; ctx.beginPath(); ctx.moveTo(x1, sy(x1) + 7 + 16 * (noise[0][i] > 0 ? 1 : 0)); ctx.lineTo(x1 + 14, sy(x1 + 14) + 7 + 16 * (noise[1][i] > 0 ? 0 : 1)); ctx.stroke(); }
      ctx.globalAlpha = 1;
      // practitioner: standing leg behind, working foot on the back, hands on the strap
      ctx.lineCap = 'round'; ctx.lineJoin = 'round';
      ctx.strokeStyle = 'rgba(250,236,220,.35)'; ctx.lineWidth = 16; line(ctx, [hip, [fx + 104, 340], [fx + 120, 470]]); ctx.stroke();
      var foot = [fx, sy(fx) - 8], knee = [fx + 46, 330];
      ctx.strokeStyle = '#efe2cf'; ctx.lineWidth = 16; line(ctx, [hip, knee, [fx + 10, foot[1] - 14]]); ctx.stroke();
      ctx.lineWidth = 18; line(ctx, [hip, sh]); ctx.stroke();
      ctx.lineWidth = 10; line(ctx, [sh, [fx + 44, 104], handL]); ctx.stroke(); line(ctx, [sh, [fx + 82, 104], handR]); ctx.stroke();
      ctx.fillStyle = '#efe2cf'; ctx.beginPath(); ctx.arc(hd[0], hd[1] - 4, 17, 0, TAU); ctx.fill();
      ctx.fillStyle = '#e9cdb0'; ctx.beginPath(); ctx.ellipse(foot[0], foot[1], 30, 9, 0, 0, TAU); ctx.fill();
      var fg = ctx.createRadialGradient(foot[0], foot[1] + 12, 0, foot[0], foot[1] + 12, 50); fg.addColorStop(0, 'rgba(224,122,60,.45)'); fg.addColorStop(1, 'rgba(224,122,60,0)'); ctx.fillStyle = fg; ctx.fillRect(foot[0] - 50, foot[1] - 38, 100, 100);
      if (!reduce && mean > .97 && !doneAt) doneAt = t;
      if (doneAt && t - doneAt > 6000) { for (i = 0; i < NC; i++) rel[i] *= Math.pow(.996, k); if (mean < .2) doneAt = 0; }
      caption(cap, reduce ? 'Barefoot, with a fabric strap' : doneAt ? 'Long and even again' : 'Slow, deep pressure along the fascia');
    }
    var S = Stage(box, 800, 500, { frame: draw });
    function aim(e) { target = Math.max(150, Math.min(660, S.pt(e)[0])); dragT = performance.now(); }
    box.addEventListener('pointerdown', function (e) { box.dataset.drag = '1'; aim(e); });
    box.addEventListener('pointermove', function (e) { if (box.dataset.drag || e.pointerType === 'mouse') aim(e); });
    ['pointerup', 'pointercancel', 'pointerleave'].forEach(function (n) { box.addEventListener(n, function () { delete box.dataset.drag; }); });
  };

  // ---------- ZEN MOUNTAIN: a river that slows while you stay ----------
  sig.zen = function (box) {
    var cap = box.querySelector('.cap'), calm = 0, px = 0, pxT = 0, lastP = null, streaks = [], rand = seeded(41), ridges = [], snd = null, sndOn = false;
    for (var r = 0; r < 3; r++) { var ph = [rand() * TAU, rand() * TAU, rand() * TAU]; ridges.push(ph); }
    for (var i = 0; i < 150; i++) streaks.push({ u: rand(), v: rand() * 2 - 1, l: .02 + rand() * .04 });
    function bez(a, b, c, d, u) { var m = 1 - u; return m * m * m * a + 3 * m * m * u * b + 3 * m * u * u * c + u * u * u * d; }
    function river(W, H, u) { return [bez(.6 * W, .86 * W, .02 * W, .36 * W, u), bez(.5 * H, .64 * H, .78 * H, 1.1 * H, u)]; }
    function draw(S, t, dt) {
      var ctx = S.ctx, W = S.W, H = S.H, k = dt / 16.7, j;
      S.full();
      if (!reduce) { calm = Math.min(1, calm + dt / 16000); px += (pxT - px) * .04 * k; } else calm = 1;
      var sky = ctx.createLinearGradient(0, 0, 0, H * .55); sky.addColorStop(0, '#e9c9a0'); sky.addColorStop(1, '#c98f68'); ctx.fillStyle = sky; ctx.fillRect(0, 0, W, H);
      var sun = ctx.createRadialGradient(W * .72, H * .28, 0, W * .72, H * .28, H * .22); sun.addColorStop(0, 'rgba(255,238,206,.95)'); sun.addColorStop(.25, 'rgba(255,230,190,.55)'); sun.addColorStop(1, 'rgba(255,230,190,0)'); ctx.fillStyle = sun; ctx.fillRect(0, 0, W, H);
      var cols = ['#a88272', '#76594a', '#46332a'], base = [.4, .5, .62];
      ridges.forEach(function (p, ri) {
        var off = px * (ri + 1) * 10; ctx.beginPath(); ctx.moveTo(-20, H);
        for (var x = -20; x <= W + 20; x += 8) { var u = (x + off) / W, y = H * base[ri] - H * (.1 + ri * .02) * (.55 + .25 * Math.sin(u * 5.2 + p[0]) + .15 * Math.sin(u * 11 + p[1]) + .06 * Math.sin(u * 27 + p[2])); ctx.lineTo(x, y); }
        ctx.lineTo(W + 20, H); ctx.closePath(); ctx.fillStyle = cols[ri]; ctx.fill();
      });
      // pines on the near slope
      ctx.fillStyle = '#33251d';
      for (j = 0; j < 16; j++) { var tx2 = (j * 97 % 100) / 100 * W, ty = H * (.6 + (j % 4) * .035), th = H * (.05 + (j % 3) * .015); ctx.beginPath(); ctx.moveTo(tx2, ty - th); ctx.lineTo(tx2 - th * .28, ty); ctx.lineTo(tx2 + th * .28, ty); ctx.closePath(); ctx.fill(); }
      // the river
      ctx.beginPath(); var left = [], right = [];
      for (j = 0; j <= 40; j++) { var u2 = j / 40, c = river(W, H, u2), c2 = river(W, H, Math.min(1, u2 + .01)), a = Math.atan2(c2[1] - c[1], c2[0] - c[0]) + Math.PI / 2, w = H * (.012 + .2 * u2 * u2); left.push([c[0] + Math.cos(a) * w, c[1] + Math.sin(a) * w]); right.push([c[0] - Math.cos(a) * w, c[1] - Math.sin(a) * w]); }
      line(ctx, left.concat(right.reverse())); ctx.closePath();
      var wg = ctx.createLinearGradient(0, H * .5, 0, H); wg.addColorStop(0, '#9fb3a8'); wg.addColorStop(1, '#5f7a74'); ctx.fillStyle = wg; ctx.fill();
      var speed = (1 - calm) * .00022 + .00003;
      ctx.lineCap = 'round';
      streaks.forEach(function (s) {
        if (!reduce) { s.u += speed * dt * (.5 + s.u); if (s.u > 1) { s.u = 0; s.v = rand() * 2 - 1; } }
        var c = river(W, H, s.u), c2 = river(W, H, Math.min(1, s.u + .01)), a = Math.atan2(c2[1] - c[1], c2[0] - c[0]), n = a + Math.PI / 2, w = H * (.012 + .2 * s.u * s.u) * .85;
        var x0 = c[0] + Math.cos(n) * w * s.v, y0 = c[1] + Math.sin(n) * w * s.v, len = (8 + 60 * s.u) * (.25 + 1.6 * (1 - calm));
        ctx.strokeStyle = 'rgba(244,240,228,' + (Math.sin(Math.PI * s.u) * (.25 + .4 * (1 - calm))).toFixed(3) + ')'; ctx.lineWidth = .6 + 2 * s.u;
        ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(x0 - Math.cos(a) * len, y0 - Math.sin(a) * len); ctx.stroke();
      });
      // a massage table on the bank, beside the water
      var bx = W * .64, by = H * .86, bw = Math.min(W * .16, 150);
      ctx.fillStyle = '#2b1d14'; ctx.fillRect(bx, by, bw, bw * .07); ctx.fillRect(bx + bw * .08, by, bw * .05, bw * .28); ctx.fillRect(bx + bw * .87, by, bw * .05, bw * .28);
      ctx.fillStyle = '#efe2cf'; ctx.beginPath(); ctx.ellipse(bx + bw * .52, by - bw * .045, bw * .4, bw * .06, 0, 0, TAU); ctx.fill(); ctx.beginPath(); ctx.arc(bx + bw * .09, by - bw * .06, bw * .06, 0, TAU); ctx.fill();
      if (snd) snd.g.gain.setTargetAtTime(sndOn ? .03 + .1 * (1 - calm) : 0, snd.c.currentTime, .4);
      caption(cap, calm < .35 ? 'Rushing' : calm < .8 ? 'Slowing' : 'Still enough to rest');
    }
    var S = Stage(box, 800, 500, { frame: draw });
    box.addEventListener('pointermove', function (e) {   // fast movement stirs the water; stillness lets it settle
      var r = box.getBoundingClientRect(); pxT = (e.clientX - r.left) / r.width - .5;
      if (lastP) { var v = Math.hypot(e.clientX - lastP[0], e.clientY - lastP[1]) / Math.max(8, e.timeStamp - lastP[2]); if (v > .9) calm = Math.max(0, calm - .02 * v); }
      lastP = [e.clientX, e.clientY, e.timeStamp];
    });
    var btn = document.getElementById('riverSound');
    if (btn) btn.addEventListener('click', function () {   // optional river sound: filtered noise, off until asked for
      if (!snd) { var AC = window.AudioContext || window.webkitAudioContext; if (!AC) return; var c = new AC(), len = c.sampleRate * 3, buf = c.createBuffer(1, len, c.sampleRate), d = buf.getChannelData(0), last = 0;
        for (var n = 0; n < len; n++) { last = (last + .02 * (Math.random() * 2 - 1)) / 1.02; d[n] = last * 3.5; }
        var src = c.createBufferSource(); src.buffer = buf; src.loop = true; var f = c.createBiquadFilter(); f.type = 'lowpass'; f.frequency.value = 900; var g = c.createGain(); g.gain.value = 0;
        src.connect(f); f.connect(g); g.connect(c.destination); src.start(); snd = { c: c, g: g }; }
      sndOn = !sndOn; if (snd.c.state === 'suspended') snd.c.resume();
      btn.setAttribute('aria-pressed', String(sndOn)); btn.firstChild.textContent = sndOn ? 'River on' : 'River sound';
      if (reduce) snd.g.gain.value = sndOn ? .06 : 0;
    });
    return S;
  };

  // ---------- FINDER: the logo's banded circle as a depth gauge ----------
  sig.finder = function (box) {
    var DATA = window.EP_FINDER || [], level = 1, my = 128, mv = 0, rings = [], lastR = 0;
    var DEPTH = [52, 128, 204, 280, 356, 432], PRESS = [0, 9, 7, 12, 22, 32], COL = ['#efd9b6', '#e6b47c', '#c96c40', '#7a4a30', '#56613f'];
    function draw(S, t, dt) {
      var ctx = S.ctx, k = dt / 16.7, i, x;
      if (reduce) my = DEPTH[level]; else { mv += (DEPTH[level] - my) * .02 * k; mv *= Math.pow(.82, k); my += mv * k; }
      bg(S, '#2e211a');
      var pressure = PRESS[level] * (level === 3 ? .6 + .4 * Math.abs(Math.sin(t * .005)) : level === 4 ? .7 + .3 * breath(t) : 1);
      ctx.save(); ctx.beginPath(); ctx.arc(250, 280, 190, 0, TAU); ctx.clip();
      for (i = 0; i < 5; i++) {
        var top = 90 + i * 76;
        ctx.beginPath(); ctx.moveTo(40, 480);
        for (x = 40; x <= 460; x += 6) { var dip = top < my ? pressure * gauss(x - 250, 80) * (1 - (my - top) / 520) : 0, wav = level === 2 ? 3 * Math.sin(x * .035 - t * .0016 + i) : 0; ctx.lineTo(x, top + dip + wav); }
        ctx.lineTo(460, 480); ctx.closePath(); ctx.fillStyle = COL[i]; ctx.fill();
      }
      ctx.restore();
      ctx.strokeStyle = 'rgba(250,236,220,.35)'; ctx.lineWidth = 1.2; ctx.beginPath(); ctx.arc(250, 280, 190, 0, TAU); ctx.stroke();
      // ripples at the depth reached
      var gap = [0, 2200, 3000, 650, 2400, 2000][level];
      if (level > 0 && (t - lastR > gap) && !reduce) { rings.push({ t: t, y: my, l: level }); lastR = t; }
      if (reduce && level > 0) rings = [{ t: t - 500, y: my, l: level }, { t: t - 1300, y: my, l: level }];
      rings = rings.filter(function (r) { return t - r.t < 2000; });
      ctx.save(); ctx.beginPath(); ctx.arc(250, 280, 190, 0, TAU); ctx.clip();
      rings.forEach(function (r) { var u = (t - r.t) / 2000, big = r.l >= 4 ? 1.4 : r.l === 2 ? 1.8 : 1; ctx.strokeStyle = 'rgba(255,236,210,' + (.7 * (1 - u)).toFixed(3) + ')'; ctx.lineWidth = r.l >= 4 ? 2.4 : 1.4; ctx.beginPath(); ctx.ellipse(250, r.y, (14 + u * 120) * big, (4 + u * 22) * big, 0, 0, TAU); ctx.stroke(); });
      ctx.restore();
      // the touch: a warm light; for Reiki it rests above and its light falls in
      var mx = 250 + (level === 3 && !reduce ? Math.sin(t * .0025) * 16 : 0);
      if (level === 0) {
        ctx.globalCompositeOperation = 'lighter';
        for (i = 0; i < 7; i++) { var a = (i - 3) * .12, ly = reduce ? .5 : ((t / 1800 + i * .29) % 1); ctx.strokeStyle = 'rgba(255,214,160,' + (.35 * Math.sin(Math.PI * ly)).toFixed(3) + ')'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(mx + a * 40, my + 22 + ly * 60); ctx.lineTo(mx + a * 70, my + 40 + ly * 90); ctx.stroke(); }
        ctx.globalCompositeOperation = 'source-over';
      } else { ctx.strokeStyle = 'rgba(255,214,160,.25)'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(mx, 10); ctx.lineTo(mx, my - 18); ctx.stroke(); }
      var g = ctx.createRadialGradient(mx, my, 0, mx, my, 40); g.addColorStop(0, 'rgba(255,240,215,1)'); g.addColorStop(.3, 'rgba(255,190,120,.7)'); g.addColorStop(1, 'rgba(255,190,120,0)');
      ctx.fillStyle = g; ctx.fillRect(mx - 40, my - 40, 80, 80);
    }
    var S = Stage(box, 500, 500, { frame: draw });
    var inp = document.getElementById('press'), out = document.getElementById('pressOut'), card = document.getElementById('pick');
    function show() {
      level = +inp.value; var d = DATA[level]; if (!d) return;
      out.textContent = d.feel;
      card.innerHTML = '<p class="over">' + d.feel + '</p><h3>' + d.name + '</h3><p>' + d.desc + '</p><div class="row"><b>' + d.price + '</b><a class="link" href="' + d.href + '">See ' + d.short + '</a></div>';
      card.classList.remove('swap'); void card.offsetWidth; card.classList.add('swap'); S.redraw();
    }
    if (inp) { inp.addEventListener('input', show); show(); }
  };

  document.querySelectorAll('[data-sig]').forEach(function (b) { if (sig[b.dataset.sig]) sig[b.dataset.sig](b); });
})();
