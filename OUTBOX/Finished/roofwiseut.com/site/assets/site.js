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

  // Drone footage: pause for reduced motion; the viewfinder timecode follows the real playback position
  var vid = document.querySelector('.hero-video'), tc = document.querySelector('[data-tc]');
  if (vid) {
    if (reduce) { vid.removeAttribute('autoplay'); vid.pause(); }
    vid.addEventListener('timeupdate', function () {
      if (!tc) return;
      var t = vid.currentTime, f = Math.floor((t % 1) * 24);
      tc.textContent = '00:' + String(Math.floor(t / 60)).padStart(2, '0') + ':' + String(Math.floor(t % 60)).padStart(2, '0') + ':' + String(f).padStart(2, '0');
    });
  }

  var par = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('.ph-bg img, .cta-bg img'));
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

  // Marked-up drone frame: list items and pins light up together
  var pins = document.querySelectorAll('.pin'), pl = document.querySelectorAll('.plist li');
  function mark(k) {
    pins.forEach(function (p) { p.classList.toggle('on', p.getAttribute('data-k') === k); });
    pl.forEach(function (li) { li.classList.toggle('on', li.getAttribute('data-k') === k); });
  }
  pins.forEach(function (p) { ['mouseenter', 'focus', 'click'].forEach(function (ev) { p.addEventListener(ev, function () { mark(p.getAttribute('data-k')); }); }); });
  pl.forEach(function (li) { li.addEventListener('mouseenter', function () { mark(li.getAttribute('data-k')); }); });

  // Find your situation: tabs
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.sit-tabs [role=tab]'));
  function pick(i, focus) {
    tabs.forEach(function (t, j) {
      var on = i === j; t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
      document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
    });
    if (focus) tabs[i].focus();
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { pick(i); });
    t.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowDown' || e.key === 'ArrowRight') { e.preventDefault(); pick((i + 1) % tabs.length, true); }
      if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') { e.preventDefault(); pick((i - 1 + tabs.length) % tabs.length, true); }
    });
  });

  // Services: the drone frame beside the list follows the row you point at
  var rows = document.querySelectorAll('.svc-rows li'), shots = document.querySelectorAll('.svc-shot');
  rows.forEach(function (li) {
    function show() {
      rows.forEach(function (r) { r.classList.toggle('on', r === li); });
      shots.forEach(function (s) { s.classList.toggle('on', s.getAttribute('data-img') === li.getAttribute('data-img')); });
    }
    li.addEventListener('mouseenter', show); li.addEventListener('focusin', show);
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
