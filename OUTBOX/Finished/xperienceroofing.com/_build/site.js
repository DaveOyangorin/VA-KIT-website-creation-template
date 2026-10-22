(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } }); }, { threshold: 0.06 });
    document.querySelectorAll('.reveal').forEach(function (el) { if (el.getBoundingClientRect().top > vh) { el.classList.add('pre'); io.observe(el); } });
  }
  // The Collection: tabs switch the system profile and spec card.
  document.querySelectorAll('.sel').forEach(function (sel) {
    var tabs = sel.querySelectorAll('.tab'), panes = sel.querySelectorAll('.pane');
    tabs.forEach(function (t) {
      t.addEventListener('click', function () {
        tabs.forEach(function (o) { var on = o === t; o.classList.toggle('on', on); o.setAttribute('aria-pressed', on); });
        panes.forEach(function (p) { p.classList.toggle('on', p.dataset.p === t.dataset.t); });
      });
    });
  });
  var drops = document.querySelectorAll('.nav details');
  document.addEventListener('click', function (e) { drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; } });
})();


/* v2: parallax on the landscape photos */
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var els = [].slice.call(document.querySelectorAll('[data-par]')); if (!els.length) return; var tick = false;
  var run = function () { els.forEach(function (el) { var p = el.closest('section') || el.parentElement, r = p.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return; el.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - innerHeight / 2) * -(+el.dataset.par)).toFixed(1) + 'px,0)'; }); tick = false; };
  addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run();
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
