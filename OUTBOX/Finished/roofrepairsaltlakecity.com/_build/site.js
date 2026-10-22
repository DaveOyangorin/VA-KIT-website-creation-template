(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var header = document.querySelector('.site-header');
  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } }); }, { threshold: 0.06 });
    document.querySelectorAll('.reveal').forEach(function (el) { if (el.getBoundingClientRect().top > vh) { el.classList.add('pre'); io.observe(el); } });
  }
  window.addEventListener('scroll', function () { if (header) header.classList.toggle('scrolled', window.scrollY > 8); }, { passive: true });

  // Symptom finder: choose a symptom, see the diagnosis, and light up the matching spots on Fig. 1.
  var syms = document.querySelectorAll('.sym'), panes = document.querySelectorAll('.pane'), spots = document.querySelectorAll('.spot');
  function show(k) {
    syms.forEach(function (b) { var on = b.dataset.sym === k; b.classList.toggle('on', on); b.setAttribute('aria-pressed', on); });
    var lit = [];
    panes.forEach(function (p) { var on = p.dataset.pane === k; p.classList.toggle('on', on); if (on) lit = (p.dataset.spots || '').split(','); });
    spots.forEach(function (s) { s.classList.toggle('lit', lit.indexOf(s.dataset.spot) > -1); });
  }
  syms.forEach(function (b) { b.addEventListener('click', function () { show(b.dataset.sym); }); });
  if (syms.length) show(syms[0].dataset.sym);

  var drops = document.querySelectorAll('.nav details');
  document.addEventListener('click', function (e) { drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; } });
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
