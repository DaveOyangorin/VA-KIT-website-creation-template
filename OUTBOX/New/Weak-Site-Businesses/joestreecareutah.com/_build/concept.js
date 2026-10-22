/* concept: drag-to-compare before/after of their own jobs (a range input drives the clip, so keyboard works); a gentle first sweep on view. */
(function () {
  var figs = document.querySelectorAll('[data-ba]'); if (!figs.length) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  figs.forEach(function (f) {
    var fr = f.querySelector('.ba-frame'), r = f.querySelector('[data-ba-range]');
    r.addEventListener('input', function () { fr.style.setProperty('--pos', r.value + '%'); });
  });
  if (reduce || !('IntersectionObserver' in window)) return;
  var first = figs[0], fr = first.querySelector('.ba-frame'), rg = first.querySelector('[data-ba-range]');
  var io = new IntersectionObserver(function (es) {
    if (!es[0].isIntersecting) return; io.disconnect();
    var t0 = null, path = [50, 15, 85, 50];
    (function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 2200), seg = Math.min(2, Math.floor(p * 3)), lp = p * 3 - seg, e = lp < .5 ? 2 * lp * lp : 1 - Math.pow(-2 * lp + 2, 2) / 2;
      var v = path[seg] + (path[seg + 1] - path[seg]) * e; fr.style.setProperty('--pos', v + '%'); rg.value = v; if (p < 1) requestAnimationFrame(step); })(performance.now());
  }, { threshold: .5 });
  io.observe(first);
})();
