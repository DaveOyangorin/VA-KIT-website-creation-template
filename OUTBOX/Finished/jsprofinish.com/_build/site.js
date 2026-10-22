/* kit2 premium layer: reveals, parallax, sticky story steps, counters, image swaps, dropdown closing. Reduced motion = static. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var html = document.documentElement; html.classList.remove('no-js'); html.classList.add('js');
  // reveals
  var rv = document.querySelectorAll('.reveal, .reveal-up');
  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: 0.08 });
    rv.forEach(function (el) { if (el.getBoundingClientRect().top > vh * 0.92) { if (el.classList.contains('reveal')) el.classList.add('pre'); io.observe(el); } else el.classList.add('in'); });
  } else rv.forEach(function (el) { el.classList.add('in'); });
  // parallax
  var px = [].slice.call(document.querySelectorAll('[data-parallax]'));
  if (px.length && !reduce) {
    var tick = false;
    var run = function () { tick = false; var h = window.innerHeight; px.forEach(function (el) { var r = el.parentElement.getBoundingClientRect(); if (r.bottom < 0 || r.top > h) return; var s = parseFloat(el.getAttribute('data-parallax')) || 0.15; el.style.transform = 'translate3d(0,' + ((r.top + r.height / 2 - h / 2) * -s).toFixed(1) + 'px,0)'; }); };
    window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(run); } }, { passive: true }); run();
  }
  // sticky story: activate step in view, light up matching layer in the visual
  document.querySelectorAll('.story').forEach(function (st) {
    var steps = st.querySelectorAll('.step'), vis = st.querySelector('.story-visual');
    if (!('IntersectionObserver' in window)) return;
    var so = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (!e.isIntersecting) return;
        steps.forEach(function (s) { s.classList.toggle('on', s === e.target); });
        var key = e.target.getAttribute('data-step');
        if (vis) { vis.classList.add('has-active'); vis.querySelectorAll('[data-layer]').forEach(function (l) { l.classList.toggle('lit', l.getAttribute('data-layer') === key); }); var sw = vis.querySelectorAll('[data-show]'); sw.forEach(function (x) { x.classList.toggle('show', x.getAttribute('data-show') === key); }); }
        var out = st.querySelector('[data-readout]'); if (out && e.target.getAttribute('data-value')) out.textContent = e.target.getAttribute('data-value');
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    steps.forEach(function (s) { so.observe(s); });
  });
  // counters
  var cs = document.querySelectorAll('[data-count]');
  if ('IntersectionObserver' in window) {
    var co = new IntersectionObserver(function (es) { es.forEach(function (e) { if (!e.isIntersecting) return; co.unobserve(e.target); var el = e.target, to = parseFloat(el.getAttribute('data-count')), suf = el.getAttribute('data-suffix') || '', t0 = null; if (reduce) { el.textContent = to + suf; return; } var step = function (t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 1400); el.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))) + suf; if (p < 1) requestAnimationFrame(step); }; requestAnimationFrame(step); }); }, { threshold: 0.4 });
    cs.forEach(function (c) { co.observe(c); });
  }
  // image swap: hovering/focusing an item shows its photo
  document.querySelectorAll('[data-swap-group]').forEach(function (g) {
    var imgs = g.querySelectorAll('[data-swap-img]');
    g.querySelectorAll('[data-swap]').forEach(function (it) {
      var on = function () { var k = it.getAttribute('data-swap'); imgs.forEach(function (im) { im.classList.toggle('show', im.getAttribute('data-swap-img') === k); }); g.querySelectorAll('[data-swap]').forEach(function (o) { o.classList.toggle('on', o === it); }); };
      it.addEventListener('mouseenter', on); it.addEventListener('focus', on); it.addEventListener('click', on);
    });
  });
  // nav dropdowns
  var drops = document.querySelectorAll('.nav details');
  document.addEventListener('click', function (e) { drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; } });
})();

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

/* MFIX-2026-10-19: mobile header fix */
(function () {
  var h = document.querySelector('.site-header'); if (!h) return;
  var root = document.documentElement;
  function y() { return Math.max(window.pageYOffset || 0, root.scrollTop || 0, document.body ? document.body.scrollTop || 0 : 0); }
  function upd() {
    var b = Math.max(0, Math.round(h.getBoundingClientRect().bottom));
    root.style.setProperty('--hdr-bottom', b + 'px');
    h.classList.toggle('scrolled', y() > 6);
  }
  window.addEventListener('scroll', upd, { passive: true });
  window.addEventListener('resize', upd, { passive: true });
  document.addEventListener('scroll', upd, { passive: true, capture: true });
  document.querySelectorAll('.menu').forEach(function (m) {
    m.addEventListener('toggle', function () { upd(); root.classList.toggle('menu-open', m.open); });
    m.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', function () { m.open = false; }); });
  });
  upd(); setTimeout(upd, 300);
})();
