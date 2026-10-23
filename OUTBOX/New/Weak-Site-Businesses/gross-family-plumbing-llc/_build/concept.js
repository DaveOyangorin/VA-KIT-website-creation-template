/* Toilet water calculator: current gpf vs WaterSense 1.28 gpf (EPA WaterSense figures). Flushes per day are the visitor's estimate. Nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-flush]'); if (!t) return;
  var p = t.querySelector('[data-p]'), f = t.querySelector('[data-f]'), a = t.querySelector('[data-a]'), b = t.querySelector('[data-b]'), out = t.querySelector('[data-out]');
  function n(el) { var x = parseFloat(el.value); return isNaN(x) || x < 0 ? 0 : x; }
  function fmt(x) { return Math.round(x).toLocaleString('en-US'); }
  function update() {
    var g = parseFloat((t.querySelector('input[name="fl-g"]:checked') || {}).value || 3.5), fl = n(p) * n(f) * 365, now = fl * g, ws = fl * 1.28, c = out.children;
    a.style.height = Math.min(100, g / 6 * 100) + '%'; b.style.height = (1.28 / 6 * 100) + '%';
    c[0].textContent = fmt(fl) + ' flushes a year at ' + g + ' gpf';
    c[1].textContent = 'About ' + fmt(now - ws) + ' gallons a year more than WaterSense';
    c[2].textContent = 'Your toilet: roughly ' + fmt(now) + ' gallons a year. A WaterSense-labeled toilet at 1.28 gallons per flush: roughly ' + fmt(ws) + '. Run the dye test below too; a leaking toilet wastes water between flushes.';
  }
  t.addEventListener('input', update); t.addEventListener('change', update); update();
})();
