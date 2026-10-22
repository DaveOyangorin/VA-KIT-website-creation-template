/* stgeorgeconcreteleveling.com: the lip gauge (2010 ADA Standards 303.2-303.4) */
(function () {
  var g = document.querySelector('[data-gauge]'); if (!g) return;
  var r = g.querySelector('.g-range'), num = g.querySelector('[data-in]'), rule = g.querySelector('[data-rule]'), ref = g.querySelector('[data-ref]');
  var frac = function (n) {
    if (n === 0) return '0'; if (n === 16) return '1';
    var a = n, b = 16; while (a % 2 === 0 && b > 1) { a /= 2; b /= 2; } return a + '/' + b;
  };
  var set = function () {
    var n = +r.value, v = n / 16, c, t, d;
    if (n === 0) { c = 'var(--ok)'; t = 'Level'; d = 'No change in level.'; }
    else if (v <= 0.25) { c = 'var(--ok)'; t = 'Allowed as a vertical edge'; d = '303.2: up to 1/4 inch may be vertical.'; }
    else if (v <= 0.5) { c = 'var(--warn)'; t = 'Must be beveled'; d = '303.3: 1/4 to 1/2 inch must be beveled, no steeper than 1:2.'; }
    else { c = 'var(--bad)'; t = 'Trip hazard: must be ramped'; d = '303.4: more than 1/2 inch must be ramped. In practice, lift the slab back into line.'; }
    g.style.setProperty('--lip', (v).toFixed(4)); g.style.setProperty('--c', c);
    num.textContent = frac(n); rule.textContent = t; ref.textContent = d;
    r.setAttribute('aria-valuetext', frac(n) + ' inch: ' + t);
  };
  r.addEventListener('input', set); set();
})();
