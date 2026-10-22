/* concept: before/after sliders (range input drives the clip; keyboard works), project tabs, a gentle first sweep on view. */
(function () {
  var w = document.querySelector('[data-ba-wrap]'); if (!w) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var figs = w.querySelectorAll('.ba'), tabs = w.querySelectorAll('[data-ba-tab]');
  figs.forEach(function (f) {
    var fr = f.querySelector('[data-ba-frame]'), r = f.querySelector('[data-ba-range]');
    r.addEventListener('input', function () { fr.style.setProperty('--pos', r.value + '%'); });
  });
  tabs.forEach(function (t) { t.addEventListener('click', function () {
    var i = t.getAttribute('data-ba-tab');
    tabs.forEach(function (x) { x.classList.toggle('on', x === t); }); figs.forEach(function (f) { f.classList.toggle('on', f.getAttribute('data-ba') === i); });
  }); });
  if (reduce || !('IntersectionObserver' in window)) return;
  var first = figs[0], fr = first.querySelector('[data-ba-frame]'), r = first.querySelector('[data-ba-range]');
  var io = new IntersectionObserver(function (es) {
    if (!es[0].isIntersecting) return; io.disconnect();
    var t0 = null, from = 50, path = [50, 18, 82, 50];
    var step = function (t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 2200), seg = Math.min(2, Math.floor(p * 3)), lp = p * 3 - seg, e = lp < .5 ? 2 * lp * lp : 1 - Math.pow(-2 * lp + 2, 2) / 2;
      var v = path[seg] + (path[seg + 1] - path[seg]) * e; fr.style.setProperty('--pos', v + '%'); r.value = v; if (p < 1) requestAnimationFrame(step); };
    requestAnimationFrame(step);
  }, { threshold: .5 });
  io.observe(first);
})();
