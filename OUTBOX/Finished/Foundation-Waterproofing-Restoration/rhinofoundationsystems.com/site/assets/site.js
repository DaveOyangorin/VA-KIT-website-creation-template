/* kit2 premium layer: reveals, parallax, sticky story steps, counters, image swaps, dropdown closing. Reduced motion = static. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var html = document.documentElement; html.classList.remove('no-js'); html.classList.add('js');
  // reveals
  var rv = document.querySelectorAll('.reveal, .reveal-up');
  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0.08 });
    rv.forEach(function (el) { if (el.getBoundingClientRect().top > vh * 0.92) { if (el.classList.contains('reveal')) el.classList.add('pre'); io.observe(el); } else el.classList.add('in'); });
  } else rv.forEach(function (el) { el.classList.add('in'); });
  // parallax
  var px = [].slice.call(document.querySelectorAll('[data-parallax]'));
  if (px.length && !reduce) {
    var tick = false;
    var run = function () { tick = false; var h = window.innerHeight; px.forEach(function (el) { var r = el.parentElement.getBoundingClientRect(); if (r.bottom < 0 || r.top > h) return; var s = parseFloat(el.getAttribute('data-parallax')) || 0.15; el.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - h / 2) * -s).toFixed(1) + 'px,0)'; }); };
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run();
  }
  // sticky story: activate step in view, light up matching layer in the visual
  document.querySelectorAll('.story').forEach(function (st) {
    var steps = st.querySelectorAll('.step'), vis = st.querySelector('.story-visual');
    if (!('IntersectionObserver' in window)) return;
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        steps.forEach(function (s) { s.classList.toggle('on', s === e.target); });
        var key = e.target.getAttribute('data-step');
        if (vis) { vis.classList.add('has-active'); vis.querySelectorAll('[data-layer]').forEach(function (l) { l.classList.toggle('lit', l.getAttribute('data-layer') === key); }); var sw = vis.querySelectorAll('[data-show]'); sw.forEach(function (x) { x.classList.toggle('show', x.getAttribute('data-show') === key); }); }
        var out = st.querySelector('[data-readout]'); if (out && e.target.getAttribute('data-value')) out.textContent = e.target.getAttribute('data-value');
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    steps.forEach(function (s) { so.observe(s); });
  });
  // counters
  var cs = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (es) { es.forEach(function (e) { if (!e.isIntersecting) return; co.unobserve(e.target); var el = e.target, to = parseFloat(el.getAttribute('data-count')), suf = el.getAttribute('data-suffix') || '', t0 = null; if (reduce) { el.textContent = to + suf; return; } var step = function (t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 1400); el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))) + suf; if (p < 1) requestAnimationFrame(step); }; requestAnimationFrame(step); }); }, { threshold: 0.4 });
    cs.forEach(function (c) { co.observe(c); });
  }
  // image swap: hovering/focusing an item shows its photo
  document.querySelectorAll('[data-swap-group]').forEach(function (g) {
    var imgs = g.querySelectorAll('[data-swap-img]');
    g.querySelectorAll('[data-swap]').forEach(function (it) {
      var on = function () { var k = it.getAttribute('data-swap'); imgs.forEach(function (im) { im.classList.toggle('show', im.getAttribute('data-swap-img') === k); }); g.querySelectorAll('[data-swap]').forEach(function (o) { o.classList.toggle('on', o === it); }); };
      it.addEventListener('mouseenter', on); it.addEventListener('focus', on); it.addEventListener('click', on);
    });
  });
  // nav dropdowns
  var drops = document.querySelectorAll('.nav details');
  document.addEventListener('click', function (e) { drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; } });
})();

/* concept: "Drive the pier". The depth gauge drives a helical pier down through the drawn soil layers; each layer shows Rhino's own
   description of that soil; past the frost line the pier bears, the house rotates back to level and the wall crack closes. */
(function () {
  var P = document.querySelector('[data-pierdemo]'); if (!P) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var r = P.querySelector('.pr-range'), house = P.querySelector('[data-house]'), pier = P.querySelector('[data-pier]'), tip = P.querySelector('[data-tip]'), shaft = P.querySelector('[data-shaft]');
  var status = P.querySelector('[data-status]'), meter = P.querySelector('[data-meter]'), tx = P.querySelectorAll('.pr-tx');
  var bounds = [232, 302, 382, 450, 9999], names = ['Loam', 'Silt', 'Clay', 'Sand', 'Below the frost line'];
  var TOP = 236, BOT = 548, FROST = 462, TILT = 2.4, cur = -1, bearing = null, touched = false, anim = null;
  var draw = function (v) {
    var y = TOP + (BOT - TOP) * v / 100, i = 0; while (y > bounds[i]) i++;
    var bear = y >= FROST, ang = bear ? 0 : TILT, drop = (517 - 210) * Math.tan(ang * Math.PI / 180);
    house.style.transform = 'rotate(' + ang + 'deg)';
    pier.setAttribute('transform', 'translate(0 ' + drop.toFixed(1) + ')');
    tip.setAttribute('transform', 'translate(0 ' + (y - drop).toFixed(1) + ')'); shaft.setAttribute('y2', (y - drop - 4).toFixed(1));
    if (i !== cur) { cur = i; P.dataset.layer = i; tx.forEach(function (t) { t.classList.toggle('on', +t.dataset.i === i); }); r.setAttribute('aria-valuetext', names[i]); }
    if (bear !== bearing) { bearing = bear; P.dataset.bearing = bear ? '1' : '0'; status.textContent = bear ? 'BEARING: LEVEL' : 'SETTLING'; meter.textContent = bear ? 'Bearing, level' : 'Settling'; }
  };
  var stop = function () { if (anim) cancelAnimationFrame(anim); anim = null; };
  var tween = function (to, dur) { stop(); var from = +r.value, t0 = performance.now();
    var step = function (t) { var k = Math.min(1, (t - t0) / dur); k = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; r.value = from + (to - from) * k; draw(+r.value); if (k < 1) anim = requestAnimationFrame(step); };
    anim = requestAnimationFrame(step); };
  r.addEventListener('input', function () { touched = true; stop(); draw(+r.value); });
  draw(0);
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); setTimeout(function () { if (!touched) tween(100, 6500); }, 600); } }, { threshold: .45 });
    io.observe(P);
  }
})();

/* MFIX-2026-10-19: mobile header fix */
(function () {
  var h = document.querySelector('.site-header'); if (!h) return;
  var root = document.documentElement;
  function y() { return Math.max(window.pageYOffset || 0, root.scrollTop || 0, document.body ? document.body.scrollTop || 0 : 0); }
  function upd() {
    var b = Math.max(0, Math.round(h.getBoundingClientRect().bottom));
    root.style.setProperty('--hdr-bottom', b + 'px');
    h.classList.toggle('scrolled', y() > 6);
  }
  window.addEventListener('scroll', upd, { passive: true });
  window.addEventListener('resize', upd, { passive: true });
  document.addEventListener('scroll', upd, { passive: true, capture: true });
  document.querySelectorAll('.menu').forEach(function (m) {
    m.addEventListener('toggle', function () { upd(); root.classList.toggle('menu-open', m.open); });
    m.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { m.open = false; }); });
  });
  upd(); setTimeout(upd, 300);
})();
