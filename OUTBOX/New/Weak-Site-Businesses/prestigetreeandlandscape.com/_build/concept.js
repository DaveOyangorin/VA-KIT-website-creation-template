/* concept: growth rings. Gold rings (and the year buttons) open that year's story; arrow keys step between them. Nothing is sent anywhere. */
(function () {
  var r = document.querySelector('[data-rings]'); if (!r) return;
  var rings = Array.prototype.slice.call(r.querySelectorAll('[data-ring]')), btns = Array.prototype.slice.call(r.querySelectorAll('[data-go]'));
  var panels = Array.prototype.slice.call(r.querySelectorAll('[data-rp]')), n = panels.length;
  function show(i, focus) {
    i = (i + n) % n;
    panels.forEach(function (p, j) { p.hidden = j !== i; });
    btns.forEach(function (b, j) { b.setAttribute('aria-pressed', j === i ? 'true' : 'false'); });
    rings.forEach(function (c) { c.classList.toggle('on', +c.getAttribute('data-ring') === i); });
    if (focus) btns[i].focus();
  }
  rings.forEach(function (c) {
    var i = +c.getAttribute('data-ring');
    c.addEventListener('click', function () { show(i); });
    c.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); show(i); } });
  });
  btns.forEach(function (b, i) {
    b.addEventListener('click', function () { show(i); });
    b.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') { e.preventDefault(); show(i + 1, true); } if (e.key === 'ArrowLeft') { e.preventDefault(); show(i - 1, true); } });
  });
  show(n - 1);
})();
