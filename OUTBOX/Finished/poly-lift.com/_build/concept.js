/* poly-lift.com: the interactive lift, project filter */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-lift]').forEach(function (w) {
    var r = w.querySelector('input[type=range]'), b = w.querySelector('[data-inject]'), out = w.querySelector('.lift-read');
    var set = function (v) {
      r.value = v; w.style.setProperty('--t', (v / 100).toFixed(3));
      out.textContent = v >= 98 ? 'Level' : v > 0 ? 'Lifting…' : 'Out of level';
      b.textContent = v >= 98 ? 'Reset' : 'Inject foam';
    };
    r.addEventListener('input', function () { set(+r.value); });
    b.addEventListener('click', function () {
      if (+r.value >= 98) { set(0); return; }
      if (reduce) { set(100); return; }
      var s = +r.value, t0 = null;
      var step = function (t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 2200); var e = 1 - Math.pow(1 - p, 3); set(Math.round(s + (100 - s) * e)); if (p < 1) requestAnimationFrame(step); };
      requestAnimationFrame(step);
    });
    set(0);
  });
  var chips = document.querySelectorAll('.g-chips button'), figs = document.querySelectorAll('[data-gallery] .m-f');
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      chips.forEach(function (x) { x.classList.toggle('on', x === c); });
      figs.forEach(function (f) { f.hidden = !(c.dataset.filter === 'all' || f.dataset.cat === c.dataset.filter); });
    });
  });
})();
