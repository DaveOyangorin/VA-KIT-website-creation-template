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

/* concept: the pin-tumbler lock (pick a problem: key slides in, pins set, plug turns, the service appears) and live open-now status
   from Lockthesmith's real hours in Utah time (storefront Mon-Fri 9-4, mobile daily 8-8). */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var now = function () {
    try {
      var p = new Intl.DateTimeFormat('en-US', { timeZone: 'America/Denver', weekday: 'short', hour: 'numeric', minute: 'numeric', hour12: false }).formatToParts(new Date());
      var g = function (t) { return (p.filter(function (x) { return x.type === t; })[0] || {}).value; };
      return { day: g('weekday'), h: (+g('hour') % 24) + (+g('minute')) / 60 };
    } catch (e) { var d = new Date(); return { day: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'][d.getDay()], h: d.getHours() + d.getMinutes() / 60 }; }
  };
  var t = now(), weekday = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'].indexOf(t.day) > -1;
  var storeOpen = weekday && t.h >= 9 && t.h < 16, mobileOpen = t.h >= 8 && t.h < 20;
  document.querySelectorAll('[data-hours] .hr').forEach(function (h) {
    var open = h.getAttribute('data-h') === 'store' ? storeOpen : mobileOpen, st = h.querySelector('[data-st]');
    st.textContent = open ? 'Open now' : 'Closed now'; st.classList.add(open ? 'open' : 'closed');
  });
  var dot = document.querySelector('[data-live-dot]'), lt = document.querySelector('[data-live-txt]');
  if (dot && mobileOpen) { dot.classList.add('on'); lt.textContent = 'Mobile service is out now · until 8 PM'; }
  else if (lt) lt.textContent = 'Mobile service · Mon–Sun 8 AM–8 PM';
  var lk = document.querySelector('[data-lock]');
  if (!lk) return;
  var sits = lk.querySelectorAll('.sit'), outs = lk.querySelectorAll('.lk-out'), note = lk.querySelector('[data-hours-note]'), timer;
  lk.querySelectorAll('[data-mode]').forEach(function (b) {
    var m = b.getAttribute('data-mode');
    b.textContent = m === 'mobile' ? (mobileOpen ? 'mobile service open now' : 'mobile service opens 8 AM') : (storeOpen ? 'storefront open now' : mobileOpen ? 'mobile service open now' : 'call to book');
  });
  if (note) note.textContent = mobileOpen ? 'Mobile service until 8 PM today' : 'Mobile service daily 8 AM–8 PM';
  var turn = function (k) {
    sits.forEach(function (s) { var on = s.getAttribute('data-sit') === k; s.classList.toggle('on', on); s.setAttribute('aria-pressed', on ? 'true' : 'false'); });
    outs.forEach(function (o) { o.classList.toggle('on', o.getAttribute('data-out') === k); });
    if (reduce) { lk.classList.add('set', 'turn'); return; }
    lk.classList.remove('set', 'turn'); void lk.offsetWidth; clearTimeout(timer);
    requestAnimationFrame(function () { lk.classList.add('set'); timer = setTimeout(function () { lk.classList.add('turn'); }, 600); });
  };
  sits.forEach(function (s) { s.addEventListener('click', function () { turn(s.getAttribute('data-sit')); }); });
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) { if (es[0].isIntersecting) { turn(sits[0].getAttribute('data-sit')); io.disconnect(); } }, { threshold: .4 }) : null;
  if (io) io.observe(lk); else turn(sits[0].getAttribute('data-sit'));
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
