/* Home safety checklist: sourced items by season; ticks kept in localStorage on this device only. Nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-list]'); if (!t) return;
  var items = [].slice.call(t.querySelectorAll('[data-items] li')), boxes = [].slice.call(t.querySelectorAll('[data-id]')), arc = t.querySelector('[data-arc]'), pct = t.querySelector('[data-pct]'), out = t.querySelector('[data-out]');
  var KEY = 'husky-checklist', saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { saved = {}; }
  boxes.forEach(function (b) { b.checked = !!saved[b.getAttribute('data-id')]; });
  var LEAD = { m: ['Start with this month’s list.', 'Two minutes: press the test button on each smoke alarm, and look at the HVAC filter.'],
    f: ['Get ready before the first freeze.', 'Outdoor faucets, the main shutoff and clear vents. IBHS notes homes built before 2010 typically don’t have frost-proof outdoor faucets.'],
    y: ['The once-a-year jobs.', 'Batteries, alarm ages, a heating system service and the water heater setting. Need a hand with any of it? Call 801-742-5282.'] };
  function update() {
    var s = (t.querySelector('input[name="ls-s"]:checked') || {}).value || 'm', done = boxes.filter(function (b) { return b.checked; }).length, c = out.children;
    items.forEach(function (li) { li.hidden = li.getAttribute('data-s') !== s; });
    var p = Math.round(done / boxes.length * 100); pct.textContent = p + '%'; arc.style.strokeDashoffset = 100 - p;
    c[0].textContent = done + ' of ' + boxes.length + ' done'; c[1].textContent = done === boxes.length ? 'Everything ticked. Nice work.' : LEAD[s][0]; c[2].textContent = LEAD[s][1];
    try { var o = {}; boxes.forEach(function (b) { if (b.checked) o[b.getAttribute('data-id')] = 1; }); localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {}
  }
  t.addEventListener('change', update); update();
})();
