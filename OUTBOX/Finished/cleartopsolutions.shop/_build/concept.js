/* cleartopsolutions.shop: blueprint hotspots, 48-hour dial, floating cards */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  // hotspots: pick the room where the water is
  document.querySelectorAll('[data-hmap]').forEach(function (map) {
    var wrap = map.parentNode, spots = map.querySelectorAll('.hs'), panels = wrap.querySelectorAll('.hp'), zones = map.querySelectorAll('.zone');
    var pick = function (z) {
      spots.forEach(function (s) { s.classList.toggle('on', s.dataset.z === z); s.setAttribute('aria-pressed', s.dataset.z === z ? 'true' : 'false'); });
      panels.forEach(function (p) { p.hidden = p.dataset.z !== z; });
      zones.forEach(function (g) { g.classList.toggle('on', g.dataset.z === z); g.classList.toggle('dim', g.dataset.z !== z); });
    };
    spots.forEach(function (s) {
      s.addEventListener('click', function () { pick(s.dataset.z); });
      s.addEventListener('mouseenter', function () { pick(s.dataset.z); });
    });
    pick(spots[0] && spots[0].dataset.z);
  });
  // 48-hour dial: fills as the section scrolls past, lights the matching step
  var sec = document.querySelector('[data-dial]');
  if (sec) {
    var dial = sec.querySelector('.clock48'), big = sec.querySelector('[data-hours]'), steps = sec.querySelectorAll('.d-step');
    var run = function () {
      var r = sec.getBoundingClientRect(), vh = window.innerHeight;
      var p = reduce ? 1 : Math.min(1, Math.max(0, (vh * 0.75 - r.top) / (r.height * 0.8)));
      dial.style.setProperty('--p', p.toFixed(3));
      big.textContent = Math.round(p * 48) + 'h';
      var k = Math.min(steps.length - 1, Math.floor(p * steps.length * 0.999));
      steps.forEach(function (s, i) { s.classList.toggle('on', i <= k); });
    };
    var tick = false;
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(function () { tick = false; run(); }); } }, { passive: true });
    window.addEventListener('resize', run); run();
  }
  // floating cards drift slightly with scroll
  var fl = document.querySelectorAll('[data-float]');
  if (fl.length && !reduce) {
    var f = function () { fl.forEach(function (c) { var r = c.getBoundingClientRect(); var d = Math.max(-36, Math.min(36, (r.top + r.height / 2 - window.innerHeight / 2) * parseFloat(c.dataset.float))); c.style.transform = 'translate3d(0,' + d.toFixed(1) + 'px,0)'; }); };
    window.addEventListener('scroll', function () { requestAnimationFrame(f); }, { passive: true }); f();
  }
})();
