/* concept: the control panel. Each appliance label around the dial is a button; pressing one turns the needle to it and shows that
   appliance's read-out (what they fix, a tip from their own articles). Arrow keys move around the dial. Nothing is sent anywhere. */
(function () {
  var p = document.querySelector('[data-panel]'); if (!p) return;
  var btns = Array.prototype.slice.call(p.querySelectorAll('[data-app]')), needle = p.querySelector('[data-needle]'), n = btns.length;
  function pick(i, focus) {
    btns.forEach(function (b, j) { b.setAttribute('aria-pressed', j === i ? 'true' : 'false'); });
    var k = btns[i].getAttribute('data-app');
    p.querySelectorAll('[data-read]').forEach(function (r) { r.hidden = r.getAttribute('data-read') !== k; });
    needle.style.setProperty('--rot', (i * 360 / n + 180) + 'deg');
    if (focus) btns[i].focus();
  }
  btns.forEach(function (b, i) {
    b.addEventListener('click', function () { pick(i); });
    b.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') { e.preventDefault(); pick((i + 1) % n, true); }
      if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') { e.preventDefault(); pick((i - 1 + n) % n, true); }
    });
  });
  pick(0);
})();
