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

/* concept: the lineup card. Tapping service chips adds them, numbered, to the card; the card writes a plain quote request that the
   visitor can copy or open in their own email app. Nothing is sent from the page. Every lineup on a page works on its own. */
(function () {
  Array.prototype.forEach.call(document.querySelectorAll('[data-lu]'), function (lu) {
    var chips = Array.prototype.slice.call(lu.querySelectorAll('.lu-chip'));
    var list = lu.querySelector('[data-lu-list]'), msg = lu.querySelector('[data-lu-msg]'), where = lu.querySelector('[data-lu-where]');
    var mail = lu.querySelector('[data-lu-mail]'), copy = lu.querySelector('[data-lu-copy]');
    var base = mail.getAttribute('href').split('?')[0];
    function picked() { return chips.filter(function (c) { return c.getAttribute('aria-pressed') === 'true'; }).map(function (c) { return c.getAttribute('data-s'); }); }
    function draw() {
      var p = picked();
      list.innerHTML = '';
      if (!p.length) { var e = document.createElement('li'); e.className = 'lu-empty'; e.textContent = 'Tap services to add them to your lineup.'; list.appendChild(e); }
      p.forEach(function (s, i) { var li = document.createElement('li'); var n = document.createElement('span'); n.className = 'varsity'; n.textContent = i + 1; li.appendChild(n); li.appendChild(document.createTextNode(s)); list.appendChild(li); });
      var w = where.value.trim();
      var t = p.length ? 'Hi Action Lawn & Yardcare, I would like a quote for:\n' + p.map(function (s) { return '- ' + s; }).join('\n') + (w ? '\n\nLocation: ' + w : '') + '\n\nThanks!' : '';
      msg.value = t;
      mail.setAttribute('href', base + (t ? '?subject=' + encodeURIComponent('Quote request') + '&body=' + encodeURIComponent(t) : ''));
      copy.disabled = !t;
    }
    chips.forEach(function (c) { c.addEventListener('click', function () { c.setAttribute('aria-pressed', c.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); draw(); }); });
    where.addEventListener('input', draw);
    copy.addEventListener('click', function () {
      var done = function () { copy.textContent = 'Copied'; setTimeout(function () { copy.textContent = 'Copy request'; }, 1600); };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(msg.value).then(done, function () { msg.select(); });
      else { msg.select(); }
    });
    draw();
  });
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
