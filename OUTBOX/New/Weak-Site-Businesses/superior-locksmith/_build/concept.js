/* Rekey, repair or replace? General guidance by situation; BHMA grades for upgrades. Nothing is sent anywhere. */
(function () {
  var t = document.querySelector('[data-pick]'); if (!t) return;
  var out = t.querySelector('[data-out]'), pins = [].slice.call(t.querySelectorAll('[data-pins] rect'));
  var D = { move: ['rekey', 'Rekey', 'Keep the locks, change the keys.', 'You don’t know who still has a key from the last owner. Rekeying changes the pins inside the lock so old keys stop working, and you keep the hardware you have.'],
    lost: ['rekey', 'Rekey', 'Make the lost key useless.', 'If a key is lost or not returned, rekeying the affected locks means it no longer opens anything. Ask whether all the locks on that key should be done.'],
    many: ['rekey', 'Rekey to one key', 'One key for several doors.', 'Locks that take the same style of key can often be rekeyed so a single key opens them all. Bring the keys you use so the locksmith can check.'],
    stiff: ['fix', 'Repair first', 'Have it looked at before you replace it.', 'A key that sticks or won’t turn can come from a worn key, the lock or the door alignment. A locksmith can tell you whether a repair, a new key or a new lock is the right fix.'],
    broken: ['new', 'Replace', 'Time for a new lock.', 'A damaged lock, or one that can’t be repaired, gets replaced. That’s the moment to look at the grade on the new one.'],
    stronger: ['new', 'Upgrade', 'Look at the grade.', 'BHMA grades locks by standard: Grade 1 bored locks under A156.2 pass one million cycles; residential Grade A locks under A156.39 pass 400,000 cycles and eleven strength and security tests. Ask which grade fits your door.'] };
  var H = { rekey: [26, 18, 32, 22], fix: [26, 34, 20, 30], new: [18, 18, 18, 18] };
  function update() {
    var k = (t.querySelector('input[name="pk"]:checked') || {}).value || 'move', d = D[k], c = out.children;
    c[0].textContent = d[1]; c[1].textContent = d[2]; c[2].textContent = d[3];
    t.classList.toggle('is-open', d[0] === 'rekey'); t.classList.toggle('is-new', d[0] === 'new'); t.classList.toggle('is-fix', d[0] === 'fix');
    pins.forEach(function (p, i) { p.setAttribute('height', H[d[0]][i]); });
  }
  t.addEventListener('change', update); update();
})();
