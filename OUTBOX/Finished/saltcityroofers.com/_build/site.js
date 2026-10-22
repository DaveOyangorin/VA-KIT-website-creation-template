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
  // before/after slider
  document.querySelectorAll('[data-compare] .cmp').forEach(function (c) {
    var r = c.querySelector('input');
    function set() { c.style.setProperty('--pos', r.value + '%'); }
    r.addEventListener('input', set); set();
  });
})();


/* v2: pinned four-chapter story and panorama parallax */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var S = document.querySelector('[data-story]');
  if (S) {
    var fr = S.querySelectorAll('.st-f'), st = S.querySelectorAll('.st-step'), bar = S.querySelector('[data-bar]'), n = S.querySelector('[data-n]'), R = ['I', 'II', 'III', 'IV'], cur = -1;
    var set = function (i) { if (i === cur) return; cur = i; fr.forEach(function (f) { f.classList.toggle('on', +f.dataset.f === i); }); st.forEach(function (s) { s.classList.toggle('on', +s.dataset.s === i); }); bar.style.width = ((i + 1) * 25) + '%'; n.textContent = R[i]; };
    var pick = function () { var vb = S.querySelector('.st-vis').getBoundingClientRect(), mid = innerWidth <= 1000 ? (Math.max(vb.bottom, 0) + innerHeight) / 2 : innerHeight / 2, best = 0, bd = 1e9; st.forEach(function (s, i) { var r = s.getBoundingClientRect(), d = Math.abs(r.top + r.height / 2 - mid); if (d < bd) { bd = d; best = i; } }); set(best); };
    addEventListener('scroll', pick, { passive: true }); addEventListener('resize', pick); pick();
  }
  if (!reduce) {
    var els = [].slice.call(document.querySelectorAll('[data-par]')), tick = false;
    var run = function () { els.forEach(function (el) { var r = el.parentElement.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return; el.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - innerHeight / 2) * -(+el.dataset.par)).toFixed(1) + 'px,0)'; }); tick = false; };
    if (els.length) { addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run(); }
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
