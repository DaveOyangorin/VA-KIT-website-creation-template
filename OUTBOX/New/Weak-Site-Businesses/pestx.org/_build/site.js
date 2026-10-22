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

/* concept: specimen plates (prev/next, dots, swipe; slow auto-advance unless reduced motion), the house diagram zones, season chart. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pl = document.querySelector('[data-plate]');
  if (pl) {
    var fs = pl.querySelectorAll('.pl-f'), dots = pl.querySelectorAll('[data-pl-dot]'), cnt = pl.querySelector('[data-pl-count]'), cur = 0, timer = null;
    var show = function (i) { cur = (i + fs.length) % fs.length; fs.forEach(function (f, k) { f.classList.toggle('on', k === cur); }); dots.forEach(function (d, k) { d.classList.toggle('on', k === cur); }); if (cnt) cnt.textContent = ('0' + (cur + 1)).slice(-2) + ' / ' + fs.length; };
    var stop = function () { if (timer) { clearInterval(timer); timer = null; } };
    pl.querySelector('[data-pl-prev]').addEventListener('click', function () { stop(); show(cur - 1); });
    pl.querySelector('[data-pl-next]').addEventListener('click', function () { stop(); show(cur + 1); });
    dots.forEach(function (d) { d.addEventListener('click', function () { stop(); show(+d.getAttribute('data-pl-dot')); }); });
    var x0 = null; pl.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    pl.addEventListener('touchend', function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) { stop(); show(cur + (dx < 0 ? 1 : -1)); } x0 = null; });
    if (!reduce) { timer = setInterval(function () { show(cur + 1); }, 4800); pl.addEventListener('mouseenter', stop); pl.addEventListener('focusin', stop); }
  }
  var hs = document.querySelector('[data-house]');
  if (hs) {
    var zs = hs.querySelectorAll('.hz'), ps = hs.querySelectorAll('.zp'), cs = hs.querySelectorAll('[data-zc]');
    var pick = function (i) { zs.forEach(function (z, k) { z.classList.toggle('on', k === i); }); ps.forEach(function (p, k) { p.classList.toggle('on', k === i); }); cs.forEach(function (c, k) { c.classList.toggle('on', k === i); c.setAttribute('aria-selected', k === i ? 'true' : 'false'); }); };
    zs.forEach(function (z, i) { z.addEventListener('click', function () { pick(i); }); z.addEventListener('mouseenter', function () { if (window.matchMedia('(hover: hover)').matches) pick(i); }); z.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(i); } }); });
    cs.forEach(function (c, i) { c.addEventListener('click', function () { pick(i); }); });
  }
  var sz = document.querySelector('[data-seasons]');
  if (sz) {
    var now = sz.querySelector('.sz-now'), m = new Date().getMonth(), tr = sz.querySelector('.sz-months');
    if (now && tr) { now.style.display = 'block'; now.style.left = 'calc(' + ((m + 0.5) / 12 * 100) + '% - 1px)'; var lab = tr.querySelector('[data-m="' + m + '"]'); if (lab) { lab.style.color = '#d6334f'; lab.style.fontWeight = '700'; } }
    if ('IntersectionObserver' in window && !reduce) { var o = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { sz.classList.add('in'); o.disconnect(); } }); }, { threshold: 0.3 }); o.observe(sz); } else sz.classList.add('in');
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
