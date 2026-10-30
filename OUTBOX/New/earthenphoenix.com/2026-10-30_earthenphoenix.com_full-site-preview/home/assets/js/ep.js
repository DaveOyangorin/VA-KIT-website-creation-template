/* Earthen Phoenix: every motion comes from something Miquelle does.
   1. Release (hero): a line drawing of held tension along the photo's lower edge. Moving across it (cursor, or a finger) presses
      the knots loose, slowly, with weight; once released the lines settle into a wave that breathes 4 in, 4 out.
   2. One service, one motion: massage ripple on linen, a yoga line that flows then holds, a singing bowl, a sprig + stars + card.
   3. Breathe: the breath circle drawn as singing-bowl rings. Timeline grows as a root; reviews rise on a breath; oil shimmer.
   Everything starts only when seen, pauses when off screen, and shows its still final state under prefers-reduced-motion. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var coarse = window.matchMedia('(pointer: coarse)').matches;
  var hasIO = 'IntersectionObserver' in window;
  var yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();
  function ease(x) { return x <= 0 ? 0 : x >= 1 ? 1 : x * x * (3 - 2 * x); }
  function inOut(x) { return x < .5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; }
  function sine(x) { return -(Math.cos(Math.PI * x) - 1) / 2; }
  // run cb(true/false) as el enters / leaves the screen
  function watch(el, cb, margin) {
    if (!hasIO) { cb(true); return; }
    new IntersectionObserver(function (es) { es.forEach(function (e) { cb(e.isIntersecting); }); }, { rootMargin: margin || '60px' }).observe(el);
  }
  // run fn once, when a good part of el is in view
  function once(el, fn, th) {
    if (!hasIO) { fn(); return; }
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { io.disconnect(); fn(); } }); }, { threshold: th || .3 });
    io.observe(el);
  }

  // ---------- header: menu, solid bar, real bottom edge for the phone panel ----------
  var bar = document.getElementById('bar'), nav = document.getElementById('nav'), mb = document.getElementById('menuBtn'), root = document.documentElement;
  function scrollY_() { return Math.max(window.pageYOffset || 0, root.scrollTop || 0, document.body.scrollTop || 0); }
  function setMenu(o) { nav.classList.toggle('open', o); mb.setAttribute('aria-expanded', String(o)); root.classList.toggle('menu-open', o); onScroll(); }
  mb.addEventListener('click', function () { setMenu(!nav.classList.contains('open')); });
  nav.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
  var dot = document.getElementById('gaugeDot');
  function onScroll() {
    var y = scrollY_();
    dot.style.top = (y / Math.max(1, document.body.scrollHeight - innerHeight) * 100) + '%';
    bar.classList.toggle('solid', y > innerHeight * .6 || nav.classList.contains('open'));
    root.style.setProperty('--hdr-bottom', Math.max(0, Math.round(bar.getBoundingClientRect().bottom)) + 'px');
  }
  addEventListener('scroll', onScroll, { passive: true }); addEventListener('resize', onScroll, { passive: true }); onScroll();

  // ---------- reveals ----------
  var seen = document.querySelectorAll('.rise, .breath-in, .years');
  if (hasIO && !reduce) {
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .18 });
    seen.forEach(function (el) { io.observe(el); });
  } else seen.forEach(function (el) { el.classList.add('in'); });

  // ---------- sound: off by default, one shared toggle, a soft bowl tone ----------
  var snd = { on: false, ctx: null }, sndBtns = document.querySelectorAll('.snd');
  function chime(level) {
    if (!snd.on || !snd.ctx) return;
    var c = snd.ctx, t = c.currentTime + .01, out = c.createGain(); out.gain.value = .1 * (level || 1); out.connect(c.destination);
    // partials of a small bowl: a beating fundamental and a few inharmonic overtones, each fading at its own pace
    [[1, .9, 6], [1.007, .55, 6], [2.74, .3, 4], [5.18, .12, 2.6], [8.6, .05, 1.6]].forEach(function (p) {
      var o = c.createOscillator(), g = c.createGain(); o.type = 'sine'; o.frequency.value = 228 * p[0];
      g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(p[1], t + .015); g.gain.exponentialRampToValueAtTime(.0001, t + p[2]);
      o.connect(g); g.connect(out); o.start(t); o.stop(t + p[2] + .1);
    });
  }
  function setSound(on) {
    snd.on = on;
    if (on && !snd.ctx) { var AC = window.AudioContext || window.webkitAudioContext; if (AC) snd.ctx = new AC(); }
    if (on && snd.ctx && snd.ctx.state === 'suspended') snd.ctx.resume();
    sndBtns.forEach(function (b) { b.setAttribute('aria-pressed', String(on)); b.firstChild.textContent = on ? 'Sound on' : 'Sound off'; });
    if (on) chime(.7);
  }
  sndBtns.forEach(function (b) { b.addEventListener('click', function (e) { e.stopPropagation(); setSound(!snd.on); }); });

  // ---------- 1. RELEASE (hero) ----------
  (function () {
    var hero = document.querySelector('.hero'), cv = document.getElementById('release'); if (!cv) return;
    var ctx = cv.getContext('2d'), hint = document.getElementById('releaseHint');
    var B = 64, rel = new Float32Array(B), tgt = new Float32Array(B), vel = new Float32Array(B);
    var W, H, narrow, strands = [], P, visible = true, raf = 0, prev = 0, last = null, lastInput = performance.now(), done = false;
    function seeded(s) { return function () { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }; }
    function build() {
      var r = cv.getBoundingClientRect(), dpr = Math.min(2, window.devicePixelRatio || 1);
      W = Math.max(200, r.width); H = Math.max(100, r.height); narrow = W < 760;
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var n = narrow ? 5 : 7, rand = seeded(11); strands = []; P = Math.round(Math.min(900, Math.max(320, W / 1.5)));
      for (var k = 0; k < n; k++) {
        var knots = [], m = 4;
        for (var j = 0; j < m; j++) {
          var kr = (narrow ? 10 : 13) + rand() * (narrow ? 8 : 11);
          // f is chosen so the trochoid actually loops back on itself: a knot, not a wiggle
          knots.push({ x: (j + .5) / m + (rand() - .5) * .3 / m, w: .034 + rand() * .034, r: kr, f: W / (kr * 6.283) * (1.9 + rand() * 1.1), ph: rand() * 6.283 });
        }
        strands.push({ y: .22 + .56 * k / (n - 1), knots: knots, j1: rand() * 6.283, j2: rand() * 6.283, wp: rand() * 6.283, a: .55 + rand() * .4 });
      }
    }
    function relAt(s) { var p = s * (B - 1), i = Math.floor(p), f = p - i; return i >= B - 1 ? rel[B - 1] : rel[i] + (rel[i + 1] - rel[i]) * f; }
    function draw(t) {
      ctx.clearRect(0, 0, W, H);
      var breath = .5 - .5 * Math.cos(t / 8000 * 6.283);   // 4 s in, 4 s out, same as the breathing section
      var g = ctx.createLinearGradient(0, 0, W, 0);
      for (var c = 0; c <= 10; c++) {
        var r = ease(relAt(c / 10));   // tension glows ember; released lines go back to cream
        g.addColorStop(c / 10, 'rgb(' + Math.round(232 + 18 * r) + ',' + Math.round(132 + 113 * r) + ',' + Math.round(78 + 158 * r) + ')');
      }
      ctx.strokeStyle = g; ctx.lineWidth = narrow ? 1.25 : 1.5; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
      for (var k = 0; k < strands.length; k++) {
        var st = strands[k], yb = st.y * H; ctx.beginPath();
        for (var i = 0; i <= P; i++) {
          var s = i / P, rr = ease(relAt(s)), ten = 1 - rr;
          var amp = (3 + 8 * breath) * (.35 + .65 * rr);   // released: long flowing curves, rising and falling with the breath
          var y = yb + Math.sin(s * 5.6 + st.wp + t * .00019) * amp + Math.sin(s * 2.3 + k * .45 + t * .00008) * (6 + 10 * rr);
          var x = s * W;
          if (ten > .002) {
            var dx = 0, dy = 0;
            for (var j = 0; j < st.knots.length; j++) {
              var kn = st.knots[j], d = (s - kn.x) / kn.w;
              if (d > -3 && d < 3) { var ga = Math.exp(-d * d), ph = (s - kn.x) * kn.f * 6.283 + kn.ph + rr * 5; dx += kn.r * ga * Math.sin(ph); dy += kn.r * ga * Math.cos(ph) * .85; }
            }
            dy += Math.sin(s * W * .19 + st.j1) * 1.5 + Math.sin(s * W * .071 + st.j2) * 2.4;   // a nervous, held quality
            x += dx * ten; y += dy * ten;
          }
          if (i) ctx.lineTo(x, y); else ctx.moveTo(x, y);
        }
        ctx.globalAlpha = st.a; ctx.stroke();
      }
      ctx.globalAlpha = 1;
    }
    function step(dt, now) {
      var k = Math.min(3, dt / 16.7), mean = 0, i;
      for (i = 0; i < B; i++) mean += tgt[i]; mean /= B;
      var idle = now - lastInput > 9000;   // left alone, it still lets go, very slowly
      for (i = 0; i < B; i++) {
        if (idle) tgt[i] = Math.min(1, tgt[i] + .00045 * k);
        if (mean > .78) tgt[i] += (1 - tgt[i]) * .005 * k;
      }
      for (i = 1; i < B - 1; i++) { var nb = (tgt[i - 1] + tgt[i + 1]) * .5; if (nb > tgt[i]) tgt[i] += (nb - tgt[i]) * .02 * k; }   // loosening spreads along the line
      var m2 = 0;
      for (i = 0; i < B; i++) {   // heavy, slightly under-damped spring: release lags the hand, like tissue under pressure
        vel[i] += (tgt[i] - rel[i]) * .0042 * k; vel[i] *= Math.pow(.905, k); rel[i] = Math.max(0, Math.min(1.02, rel[i] + vel[i] * k)); m2 += rel[i];
      }
      if (!done && m2 / B > .97) {
        done = true; hint.firstChild.textContent = hint.lastChild.textContent = 'Released. Breathe with it.';
        hint.classList.remove('gone'); setTimeout(function () { hint.classList.add('gone'); }, 5000);
      }
    }
    function frame(now) {
      raf = 0; if (!visible || document.hidden) return;
      step(prev ? now - prev : 16.7, now); prev = now; draw(now); raf = requestAnimationFrame(frame);
    }
    function start() { if (!raf && !reduce) { prev = 0; raf = requestAnimationFrame(frame); } }
    function press(x, y) {
      var r = cv.getBoundingClientRect(), s = (x - r.left) / r.width;
      var prox = Math.max(.3, 1 - Math.abs(y - (r.top + r.height * .5)) / (r.height * 1.6));
      if (last) {
        var amt = Math.min(Math.hypot(x - last[0], y - last[1]), 70) / r.width * 3.6 * prox;
        for (var i = 0; i < B; i++) { var dd = (i / (B - 1) - s) / .075; tgt[i] = Math.min(1, tgt[i] + amt * Math.exp(-dd * dd)); }
        if (!done) hint.classList.add('gone');
      }
      last = [x, y]; lastInput = performance.now();
    }
    build();
    if (reduce) { for (var i = 0; i < B; i++) rel[i] = tgt[i] = 1; draw(2000); hint.hidden = true; }
    else {
      hero.addEventListener('pointermove', function (e) { if (e.pointerType === 'mouse' || e.buttons) press(e.clientX, e.clientY); }, { passive: true });
      hero.addEventListener('pointerdown', function (e) { last = [e.clientX, e.clientY]; }, { passive: true });
      ['pointerleave', 'pointerup', 'pointercancel'].forEach(function (n) { hero.addEventListener(n, function () { last = null; }, { passive: true }); });
      watch(hero, function (v) { visible = v; if (v) start(); });
      document.addEventListener('visibilitychange', start);
      start();
    }
    addEventListener('resize', function () { clearTimeout(build.t); build.t = setTimeout(function () { build(); if (reduce) draw(2000); }, 200); });
  })();

  // ---------- 2. one service, one motion ----------
  var NS = 'http://www.w3.org/2000/svg';
  function svgPoint(svg, e) { var r = svg.getBoundingClientRect(); return [(e.clientX - r.left) / r.width * 240, (e.clientY - r.top) / r.height * 240]; }

  var makers = {
    // massage: warm pressure spreading from the touch point across linen; the tags under it flow like lymph
    massage: function (v) {
      var svg = v.querySelector('svg'), layer = v.querySelector('.m-ripples'), tags = v.parentNode.querySelectorAll('.tags li'), lastT = 0;
      function circle(x, y, r, cls, fill) { var c = document.createElementNS(NS, 'circle'); c.setAttribute('cx', x); c.setAttribute('cy', y); c.setAttribute('r', r); if (cls) c.setAttribute('class', cls); if (fill) c.setAttribute('fill', fill); c.style.transformOrigin = x + 'px ' + y + 'px'; layer.appendChild(c); return c; }
      function ripple(x, y) {
        var now = performance.now(); if (now - lastT < 900) return; lastT = now;
        var dent = circle(x, y, 34, '', 'url(#dent)');
        dent.animate([{ opacity: 0, transform: 'scale(.6)' }, { opacity: 1, transform: 'scale(1)', offset: .25 }, { opacity: 0, transform: 'scale(1.15)' }], { duration: 2200, easing: 'cubic-bezier(.45,.05,.25,1)' }).onfinish = function () { dent.remove(); };
        var warm = circle(x, y, 90, '', 'url(#warmth)');
        warm.animate([{ opacity: 0, transform: 'scale(.15)' }, { opacity: 1, offset: .3 }, { opacity: 0, transform: 'scale(1.6)' }], { duration: 2600, easing: 'cubic-bezier(.2,.7,.2,1)' }).onfinish = function () { warm.remove(); };
        [0, 420, 840].forEach(function (d, i) {
          var c = circle(x, y, 100, 'm-ring' + (i ? ' soft' : ''));
          c.animate([{ opacity: 0, transform: 'scale(.05)' }, { opacity: .8, offset: .12 }, { opacity: 0, transform: 'scale(1.7)' }], { duration: 2800, delay: d, easing: 'cubic-bezier(.2,.65,.25,1)', fill: 'backwards' }).onfinish = function () { c.remove(); };
        });
        // the ripple reaches the modality tags one after another
        tags.forEach(function (li, i) { li.animate([{ transform: 'none' }, { transform: 'translateY(-3px)' }, { transform: 'none' }], { duration: 1400, delay: 500 + i * 140, easing: 'cubic-bezier(.45,.05,.25,1)' }); });
      }
      var api = {
        play: function () { ripple(120, 120); },
        tap: function (e) { var p = svgPoint(svg, e); ripple(p[0], p[1]); }
      };
      svg.addEventListener('pointermove', function (e) { if (e.pointerType === 'mouse') api.tap(e); });
      return api;
    },

    // yoga: one continuous line moves through a Vinyasa sequence quickly, then eases into child's pose and holds (Yin)
    yoga: function (v) {
      var path = v.querySelector('.y-line'), cap = v.querySelector('.y-cap'), visible = false, raf = 0, drawn = false;
      var P = {
        mountain: { F: [120, 200], K: [120, 166], H: [120, 132], S: [120, 84], E: [122, 108], W: [123, 132], C: [120, 68] },
        salute:   { F: [120, 200], K: [120, 166], H: [120, 132], S: [119, 84], E: [117, 60], W: [116, 36], C: [123, 69] },
        fold:     { F: [120, 200], K: [120, 166], H: [118, 132], S: [140, 172], E: [138, 190], W: [130, 200], C: [151, 184] },
        plank:    { F: [52, 198], K: [83, 185], H: [114, 171], S: [158, 152], E: [158, 176], W: [158, 200], C: [172, 146] },
        updog:    { F: [52, 198], K: [86, 197], H: [119, 194], S: [143, 152], E: [146, 176], W: [148, 200], C: [152, 138] },
        downdog:  { F: [72, 200], K: [85, 168], H: [98, 136], S: [131, 168], E: [147, 184], W: [163, 200], C: [139, 181] },
        child:    { F: [70, 198], K: [108, 198], H: [78, 176], S: [122, 186], E: [150, 196], W: [176, 198], C: [136, 189] }
      };
      var FLOW = [['salute', 620, 260], ['fold', 640, 260], ['plank', 700, 240], ['updog', 620, 260], ['downdog', 700, 420], ['child', 2200, 0]];
      var cur = clone(P.mountain), state = 'idle', seq = 0, segFrom = null, segT0 = 0, holdT0 = 0;
      function clone(p) { var o = {}; for (var k in p) o[k] = p[k].slice(); return o; }
      function mix(a, b, t) { var o = {}; for (var k in a) o[k] = [a[k][0] + (b[k][0] - a[k][0]) * t, a[k][1] + (b[k][1] - a[k][1]) * t]; return o; }
      function render(p, br) {
        var S = [p.S[0], p.S[1] - br], H = [p.H[0], p.H[1] - br * .5], C = [p.C[0], p.C[1] - br * .7];
        var a0 = Math.atan2(S[1] - C[1], S[0] - C[0]), N = [C[0] + Math.cos(a0) * 10, C[1] + Math.sin(a0) * 10];
        var pts = [[24, 200], p.F, p.K, H, S, N];
        for (var i = 1; i <= 18; i++) { var a = a0 + i / 18 * 6.283; pts.push([C[0] + Math.cos(a) * 10, C[1] + Math.sin(a) * 10]); }
        pts.push(S, p.E, p.W);
        path.setAttribute('d', 'M' + pts.map(function (q) { return q[0].toFixed(1) + ' ' + q[1].toFixed(1); }).join('L'));
      }
      function caption(txt) { if (cap.textContent === txt) return; cap.classList.add('fade'); setTimeout(function () { cap.textContent = txt; cap.classList.remove('fade'); }, 600); }
      function frame(now) {
        raf = 0;
        if (state === 'flow') {
          var step = FLOW[seq], d = step[1], t = (now - segT0) / d;
          if (t < 1) cur = mix(segFrom, P[step[0]], seq === FLOW.length - 1 ? sine(t) : inOut(t));
          else {
            cur = clone(P[step[0]]);
            if (now - segT0 > d + step[2]) {
              if (seq === FLOW.length - 1) { state = 'hold'; holdT0 = now; caption('Yin · hold'); }
              else { seq++; segFrom = clone(cur); segT0 = now; if (seq === FLOW.length - 1) caption('Yin · slow'); }
            }
          }
          render(cur, 0);
        } else if (state === 'hold') render(cur, (.5 - .5 * Math.cos((now - holdT0) / 8000 * 6.283)) * 1.6);   // still, just breathing
        if (visible && state !== 'idle') raf = requestAnimationFrame(frame);
      }
      function begin() { state = 'flow'; seq = 0; segFrom = clone(cur); segT0 = performance.now(); caption('Vinyasa · flow'); if (!raf) raf = requestAnimationFrame(frame); }
      render(cur, 0);
      if (reduce) { cur = clone(P.child); render(cur, 0); cap.textContent = 'Yin · hold'; return { play: function () {}, tap: function () {} }; }
      path.style.strokeDasharray = '1 1'; path.style.strokeDashoffset = '1';
      watch(v, function (vis) { visible = vis; if (vis && state !== 'idle' && !raf) raf = requestAnimationFrame(frame); });
      function play() {
        if (state === 'flow' || state === 'back') return;
        if (!drawn) {   // first time: the line draws itself into mountain pose, then the flow begins
          drawn = true;
          path.animate([{ strokeDashoffset: 1 }, { strokeDashoffset: 0 }], { duration: 1300, easing: 'cubic-bezier(.45,.05,.25,1)', fill: 'forwards' }).onfinish = function () { path.style.strokeDasharray = 'none'; setTimeout(begin, 300); };
          return;
        }
        if (state === 'hold') {   // rise back to mountain, then flow again
          state = 'back'; segFrom = clone(cur); segT0 = performance.now(); caption('Vinyasa · flow');
          var back = function (now) { var t = (now - segT0) / 1100; cur = mix(segFrom, P.mountain, sine(Math.min(1, t))); render(cur, 0); if (t < 1) requestAnimationFrame(back); else setTimeout(begin, 250); };
          requestAnimationFrame(back); return;
        }
        begin();
      }
      return { play: play, tap: play };
    },

    // Reiki & sound: a tap sends sound rings out from the rim; warm light circles the bowl
    bowl: function (v) {
      var svg = v.querySelector('svg'), layer = v.querySelector('.b-rings'), back = v.querySelector('.b-light.back'), front = v.querySelector('.b-light.front'), visible = false, raf = 0, lastT = 0, t0 = performance.now();
      function strike(level) {
        var now = performance.now(); if (now - lastT < 1200) return; lastT = now;
        v.classList.add('struck'); setTimeout(function () { v.classList.remove('struck'); }, 700);
        [0, 380, 760, 1140].forEach(function (d, i) {
          var g = document.createElementNS(NS, 'g');
          g.innerHTML = '<ellipse class="b-ring wide" cx="120" cy="150" rx="70" ry="30"/><ellipse class="b-ring" cx="120" cy="150" rx="70" ry="30"/>';
          g.style.transformOrigin = '120px 150px'; layer.appendChild(g);
          g.animate([{ opacity: 0, transform: 'scale(.9)' }, { opacity: .9 - i * .15, offset: .12 }, { opacity: 0, transform: 'scale(2.3)' }], { duration: 3200, delay: d, easing: 'cubic-bezier(.2,.65,.25,1)', fill: 'backwards' }).onfinish = function () { g.remove(); };
        });
        chime(level);
      }
      function frame(now) {   // Reiki light: one slow orbit every 14 s, passing behind the bowl and in front of it
        raf = 0; var a = (now - t0) / 14000 * 6.283, x = 120 + Math.cos(a) * 92, y = 158 + Math.sin(a) * 34, behind = Math.sin(a) < 0;
        var c = behind ? back : front, o = behind ? front : back; c.setAttribute('cx', x.toFixed(1)); c.setAttribute('cy', y.toFixed(1)); c.style.opacity = (.55 + .35 * Math.abs(Math.sin(a))).toFixed(2); o.style.opacity = 0;
        if (visible) raf = requestAnimationFrame(frame);
      }
      if (reduce) {
        back.style.opacity = 0; front.setAttribute('cx', 196); front.setAttribute('cy', 168); front.style.opacity = .7;
        [1.35, 1.8].forEach(function (s, i) { var e = document.createElementNS(NS, 'ellipse'); e.setAttribute('class', 'b-ring'); e.setAttribute('cx', 120); e.setAttribute('cy', 150); e.setAttribute('rx', 70 * s); e.setAttribute('ry', 30 * s); e.style.opacity = .5 - i * .2; layer.appendChild(e); });
        return { play: function () {}, tap: function () { chime(); } };
      }
      back.style.opacity = front.style.opacity = 0;
      watch(v, function (vis) { visible = vis; if (vis && !raf) raf = requestAnimationFrame(frame); });
      return { play: function () { strike(.6); }, tap: function () { strike(1); } };
    },

    // astrology, herbs & tarot: the sprig grows leaf by leaf, the stars join up, then the card turns over
    astro: function (v) {
      var busy = false;
      if (reduce) { v.classList.add('on'); return { play: function () {}, tap: function () {} }; }
      function play() {
        if (busy) return; busy = true;
        if (v.classList.contains('on')) { v.classList.remove('on'); setTimeout(function () { v.classList.add('on'); }, 650); }
        else v.classList.add('on');
        setTimeout(function () { busy = false; }, 5200);
      }
      return { play: play, tap: play };
    }
  };

  document.querySelectorAll('.svc').forEach(function (card) {
    var v = card.querySelector('.vig'); if (!v) return;
    var api = makers[v.dataset.anim](v);
    once(card, function () { setTimeout(api.play, 450); }, .35);
    card.addEventListener('pointerenter', function (e) { if (e.pointerType === 'mouse') api.play(); });
    v.addEventListener('pointerdown', function (e) { if (e.target.closest('.snd')) return; api.tap(e); });
    // a tap anywhere else on the card (not on a link) plays it too, so touch has the same as hover
    card.addEventListener('click', function (e) { if (e.target.closest('a, button, .vig') || e.pointerType === 'mouse') return; api.play(); });
  });

  // ---------- 3. breathe: the circle as singing-bowl rings ----------
  (function () {
    var sec = document.getElementById('breathe'), svg = document.getElementById('breathRings'); if (!svg) return;
    var layer = svg.querySelector('.br-rings'), core = svg.querySelector('.br-core'), halo = svg.querySelector('.br-halo');
    var btn = document.getElementById('breatheBtn'), stat = document.getElementById('breathStatus'), rings = [], N = 7, visible = false, raf = 0;
    for (var i = 0; i < N; i++) { var c = document.createElementNS(NS, 'circle'); c.setAttribute('class', 'br-ring'); c.setAttribute('cx', 200); c.setAttribute('cy', 200); layer.appendChild(c); rings.push(c); }
    var fill = 0, phase = null;   // fill: 0 settled, 1 full. phase: { dir: 1 in / -1 out, t0, from }
    function draw(now, f) {
      var spread = 30 + 128 * f, coreR = 46 + 26 * f;
      core.setAttribute('r', coreR.toFixed(1)); halo.setAttribute('r', (coreR + 40 + 70 * f).toFixed(1));
      for (var i = 0; i < N; i++) {
        var u = reduce ? (i + .5) / N : ((now / 7000) + i / N) % 1;   // rings keep travelling outward, like a bowl's sustain
        rings[i].setAttribute('r', (coreR + 4 + u * spread).toFixed(1));
        rings[i].style.opacity = (Math.pow(1 - u, 1.4) * (.3 + .6 * f)).toFixed(3);
        rings[i].style.strokeWidth = (.8 + 1.4 * (1 - u)).toFixed(2);
      }
    }
    function frame(now) {
      raf = 0;
      if (phase) { var t = Math.min(1, (now - phase.t0) / 4000); fill = phase.from + ((phase.dir > 0 ? 1 : 0) - phase.from) * sine(t); }
      else fill += (.12 - fill) * .02;
      draw(now, fill);
      if (visible || phase) raf = requestAnimationFrame(frame);
    }
    if (reduce) draw(0, .6); else watch(sec, function (v) { visible = v; if (v && !raf) raf = requestAnimationFrame(frame); });
    var running = false;
    btn.addEventListener('click', function () {
      if (running) return; running = true; btn.disabled = true;
      var steps = [], n, k = 0;
      for (n = 1; n <= 3; n++) steps.push([1, 'Breathe in… (' + n + ' of 3)'], [-1, 'And out…']);
      (function next() {
        if (k >= steps.length) { phase = null; stat.textContent = 'Welcome back to earth.'; btn.disabled = false; btn.textContent = 'Again'; running = false; return; }
        phase = { dir: steps[k][0], t0: performance.now(), from: fill }; if (steps[k][0] > 0) chime(.5);
        if (reduce) draw(0, steps[k][0] > 0 ? 1 : .2); else if (!raf) raf = requestAnimationFrame(frame);
        stat.textContent = steps[k][1]; k++; setTimeout(next, 4000);
      })();
    });
  })();

  // ---------- oil shimmer: hover on desktop; on touch it plays once when the shelf comes into view, and on touch ----------
  document.querySelectorAll('.oil').forEach(function (o, i) {
    function shine() { o.classList.remove('shimmer'); void o.offsetWidth; o.classList.add('shimmer'); }
    if (coarse && !reduce) once(o, function () { setTimeout(shine, i * 900); }, .6);
    o.parentNode.addEventListener('touchstart', shine, { passive: true });
  });
})();
