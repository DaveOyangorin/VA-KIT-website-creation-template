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

/* concept: the tree check. ISA's tree risk checklist as yes/no buttons; a "yes" lights the matching zone of the drawn tree (canopy,
   branch unions, trunk, roots and site). Any yes shows ISA's advice to have the tree examined by an ISA Certified Arborist and the ways
   an arborist may manage the risk. Nothing is sent anywhere. */
(function () {
  var c = document.querySelector('[data-tc]'); if (!c) return;
  var btns = Array.prototype.slice.call(c.querySelectorAll('[data-q]'));
  var ans = {}, zones = {};
  var yesN = c.querySelector('[data-tc-yes]'), ansN = c.querySelector('[data-tc-ans]');
  var h = c.querySelector('[data-tc-h]'), p = c.querySelector('[data-tc-p]'), more = c.querySelector('[data-tc-more]');
  var total = btns.length / 2;
  function draw() {
    var keys = Object.keys(ans), yes = keys.filter(function (k) { return ans[k].v === 'yes'; });
    yesN.textContent = yes.length; ansN.textContent = keys.length;
    var lit = {}; yes.forEach(function (k) { lit[ans[k].z] = 1; });
    ['canopy', 'union', 'trunk', 'roots'].forEach(function (z) {
      var g = c.querySelector('.z-' + z), t = c.querySelector('.t-' + z);
      if (g) g.classList.toggle('on', !!lit[z]); if (t) t.classList.toggle('on', !!lit[z]);
    });
    if (yes.length) {
      h.textContent = yes.length === 1 ? 'One sign worth a closer look' : yes.length + ' signs worth a closer look';
      p.textContent = 'ISA’s advice: if you answered yes to any question on the checklist, your tree should be examined by an ISA Certified Arborist.';
      more.hidden = false;
    } else if (keys.length === total) {
      h.textContent = 'No warning signs flagged';
      p.textContent = 'Good news. Mature trees still benefit from routine care, and regular care by an ISA Certified Arborist is a chance to catch defects early.';
      more.hidden = true;
    } else {
      h.textContent = keys.length ? 'Keep going' : 'Answer the questions above';
      p.textContent = 'Look at one tree at a time. Based on the ISA’s tree risk checklist.';
      more.hidden = true;
    }
  }
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      var q = b.getAttribute('data-q');
      btns.filter(function (x) { return x.getAttribute('data-q') === q; }).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      ans[q] = { v: b.getAttribute('data-v'), z: b.getAttribute('data-z') };
      draw();
    });
  });
  draw();
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
