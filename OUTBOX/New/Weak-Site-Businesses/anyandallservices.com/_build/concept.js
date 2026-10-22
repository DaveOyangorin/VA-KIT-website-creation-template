/* concept: the breaker panel. Each breaker is a part of the job; switching it on lights it amber and adds it to a one-line project
   description. "Put this in my estimate request" copies that line (plus any extra note) into the estimate form's description field and
   scrolls to it. Nothing is sent from the page. */
(function () {
  var p = document.querySelector('[data-pnl]'); if (!p) return;
  var brks = Array.prototype.slice.call(p.querySelectorAll('[data-b]'));
  var line = p.querySelector('[data-pnl-line]'), count = p.querySelector('[data-pnl-count]'), bulb = p.querySelector('[data-pnl-bulb]');
  var extra = p.querySelector('[data-pnl-extra]'), go = p.querySelector('[data-pnl-go]');
  function text() {
    var on = brks.filter(function (b) { return b.getAttribute('aria-pressed') === 'true'; }).map(function (b) { return b.getAttribute('data-t'); });
    if (!on.length) return '';
    var list = on.length === 1 ? on[0] : on.slice(0, -1).join(', ') + ' and ' + on[on.length - 1];
    var x = extra.value.trim();
    return 'I would like an estimate for ' + list + '.' + (x ? ' ' + x : '');
  }
  function draw() {
    var n = brks.filter(function (b) { return b.getAttribute('aria-pressed') === 'true'; }).length;
    count.textContent = n + (n === 1 ? ' circuit on' : ' circuits on');
    bulb.classList.toggle('on', n > 0);
    line.textContent = text() || 'Flip a breaker for each part of the job.';
  }
  brks.forEach(function (b) { b.addEventListener('click', function () { b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); draw(); }); });
  extra.addEventListener('input', draw);
  go.addEventListener('click', function () {
    var t = text(), msg = document.getElementById('f-msg');
    if (t && msg) { msg.value = t; setTimeout(function () { msg.focus(); }, 400); }
  });
  draw();
})();
