/* concept: the season planner. Twelve month buttons; today's month is marked and selected on load. Choosing a month lists what Everwork
   does then (their own timing), with the time-sensitive jobs (startup, blowout, plowing) highlighted. Nothing is sent anywhere. */
(function () {
  var p = document.querySelector('[data-plan]'); if (!p) return;
  var data = JSON.parse(p.querySelector('[data-pl-data]').textContent);
  var names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  var key = { start: 1, blow: 1, snow: 1 };
  var btns = Array.prototype.slice.call(p.querySelectorAll('[data-m]'));
  var title = p.querySelector('[data-pl-title]'), now = p.querySelector('[data-pl-now]'), box = p.querySelector('[data-pl-tasks]');
  var cur = new Date().getMonth() + 1;
  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function show(m, focus) {
    btns.forEach(function (b) { b.setAttribute('aria-pressed', +b.getAttribute('data-m') === m ? 'true' : 'false'); });
    title.textContent = names[m - 1];
    now.textContent = m === cur ? 'This month' : (m === cur % 12 + 1 ? 'Next month' : 'Plan ahead');
    var order = ['start', 'blow', 'snow', 'clean_s', 'clean_f', 'lawn', 'install', 'repair'], h = '';
    order.forEach(function (k) {
      var t = data[k]; if (!t || t.m.indexOf(m) < 0) return;
      var tag = key[k] ? (k === 'snow' ? 'When it snows' : 'Book now') : (k === 'repair' ? 'All year' : 'In season');
      h += '<a class="pl-t' + (key[k] ? ' is-key' : '') + '" href="' + t.href + '"><em>' + tag + '</em><b>' + t.t + '</b><p>' + esc(t.d) + '</p></a>';
    });
    box.innerHTML = h;
    if (focus) btns[m - 1].focus();
  }
  btns.forEach(function (b, i) {
    if (i + 1 === cur) b.classList.add('is-now');
    b.addEventListener('click', function () { show(i + 1); });
    b.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight') { e.preventDefault(); show(i % 12 + 2 > 12 ? 1 : i + 2, true); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); show(i === 0 ? 12 : i, true); }
    });
  });
  show(cur);
})();
