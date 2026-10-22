/* swiftrestoreutah.com: pinned horizontal recovery timeline + before/after compare */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-hscroll]').forEach(function (sec) {
    var track = sec.querySelector('.hs-track'), bar = sec.querySelector('.hs-bar span');
    if (!track) return;
    var narrow = function () { return window.innerWidth < 900 || reduce; };
    var size = function () {
      if (narrow()) { sec.classList.add('no-hs'); sec.style.height = ''; track.style.transform = ''; return; }
      sec.classList.remove('no-hs');
      var dist = Math.max(0, track.scrollWidth - window.innerWidth + 80);
      sec.style.height = (window.innerHeight + dist) + 'px'; sec.dataset.dist = dist; run();
    };
    var run = function () {
      if (narrow()) return;
      var r = sec.getBoundingClientRect(), dist = parseFloat(sec.dataset.dist || 0);
      var p = Math.min(1, Math.max(0, -r.top / Math.max(1, sec.offsetHeight - window.innerHeight)));
      track.style.transform = 'translate3d(' + (-p * dist).toFixed(1) + 'px,0,0)'; if (bar) bar.style.width = (p * 100).toFixed(1) + '%';
    };
    var tick = false;
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(function () { tick = false; run(); }); } }, { passive: true });
    window.addEventListener('resize', size); window.addEventListener('load', size); size();
  });
  document.querySelectorAll('[data-compare]').forEach(function (st) {
    var r = st.querySelector('.cmp-range'); if (!r) return;
    var set = function () { st.style.setProperty('--pos', r.value + '%'); }; r.addEventListener('input', set); set();
  });
})();
