/* concept: "After the damage". Each step opens its card; arrow keys step along the track. Nothing is sent anywhere. */
(function () {
  var r = document.querySelector('[data-lanes]'); if (!r) return;
  var btns = Array.prototype.slice.call(r.querySelectorAll('[data-ln]')), cards = Array.prototype.slice.call(r.querySelectorAll('[data-lc]')), n = btns.length;
  function show(i, focus) {
    i = (i + n) % n;
    cards.forEach(function (c, j) { c.hidden = j !== i; });
    btns.forEach(function (b, j) { b.setAttribute('aria-pressed', j === i ? 'true' : 'false'); });
    if (focus) btns[i].focus();
  }
  btns.forEach(function (b, i) {
    b.addEventListener('click', function () { show(i); });
    b.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') { e.preventDefault(); show(i + 1, true); } if (e.key === 'ArrowLeft') { e.preventDefault(); show(i - 1, true); } });
  });
})();
