/* EMBER — the extra motion layer: fuse, ember trail, magnetic buttons + spark bursts, kiln-door photo reveals,
   parallax inside frames, scroll-velocity bands, floating previews, stacking cards, heat lines, word-by-word headings,
   and the burning "Ground your soul" at the foot of every page. All of it switches off for reduced motion. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var fine = window.matchMedia('(pointer: fine)').matches, hasIO = 'IntersectionObserver' in window, root = document.documentElement;
  function io(els, cb, opt) { if (!hasIO) { els.forEach(function (e) { cb(e); }); return; } var o = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { cb(e.target); o.unobserve(e.target); } }); }, opt || { threshold: .2 }); els.forEach(function (e) { o.observe(e); }); }

  // headings: every h2 also rises word by word, heating to ember and cooling as it lands
  document.querySelectorAll('h2:not([data-split])').forEach(function (h) { h.setAttribute('data-split', ''); });
  // (ember.js splits [data-split]; it runs after this file adds the attribute)
  var splitTargets = [];
  document.addEventListener('DOMContentLoaded', function () {});
  setTimeout(function () {
    splitTargets = Array.prototype.slice.call(document.querySelectorAll('h2[data-split]'));
    if (reduce) splitTargets.forEach(function (h) { h.classList.add('in'); });
    else io(splitTargets, function (h) { h.classList.add('in'); }, { threshold: .3 });
  }, 0);

  if (!reduce) document.querySelectorAll('.vessel').forEach(function (v) { if (!v.closest('.hero')) v.classList.add('door'); });
  if (reduce) { document.querySelectorAll('.door').forEach(function (d) { d.classList.add('open'); }); root.classList.add('still'); return; }

  // ---------- scroll fuse ----------
  var fuse = document.createElement('div'); fuse.className = 'fuse'; fuse.setAttribute('aria-hidden', 'true'); fuse.innerHTML = '<i></i>'; document.body.appendChild(fuse);

  // ---------- ember FX canvas: cursor trail + spark bursts ----------
  var fx = document.createElement('canvas'); fx.className = 'fx'; fx.setAttribute('aria-hidden', 'true'); document.body.appendChild(fx);
  var g = fx.getContext('2d'), P = [], fxRaf = 0, dpr = 1, W = 0, H = 0;
  function fxSize() { dpr = Math.min(2, window.devicePixelRatio || 1); W = innerWidth; H = innerHeight; fx.width = W * dpr; fx.height = H * dpr; }
  fxSize(); addEventListener('resize', fxSize);
  function emit(x, y, n, sp, up, life) {
    for (var i = 0; i < n; i++) { var a = Math.random() * Math.PI * 2, v = Math.random() * sp; P.push({ x: x, y: y, vx: Math.cos(a) * v, vy: Math.sin(a) * v - up, l: 1, d: 1 / (life || 50) * (.7 + Math.random() * .6), r: .8 + Math.random() * 1.8 }); }
    if (P.length > 400) P.splice(0, P.length - 400);
    if (!fxRaf) fxRaf = requestAnimationFrame(fxFrame);
  }
  function fxFrame() {
    fxRaf = 0; g.setTransform(dpr, 0, 0, dpr, 0, 0); g.clearRect(0, 0, W, H); g.globalCompositeOperation = 'lighter';
    for (var i = P.length - 1; i >= 0; i--) {
      var p = P[i]; p.x += p.vx; p.y += p.vy; p.vy -= .025; p.vx *= .97; p.l -= p.d;
      if (p.l <= 0) { P.splice(i, 1); continue; }
      var hot = p.l > .6 ? '255,226,176' : p.l > .3 ? '242,163,58' : '196,83,45';
      g.fillStyle = 'rgba(' + hot + ',' + (p.l * .9).toFixed(3) + ')'; g.beginPath(); g.arc(p.x, p.y, p.r * (.5 + p.l * .7), 0, 6.283); g.fill();
      g.fillStyle = 'rgba(242,163,58,' + (p.l * .12).toFixed(3) + ')'; g.beginPath(); g.arc(p.x, p.y, p.r * 4, 0, 6.283); g.fill();
    }
    g.globalCompositeOperation = 'source-over';
    if (P.length) fxRaf = requestAnimationFrame(fxFrame);
  }
  if (fine) { var lx = 0, ly = 0; addEventListener('pointermove', function (e) { var d = Math.hypot(e.clientX - lx, e.clientY - ly); if (d > 14) { lx = e.clientX; ly = e.clientY; emit(e.clientX, e.clientY, 1, .5, .4, 55); } }, { passive: true }); }
  document.addEventListener('click', function (e) { var b = e.target.closest('.btn, .ctrl button, .deck button, .ticks button'); if (b) emit(e.clientX, e.clientY, 22, 3.6, 1, 45); });

  // ---------- magnetic buttons ----------
  if (fine) document.querySelectorAll('.btn').forEach(function (b) {
    b.addEventListener('pointermove', function (e) { var r = b.getBoundingClientRect(); b.style.transform = 'translate(' + ((e.clientX - r.left - r.width / 2) * .22).toFixed(1) + 'px,' + ((e.clientY - r.top - r.height / 2) * .35).toFixed(1) + 'px)'; });
    b.addEventListener('pointerleave', function () { b.style.transform = ''; });
  });

  // ---------- kiln-door reveals for every photo frame ----------
  // (a closed door is clipped to nothing, so watch its container instead of the door itself)
  io(Array.prototype.slice.call(document.querySelectorAll('.door')).map(function (d) { d.parentNode._door = d; return d.parentNode; }), function (w) { w._door.classList.add('open'); }, { threshold: .2 });

  // ---------- heat lines across sections ----------
  io(Array.prototype.slice.call(document.querySelectorAll('.sec, .finale')), function (s) { s.classList.add('lit'); }, { threshold: .08 });

  // ---------- floating previews on session rows ----------
  var peek = null;
  if (fine) {
    peek = document.createElement('div'); peek.className = 'peek'; peek.setAttribute('aria-hidden', 'true'); peek.innerHTML = '<img alt="">'; document.body.appendChild(peek);
    var pimg = peek.firstChild, px = 0, py = 0, tx = 0, ty = 0, on = false, praf = 0;
    function pf() { praf = 0; px += (tx - px) * .16; py += (ty - py) * .16; peek.style.transform = 'translate(' + px.toFixed(1) + 'px,' + py.toFixed(1) + 'px) rotate(' + ((tx - px) * .04).toFixed(2) + 'deg)'; if (on || Math.abs(tx - px) > .5) praf = requestAnimationFrame(pf); }
    document.querySelectorAll('[data-img]').forEach(function (a) {
      a.addEventListener('pointerenter', function (e) { pimg.src = a.dataset.img; on = true; peek.classList.add('on'); tx = px = e.clientX + 24; ty = py = e.clientY - 120; if (!praf) praf = requestAnimationFrame(pf); });
      a.addEventListener('pointermove', function (e) { tx = e.clientX + 24; ty = e.clientY - 120; });
      a.addEventListener('pointerleave', function () { on = false; peek.classList.remove('on'); });
    });
  }

  // ---------- scroll-driven: fuse, parallax, velocity bands, stacking cards, burning text, gallery skew ----------
  var pics = Array.prototype.slice.call(document.querySelectorAll('.vessel img')).filter(function (i) { return !i.closest('.hero'); });
  var bands = Array.prototype.slice.call(document.querySelectorAll('.vtrack')).map(function (t, i) { return { el: t, x: 0, dir: i % 2 ? 1 : -1 }; });
  var cards = Array.prototype.slice.call(document.querySelectorAll('.stack article'));
  var burns = Array.prototype.slice.call(document.querySelectorAll('.burn'));
  var strips = Array.prototype.slice.call(document.querySelectorAll('.strip')).map(function (s) { return { el: s, last: s.scrollLeft, sk: 0 }; });
  var lastY = scrollY, vel = 0, lastT = performance.now(), sdir = 1;
  function tick(now) {
    var dt = Math.min(50, now - lastT) || 16; lastT = now;
    var y = scrollY, dy = y - lastY; lastY = y; vel += (dy / dt * 16 - vel) * .12; if (Math.abs(dy) > .5) sdir = dy > 0 ? 1 : -1;
    var max = document.documentElement.scrollHeight - innerHeight; fuse.firstChild.style.transform = 'scaleX(' + (max > 0 ? y / max : 0).toFixed(4) + ')';
    pics.forEach(function (im) { var r = im.parentNode.getBoundingClientRect(); if (r.bottom < -100 || r.top > innerHeight + 100) return; var c = (r.top + r.height / 2 - innerHeight / 2) / innerHeight; im.style.setProperty('--py', (c * -7).toFixed(2) + '%'); });
    bands.forEach(function (b) {
      var w = b.el.scrollWidth / 2; if (!w) return;
      b.x += (1.1 + Math.min(28, Math.abs(vel)) * .9) * b.dir * sdir * dt / 16; if (b.x < -w) b.x += w; if (b.x > 0) b.x -= w;
      b.el.style.transform = 'translate3d(' + b.x.toFixed(1) + 'px,0,0) skewX(' + (Math.max(-12, Math.min(12, -vel * .35)) * b.dir).toFixed(2) + 'deg)';
    });
    cards.forEach(function (c, i) { var n = cards[i + 1]; if (!n) return; var a = c.getBoundingClientRect(), b = n.getBoundingClientRect(), p = Math.max(0, Math.min(1, 1 - (b.top - a.top) / a.height)); c.style.transform = 'scale(' + (1 - p * .07).toFixed(4) + ')'; c.style.filter = 'brightness(' + (1 - p * .45).toFixed(3) + ')'; });
    burns.forEach(function (bn) { var r = bn.getBoundingClientRect(), p = Math.max(0, Math.min(1, (innerHeight - r.top) / (innerHeight * .9))); bn.style.setProperty('--p', (p * 100).toFixed(1) + '%'); });
    strips.forEach(function (s) { var d = s.el.scrollLeft - s.last; s.last = s.el.scrollLeft; s.sk += (Math.max(-8, Math.min(8, d * .4)) - s.sk) * .15; s.el.style.setProperty('--sk', s.sk.toFixed(2) + 'deg'); });
    requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
})();
