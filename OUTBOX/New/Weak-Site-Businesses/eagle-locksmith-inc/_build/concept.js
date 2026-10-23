/* Locksmith call checklist: BBB locksmith-scam tips (2020) as a tick-list. Nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-chk]'); if (!t) return;
  var ks = [].slice.call(t.querySelectorAll('[data-k]')), arc = t.querySelector('[data-arc]'), n = t.querySelector('[data-n]'), out = t.querySelector('[data-out]');
  function update() {
    var c = ks.filter(function (k) { return k.checked; }).length, p = out.children;
    n.textContent = c; arc.style.strokeDashoffset = 100 - c / ks.length * 100; arc.style.opacity = c ? 1 : 0; p[0].textContent = c + ' of ' + ks.length + ' checked';
    if (c === 0) { p[1].textContent = 'Start ticking as you go.'; p[2].textContent = 'Ask each question on the phone before anyone is sent.'; }
    else if (c < 4) { p[1].textContent = 'Keep asking.'; p[2].textContent = 'Unchecked items are the questions to ask next. The BBB says to get the full price, including service call, mileage and parts, before agreeing.'; }
    else if (c < ks.length) { p[1].textContent = 'Mostly reassuring.'; p[2].textContent = 'Check the last items when the locksmith arrives. If the on-site price doesn’t match the quote, the BBB says to have someone else do the job.'; }
    else { p[1].textContent = 'Every box ticked.'; p[2].textContent = 'That matches what the BBB says to expect from a legitimate locksmith. Pay by card and keep the itemized invoice.'; }
  }
  t.addEventListener('change', update); update();
})();
