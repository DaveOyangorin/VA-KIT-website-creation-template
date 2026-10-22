/* concept: the Community Action Items board. Pick a request; its card moves across the four columns, each step naming the ACS
   service that handles it. Reduced motion: the card shows the final state with all steps listed. */
(function () {
  var b = document.querySelector('[data-board]'); if (!b) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var tks = b.querySelectorAll('.tk'), cols = b.querySelectorAll('.col'), card = b.querySelector('[data-card]');
  var ct = b.querySelector('[data-card-t]'), cs = b.querySelector('[data-card-step]'), cw = b.querySelector('[data-card-stage]');
  var STAGES = ['Reported', "On the board’s list", 'Manager on it', 'Closed'], timer;
  var place = function (j, steps) {
    cols.forEach(function (c, k) { c.classList.toggle('past', k < j); c.classList.toggle('here', k === j); });
    cs.innerHTML = steps[j]; cw.textContent = STAGES[j];
    if (window.innerWidth > 640) { var w = cols[0].getBoundingClientRect().width + 10; card.style.transform = 'translateX(' + (j * w) + 'px)'; } else card.style.transform = '';
  };
  var run = function (t) {
    tks.forEach(function (x) { var on = x === t; x.classList.toggle('on', on); x.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    var tpl = b.querySelector('template[data-tpl="' + t.getAttribute('data-t') + '"]');
    var steps = [].map.call(tpl.content.querySelectorAll('p'), function (p) { return p.innerHTML; });
    ct.innerHTML = t.innerHTML; clearTimeout(timer);
    if (reduce) { place(3, steps); cs.innerHTML = steps.join(' '); return; }
    var j = 0; place(0, steps);
    var next = function () { j++; if (j < 4) { place(j, steps); timer = setTimeout(next, 1700); } };
    timer = setTimeout(next, 1500);
  };
  tks.forEach(function (t) { t.addEventListener('click', function () { run(t); }); });
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) { if (es[0].isIntersecting) { run(tks[0]); io.disconnect(); } }, { threshold: .35 }) : null;
  if (io) io.observe(b); else run(tks[0]);
  window.addEventListener('resize', function () { var on = b.querySelector('.tk.on'); if (on) { var j = [].indexOf.call(cols, b.querySelector('.col.here')); if (j > -1 && window.innerWidth > 640) card.style.transform = 'translateX(' + (j * (cols[0].getBoundingClientRect().width + 10)) + 'px)'; } });
})();
