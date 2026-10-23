/* Snow load calculator: IBHS rules of thumb (via Maine Emergency Management). Fresh 11 in, packed 4 in or ice 1 in ~ 5 psf each. Nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-snow]'); if (!t) return;
  var f = t.querySelector('[data-fresh]'), p = t.querySelector('[data-packed]'), i = t.querySelector('[data-ice]'), fill = t.querySelector('[data-fill]'), num = t.querySelector('[data-psf]'), out = t.querySelector('[data-out]');
  function v(el) { var x = parseFloat(el.value); return isNaN(x) || x < 0 ? 0 : x; }
  function update() {
    var psf = v(f) / 11 * 5 + v(p) / 4 * 5 + v(i) * 5, pct = Math.min(100, psf / 60 * 100), c = out.children;
    num.textContent = Math.round(psf); fill.style.height = pct + '%'; t.classList.toggle('is-over', psf >= 20);
    c[0].textContent = 'About ' + Math.round(psf) + ' lb per square foot';
    if (psf < 12) { c[1].textContent = 'Well under a typical roof’s estimate.'; c[2].textContent = 'IBHS estimates a typical roof can take about 20 lb per sq ft of extra weight. Keep an eye on drifts and on new snow stacking up.'; }
    else if (psf < 20) { c[1].textContent = 'Getting closer to 20 psf.'; c[2].textContent = 'That is approaching the 20 lb per sq ft IBHS estimates for a typical roof, and older roofs may handle less. Watch for FEMA’s warning signs below.'; }
    else { c[1].textContent = 'At or above a typical roof’s estimate.'; c[2].textContent = 'This is beyond the 20 lb per sq ft IBHS estimates a typical roof can handle. Watch for sagging, cracking sounds or sticking doors; if you see them, FEMA says to get out and have a professional inspect. Call 435-375-3396.'; }
  }
  t.addEventListener('input', update); update();
})();
