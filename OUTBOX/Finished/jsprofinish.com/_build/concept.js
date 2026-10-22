/* jsprofinish.com: same-room stage scrubber, trade hover preview, gallery filter, chalk-line draw */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var LAB = [['Visit 1', 'Drywall hung'], ['Visit 2', 'Taped &amp; textured'], ['Visit 3', 'Finished']];
  document.querySelectorAll('[data-scrub]').forEach(function (sc) {
    var range = sc.querySelector('.sc-range'), now = sc.querySelector('.sc-now'), room = 0, last = -1;
    var imgs = sc.querySelectorAll('.sc-img'), tabs = sc.querySelectorAll('.sc-tabs button');
    var paint = function () {
      var v = +range.value / 100, s = Math.min(1, Math.floor(v)), f = v - s; // stage pair s -> s+1, fraction f
      if (v >= 2) { s = 1; f = 1; }
      imgs.forEach(function (im) {
        var r = +im.dataset.r, k = +im.dataset.s, o = 0;
        if (r === room) { if (k === s) o = 1 - f; else if (k === s + 1) o = f; }
        im.style.opacity = o; im.classList.toggle('on', o > 0.5);
      });
      sc.style.setProperty('--p', (v / 2).toFixed(4));
      var st = Math.round(v);
      if (st !== last) { last = st; now.innerHTML = '<span>' + LAB[st][0] + '</span> ' + LAB[st][1]; }
      range.setAttribute('aria-valuetext', LAB[st][0] + ': ' + LAB[st][1].replace('&amp;', 'and'));
    };
    range.addEventListener('input', paint);
    tabs.forEach(function (t) {
      t.addEventListener('click', function () {
        room = +t.dataset.room; tabs.forEach(function (b) { b.setAttribute('aria-selected', b === t ? 'true' : 'false'); }); paint();
      });
    });
    paint();
    // play the job once when it first comes into view
    if (!reduce && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return; io.disconnect();
          var t0 = null, touched = false;
          range.addEventListener('pointerdown', function () { touched = true; }, { once: true });
          var step = function (t) {
            if (touched) return; if (!t0) t0 = t;
            var p = Math.min(1, (t - t0) / 3600), e2 = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
            range.value = Math.round(e2 * 200); paint(); if (p < 1) requestAnimationFrame(step);
          };
          setTimeout(function () { requestAnimationFrame(step); }, 500);
        });
      }, { threshold: 0.55 });
      io.observe(sc.querySelector('.sc-frame'));
    }
  });
  // trades: hover / focus swaps the preview photo
  var prev = document.querySelectorAll('.tp-img');
  document.querySelectorAll('.trade').forEach(function (a) {
    var go = function () {
      document.querySelectorAll('.trade').forEach(function (b) { b.classList.toggle('on', b === a); });
      prev.forEach(function (p) { p.classList.toggle('on', p.dataset.img === a.dataset.img); });
    };
    a.addEventListener('mouseenter', go); a.addEventListener('focus', go);
  });
  // gallery filter
  var chips = document.querySelectorAll('.g-chips button');
  chips.forEach(function (c) {
    c.addEventListener('click', function () {
      chips.forEach(function (b) { b.classList.toggle('on', b === c); });
      document.querySelectorAll('.g-sec').forEach(function (s) { s.hidden = !(c.dataset.filter === 'all' || s.dataset.cat === c.dataset.filter); });
    });
  });
  // chalk line across the process steps
  var steps = document.querySelector('.steps3');
  if (steps) {
    if (reduce || !('IntersectionObserver' in window)) steps.classList.add('drawn');
    else { var so = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { steps.classList.add('drawn'); so.disconnect(); } }, { threshold: 0.4 }); so.observe(steps); }
  }
})();
