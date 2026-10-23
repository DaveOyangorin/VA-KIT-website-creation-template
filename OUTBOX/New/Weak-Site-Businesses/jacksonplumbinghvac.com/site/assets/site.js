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

/* concept: the two-hour leak test (EPA WaterSense method). Two meter readings in, gallons per day and per year out. Nothing is sent anywhere. */
(function () {
  var m = document.querySelector('[data-meter]'); if (!m) return;
  var a = m.querySelector('[data-a]'), b = m.querySelector('[data-b]'), h = m.querySelector('[data-h]'), out = m.querySelector('[data-mout]');
  var digits = m.querySelector('[data-digits]'), sweep = m.querySelector('[data-sweep]');
  function num(el) { var v = parseFloat(String(el.value).replace(/,/g, '')); return isNaN(v) ? null : v; }
  function fmt(n) { return n >= 100 ? Math.round(n).toLocaleString('en-US') : (Math.round(n * 10) / 10).toLocaleString('en-US'); }
  function say(cls, label, head, text) { out.className = 'mt-out ' + cls; out.innerHTML = '<p class="mono"></p><h3></h3><p></p>'; var p = out.children; p[0].textContent = label; p[1].textContent = head; p[2].textContent = text; }
  function update() {
    var x = num(a), y = num(b), hrs = num(h) || 2, cf = (m.querySelector('input[name="mt-u"]:checked') || {}).value === 'cf';
    var show = y != null ? y : x; digits.textContent = show == null ? '0000000' : String(Math.floor(show)).padStart(7, '0').slice(-7);
    m.classList.remove('is-leak', 'is-big', 'is-ok');
    if (x == null || y == null) { sweep.style.animationDuration = ''; say('', 'Waiting for two readings', 'Type both readings to see the result.', 'Most water meters sit in a box near the curb. If the readings match, there is no sign of a leak while the house was quiet.'); return; }
    var d = y - x; if (cf) d *= 7.48052;
    if (d < 0) { say('', 'Check the readings', 'The second reading is lower than the first.', 'Meters only count up. Check that the readings are in the right boxes and read from the same digits.'); return; }
    if (d === 0) { m.classList.add('is-ok'); sweep.style.animationDuration = '0s'; say('ok', 'No change', 'No sign of a leak while the house was quiet.', 'Your meter did not move in ' + fmt(hrs) + ' hours. WaterSense also suggests the toilet food-coloring test, since a slow flapper leak can be small.'); return; }
    var day = d / hrs * 24, yr = day * 365;
    m.classList.add('is-leak'); if (day >= 50) m.classList.add('is-big');
    sweep.style.animationDuration = Math.max(.4, 6 - Math.min(day, 500) / 100) + 's';
    say(day >= 50 ? 'big' : 'leak', 'About ' + fmt(day) + ' gallons a day', 'Your meter moved: you probably have a leak.',
      'That pace is roughly ' + fmt(yr) + ' gallons a year. ' + (day >= 50 ? 'WaterSense says nine percent of homes have leaks wasting 50 gallons or more a day; this reading puts yours in that group. ' : 'For comparison, WaterSense says the average household’s leaks waste more than 9,300 gallons a year. ') + 'Call 385-595-5700 and tell us what the meter did.');
  }
  m.addEventListener('input', update); m.addEventListener('change', update);
  m.querySelector('[data-mform]').addEventListener('submit', function (e) { e.preventDefault(); update(); });
  update();
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
