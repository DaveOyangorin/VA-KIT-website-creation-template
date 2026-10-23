/* concept: "Maintain, repair or replace?" dial. System type, age and condition point to one of the three services. Guidance is ENERGY
   STAR's (yearly tune-ups, monthly filter checks, a professional look at equipment more than 10 years old). Nothing is sent anywhere. */
(function () {
  var d = document.querySelector('[data-dial]'); if (!d) return;
  var age = d.querySelector('[data-age]'), out = d.querySelector('[data-age-out]'), needle = d.querySelector('[data-needle]');
  var read = d.querySelector('[data-read]'), head = d.querySelector('[data-head]'), text = d.querySelector('[data-text]');
  var NAMES = { furnace: 'furnace', ac: 'air conditioner', hp: 'heat pump', mini: 'ductless system' };
  function val(n) { var c = d.querySelector('input[name="' + n + '"]:checked'); return c ? c.value : ''; }
  function update() {
    var a = +age.value, t = NAMES[val('dl-type')] || 'system', bad = val('dl-run') === 'bad', old = a > 10;
    out.textContent = a >= 25 ? '25+' : a;
    needle.setAttribute('transform', 'rotate(' + (-135 + a * 10.8) + ')');
    d.classList.toggle('is-old', old); d.classList.toggle('is-new', !old); d.classList.toggle('is-bad', bad);
    if (!bad && !old) { read.textContent = 'Maintenance service'; head.textContent = 'Keep it running like new';
      text.textContent = 'A ' + a + '-year-old ' + t + ' that runs fine mostly needs care: a yearly tune-up and a filter check every month. Regular maintenance prevents premature parts failures.'; }
    else if (!bad) { read.textContent = 'Maintenance + a check-up'; head.textContent = 'Worth a professional look';
      text.textContent = 'Your ' + t + ' is past 10 years. ENERGY STAR suggests having equipment that age evaluated by a professional, and considering replacement if it is not performing efficiently. We will tell you honestly which it is.'; }
    else if (!old) { read.textContent = 'Repair'; head.textContent = 'The Fixer Upper';
      text.textContent = 'A ' + a + '-year-old ' + t + ' that is acting up is usually a repair. Whatever you need, we can fix, on all major brands.'; }
    else { read.textContent = 'Repair or new installation'; head.textContent = 'Fix it, or replace it?';
      text.textContent = 'An older ' + t + ' that is not working right is the classic judgment call. We can help you get the last few years out of it, or quote a new installation with a 2 year labor warranty and 10 year parts warranties. Quotes are free.'; }
  }
  d.addEventListener('input', update); d.addEventListener('change', update); update();
})();
