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

  // Slow parallax on the full-bleed photos
  var par = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('.hero-bg img, .ph-bg img, .cta-bg img, .winter-bg img'));
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  var heads = tocLinks.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
  var ticking = false;
  function onScroll() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 40);
    var h = window.innerHeight;
    par.forEach(function (im) {
      var r = im.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > h) return;
      im.style.transform = 'translate3d(0,' + ((r.top / (h + r.height)) * -12).toFixed(2) + '%,0)';
    });
    if (heads.length) {
      var cur = 0;
      heads.forEach(function (el, i) { if (el && el.getBoundingClientRect().top < 160) cur = i; });
      tocLinks.forEach(function (a, i) { a.classList.toggle('on', i === cur); });
    }
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  // The path of the water: the list and the drawing's numbered points light up together
  var items = document.querySelectorAll('.wlist li[data-k]');
  function mark(k) {
    document.querySelectorAll('.section-drawing .hs').forEach(function (g) { g.classList.toggle('on', g.getAttribute('data-k') === k); });
    items.forEach(function (li) { li.classList.toggle('on', li.getAttribute('data-k') === k); });
  }
  items.forEach(function (li) {
    var k = li.getAttribute('data-k');
    li.addEventListener('mouseenter', function () { mark(k); });
    li.addEventListener('focusin', function () { mark(k); });
  });
  document.querySelectorAll('.section-drawing .hs').forEach(function (g) {
    g.addEventListener('mouseenter', function () { mark(g.getAttribute('data-k')); });
  });

  // Gallery lightbox
  var lb = document.querySelector('.lightbox');
  if (lb && lb.showModal) {
    var big = lb.appendChild(document.createElement('img'));
    document.querySelectorAll('.zoom').forEach(function (b) {
      b.addEventListener('click', function () { var i = b.querySelector('img'); big.src = i.currentSrc || i.src; big.alt = i.alt; lb.showModal(); });
    });
    lb.querySelector('.lb-close').addEventListener('click', function () { lb.close(); });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
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
