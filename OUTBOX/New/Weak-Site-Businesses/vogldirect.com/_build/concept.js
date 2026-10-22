/* concept: Comfort Club builder. Pick a plan, tick add-ons, and the service tag shows the plan's inclusions, the monthly total and the
   12-month total, from Vogl Direct's published prices. Works on the home page and the Comfort Club page. Nothing is sent anywhere. */
(function () {
  var NAMES = { basic: 'Basic', preferred: 'Preferred', plus: 'Preferred Plus' };
  var ADD = { salt: 'Water softener salt', dryer: 'Dryer vent cleaning', wh: 'Water heater inspection & drain', smoke: 'Smoke & CO detector batteries' };
  document.querySelectorAll('[data-cc]').forEach(function (cc, n) {
    cc.querySelectorAll('input[name="plan"]').forEach(function (r) { r.name = 'plan' + n; });
    function money(v) { return '$' + v.toFixed(2).replace(/\B(?=(\d{3})+(?!\d))/g, ','); }
    function upd() {
      var p = cc.querySelector('input[name="plan' + n + '"]:checked'); if (!p) return;
      var tot = +p.getAttribute('data-price'), lines = [];
      cc.querySelectorAll('[data-add]').forEach(function (a) { if (a.checked) { tot += +a.getAttribute('data-add'); lines.push('<li>' + ADD[a.value] + ' <span>(+$' + a.getAttribute('data-add') + '/mo)</span></li>'); } });
      cc.querySelector('[data-cc-name]').textContent = NAMES[p.value];
      cc.querySelector('[data-cc-mo]').textContent = money(tot);
      cc.querySelector('[data-cc-yr]').textContent = money(tot * 12);
      cc.querySelectorAll('[data-feats]').forEach(function (u) { u.hidden = u.getAttribute('data-feats') !== p.value; });
      cc.querySelector('[data-cc-adds]').innerHTML = lines.join('');
    }
    cc.addEventListener('change', upd); upd();
  });
})();
