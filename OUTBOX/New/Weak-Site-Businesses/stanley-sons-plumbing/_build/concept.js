/* Water heater thermometer: CPSC Publication 5098 burn times at 120/130/140/150 F. Nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-therm]'); if (!t) return;
  var s = t.querySelector('[data-t]'), tv = t.querySelector('[data-tv]'), merc = t.querySelector('[data-merc]'), time = t.querySelector('[data-time]'), out = t.querySelector('[data-out]');
  var D = { 120: ['5 minutes', '120°F · CPSC’s recommendation', 'The setting CPSC urges for every home.', 'Even here, CPSC says a five-minute exposure could cause third-degree burns. Always hand-test bath water for young children.'],
    130: ['30 seconds', '130°F', 'Ten degrees over the recommendation.', 'At 130°F, CPSC says a thirty-second exposure can cause third-degree burns in most adults. Consider turning it down to 120°F.'],
    140: ['6 seconds', '140°F', 'Hot enough to burn in seconds.', 'At 140°F, CPSC says a six-second exposure can cause third-degree burns. Children under five and older adults are most at risk.'],
    150: ['2 seconds', '150°F', 'Dangerously hot.', 'CPSC says most adults suffer third-degree burns from 150°F water in two seconds. Turn it down, or call a plumber if you can’t reach the controls safely: 385-333-7488.'] };
  function update() {
    var v = +s.value, d = D[v], c = out.children;
    tv.textContent = v; time.textContent = d[0]; merc.style.height = (12 + (v - 120) / 30 * 88) + '%'; t.classList.toggle('is-safe', v === 120);
    c[0].textContent = d[1]; c[1].textContent = d[2]; c[2].textContent = d[3];
  }
  s.addEventListener('input', update); update();
})();
