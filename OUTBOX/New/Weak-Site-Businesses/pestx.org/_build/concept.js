/* concept: specimen plates (prev/next, dots, swipe; slow auto-advance unless reduced motion), the house diagram zones, season chart. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pl = document.querySelector('[data-plate]');
  if (pl) {
    var fs = pl.querySelectorAll('.pl-f'), dots = pl.querySelectorAll('[data-pl-dot]'), cnt = pl.querySelector('[data-pl-count]'), cur = 0, timer = null;
    var show = function (i) { cur = (i + fs.length) % fs.length; fs.forEach(function (f, k) { f.classList.toggle('on', k === cur); }); dots.forEach(function (d, k) { d.classList.toggle('on', k === cur); }); if (cnt) cnt.textContent = ('0' + (cur + 1)).slice(-2) + ' / ' + fs.length; };
    var stop = function () { if (timer) { clearInterval(timer); timer = null; } };
    pl.querySelector('[data-pl-prev]').addEventListener('click', function () { stop(); show(cur - 1); });
    pl.querySelector('[data-pl-next]').addEventListener('click', function () { stop(); show(cur + 1); });
    dots.forEach(function (d) { d.addEventListener('click', function () { stop(); show(+d.getAttribute('data-pl-dot')); }); });
    var x0 = null; pl.addEventListener('touchstart', function (e) { x0 = e.touches[0].clientX; }, { passive: true });
    pl.addEventListener('touchend', function (e) { if (x0 === null) return; var dx = e.changedTouches[0].clientX - x0; if (Math.abs(dx) > 40) { stop(); show(cur + (dx < 0 ? 1 : -1)); } x0 = null; });
    if (!reduce) { timer = setInterval(function () { show(cur + 1); }, 4800); pl.addEventListener('mouseenter', stop); pl.addEventListener('focusin', stop); }
  }
  var hs = document.querySelector('[data-house]');
  if (hs) {
    var zs = hs.querySelectorAll('.hz'), ps = hs.querySelectorAll('.zp'), cs = hs.querySelectorAll('[data-zc]');
    var pick = function (i) { zs.forEach(function (z, k) { z.classList.toggle('on', k === i); }); ps.forEach(function (p, k) { p.classList.toggle('on', k === i); }); cs.forEach(function (c, k) { c.classList.toggle('on', k === i); c.setAttribute('aria-selected', k === i ? 'true' : 'false'); }); };
    zs.forEach(function (z, i) { z.addEventListener('click', function () { pick(i); }); z.addEventListener('mouseenter', function () { if (window.matchMedia('(hover: hover)').matches) pick(i); }); z.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(i); } }); });
    cs.forEach(function (c, i) { c.addEventListener('click', function () { pick(i); }); });
  }
  var sz = document.querySelector('[data-seasons]');
  if (sz) {
    var now = sz.querySelector('.sz-now'), m = new Date().getMonth(), tr = sz.querySelector('.sz-months');
    if (now && tr) { now.style.display = 'block'; now.style.left = 'calc(' + ((m + 0.5) / 12 * 100) + '% - 1px)'; var lab = tr.querySelector('[data-m="' + m + '"]'); if (lab) { lab.style.color = '#d6334f'; lab.style.fontWeight = '700'; } }
    if ('IntersectionObserver' in window && !reduce) { var o = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { sz.classList.add('in'); o.disconnect(); } }); }, { threshold: 0.3 }); o.observe(sz); } else sz.classList.add('in');
  }
})();
