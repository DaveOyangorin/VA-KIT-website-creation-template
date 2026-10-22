/* concept: Rent math. Owner / renter modes; every figure comes from Equity's published fees and criteria. */
(function () {
  var c = document.querySelector('[data-calc]'); if (!c) return;
  var rent = c.querySelector('[data-rent]'), sl = c.querySelector('[data-slider]'), modes = c.querySelectorAll('[data-mode]'), groups = c.querySelectorAll('[data-rows]');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (n) { return '$' + Math.round(n).toLocaleString('en-US'); };
  var set = function (k, v) { var el = c.querySelector('[data-f="' + k + '"]'); if (!el || el.textContent === v) return; el.textContent = v; if (!reduce) { el.classList.remove('pulse'); void el.offsetWidth; el.classList.add('pulse'); } };
  var calc = function () {
    var r = Math.max(0, +rent.value || 0);
    set('place', $(r * .5) + '–' + $(r));
    set('mgmt', $(r * .08) + '–' + $(r * .10) + '/mo');
    set('dep', $(r)); set('dep2', $(r));
    set('inc', $(r * 3) + '/mo'); set('sav', $(r * 12));
  };
  rent.addEventListener('input', function () { sl.value = Math.min(6000, Math.max(500, +rent.value || 500)); calc(); });
  sl.addEventListener('input', function () { rent.value = sl.value; calc(); });
  modes.forEach(function (m) { m.addEventListener('click', function () {
    modes.forEach(function (x) { var on = x === m; x.classList.toggle('on', on); x.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    groups.forEach(function (g) { g.hidden = g.getAttribute('data-rows') !== m.getAttribute('data-mode'); });
  }); });
  calc();
})();
