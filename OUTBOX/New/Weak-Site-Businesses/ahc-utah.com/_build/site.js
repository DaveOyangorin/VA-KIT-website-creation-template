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

/* concept: the thermostat card. HEAT/COOL switches the banner photo (winter / summer park), the headline, the credit line and the service
   tab; +/- moves the set point and the dial arc. It starts in the current season (October to April: heat). Nothing is sent anywhere. */
(function () {
  var hero = document.querySelector('[data-season]'), ts = document.querySelector('[data-tstat]'); if (!hero || !ts) return;
  var M = { heat: { set: 70, lab: 'Heating to', em: 'for the coldest mornings.', note: 'Furnace installs, repairs and tune-ups, all makes and models.', credit: 'Sugar House Park in snow · claralieu, CC BY 2.0', tab: 'heating' },
            cool: { set: 74, lab: 'Cooling to', em: 'for the hottest afternoons.', note: 'Air conditioning installs, repairs and tune-ups, central air to ductless.', credit: 'Liberty Park, Salt Lake City · Pollardjosephd, CC BY-SA 4.0', tab: 'cooling' } };
  var mode = 'heat', setEl = ts.querySelector('[data-set]'), arc = ts.querySelector('[data-arc]');
  function draw() { var v = M[mode].set; setEl.textContent = v; arc.style.strokeDasharray = (6 + (v - 60) / 20 * 69).toFixed(1) + ' 100'; }
  function tab(k) {
    document.querySelectorAll('[data-tab]').forEach(function (b) { var on = b.getAttribute('data-tab') === k; b.classList.toggle('on', on); b.setAttribute('aria-pressed', on); });
    document.querySelectorAll('[data-panel]').forEach(function (p) { p.classList.toggle('on', p.getAttribute('data-panel') === k); });
  }
  function setMode(m, init) {
    mode = m; hero.classList.toggle('mode-cool', m === 'cool'); hero.classList.toggle('mode-heat', m === 'heat');
    ts.querySelectorAll('[data-mode]').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-mode') === m); });
    ts.querySelector('[data-lab]').textContent = M[m].lab; ts.querySelector('[data-note]').textContent = M[m].note;
    var em = hero.querySelector('[data-h1em]'); if (em) em.textContent = M[m].em;
    var cr = hero.querySelector('[data-credit]'); if (cr) cr.textContent = M[m].credit;
    draw(); if (!init) tab(M[m].tab);
  }
  ts.querySelectorAll('[data-mode]').forEach(function (b) { b.addEventListener('click', function () { setMode(b.getAttribute('data-mode')); }); });
  ts.querySelectorAll('[data-step]').forEach(function (b) { b.addEventListener('click', function () { M[mode].set = Math.max(60, Math.min(80, M[mode].set + +b.getAttribute('data-step'))); draw(); }); });
  document.querySelectorAll('[data-tab]').forEach(function (b) { b.addEventListener('click', function () { tab(b.getAttribute('data-tab')); }); });
  var mo = new Date().getMonth(); setMode(mo >= 4 && mo <= 8 ? 'cool' : 'heat', true); tab(M[mode].tab);
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
