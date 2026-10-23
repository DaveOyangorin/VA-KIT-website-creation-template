/* 811 color guide: APWA uniform color code (as listed by Virginia 811) plus Blue Stakes of Utah notes. Nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-locate]'); if (!t) return;
  var C = [['Red', '#e2231a', 'Electric power lines, cables, conduit and lighting cables', 'Power to a detached garage or a yard lamppost is private wiring and may not be marked.'],
    ['Yellow', '#f6d000', 'Gas, oil, steam, petroleum or gaseous material', 'Lines to a propane tank are private and may not be marked.'],
    ['Orange', '#f7941d', 'Communication, alarm or signal lines, cables or conduit', 'Utah law requires operators to mark only the lines they own and maintain, usually up to the meter.'],
    ['Blue', '#1f75c4', 'Potable water', 'Operators usually mark water up to the meter; the lateral from the meter to the house is typically private.'],
    ['Green', '#2ca02c', 'Sewers and drain lines', 'Sewer laterals from the house to the main are typically private and may not be marked. That is where a plumber with an excavator comes in.'],
    ['Purple', '#8e44ad', 'Reclaimed water, irrigation and slurry lines', 'Your own sprinkler and irrigation lines are private and may not be marked.'],
    ['White', '#ffffff', 'Proposed excavation', 'You can outline a small dig area in white paint or flags so only the utilities there get located.']];
  var btns = [].slice.call(t.querySelectorAll('[data-c]')), out = t.querySelector('[data-out]');
  function show(i, focus) {
    i = (i + C.length) % C.length; var c = C[i], p = out.children;
    btns.forEach(function (b, j) { b.setAttribute('aria-pressed', j === i ? 'true' : 'false'); });
    t.style.setProperty('--lc', c[1]); p[0].textContent = c[0]; p[1].textContent = c[2]; p[2].textContent = c[3];
    if (focus) btns[i].focus();
  }
  btns.forEach(function (b, i) {
    b.addEventListener('click', function () { show(i); });
    b.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') { e.preventDefault(); show(i + 1, true); } if (e.key === 'ArrowLeft') { e.preventDefault(); show(i - 1, true); } });
  });
  show(0);
})();
