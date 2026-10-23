/* concept: the two-hour leak test (EPA WaterSense method). Two meter readings in, gallons per day and per year out. Nothing is sent anywhere. */
(function () {
  var m = document.querySelector('[data-meter]'); if (!m) return;
  var a = m.querySelector('[data-a]'), b = m.querySelector('[data-b]'), h = m.querySelector('[data-h]'), out = m.querySelector('[data-mout]');
  var digits = m.querySelector('[data-digits]'), sweep = m.querySelector('[data-sweep]');
  function num(el) { var v = parseFloat(String(el.value).replace(/,/g, '')); return isNaN(v) ? null : v; }
  function fmt(n) { return n >= 100 ? Math.round(n).toLocaleString('en-US') : (Math.round(n * 10) / 10).toLocaleString('en-US'); }
  function say(cls, label, head, text) { out.className = 'mt-out ' + cls; out.innerHTML = '<p class="mono"></p><h3></h3><p></p>'; var p = out.children; p[0].textContent = label; p[1].textContent = head; p[2].textContent = text; }
  function update() {
    var x = num(a), y = num(b), hrs = num(h) || 2, cf = (m.querySelector('input[name="mt-u"]:checked') || {}).value === 'cf';
    var show = y != null ? y : x; digits.textContent = show == null ? '0000000' : String(Math.floor(show)).padStart(7, '0').slice(-7);
    m.classList.remove('is-leak', 'is-big', 'is-ok');
    if (x == null || y == null) { sweep.style.animationDuration = ''; say('', 'Waiting for two readings', 'Type both readings to see the result.', 'Most water meters sit in a box near the curb. If the readings match, there is no sign of a leak while the house was quiet.'); return; }
    var d = y - x; if (cf) d *= 7.48052;
    if (d < 0) { say('', 'Check the readings', 'The second reading is lower than the first.', 'Meters only count up. Check that the readings are in the right boxes and read from the same digits.'); return; }
    if (d === 0) { m.classList.add('is-ok'); sweep.style.animationDuration = '0s'; say('ok', 'No change', 'No sign of a leak while the house was quiet.', 'Your meter did not move in ' + fmt(hrs) + ' hours. WaterSense also suggests the toilet food-coloring test, since a slow flapper leak can be small.'); return; }
    var day = d / hrs * 24, yr = day * 365;
    m.classList.add('is-leak'); if (day >= 50) m.classList.add('is-big');
    sweep.style.animationDuration = Math.max(.4, 6 - Math.min(day, 500) / 100) + 's';
    say(day >= 50 ? 'big' : 'leak', 'About ' + fmt(day) + ' gallons a day', 'Your meter moved: you probably have a leak.',
      'That pace is roughly ' + fmt(yr) + ' gallons a year. ' + (day >= 50 ? 'WaterSense says nine percent of homes have leaks wasting 50 gallons or more a day; this reading puts yours in that group. ' : 'For comparison, WaterSense says the average household’s leaks waste more than 9,300 gallons a year. ') + 'Call 385-595-5700 and tell us what the meter did.');
  }
  m.addEventListener('input', update); m.addEventListener('change', update);
  m.querySelector('[data-mform]').addEventListener('submit', function (e) { e.preventDefault(); update(); });
  update();
})();
