/* concept: the pipeline. Five valves on a copper pipe; opening one fills the pipe with water up to that valve and shows that step's card
   (their own words). Previous / Next buttons and arrow keys walk the steps. Nothing is sent anywhere. */
(function () {
  var p = document.querySelector('[data-pipe]'); if (!p) return;
  var valves = Array.prototype.slice.call(p.querySelectorAll('[data-step]')), cards = Array.prototype.slice.call(p.querySelectorAll('[data-card]'));
  var water = p.querySelector('[data-water]'), n = valves.length, cur = 0;
  function go(i, focus) {
    cur = (i + n) % n;
    valves.forEach(function (v, j) { v.setAttribute('aria-pressed', j === cur ? 'true' : 'false'); v.classList.toggle('done', j < cur); });
    cards.forEach(function (c, j) { c.hidden = j !== cur; });
    p.style.setProperty('--fill', ((cur + .5) / n * 100) + '%');
    p.querySelector('[data-prev]').disabled = cur === 0;
    p.querySelector('[data-next]').innerHTML = cur === n - 1 ? 'Start over' : 'Next step <span aria-hidden="true">→</span>';
    if (focus) valves[cur].focus();
  }
  valves.forEach(function (v, i) {
    v.addEventListener('click', function () { go(i); });
    v.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') { e.preventDefault(); go(i + 1, true); } if (e.key === 'ArrowLeft') { e.preventDefault(); go(i - 1, true); } });
  });
  p.querySelector('[data-prev]').addEventListener('click', function () { go(cur - 1); });
  p.querySelector('[data-next]').addEventListener('click', function () { go(cur === n - 1 ? 0 : cur + 1); });
  go(0);
})();
