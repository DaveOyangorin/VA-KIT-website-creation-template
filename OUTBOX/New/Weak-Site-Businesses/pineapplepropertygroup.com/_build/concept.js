/* concept: the investment valuation tool, rebuilt. Standard rental math: effective rent = rent x 12 x (1 - vacancy); management = 5% of
   effective rent; NOI = effective rent - (tax + insurance + repairs + utilities + management); debt service from a fixed-rate amortized loan;
   cap rate = NOI / price; cash flow = NOI - debt service; cash on cash = annual cash flow / (down payment + closing costs). It also compares
   a 5% fee with 10% and shows three fee-free months at 5%. Nothing is sent anywhere. */
(function () {
  Array.prototype.forEach.call(document.querySelectorAll('[data-calc]'), function (c) {
    var ins = {}; Array.prototype.forEach.call(c.querySelectorAll('[data-k]'), function (i) { ins[i.getAttribute('data-k')] = i; });
    var out = function (k, v) { var e = c.querySelector('[data-o="' + k + '"]'); if (e) e.textContent = v; };
    var $ = function (n) { var s = Math.round(n), neg = s < 0; return (neg ? '-$' : '$') + Math.abs(s).toLocaleString('en-US'); };
    var pct = function (n) { return isFinite(n) ? n.toFixed(1) + '%' : '—'; };
    var v = function (k) { var x = parseFloat(ins[k].value); return isFinite(x) && x >= 0 ? x : 0; };
    function calc() {
      var price = v('price'), down = price * v('down') / 100, loan = price - down, r = v('rate') / 100 / 12, n = v('years') * 12;
      var pay = loan <= 0 || n <= 0 ? 0 : (r === 0 ? loan / n : loan * r / (1 - Math.pow(1 + r, -n)));
      var egi = v('rent') * 12 * (1 - Math.min(v('vac'), 100) / 100);
      var m5 = egi * 0.05, m10 = egi * 0.10;
      var opex = v('tax') + v('ins') + v('rep') * 12 + v('util') * 12;
      var noi = egi - opex - m5, debt = pay * 12, cf = noi - debt, invested = down + v('closing');
      out('egi', $(egi)); out('opex', $(opex)); out('mgmt', $(m5)); out('noi', $(noi)); out('debt', $(debt));
      out('cf', $(cf / 12)); out('cap', pct(price > 0 ? noi / price * 100 : NaN)); out('coc', pct(invested > 0 ? cf / invested * 100 : NaN));
      out('f5', $(m5)); out('f10', $(m10)); out('diff', $(m10 - m5)); out('free', $(v('rent') * (1 - Math.min(v('vac'), 100) / 100) * 3 * 0.05));
      var big = c.querySelector('[data-o="cf"]'); if (big) big.classList.toggle('neg', cf < 0);
    }
    Object.keys(ins).forEach(function (k) { ins[k].addEventListener('input', calc); });
    calc();
  });
})();
