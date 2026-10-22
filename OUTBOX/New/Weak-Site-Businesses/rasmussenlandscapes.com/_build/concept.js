/* concept: the Yard year dial. Click or key through months; the list shows the jobs Rasmussen's pages place in that month.
   Starts on the current month. */
(function () {
  var y = document.querySelector('[data-year]');
  if (!y) return;
  var MON = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
  var segs = y.querySelectorAll('.seg'), items = y.querySelectorAll('.yr-list li'), hm = y.querySelector('[data-hub-m]'), hn = y.querySelector('[data-hub-n]'), cur = new Date().getMonth();
  var pick = function (m) {
    cur = (m + 12) % 12; var n = 0;
    segs.forEach(function (s) { s.classList.toggle('on', +s.getAttribute('data-m') === cur); });
    items.forEach(function (li) { var on = li.getAttribute('data-ms').split(' ').indexOf(String(cur)) > -1; li.classList.toggle('on', on); if (on) { li.style.setProperty('--i', n); n++; } });
    hm.textContent = MON[cur]; hn.textContent = n + (n === 1 ? ' job' : ' jobs') + ' this month';
  };
  segs.forEach(function (s) {
    s.addEventListener('click', function () { pick(+s.getAttribute('data-m')); });
    s.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(+s.getAttribute('data-m')); } if (e.key === 'ArrowRight') pick(cur + 1); if (e.key === 'ArrowLeft') pick(cur - 1); });
  });
  y.querySelector('[data-yr-prev]').addEventListener('click', function () { pick(cur - 1); });
  y.querySelector('[data-yr-next]').addEventListener('click', function () { pick(cur + 1); });
  pick(cur);
})();
