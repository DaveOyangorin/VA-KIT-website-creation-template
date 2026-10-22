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

/* cleartopsolutions.shop: blueprint hotspots, 48-hour dial, floating cards */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // hotspots: pick the room where the water is
  document.querySelectorAll('[data-hmap]').forEach(function (map) {
    var wrap = map.parentNode, spots = map.querySelectorAll('.hs'), panels = wrap.querySelectorAll('.hp'), zones = map.querySelectorAll('.zone');
    var pick = function (z) {
      spots.forEach(function (s) { s.classList.toggle('on', s.dataset.z === z); s.setAttribute('aria-pressed', s.dataset.z === z ? 'true' : 'false'); });
      panels.forEach(function (p) { p.hidden = p.dataset.z !== z; });
      zones.forEach(function (g) { g.classList.toggle('on', g.dataset.z === z); g.classList.toggle('dim', g.dataset.z !== z); });
    };
    spots.forEach(function (s) {
      s.addEventListener('click', function () { pick(s.dataset.z); });
      s.addEventListener('mouseenter', function () { pick(s.dataset.z); });
    });
    pick(spots[0] && spots[0].dataset.z);
  });
  // 48-hour dial: fills as the section scrolls past, lights the matching step
  var sec = document.querySelector('[data-dial]');
  if (sec) {
    var dial = sec.querySelector('.clock48'), big = sec.querySelector('[data-hours]'), steps = sec.querySelectorAll('.d-step');
    var run = function () {
      var r = sec.getBoundingClientRect(), vh = window.innerHeight;
      var p = reduce ? 1 : Math.min(1, Math.max(0, (vh * 0.75 - r.top) / (r.height * 0.8)));
      dial.style.setProperty('--p', p.toFixed(3));
      big.textContent = Math.round(p * 48) + 'h';
      var k = Math.min(steps.length - 1, Math.floor(p * steps.length * 0.999));
      steps.forEach(function (s, i) { s.classList.toggle('on', i <= k); });
    };
    var tick = false;
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(function () { tick = false; run(); }); } }, { passive: true });
    window.addEventListener('resize', run); run();
  }
  // floating cards drift slightly with scroll
  var fl = document.querySelectorAll('[data-float]');
  if (fl.length && !reduce) {
    var f = function () { fl.forEach(function (c) { var r = c.getBoundingClientRect(); var d = Math.max(-36, Math.min(36, (r.top + r.height / 2 - window.innerHeight / 2) * parseFloat(c.dataset.float))); c.style.transform = 'translate3d(0,' + d.toFixed(1) + 'px,0)'; }); };
    window.addEventListener('scroll', function () { requestAnimationFrame(f); }, { passive: true }); f();
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
