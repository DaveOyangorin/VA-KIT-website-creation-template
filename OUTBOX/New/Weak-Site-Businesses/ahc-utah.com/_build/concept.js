/* concept: the thermostat card. HEAT/COOL switches the banner photo (winter / summer park), the headline, the credit line and the service
   tab; +/- moves the set point and the dial arc. It starts in the current season (October to April: heat). Nothing is sent anywhere. */
(function () {
  var hero = document.querySelector('[data-season]'), ts = document.querySelector('[data-tstat]'); if (!hero || !ts) return;
  var M = { heat: { set: 70, lab: 'Heating to', em: 'for the coldest mornings.', note: 'Furnace installs, repairs and tune-ups, all makes and models.', credit: 'Sugar House Park in snow · claralieu, CC BY 2.0', tab: 'heating' },
            cool: { set: 74, lab: 'Cooling to', em: 'for the hottest afternoons.', note: 'Air conditioning installs, repairs and tune-ups, central air to ductless.', credit: 'Liberty Park, Salt Lake City · Pollardjosephd, CC BY-SA 4.0', tab: 'cooling' } };
  var mode = 'heat', setEl = ts.querySelector('[data-set]'), arc = ts.querySelector('[data-arc]');
  function draw() { var v = M[mode].set; setEl.textContent = v; arc.style.strokeDasharray = (6 + (v - 60) / 20 * 69).toFixed(1) + ' 100'; }
  function tab(k) {
    document.querySelectorAll('[data-tab]').forEach(function (b) { var on = b.getAttribute('data-tab') === k; b.classList.toggle('on', on); b.setAttribute('aria-pressed', on); });
    document.querySelectorAll('[data-panel]').forEach(function (p) { p.classList.toggle('on', p.getAttribute('data-panel') === k); });
  }
  function setMode(m, init) {
    mode = m; hero.classList.toggle('mode-cool', m === 'cool'); hero.classList.toggle('mode-heat', m === 'heat');
    ts.querySelectorAll('[data-mode]').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-mode') === m); });
    ts.querySelector('[data-lab]').textContent = M[m].lab; ts.querySelector('[data-note]').textContent = M[m].note;
    var em = hero.querySelector('[data-h1em]'); if (em) em.textContent = M[m].em;
    var cr = hero.querySelector('[data-credit]'); if (cr) cr.textContent = M[m].credit;
    draw(); if (!init) tab(M[m].tab);
  }
  ts.querySelectorAll('[data-mode]').forEach(function (b) { b.addEventListener('click', function () { setMode(b.getAttribute('data-mode')); }); });
  ts.querySelectorAll('[data-step]').forEach(function (b) { b.addEventListener('click', function () { M[mode].set = Math.max(60, Math.min(80, M[mode].set + +b.getAttribute('data-step'))); draw(); }); });
  document.querySelectorAll('[data-tab]').forEach(function (b) { b.addEventListener('click', function () { tab(b.getAttribute('data-tab')); }); });
  var mo = new Date().getMonth(); setMode(mo >= 4 && mo <= 8 ? 'cool' : 'heat', true); tab(M[mode].tab);
})();
