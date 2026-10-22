/* concept: tap-a-zone yard plan. The zone buttons (and the zones on the plan) pick a zone: it is outlined, the rest dim, and the panel shows
   that service with a photo from one of their jobs. Nothing is sent anywhere. */
(function () {
  var y = document.querySelector('[data-yard]'); if (!y) return;
  var btns = y.querySelectorAll('[data-zone]'), zones = y.querySelectorAll('[data-z]');
  function pick(k) {
    btns.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-zone') === k); });
    zones.forEach(function (z) { var on = z.getAttribute('data-z') === k; z.classList.toggle('on', on); z.classList.toggle('dim', !on); });
    y.querySelectorAll('[data-panel]').forEach(function (p) { p.hidden = p.getAttribute('data-panel') !== k; });
  }
  btns.forEach(function (b) { b.addEventListener('click', function () { pick(b.getAttribute('data-zone')); }); });
  zones.forEach(function (z) { z.addEventListener('click', function () { pick(z.getAttribute('data-z')); }); });
  pick(btns[0].getAttribute('data-zone'));
})();
