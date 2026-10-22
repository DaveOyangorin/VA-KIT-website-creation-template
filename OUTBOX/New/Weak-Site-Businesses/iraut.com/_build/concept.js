/* concept: the ecosystem wheel. Each segment is a keyboard-operable button; choosing one highlights it and shows that service's panel
   (their words, one of their properties, the figure that goes with it). Arrow keys move around the wheel. Nothing is sent anywhere. */
(function () {
  var e = document.querySelector('[data-eco]'); if (!e) return;
  var segs = Array.prototype.slice.call(e.querySelectorAll('[data-seg]'));
  function pick(i, focus) {
    segs.forEach(function (s, j) { s.setAttribute('aria-pressed', j === i ? 'true' : 'false'); });
    var k = segs[i].getAttribute('data-seg');
    e.querySelectorAll('[data-wp]').forEach(function (p) { p.hidden = p.getAttribute('data-wp') !== k; });
    if (focus) segs[i].focus();
  }
  segs.forEach(function (s, i) {
    s.addEventListener('click', function () { pick(i); });
    s.addEventListener('keydown', function (ev) {
      if (ev.key === 'Enter' || ev.key === ' ') { ev.preventDefault(); pick(i); }
      if (ev.key === 'ArrowRight' || ev.key === 'ArrowDown') { ev.preventDefault(); pick((i + 1) % segs.length, true); }
      if (ev.key === 'ArrowLeft' || ev.key === 'ArrowUp') { ev.preventDefault(); pick((i - 1 + segs.length) % segs.length, true); }
    });
  });
})();
