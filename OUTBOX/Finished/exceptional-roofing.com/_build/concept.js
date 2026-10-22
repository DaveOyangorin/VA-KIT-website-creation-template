/* exceptional-roofing.com: before/after compare slider */
(function () {
  document.querySelectorAll('[data-compare]').forEach(function (st) {
    var r = st.querySelector('.cmp-range'); if (!r) return;
    var set = function () { st.style.setProperty('--pos', r.value + '%'); };
    r.addEventListener('input', set); set();
  });
})();
