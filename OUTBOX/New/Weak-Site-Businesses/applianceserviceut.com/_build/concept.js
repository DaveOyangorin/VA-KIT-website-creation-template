/* concept: the carbon-copy service ticket. The three selects fill the ticket; it confirms coverage from ASI's own lists and works out the
   next service day from their hours (Mon-Fri 8-5, same or next-day service) and the holidays they close. Nothing is sent anywhere. */
(function () {
  function nthDow(y, m, dow, n) { var d = new Date(y, m, 1), c = 0; while (true) { if (d.getDay() === dow && ++c === n) return d; d.setDate(d.getDate() + 1); } }
  function lastDow(y, m, dow) { var d = new Date(y, m + 1, 0); while (d.getDay() !== dow) d.setDate(d.getDate() - 1); return d; }
  function holiday(d) {
    var y = d.getFullYear(), k = d.getMonth() * 100 + d.getDate();
    if (k === 1 || k === 604 || k === 624 || k === 1125) return true; // Jan 1, Jul 4, Jul 24, Dec 25
    var s = function (x) { return x.getMonth() === d.getMonth() && x.getDate() === d.getDate(); };
    return s(lastDow(y, 4, 1)) || s(nthDow(y, 8, 1, 1)) || s(nthDow(y, 10, 4, 4)); // Memorial, Labor, Thanksgiving
  }
  function open(d) { var w = d.getDay(); return w > 0 && w < 6 && !holiday(d); }
  function fmt(d) { return d.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' }); }
  function nextDay() {
    var now = new Date(), d = new Date(now), first;
    if (open(now) && now.getHours() < 17) first = new Date(now);
    else { d.setDate(d.getDate() + 1); while (!open(d)) d.setDate(d.getDate() + 1); first = d; }
    var second = new Date(first); second.setDate(second.getDate() + 1); while (!open(second)) second.setDate(second.getDate() + 1);
    var today = first.toDateString() === now.toDateString();
    return (today ? 'Call today: ' : 'Call ' + fmt(first) + ': ') + 'service ' + (today ? 'today or ' : fmt(first) + ' or ') + fmt(second);
  }
  document.querySelectorAll('[data-ticket]').forEach(function (t) {
    var card = t.querySelector('.tk-card'), no = t.querySelector('[data-t-no]');
    no.textContent = String(1000 + (new Date().getDate() * 37 + new Date().getMonth() * 11) % 9000);
    function upd() {
      var v = {}; ['area', 'app', 'brand'].forEach(function (k) { var s = t.querySelector('[data-t="' + k + '"]'); v[k] = s.value; t.querySelector('[data-t-out="' + k + '"]').textContent = s.value ? (s.value === 'other' ? s.options[s.selectedIndex].text : s.value) : '—'; });
      var done = v.area && v.app && v.brand, ok = done && v.area !== 'other' && v.brand !== 'other';
      t.querySelector('[data-t-day]').textContent = done ? nextDay() : '—';
      card.classList.toggle('ok', !!ok); card.classList.toggle('ask', !!done && !ok);
      t.querySelector('[data-t-stamp]').textContent = ok ? 'COVERED' : 'CALL US';
      t.querySelector('[data-t-status]').textContent = !done ? 'Fill in the three fields to check coverage.' :
        ok ? 'We service ' + v.app.toLowerCase() + ' from ' + v.brand + ' in the ' + v.area + '. Call (801) 487-8591 to book.' :
        'Call (801) 487-8591 and we’ll tell you whether we can help: we repair most brand names across the Wasatch Front.';
    }
    t.addEventListener('change', upd); upd();
  });
})();
