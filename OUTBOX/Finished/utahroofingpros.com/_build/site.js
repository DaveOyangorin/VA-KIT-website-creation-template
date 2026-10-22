(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var header = document.querySelector('.site-header');
  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } }); }, { threshold: 0.06 });
    document.querySelectorAll('.reveal').forEach(function (el) { if (el.getBoundingClientRect().top > vh) { el.classList.add('pre'); io.observe(el); } });
  }
  window.addEventListener('scroll', function () { if (header) header.classList.toggle('scrolled', window.scrollY > 8); }, { passive: true });
  var drops = document.querySelectorAll('.nav details');
  document.addEventListener('click', function (e) { drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; } });
  // service-area map: region filter
  document.querySelectorAll('[data-map]').forEach(function (wrap) {
    var btns = wrap.querySelectorAll('.tabs button');
    function pick(r) {
      btns.forEach(function (b) { b.classList.toggle('on', b.dataset.r === r); b.setAttribute('aria-pressed', b.dataset.r === r ? 'true' : 'false'); });
      wrap.classList.toggle('filter', r !== 'all');
      wrap.querySelectorAll('.map [data-r], .reg').forEach(function (el) { el.classList.toggle('show', el.dataset.r === r); });
    }
    btns.forEach(function (b) { b.addEventListener('click', function () { pick(b.dataset.r); }); });
    var h = location.hash.slice(1);
    wrap.querySelectorAll('.reg').forEach(function (g) { if (g.id === h) pick(g.dataset.r); });
  });
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
