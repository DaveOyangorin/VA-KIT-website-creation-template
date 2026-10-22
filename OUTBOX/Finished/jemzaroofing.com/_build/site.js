(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var header = document.querySelector('.site-header');

  // Everything is visible at rest. Only sections that start below the fold get a gentle rise.
  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(function (el) {
      if (el.getBoundingClientRect().top > vh) { el.classList.add('pre'); io.observe(el); }
    });
  }

  var par = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('.ph-bg img, .cta-bg img'));
  var strip = document.querySelector('.strip-sec'), track = strip && strip.querySelector('.strip-track'), bar = strip && strip.querySelector('.strip-bar i');
  var wide = window.matchMedia('(min-width: 961px)');
  var ticking = false;
  function onScroll() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 60);
    var h = window.innerHeight;
    par.forEach(function (im) {
      var r = im.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > h) return;
      im.style.transform = 'translate3d(0,' + ((r.top / (h + r.height)) * -12).toFixed(2) + '%,0)';
    });
    // Film strip: the tall section's scroll progress moves the track sideways
    if (strip && track && wide.matches && !reduce) {
      var r = strip.getBoundingClientRect(), total = strip.offsetHeight - h;
      var p = Math.min(1, Math.max(0, -r.top / total));
      var dist = track.scrollWidth - window.innerWidth + 56;
      track.style.transform = 'translate3d(' + (-p * Math.max(0, dist)).toFixed(1) + 'px,0,0)';
      if (bar) bar.style.setProperty('--p', (p * 100).toFixed(1) + '%');
    }
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  window.addEventListener('resize', onScroll);
  onScroll();

  // Services index: the row's photo follows the pointer
  var wrap = document.querySelector('.index-wrap');
  if (wrap && !reduce) {
    var fls = wrap.querySelectorAll('.fl'), cur = null;
    wrap.querySelectorAll('.idx').forEach(function (row) {
      row.addEventListener('mouseenter', function () {
        cur = row.getAttribute('data-img');
        fls.forEach(function (f) { f.classList.toggle('on', f.getAttribute('data-img') === cur); });
      });
    });
    wrap.addEventListener('mousemove', function (e) {
      var r = wrap.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top;
      fls.forEach(function (f) { f.style.left = (x + 170) + 'px'; f.style.top = y + 'px'; });
    });
    wrap.addEventListener('mouseleave', function () { fls.forEach(function (f) { f.classList.remove('on'); }); });
  }

  var drops = document.querySelectorAll('.nav details');
  drops.forEach(function (d) { d.addEventListener('toggle', function () { if (d.open) drops.forEach(function (o) { if (o !== d) o.open = false; }); }); });
  document.addEventListener('click', function (e) { drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; }); });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; }
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
