/* concept: the itemized plan calculator. Three sliders (plumbing hours, after-hours hours, service calls); each row totals one option from
   the memberships page's published figures (annual fee + hours x rate + after-hours surcharge + call fees) and the lowest total is marked.
   Every calculator on a page works on its own. Nothing is sent anywhere. */
(function () {
  Array.prototype.forEach.call(document.querySelectorAll('[data-calc]'), function (c) {
    var plans = JSON.parse(c.querySelector('[data-calc-data]').textContent);
    var ins = {}; Array.prototype.forEach.call(c.querySelectorAll('[data-in]'), function (i) { ins[i.getAttribute('data-in')] = i; });
    var money = function (n) { return '$' + Math.round(n).toLocaleString('en-US'); };
    function calc() {
      var h = +ins.h.value, a = +ins.a.value, n = +ins.c.value;
      ['h', 'a', 'c'].forEach(function (k) { c.querySelector('[data-out="' + k + '"]').textContent = ins[k].value; });
      var best = null;
      plans.forEach(function (p) {
        p.total = p.fee + (h + a) * p.rate + a * p.ah + n * p.call;
        c.querySelector('[data-tot="' + p.k + '"]').textContent = money(p.total);
        if (!best || p.total < best.total) best = p;
      });
      plans.forEach(function (p) { c.querySelector('[data-row="' + p.k + '"]').classList.toggle('is-best', p === best); });
      var none = plans[0], line = best.k === 'none' ? 'At this level of use, paying standard rates costs least, before any plan perks.'
        : best.n + ' comes to ' + money(best.total) + ', ' + money(none.total - best.total) + ' less than standard rates, before percentage discounts and perks.';
      c.querySelector('[data-best]').textContent = line;
    }
    Object.keys(ins).forEach(function (k) { ins[k].addEventListener('input', calc); });
    calc();
  });
})();
