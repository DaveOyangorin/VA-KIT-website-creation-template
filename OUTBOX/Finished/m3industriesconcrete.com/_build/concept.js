/* m3industriesconcrete.com: the exploded slab (layers separate and photos swap as each step scrolls into view) */
(function () {
  var w = document.querySelector('[data-layers]'); if (!w) return;
  var steps = w.querySelectorAll('.step'), frames = w.querySelectorAll('.lframe'), lys = w.querySelectorAll('.ly');
  var order = ['ground', 'base', 'steel', 'pour', 'finish'];
  var set = function (k) {
    var i = order.indexOf(k); w.setAttribute('data-at', i);
    steps.forEach(function (s) { s.classList.toggle('on', s.dataset.step === k); });
    frames.forEach(function (f) { f.classList.toggle('show', f.dataset.show === k); });
    lys.forEach(function (l) { var j = order.indexOf(l.dataset.l); l.classList.toggle('on', j <= i); l.classList.toggle('cur', j === i); });
  };
  set('ground');
  if (!('IntersectionObserver' in window)) { set('finish'); return; }
  var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) set(e.target.dataset.step); }); }, { rootMargin: '-45% 0px -45% 0px' });
  steps.forEach(function (s) { io.observe(s); });
})();
