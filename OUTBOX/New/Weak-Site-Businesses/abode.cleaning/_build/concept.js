/* concept: the get-ready checklist (Abode's own pre-cleaning instructions). Each tick fills the readiness meter; at 100% the arrival
   windows light up. Ticks are remembered in this browser only. */
(function () {
  var list = document.querySelector('[data-prep-list]'); if (!list) return;
  var boxes = [].slice.call(list.querySelectorAll('[data-prep]')), meter = document.querySelector('[data-meter]'), ring = document.querySelector('[data-ring]');
  var pct = document.querySelector('[data-pct]'), msg = document.querySelector('[data-msg]'), slots = document.querySelector('[data-slots]'), C = 327;
  try { var saved = JSON.parse(localStorage.getItem('abode-prep') || '[]'); boxes.forEach(function (b, i) { b.checked = saved.indexOf(i) > -1; }); } catch (e) {}
  var upd = function () {
    var n = boxes.filter(function (b) { return b.checked; }).length, p = Math.round(n / boxes.length * 100);
    ring.style.strokeDashoffset = C - C * n / boxes.length; pct.textContent = p + '%';
    msg.textContent = n === boxes.length ? 'ready for your team' : n === 0 ? 'ready' : (boxes.length - n) + ' to go';
    meter.classList.toggle('full', n === boxes.length); slots.classList.toggle('on', n === boxes.length);
    try { localStorage.setItem('abode-prep', JSON.stringify(boxes.map(function (b, i) { return b.checked ? i : -1; }).filter(function (i) { return i > -1; }))); } catch (e) {}
  };
  boxes.forEach(function (b) { b.addEventListener('change', upd); }); upd();
})();
