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

/* concept: (1) the hero glass: a canvas of hard-water haze and mineral spots over the valley photo; dragging squeegees it clear, one
   stroke plays on load, "Clean the glass" clears it all (and is the only motion under reduced motion). (2) the quote-page estimator: their
   published prices, a range where the price is a range, and the $150 visit minimum. Nothing is sent anywhere. */
(function () {
  var hero = document.querySelector('[data-glass]'); if (!hero) return;
  var cv = hero.querySelector('[data-haze]'), ctx = cv.getContext('2d'), reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var W = 0, H = 0, dpr = Math.min(2, window.devicePixelRatio || 1), seed = 7;
  function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
  function paint() {
    var r = hero.getBoundingClientRect(); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.globalCompositeOperation = 'source-over'; seed = 7;
    var x0 = W < 640 ? 0 : W * .38, g = ctx.createLinearGradient(x0, 0, W, H);
    g.addColorStop(0, 'rgba(226,236,240,0)'); g.addColorStop(.18, 'rgba(226,236,240,.5)'); g.addColorStop(1, 'rgba(214,226,232,.62)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    for (var i = 0; i < Math.round(W * H / 2600); i++) {
      var x = x0 + rnd() * (W - x0), y = rnd() * H, s = 1.5 + rnd() * 6;
      ctx.beginPath(); ctx.arc(x, y, s, 0, 6.283); ctx.fillStyle = 'rgba(255,255,255,' + (.25 + rnd() * .45) + ')'; ctx.fill();
      ctx.lineWidth = .8; ctx.strokeStyle = 'rgba(170,150,120,' + (.18 + rnd() * .25) + ')'; ctx.stroke();
    }
    hero.classList.remove('clean');
  }
  var last = null, wiped = 0;
  function wipe(x, y) {
    ctx.globalCompositeOperation = 'destination-out'; ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.lineWidth = Math.max(70, Math.min(140, W * .08));
    ctx.beginPath(); ctx.moveTo(last ? last[0] : x, last ? last[1] : y); ctx.lineTo(x, y); ctx.stroke(); last = [x, y];
    if (++wiped > 40) hero.classList.add('clean');
  }
  function pos(e) { var r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; }
  var down = false;
  cv.addEventListener('pointerdown', function (e) { down = true; last = null; var p = pos(e); wipe(p[0], p[1]); });
  cv.addEventListener('pointermove', function (e) { if (!down && e.pointerType !== 'mouse') return; if (e.pointerType === 'mouse' && !down && e.buttons === 0) { var p = pos(e); if (last && Math.hypot(p[0] - last[0], p[1] - last[1]) > 120) last = null; wipe(p[0], p[1]); return; } var q = pos(e); wipe(q[0], q[1]); });
  window.addEventListener('pointerup', function () { down = false; last = null; });
  cv.addEventListener('pointerleave', function () { last = null; });
  hero.querySelector('[data-clean]').addEventListener('click', function () {
    if (hero.classList.contains('clean') && this.textContent === 'Fog it up again') { paint(); this.textContent = 'Clean the glass'; return; }
    if (reduce) { ctx.clearRect(0, 0, W, H); hero.classList.add('clean'); this.textContent = 'Fog it up again'; return; }
    var b = this, t0 = null, rows = 4;
    (function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 1600), row = Math.min(rows - 1, Math.floor(p * rows)), lp = p * rows - row;
      var y = H * (row + .5) / rows, x = row % 2 ? W * (1 - lp) : W * lp; if (lp < .03) last = null; wipe(x, y);
      if (p < 1) requestAnimationFrame(step); else { ctx.clearRect(0, 0, W, H); hero.classList.add('clean'); b.textContent = 'Fog it up again'; } })(performance.now());
  });
  paint();
  var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { if (Math.abs(hero.getBoundingClientRect().width - W) > 40) paint(); }, 200); });
  if (!reduce) setTimeout(function () {
    var t0 = null, x1 = W < 640 ? W * .1 : W * .45, x2 = W * .95, y1 = H * .3, y2 = H * .52;
    (function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 1100), e = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      wipe(x1 + (x2 - x1) * e, y1 + (y2 - y1) * e + Math.sin(e * 3.14) * -20); if (p < 1) requestAnimationFrame(step); else { last = null; wiped = 0; hero.classList.remove('clean'); } })(performance.now());
  }, 700);
})();

(function () {
  var es = document.querySelector('[data-est]'); if (!es) return;
  var NAMES = { ext: 'Outside windows', int: 'Inside windows', scr: 'Screens', trk: 'Window tracks', sol: 'Solar panels' };
  var CNT = { ext: 'panes', int: 'panes', scr: 'scr', trk: 'trk', sol: 'sol' };
  function n(k) { var i = es.querySelector('[data-cnt="' + k + '"] input'); return Math.max(0, Math.min(400, parseInt(i.value, 10) || 0)); }
  function money(v) { return '$' + Math.round(v).toLocaleString('en-US'); }
  function upd() {
    var lo = 0, hi = 0, lines = [], used = {};
    es.querySelectorAll('[data-es]').forEach(function (c) {
      var k = c.getAttribute('data-es'), q = n(CNT[k]); if (c.checked) used[CNT[k]] = 1;
      if (!c.checked || !q) return; var a = q * +c.getAttribute('data-lo'), b = q * +c.getAttribute('data-hi'); lo += a; hi += b;
      lines.push('<li><span>' + NAMES[k] + ' &times; ' + q + '</span><span>' + (a === b ? money(a) : money(a) + '&ndash;' + money(b)) + '</span></li>');
    });
    es.querySelectorAll('[data-cnt]').forEach(function (r) { r.classList.toggle('off', !used[r.getAttribute('data-cnt')]); });
    var min = 150, L = Math.max(lo, lo ? min : 0), Hh = Math.max(hi, hi ? min : 0);
    es.querySelector('[data-total]').textContent = !lo ? '$0' : (L === Hh ? money(L) : money(L) + '–' + money(Hh));
    es.querySelector('[data-range]').textContent = lo ? 'Estimate for a one-time clean' : 'Pick a service and add a count';
    es.querySelector('[data-lines]').innerHTML = lines.join('');
    es.querySelector('[data-min]').textContent = lo && lo < min ? 'Your total is below the $150 visit minimum, so the visit is $150.' : 'Every visit has a $150 minimum.';
  }
  es.addEventListener('click', function (e) {
    var b = e.target.closest('[data-inc],[data-dec]'); if (!b) return; var i = b.parentNode.querySelector('input');
    i.value = Math.max(0, Math.min(400, (parseInt(i.value, 10) || 0) + (b.hasAttribute('data-inc') ? 1 : -1))); upd();
  });
  es.addEventListener('input', upd); es.addEventListener('change', upd); upd();
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
