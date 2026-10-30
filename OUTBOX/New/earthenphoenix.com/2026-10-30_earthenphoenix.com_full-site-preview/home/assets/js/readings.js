/* Earthen Phoenix, astrology / tarot / herbs page. ep.js already runs the header, reveals and gauge; this adds:
   star trails over the hero, the birth-chart wheel, the tarot spread and its candle, the remedies, the herbs' journey,
   and the per-minute cost meter. Animations start when seen, pause off screen, and rest in their final state under reduced motion. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;
  var NS = 'http://www.w3.org/2000/svg';
  function sine(x) { return -(Math.cos(Math.PI * Math.max(0, Math.min(1, x))) - 1) / 2; }
  function watch(el, cb) { if (!hasIO) { cb(true); return; } new IntersectionObserver(function (es) { es.forEach(function (e) { cb(e.isIntersecting); }); }, { rootMargin: '60px' }).observe(el); }
  function once(el, fn, th) { if (!hasIO) { fn(); return; } var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { io.disconnect(); fn(); } }); }, { threshold: th || .3 }); io.observe(el); }

  // ---------- star trails: the sky turning slowly around the pole star, like a long exposure over the canyon ----------
  (function () {
    var cv = document.getElementById('trails'); if (!cv) return;
    var ctx = cv.getContext('2d'), hero = cv.parentNode, W, H, stars = [], px, py, visible = true, raf = 0, prev = 0, ang = 0;
    function build() {
      var r = cv.getBoundingClientRect(), dpr = Math.min(2, window.devicePixelRatio || 1);
      W = r.width; H = r.height; cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      px = W * (W < 760 ? .78 : .8); py = H * .1;
      var n = W < 760 ? 110 : 220, maxR = Math.hypot(Math.max(px, W - px), H); stars = [];
      for (var i = 0; i < n; i++) { var rr = Math.sqrt(Math.random()) * maxR; stars.push({ r: rr, a: Math.random() * 6.283, s: .5 + Math.random() * 1.2, b: .3 + Math.random() * .6, w: Math.random() < .14, tw: Math.random() * 6.283, len: .25 + Math.random() * .45 }); }
      ctx.clearRect(0, 0, W, H);
    }
    function paint(t) {   // long-exposure arcs: each star leaves a fading trail behind its head, all turning about the pole
      ctx.clearRect(0, 0, W, H); ctx.lineCap = 'round';
      for (var i = 0; i < stars.length; i++) {
        var s = stars[i], a = s.a + ang, len = s.len, col = s.w ? '255,214,170,' : '250,245,236,';
        var hx = px + Math.cos(a) * s.r, hy = py + Math.sin(a) * s.r;
        if (s.r * len < 2 || hx < -60 || hx > W + 60 || hy < -60 || hy > H + 60) continue;
        ctx.lineWidth = s.s * .7;
        for (var k = 0; k < 4; k++) { ctx.strokeStyle = 'rgba(' + col + (s.b * (.08 + k * .1)) + ')'; ctx.beginPath(); ctx.arc(px, py, s.r, a - len * (1 - k / 4), a - len * (1 - (k + 1) / 4)); ctx.stroke(); }
        ctx.fillStyle = 'rgba(' + col + (s.b * (.75 + .25 * Math.sin(t * .0016 + s.tw))) + ')'; ctx.beginPath(); ctx.arc(hx, hy, s.s * .75, 0, 6.283); ctx.fill();
      }
      ctx.fillStyle = 'rgba(255,232,200,.95)'; ctx.beginPath(); ctx.arc(px, py, 2.2, 0, 6.283); ctx.fill();   // the pole star stays put
    }
    function frame(now) {
      raf = 0; if (!visible || document.hidden) return;
      var dt = prev ? Math.min(50, now - prev) : 16; prev = now; ang += dt * 6.283 / 600000;   // one turn every 10 minutes
      paint(now); raf = requestAnimationFrame(frame);
    }
    function start() { if (!raf && !reduce) { prev = 0; raf = requestAnimationFrame(frame); } }
    build();
    if (reduce) paint(0); else { watch(hero, function (v) { visible = v; if (v) start(); }); document.addEventListener('visibilitychange', start); start(); }
    addEventListener('resize', function () { clearTimeout(build.t); build.t = setTimeout(function () { build(); if (reduce) paint(0); }, 200); });
  })();

  // ---------- birth-chart wheel ----------
  (function () {
    var wrap = document.querySelector('.wheel-wrap'); if (!wrap) return;
    var turn = document.getElementById('wheelTurn'), gS = turn.querySelector('.w-sectors'), gH = turn.querySelector('.w-houses'), gG = turn.querySelector('.w-glyphs'), ray = document.getElementById('sunRay');
    var mSel = document.getElementById('bMonth'), dSel = document.getElementById('bDay'), out = document.getElementById('birthOut');
    var SIGNS = [ // tropical sun-sign dates as commonly given; cusps can shift by a day in some years
      ['Aries', '♈', 3, 21, 'Mar 21 – Apr 19'], ['Taurus', '♉', 4, 20, 'Apr 20 – May 20'], ['Gemini', '♊', 5, 21, 'May 21 – Jun 20'],
      ['Cancer', '♋', 6, 21, 'Jun 21 – Jul 22'], ['Leo', '♌', 7, 23, 'Jul 23 – Aug 22'], ['Virgo', '♍', 8, 23, 'Aug 23 – Sep 22'],
      ['Libra', '♎', 9, 23, 'Sep 23 – Oct 22'], ['Scorpio', '♏', 10, 23, 'Oct 23 – Nov 21'], ['Sagittarius', '♐', 11, 22, 'Nov 22 – Dec 21'],
      ['Capricorn', '♑', 12, 22, 'Dec 22 – Jan 19'], ['Aquarius', '♒', 1, 20, 'Jan 20 – Feb 18'], ['Pisces', '♓', 2, 19, 'Feb 19 – Mar 20']];
    function rad(d) { return d * Math.PI / 180; }
    function pt(r, d) { return [r * Math.cos(rad(d)), r * Math.sin(rad(d))]; }
    var sectors = [], glyphs = [];
    for (var i = 0; i < 12; i++) {
      // signs run counter-clockwise from the ascendant (left), as on a chart
      var a1 = 180 - i * 30, a2 = 180 - (i + 1) * 30, p1 = pt(196, a1), p2 = pt(196, a2), q2 = pt(152, a2), q1 = pt(152, a1);
      var path = document.createElementNS(NS, 'path');
      path.setAttribute('d', 'M' + p1 + 'A196 196 0 0 0 ' + p2 + 'L' + q2 + 'A152 152 0 0 1 ' + q1 + 'Z'); gS.appendChild(path); sectors.push(path);
      var c = pt(174, a1 - 15), tx = document.createElementNS(NS, 'text'); tx.setAttribute('x', c[0].toFixed(1)); tx.setAttribute('y', c[1].toFixed(1)); tx.style.setProperty('--g', i);
      tx.textContent = SIGNS[i][1] + '︎'; gG.appendChild(tx); glyphs.push({ el: tx, x: c[0], y: c[1] });
      var h1 = pt(64, a1 - 9), h2 = pt(152, a1 - 9), ln = document.createElementNS(NS, 'line');
      ln.setAttribute('x1', h1[0].toFixed(1)); ln.setAttribute('y1', h1[1].toFixed(1)); ln.setAttribute('x2', h2[0].toFixed(1)); ln.setAttribute('y2', h2[1].toFixed(1)); gH.appendChild(ln);
    }
    var phi = 0, visible = false, raf = 0, prev = 0, anim = null, chosen = -1;
    function set(p) { phi = p; turn.setAttribute('transform', 'rotate(' + p.toFixed(2) + ')'); glyphs.forEach(function (g) { g.el.setAttribute('transform', 'rotate(' + (-p).toFixed(2) + ' ' + g.x.toFixed(1) + ' ' + g.y.toFixed(1) + ')'); }); }
    function frame(now) {
      raf = 0; var dt = prev ? Math.min(50, now - prev) : 16; prev = now;
      if (anim) { var t = (now - anim.t0) / anim.d; set(anim.from + (anim.to - anim.from) * sine(t)); if (t >= 1) { anim = null; light(); } }
      else if (chosen < 0) set(phi + dt * 360 / 240000);   // idle: one slow turn every four minutes
      if (visible && (anim || chosen < 0)) raf = requestAnimationFrame(frame);
    }
    function start() { if (!raf && !reduce) { prev = 0; raf = requestAnimationFrame(frame); } }
    function light() {
      sectors.forEach(function (s, k) { s.classList.toggle('lit', k === chosen); }); glyphs.forEach(function (g, k) { g.el.classList.toggle('lit', k === chosen); });
      ray.classList.toggle('on', chosen >= 0);
    }
    function signOf(m, d) { for (var i = 0; i < 12; i++) { var s = SIGNS[i], n = SIGNS[(i + 1) % 12]; var after = (m === s[2] && d >= s[3]), before = (m === n[2] && d < n[3]); if (after || before) return i; } return -1; }
    var days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
    function fillDays() {
      var m = +mSel.value, keep = +dSel.value, n = m ? days[m - 1] : 31, html = '<option value="">Day</option>';
      for (var d = 1; d <= n; d++) html += '<option value="' + d + '"' + (d === keep ? ' selected' : '') + '>' + d + '</option>';
      dSel.innerHTML = html;
    }
    function choose() {
      var m = +mSel.value, d = +dSel.value; if (!m || !d) return;
      var i = signOf(m, d); if (i < 0) return; chosen = i;
      var target = i * 30 + 15, from = ((phi % 360) + 360) % 360, delta = ((target - from + 540) % 360) - 180;
      out.innerHTML = 'Your sun is in <b>' + SIGNS[i][0] + '</b> (' + SIGNS[i][4] + '). That is one point on the wheel; a reading explores your whole birth chart.';
      sectors.forEach(function (s) { s.classList.remove('lit'); }); glyphs.forEach(function (g) { g.el.classList.remove('lit'); }); ray.classList.remove('on');
      if (reduce) { set(target); light(); return; }
      anim = { from: from, to: from + delta, t0: performance.now(), d: 1800 }; set(from); start();
    }
    fillDays();
    mSel.addEventListener('change', function () { fillDays(); choose(); }); dSel.addEventListener('change', choose);
    set(0);
    if (reduce) wrap.classList.add('in'); else once(wrap, function () { wrap.classList.add('in'); }, .25);
    watch(wrap, function (v) { visible = v; if (v) start(); });
  })();

  // ---------- tarot spread + the candle at its centre ----------
  (function () {
    var spread = document.getElementById('spread'); if (!spread) return;
    var cards = spread.querySelectorAll('.card');
    function open(c, o) { c.classList.toggle('open', o); c.setAttribute('aria-pressed', String(o)); }
    cards.forEach(function (c) { c.addEventListener('click', function () { open(c, !c.classList.contains('open')); puff(c); }); });
    if (reduce) cards.forEach(function (c) { open(c, true); });
    else once(spread, function () { cards.forEach(function (c, i) { setTimeout(function () { open(c, true); }, 600 + i * 750); }); }, .35);
    var oracle = document.getElementById('oracle');
    if (oracle) oracle.addEventListener('click', function () { oracle.classList.remove('sway'); void oracle.offsetWidth; if (!reduce) oracle.classList.add('sway'); });

    var cv = document.getElementById('flame'), ctx = cv.getContext('2d'), sec = document.getElementById('table');
    var W, H, visible = false, raf = 0, lean = 0, leanV = 0, air = 0, last = null;
    function size() { var r = cv.getBoundingClientRect(), dpr = Math.min(2, window.devicePixelRatio || 1); W = r.width; H = r.height; cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
    function draw(t) {
      ctx.clearRect(0, 0, W, H);
      var cx = W / 2, bw = Math.min(46, W * .34), bh = H * .38, top = H - bh, fl = Math.min(64, H * .26);
      var fk = reduce ? 1 : 1 + .07 * Math.sin(t * .011) + .045 * Math.sin(t * .027 + 1.3) + .03 * Math.sin(t * .053 + .4);
      var h = fl * fk, tipX = cx + lean * h * .9 + (reduce ? 0 : Math.sin(t * .004) * 1.5), tipY = top - 10 - h * (1 - Math.abs(lean) * .25);
      var hr = Math.min(W / 2, (top - h * .4)) * .98, halo = ctx.createRadialGradient(cx, top - h * .4, 2, cx, top - h * .4, hr);   // fades to nothing inside the canvas, so no edge shows   // glow on the table
      halo.addColorStop(0, 'rgba(255,196,120,' + (.34 * fk) + ')'); halo.addColorStop(.6, 'rgba(255,196,120,' + (.08 * fk) + ')'); halo.addColorStop(1, 'rgba(255,196,120,0)');
      ctx.fillStyle = halo; ctx.fillRect(0, 0, W, H);
      var wax = ctx.createLinearGradient(cx - bw / 2, 0, cx + bw / 2, 0); wax.addColorStop(0, '#d8c3a5'); wax.addColorStop(.45, '#f7ecdb'); wax.addColorStop(1, '#c4a987');
      ctx.fillStyle = wax; ctx.beginPath(); ctx.moveTo(cx - bw / 2, H); ctx.lineTo(cx - bw / 2, top + 4); ctx.quadraticCurveTo(cx, top - 3, cx + bw / 2, top + 4); ctx.lineTo(cx + bw / 2, H); ctx.fill();
      ctx.strokeStyle = '#2b1d14'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(cx, top + 1); ctx.quadraticCurveTo(cx + lean * 3, top - 5, cx + lean * 5, top - 9); ctx.stroke();
      var base = top - 6, w = 9 + 2 * fk;
      var g = ctx.createLinearGradient(0, tipY, 0, base + 4); g.addColorStop(0, 'rgba(255,200,110,0)'); g.addColorStop(.25, 'rgba(255,180,90,.9)'); g.addColorStop(.75, 'rgba(255,226,160,1)'); g.addColorStop(1, 'rgba(255,170,90,.6)');
      ctx.fillStyle = g; ctx.beginPath(); ctx.moveTo(cx + lean * 4, base + 4);
      ctx.bezierCurveTo(cx - w * 1.3, base - 2, cx - w * .6 + lean * h * .4, tipY + h * .45, tipX, tipY);
      ctx.bezierCurveTo(cx + w * .6 + lean * h * .4, tipY + h * .45, cx + w * 1.3, base - 2, cx + lean * 4, base + 4); ctx.fill();
      var core = ctx.createRadialGradient(cx + lean * 6, base - 4, 1, cx + lean * 6, base - 4, w); core.addColorStop(0, 'rgba(255,252,236,.95)'); core.addColorStop(1, 'rgba(255,252,236,0)');
      ctx.fillStyle = core; ctx.beginPath(); ctx.ellipse(cx + lean * 6, base - 5, w * .55, w * 1.1, lean * .5, 0, 6.283); ctx.fill();
    }
    function frame(now) {
      raf = 0; if (!visible || document.hidden) return;
      air *= .94; var target = Math.max(-.7, Math.min(.7, air));   // the flame bends away from moving air, then rights itself
      leanV += (target - lean) * .05; leanV *= .86; lean += leanV;
      draw(now); raf = requestAnimationFrame(frame);
    }
    function push(x, y, t) {
      var r = cv.getBoundingClientRect(), cx = r.left + r.width / 2, cy = r.top + r.height * .5;
      if (last) { var dt = Math.max(8, t - last[2]), vx = (x - last[0]) / dt, d = Math.hypot(x - cx, y - cy), fall = Math.max(0, 1 - d / 520); air += vx * .22 * fall; }
      last = [x, y, t];
    }
    function puff(c) { var r = c.getBoundingClientRect(), f = cv.getBoundingClientRect(); air += (r.left + r.width / 2 < f.left + f.width / 2 ? .35 : -.35); }
    size(); draw(0);
    if (!reduce) {
      sec.addEventListener('pointermove', function (e) { if (e.pointerType === 'mouse' || e.buttons) push(e.clientX, e.clientY, e.timeStamp); }, { passive: true });
      sec.addEventListener('pointerleave', function () { last = null; });
      watch(cv, function (v) { visible = v; if (v && !raf) raf = requestAnimationFrame(frame); });
      document.addEventListener('visibilitychange', function () { if (!raf && visible) raf = requestAnimationFrame(frame); });
    }
    addEventListener('resize', function () { clearTimeout(size.t); size.t = setTimeout(function () { size(); draw(0); }, 200); });
  })();

  // ---------- remedies: tea steeps, the rollie rolls, the tincture drops ----------
  document.querySelectorAll('.rem').forEach(function (r, i) {
    var busy = false;
    function go() { if (busy || reduce) return; busy = true; r.classList.remove('go'); void r.getBoundingClientRect(); r.classList.add('go'); setTimeout(function () { busy = false; }, 3600); }
    once(r, function () { setTimeout(go, i * 700); }, .5);
    r.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') go(); });
    r.addEventListener('click', go);
  });

  // ---------- the herbs' journey: Oregon to Salt Lake City ----------
  (function () {
    var j = document.getElementById('journey'); if (!j) return;
    var route = document.getElementById('route'), leaf = j.querySelector('.traveller'), L = route.getTotalLength(), running = false;
    function place(u) {
      var p = route.getPointAtLength(L * u), q = route.getPointAtLength(Math.min(L, L * u + 1)), a = Math.atan2(q.y - p.y, q.x - p.x) * 180 / Math.PI;
      leaf.setAttribute('transform', 'translate(' + p.x.toFixed(1) + ' ' + (p.y - 10).toFixed(1) + ') rotate(' + (a + 90).toFixed(1) + ')');
    }
    function travel() {
      if (running) return; running = true; var t0 = performance.now();
      (function step(now) { var u = sine((now - t0) / 5200); place(u); if (u < 1) requestAnimationFrame(step); else running = false; })(t0);
    }
    if (reduce) { place(1); return; }
    place(0); once(j, function () { setTimeout(travel, 400); }, .5);
    j.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') travel(); }); j.addEventListener('click', travel);
  })();

  // ---------- cost meter: $2 per minute ----------
  (function () {
    var inp = document.getElementById('mins'); if (!inp) return;
    var arc = document.getElementById('mArc'), out = document.getElementById('mOut');
    function upd() { var m = +inp.value; out.innerHTML = '<b>$' + (m * 2) + '</b><span>' + m + ' minutes</span>'; arc.style.strokeDashoffset = (1 - m / 90).toFixed(3); }
    inp.addEventListener('input', upd); upd();
  })();
})();
