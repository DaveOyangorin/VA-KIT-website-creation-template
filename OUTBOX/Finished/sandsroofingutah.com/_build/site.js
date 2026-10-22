/* S&S Roofing v2 ("Above the valley"): reveals, menus, hero parallax, the "Layer by layer" roof builder, services cursor photos,
   crew strip drift and the review rotator. Every moving part stands still for visitors who prefer reduced motion. */
(function () {
  var doc = document.documentElement; doc.classList.add('js');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if ('IntersectionObserver' in window && !reduce) {
    var vh = window.innerHeight;
    var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } }); }, { threshold: 0.08 });
    document.querySelectorAll('.reveal').forEach(function (el) { if (el.getBoundingClientRect().top > vh * 0.92) { el.classList.add('pre'); io.observe(el); } });
  }

  var drops = document.querySelectorAll('.nav details');
  document.addEventListener('click', function (e) { drops.forEach(function (d) { if (!d.contains(e.target)) d.open = false; }); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') { drops.forEach(function (d) { d.open = false; }); var m = document.querySelector('.menu'); if (m) m.open = false; } });

  /* hero parallax */
  var hb = document.querySelector('.hero-bg img');
  if (hb && !reduce) {
    var ticking = false;
    var par = function () { var y = window.pageYOffset; if (y < window.innerHeight * 1.2) hb.style.transform = 'translate3d(0,' + (y * 0.22).toFixed(1) + 'px,0) scale(1.06)'; ticking = false; };
    window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(par); } }, { passive: true });
  }

  /* signature: layer by layer */
  var L = document.querySelector('[data-layers]');
  if (L) {
    var r = L.querySelector('.ly-range'), gs = L.querySelectorAll('.ly-g'), ph = L.querySelectorAll('.ly-ph'), tx = L.querySelectorAll('.ly-tx'), bt = L.querySelectorAll('[data-go]');
    var names = ['Tear-off', 'Flashing and underlayment', 'Shingles', 'Ridge and ventilation', 'Final inspection'];
    var cur = -1, touched = false, anim = null;
    var draw = function (v) {
      gs.forEach(function (g) { var i = +g.dataset.l, o = i === 0 ? 1 : Math.max(0, Math.min(1, v - i + 1)); g.style.opacity = o; g.style.transform = 'translate(0px,' + ((o - 1) * 22).toFixed(1) + 'px)'; });
      var s = Math.max(0, Math.min(4, Math.round(v)));
      if (s !== cur) {
        cur = s; L.dataset.stage = s;
        ph.forEach(function (p) { p.classList.toggle('on', +p.dataset.i === s); });
        tx.forEach(function (t) { t.classList.toggle('on', +t.dataset.i === s); });
        bt.forEach(function (b) { b.setAttribute('aria-pressed', +b.dataset.go === s ? 'true' : 'false'); });
        r.setAttribute('aria-valuetext', names[s]);
      }
    };
    var stop = function () { if (anim) cancelAnimationFrame(anim); anim = null; };
    var tween = function (to, dur) {
      stop(); var from = +r.value, t0 = performance.now();
      var step = function (t) { var k = Math.min(1, (t - t0) / dur); k = k < 0.5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; r.value = from + (to - from) * k; draw(+r.value); if (k < 1) anim = requestAnimationFrame(step); };
      anim = requestAnimationFrame(step);
    };
    r.addEventListener('input', function () { touched = true; stop(); draw(+r.value); });
    r.addEventListener('change', function () { if (!reduce) tween(Math.round(+r.value), 250); });
    bt.forEach(function (b) { b.addEventListener('click', function () { touched = true; if (reduce) { r.value = b.dataset.go; draw(+r.value); } else tween(+b.dataset.go, 700); }); });
    draw(0);
    if (!reduce && 'IntersectionObserver' in window) {
      var lo = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { lo.disconnect(); setTimeout(function () { if (!touched) tween(4, 6000); }, 500); } }, { threshold: 0.4 });
      lo.observe(L);
    }
  }

  /* services: photo follows the cursor */
  var sl = document.querySelector('[data-svc]');
  if (sl && window.matchMedia('(hover: hover)').matches) {
    sl.addEventListener('mousemove', function (e) { var b = sl.getBoundingClientRect(); sl.style.setProperty('--mx', (e.clientX - b.left) + 'px'); });
  }

  /* crew strip drift */
  var fs = document.querySelector('.filmstrip');
  if (fs && !reduce) {
    var paused = false, last = 0, seen = false;
    fs.addEventListener('mouseenter', function () { paused = true; }); fs.addEventListener('mouseleave', function () { paused = false; });
    fs.addEventListener('touchstart', function () { paused = true; }, { passive: true });
    fs.addEventListener('focusin', function () { paused = true; });
    if ('IntersectionObserver' in window) new IntersectionObserver(function (es) { seen = es[0].isIntersecting; }).observe(fs); else seen = true;
    var tick = function (t) { if (seen && !paused && t - last > 24) { last = t; fs.scrollLeft += 1; if (fs.scrollLeft + fs.clientWidth >= fs.scrollWidth - 2) fs.scrollLeft = 0; } requestAnimationFrame(tick); };
    requestAnimationFrame(tick);
  }

  /* reviews */
  var R = document.querySelector('[data-rev]');
  if (R) {
    var qs = R.querySelectorAll('.rv'), n = R.querySelector('.rev-n b'), ri = 0, timer = null;
    var show = function (i) { ri = (i + qs.length) % qs.length; qs.forEach(function (q) { q.classList.toggle('on', +q.dataset.i === ri); }); n.textContent = ('0' + (ri + 1)).slice(-2); };
    var auto = function () { if (reduce) return; clearInterval(timer); timer = setInterval(function () { show(ri + 1); }, 7000); };
    R.querySelector('.rv-prev').addEventListener('click', function () { show(ri - 1); auto(); });
    R.querySelector('.rv-next').addEventListener('click', function () { show(ri + 1); auto(); });
    R.addEventListener('mouseenter', function () { clearInterval(timer); }); R.addEventListener('mouseleave', auto);
    auto();
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
