(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var header = document.querySelector('.site-header');

  // Everything is visible at rest. Only sections that start below the fold get a gentle rise.
  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); e.target.classList.remove('pre-x'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(function (el) {
      if (el.getBoundingClientRect().top > vh) { el.classList.add('pre'); io.observe(el); }
    });
    // The roof assembly starts collapsed and opens out when it scrolls into view
    document.querySelectorAll('.asm').forEach(function (el) {
      if (el.getBoundingClientRect().top > vh * 0.6) { el.classList.add('pre-x'); io.observe(el); }
    });
  }

  // Hero slides, with captions that double as controls
  var slides = document.querySelectorAll('.slide'), caps = document.querySelectorAll('.slide-caps li'), cur = 0, timer;
  function show(i) {
    cur = (i + slides.length) % slides.length;
    slides.forEach(function (s, j) { s.classList.toggle('on', j === cur); });
    caps.forEach(function (c, j) { c.classList.remove('on'); if (j === cur) { void c.offsetWidth; c.classList.add('on'); } });
  }
  function auto() { clearInterval(timer); if (!reduce && slides.length > 1) timer = setInterval(function () { show(cur + 1); }, 6000); }
  caps.forEach(function (c, j) { c.addEventListener('click', function () { show(j); auto(); }); });
  auto();

  // Parallax on page heroes and the closing band
  var par = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('.ph-bg img, .cta-bg img'));
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  var heads = tocLinks.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); });
  var ticking = false;
  function onScroll() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 60);
    var h = window.innerHeight;
    par.forEach(function (im) {
      var r = im.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > h) return;
      im.style.transform = 'translate3d(0,' + ((r.top / (h + r.height)) * -12).toFixed(2) + '%,0)';
    });
    if (heads.length) {
      var c = 0;
      heads.forEach(function (el, i) { if (el && el.getBoundingClientRect().top < 160) c = i; });
      tocLinks.forEach(function (a, i) { a.classList.toggle('on', i === c); });
    }
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  // Roof assembly: membrane tabs
  document.querySelectorAll('.asm').forEach(function (asm) {
    var tabs = Array.prototype.slice.call(asm.querySelectorAll('.mem-tabs button'));
    function pick(i, focus) {
      var m = tabs[i].getAttribute('data-m');
      asm.setAttribute('data-m', m);
      tabs.forEach(function (t, j) { t.setAttribute('aria-selected', i === j); t.tabIndex = i === j ? 0 : -1; });
      asm.querySelectorAll('.mem-panel').forEach(function (p) { p.hidden = p.getAttribute('data-m') !== m; });
      if (focus) tabs[i].focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { pick(i); });
      t.addEventListener('keydown', function (e) {
        if (e.key === 'ArrowRight') { e.preventDefault(); pick((i + 1) % tabs.length, true); }
        if (e.key === 'ArrowLeft') { e.preventDefault(); pick((i - 1 + tabs.length) % tabs.length, true); }
      });
    });
  });

  // Project index: the preview follows the row you point at
  document.querySelectorAll('.pindex').forEach(function (pi) {
    var rows = pi.querySelectorAll('.pi-list li'), shots = pi.querySelectorAll('.pi-shot');
    rows.forEach(function (li) {
      function on() {
        rows.forEach(function (r) { r.classList.toggle('on', r === li); });
        shots.forEach(function (s) { s.classList.toggle('on', s.getAttribute('data-img') === li.getAttribute('data-img')); });
      }
      li.addEventListener('mouseenter', on); li.addEventListener('focusin', on);
    });
    if (rows[0]) rows[0].classList.add('on');
  });

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
