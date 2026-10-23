/* Water hardness converter: USGS classes in mg/L as CaCO3; 1 gpg = 17.1 mg/L. Nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-hard]'); if (!t) return;
  var v = t.querySelector('[data-v]'), out = t.querySelector('[data-out]'), cls = t.querySelector('[data-cls]'), pin = t.querySelector('[data-pin]'), water = t.querySelector('[data-water]');
  var K = [[60, 'Soft', 'Little scale or soap scum to worry about, by the USGS scale.'], [120, 'Moderately hard', 'Some spotting and scale over time. USGS calls hardness a nuisance, not a health concern.'],
    [180, 'Hard', 'Expect soap scum, spots on glassware and scale in the water heater, which USGS says can raise heating costs and shorten equipment life.'],
    [1e9, 'Very hard', 'Scale builds up fastest here: on fixtures, inside water heaters and, over years, inside pipes. A plumber can talk through maintenance and treatment: 435-850-6314.']];
  function update() {
    var x = parseFloat(v.value), gpg = (t.querySelector('input[name="hd-u"]:checked') || {}).value !== 'mgl', c = out.children;
    if (isNaN(x) || x < 0) { c[0].textContent = 'Enter a number'; c[1].textContent = '—'; c[2].textContent = ''; return; }
    var mg = gpg ? x * 17.1 : x, k = K.filter(function (q) { return mg <= q[0]; })[0];
    cls.textContent = k[1]; c[0].textContent = Math.round(mg) + ' mg/L as calcium carbonate' + (gpg ? '' : ' · ' + (mg / 17.1).toFixed(1) + ' gpg'); c[1].textContent = k[1]; c[2].textContent = k[2];
    pin.style.left = Math.min(100, mg <= 180 ? mg / 240 * 100 : 75 + Math.min(25, (mg - 180) / 180 * 25)) + '%';
    water.setAttribute('r', Math.max(46, 79 - Math.min(mg, 360) / 360 * 33).toFixed(1));
  }
  t.addEventListener('input', update); t.addEventListener('change', update); update();
})();
