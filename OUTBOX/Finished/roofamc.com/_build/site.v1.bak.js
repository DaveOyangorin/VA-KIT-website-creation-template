(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var header = document.querySelector('.site-header');

  // reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // header shadow + light parallax on big photos
  var par = reduce ? [] : Array.prototype.slice.call(document.querySelectorAll('.hero-media img, .bleed > img'));
  var ticking = false;
  function onScroll() {
    if (header) header.classList.toggle('scrolled', window.scrollY > 8);
    par.forEach(function (im) {
      var r = im.parentElement.getBoundingClientRect();
      if (r.bottom < 0 || r.top > window.innerHeight) return;
      var shift = (r.top + r.height / 2 - window.innerHeight / 2) * -0.08;
      im.style.transform = 'translate3d(0,' + shift.toFixed(1) + 'px,0)';
    });
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  // only one desktop dropdown open at a time; close on outside click
  var drops = document.querySelectorAll('.nav details');
  drops.forEach(function (d) {
    d.addEventListener('toggle', function () { if (d.open) drops.forEach(function (o) { if (o !== d) o.open = false; }); });
  });
  document.addEventListener('click', function (e) {
    drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; });
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; }
  });
})();
