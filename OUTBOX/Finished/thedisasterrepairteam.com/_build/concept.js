/* thedisasterrepairteam.com: damage-type switcher, one-team line */
(function () {
  document.querySelectorAll('[data-els]').forEach(function (h) {
    var tabs = h.querySelectorAll('.et'), bgs = h.querySelectorAll('.eb'), panels = h.querySelectorAll('.ep');
    var pick = function (e) {
      h.className = h.className.replace(/\bel-\w+/, 'el-' + e);
      tabs.forEach(function (t) { t.setAttribute('aria-selected', t.dataset.el === e ? 'true' : 'false'); });
      bgs.forEach(function (b) { b.classList.toggle('on', b.dataset.el === e); });
      panels.forEach(function (p) { p.hidden = p.dataset.el !== e; });
    };
    tabs.forEach(function (t, n) {
      t.addEventListener('click', function () { pick(t.dataset.el); });
      t.addEventListener('keydown', function (ev) {
        var d = ev.key === 'ArrowRight' ? 1 : ev.key === 'ArrowLeft' ? -1 : 0; if (!d) return;
        ev.preventDefault(); var nx = tabs[(n + d + tabs.length) % tabs.length]; nx.focus(); pick(nx.dataset.el);
      });
    });
  });
  var ho = document.querySelector('[data-handoff]');
  if (ho) {
    if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) ho.classList.add('in');
    else { var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { ho.classList.add('in'); io.disconnect(); } }, { threshold: .4 }); io.observe(ho); }
  }
})();
