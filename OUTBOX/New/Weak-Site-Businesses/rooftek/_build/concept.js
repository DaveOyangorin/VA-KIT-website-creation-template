/* Roof pitch calculator: rise over 12 -> angle, slope factor, roof area. Geometry only; nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-pitch]'); if (!t) return;
  var r = t.querySelector('[data-r]'), f = t.querySelector('[data-f]'), rv = t.querySelector('[data-rv]'), poly = t.querySelector('[data-poly]'), rise = t.querySelector('[data-rise]'), lbl = t.querySelector('[data-plbl]'), out = t.querySelector('[data-out]');
  function update() {
    var x = +r.value, ang = Math.atan(x / 12) * 180 / Math.PI, k = Math.sqrt(x * x + 144) / 12, h = Math.min(150, 140 * x / 12), fp = parseFloat(f.value);
    rv.textContent = x; lbl.textContent = x + ' / 12';
    poly.setAttribute('points', '20,170 160,' + (170 - h).toFixed(1) + ' 300,170'); rise.setAttribute('y2', (170 - h).toFixed(1));
    var p = out.children;
    p[0].textContent = x + '/12 pitch' + (x < 4 ? ' · low slope' : x >= 9 ? ' · steep' : '');
    p[1].textContent = ang.toFixed(1) + '° roof angle';
    p[2].textContent = 'Slope factor ' + k.toFixed(3) + (fp > 0 ? ': a ' + Math.round(fp).toLocaleString('en-US') + ' sq ft footprint is roughly ' + Math.round(fp * k).toLocaleString('en-US') + ' sq ft of roof, about ' + (fp * k / 100).toFixed(1) + ' roofing squares, before overhangs and waste.' : ': every square foot of floor below is about ' + k.toFixed(2) + ' square feet of roof.');
  }
  t.addEventListener('input', update); update();
})();
