/* stgeorgehomeservices.com: the printing receipt, the town switcher, before/after compare */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var rc = document.querySelector('.receipt');
  if (rc) {
    if (reduce || !('IntersectionObserver' in window)) rc.classList.add('printed');
    else { var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { rc.classList.add('printed'); io.disconnect(); } }, { threshold: 0.35 }); io.observe(rc); }
  }
  document.querySelectorAll('[data-towns]').forEach(function (w) {
    var tabs = w.querySelectorAll('[role="tab"]'), panels = w.querySelectorAll('.tp');
    var pick = function (i) {
      tabs.forEach(function (t) { t.setAttribute('aria-selected', t.dataset.town === i ? 'true' : 'false'); });
      panels.forEach(function (p) { p.hidden = p.dataset.town !== i; });
    };
    tabs.forEach(function (t, n) {
      t.addEventListener('click', function () { pick(t.dataset.town); });
      t.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowDown' || e.key === 'ArrowRight' ? 1 : e.key === 'ArrowUp' || e.key === 'ArrowLeft' ? -1 : 0;
        if (!d) return; e.preventDefault(); var nx = tabs[(n + d + tabs.length) % tabs.length]; nx.focus(); pick(nx.dataset.town);
      });
    });
  });
  document.querySelectorAll('[data-compare]').forEach(function (st) {
    var r = st.querySelector('.cmp-range'); if (!r) return;
    var set = function () { st.style.setProperty('--pos', r.value + '%'); }; r.addEventListener('input', set); set();
  });
})();
