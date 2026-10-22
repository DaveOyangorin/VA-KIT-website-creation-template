(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var header = document.querySelector('.site-header');

  // Everything is visible at rest. Only sections that start below the fold get a gentle rise.
  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.06 });
    document.querySelectorAll('.reveal').forEach(function (el) {
      if (el.getBoundingClientRect().top > vh) { el.classList.add('pre'); io.observe(el); }
    });
  }

  var par = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('.hero > img, .band > img'));
  var ticking = false;
  function onScroll() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 6);
    par.forEach(function (im) {
      var r = im.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > window.innerHeight) return;
      im.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - window.innerHeight / 2) * -0.07).toFixed(1) + 'px,0)';
    });
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  var drops = document.querySelectorAll('.nav details');
  drops.forEach(function (d) { d.addEventListener('toggle', function () { if (d.open) drops.forEach(function (o) { if (o !== d) o.open = false; }); }); });
  document.addEventListener('click', function (e) { drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; }); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; }
  });

  // Pick the right roof: tabs
  var ptabs = Array.prototype.slice.call(document.querySelectorAll('.pick-tabs [role=tab]'));
  function ppick(i, focus) {
    var k = ptabs[i].getAttribute('data-k');
    ptabs.forEach(function (t, j) { t.setAttribute('aria-selected', i === j); t.tabIndex = i === j ? 0 : -1; });
    document.querySelectorAll('.pick-panel').forEach(function (p) { p.hidden = p.getAttribute('data-k') !== k; });
    if (focus) ptabs[i].focus();
  }
  ptabs.forEach(function (t, i) {
    t.addEventListener('click', function () { ppick(i); });
    t.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { e.preventDefault(); ppick((i + 1) % ptabs.length, true); }
      if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { e.preventDefault(); ppick((i - 1 + ptabs.length) % ptabs.length, true); }
    });
  });

  // Slow parallax on photo heroes
  var pimgs = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('.hero-bg img, .ph-bg img'));
  window.addEventListener('scroll', function () {
    var h = window.innerHeight;
    pimgs.forEach(function (im) {
      var r = im.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > h) return;
      im.style.transform = 'translate3d(0,' + ((r.top / (h + r.height)) * -10).toFixed(2) + '%,0)';
    });
  }, { passive: true });
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
