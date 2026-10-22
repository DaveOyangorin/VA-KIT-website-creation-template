/* concept: "Heave or settle?". The gauge wets the clay (heave mode: cells swell, the floor bows up in the middle and cracks) or,
   in settlement mode, washes out soil under one side (the right wall and floor drop). Text is the client's own. */
(function () {
  var H = document.querySelector('[data-heave]'); if (!H) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var r = H.querySelector('.hv-range'), slab = H.querySelector('[data-slab]'), crack = H.querySelector('[data-crack]'), read = H.querySelector('[data-read]');
  var glab = H.querySelector('[data-glabel]'), btns = H.querySelectorAll('[data-mode]'), tx = H.querySelectorAll('.hv-tx'), ends = H.querySelectorAll('.hv-gauge i');
  var mode = 0, touched = false, anim = null;
  var draw = function () {
    var w = +r.value / 100; H.style.setProperty('--w', w.toFixed(3));
    if (mode === 0) {
      var up = 56 * w;
      slab.setAttribute('d', 'M224 318 Q450 ' + (318 - up).toFixed(1) + ' 676 318 L676 340 Q450 ' + (340 - up).toFixed(1) + ' 224 340 Z');
      crack.setAttribute('transform', 'translate(0 ' + (-up / 2).toFixed(1) + ')');
      read.textContent = w < .25 ? 'DRY' : w < .6 ? 'DAMP: SWELLING' : 'WET: HEAVING';
    } else {
      var dn = 22 * w;
      slab.setAttribute('d', 'M224 318 L676 ' + (318 + dn).toFixed(1) + ' L676 ' + (340 + dn).toFixed(1) + ' L224 340 Z');
      crack.setAttribute('transform', 'translate(0 ' + (dn / 2).toFixed(1) + ')');
      read.textContent = w < .25 ? 'SOUND' : w < .6 ? 'SETTLING' : 'SETTLED: ONE SIDE DOWN';
    }
    crack.style.opacity = w > .55 ? Math.min(1, (w - .55) * 4) : 0;
    r.setAttribute('aria-valuetext', read.textContent.toLowerCase());
  };
  var setMode = function (m) {
    mode = m; H.dataset.mode = m;
    btns.forEach(function (b) { b.setAttribute('aria-pressed', +b.dataset.mode === m ? 'true' : 'false'); });
    tx.forEach(function (t) { t.classList.toggle('on', +t.dataset.i === m); });
    glab.textContent = m === 0 ? 'Moisture in the clay' : 'Soil washed out under one side';
    ends[0].textContent = m === 0 ? 'Dry' : 'None'; ends[1].textContent = m === 0 ? 'Wet' : 'A lot';
    r.setAttribute('aria-label', m === 0 ? 'Moisture in the clay, dry to wet' : 'Soil washed out under one side, none to a lot');
    draw();
  };
  var stop = function () { if (anim) cancelAnimationFrame(anim); anim = null; };
  var tween = function (to, dur) { stop(); var from = +r.value, t0 = performance.now();
    var step = function (t) { var k = Math.min(1, (t - t0) / dur); k = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; r.value = from + (to - from) * k; draw(); if (k < 1) anim = requestAnimationFrame(step); };
    anim = requestAnimationFrame(step); };
  r.addEventListener('input', function () { touched = true; stop(); draw(); });
  btns.forEach(function (b) { b.addEventListener('click', function () { touched = true; stop(); setMode(+b.dataset.mode); }); });
  setMode(0);
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); setTimeout(function () { if (!touched) tween(100, 4500); }, 600); } }, { threshold: .45 });
    io.observe(H);
  }
})();
/* v2: slow parallax on the archive photographs */
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var els = [].slice.call(document.querySelectorAll('[data-par]')); if (!els.length) return;
  var tick = false;
  var run = function () { els.forEach(function (el) { var r = el.parentElement.getBoundingClientRect(); if (r.bottom < 0 || r.top > innerHeight) return; var k = +el.dataset.par; el.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - innerHeight / 2) * -k).toFixed(1) + 'px,0)'; }); tick = false; };
  addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run();
})();
