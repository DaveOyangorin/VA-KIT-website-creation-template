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

/* concept: Plan your basement. Chosen rooms are laid into the basement of the section drawing (widths follow a rough share of the floor),
   the dimension line shows the size, and RWK's three project rules are checked live. Works without motion; nothing is sent anywhere. */
(function () {
  var pl = document.querySelector('[data-planner]'); if (!pl) return;
  var NS = 'http://www.w3.org/2000/svg';
  var NAMES = { family: 'Family room', theater: 'Theater', bed: 'Bedroom', bath: 'Bathroom', gym: 'Home gym', play: 'Playroom', office: 'Office', bar: 'Kitchenette', store: 'Storage' };
  var SHARE = { family: 3, theater: 2.6, bed: 1.6, bath: 1, gym: 1.6, play: 1.8, office: 1.2, bar: 1.2, store: 1 };
  var COL = { family: '#f2b705', theater: '#ffd23f', bed: '#e9e5dc', bath: '#c9d6df', gym: '#f6c94a', play: '#ffe08a', office: '#d9d4c8', bar: '#f0d27a', store: '#bdb7aa' };
  var sq = pl.querySelector('[data-pl-sq]'), yr = pl.querySelector('[data-pl-yr]'), walk = pl.querySelector('[data-pl-walk]'), whole = pl.querySelector('[data-pl-whole]');
  var g = pl.querySelector('[data-sx-rooms]'), base = pl.querySelector('.sx-base'), dim = pl.querySelector('[data-sx-dim]');
  var fmt = function (n) { return n.toLocaleString('en-US'); };
  var prev = '';
  function list(a) { return a.length < 2 ? a.join('') : a.slice(0, -1).join(', ') + ' and ' + a[a.length - 1]; }
  function draw(rooms, s) {
    var key = rooms.join() + '|' + s; if (key === prev) return; prev = key;
    while (g.firstChild) g.removeChild(g.firstChild);
    var w = Math.round(420 * Math.sqrt(s / 3000)), x0 = 110, y = 222, h = 116;
    base.setAttribute('width', w); pl.style.setProperty('--bw', w);
    pl.querySelector('.sx-door').setAttribute('x', x0 + w - 8);
    pl.querySelector('.sx-dim path').setAttribute('d', 'M110 372H' + (x0 + w) + 'M110 364v16M' + (x0 + w) + ' 364v16');
    dim.setAttribute('x', x0 + w / 2); dim.textContent = fmt(s) + ' SQ FT';
    var tot = rooms.reduce(function (t, r) { return t + SHARE[r]; }, 0), x = x0 + 8, inner = w - 16;
    rooms.forEach(function (r, i) {
      var rw = inner * SHARE[r] / tot, grp = document.createElementNS(NS, 'g'); grp.setAttribute('class', 'sx-room'); grp.style.animationDelay = (i * 60) + 'ms';
      var re = document.createElementNS(NS, 'rect'); re.setAttribute('x', x); re.setAttribute('y', y); re.setAttribute('width', Math.max(4, rw - 2)); re.setAttribute('height', h); re.setAttribute('fill', COL[r]);
      grp.appendChild(re);
      if (rw > 44) { var t = document.createElementNS(NS, 'text'); t.setAttribute('x', x + rw / 2 - 1); t.setAttribute('y', y + h / 2 + 4); t.setAttribute('text-anchor', 'middle');
        t.textContent = rw > 70 ? NAMES[r] : NAMES[r].slice(0, 4) + '.'; grp.appendChild(t); }
      g.appendChild(grp); x += rw;
    });
  }
  function rule(name, ok, msg) { var li = pl.querySelector('[data-rule="' + name + '"]'); li.classList.toggle('no', !ok); pl.querySelector('[data-r-' + name + ']').textContent = msg; return ok; }
  function update() {
    var rooms = Array.prototype.map.call(pl.querySelectorAll('input[name="room"]:checked'), function (c) { return c.value; });
    var s = +sq.value, y = parseInt(yr.value, 10), w = walk.checked, wh = whole.checked;
    pl.querySelector('[data-pl-sqv]').textContent = fmt(s); pl.classList.toggle('walk', w);
    draw(rooms, s);
    var a = rule('size', s >= 500, s >= 500 ? fmt(s) + ' sq ft. Good to go.' : fmt(s) + ' sq ft. Basements need to be at least 500 sq ft.');
    var b = rule('year', !(y < 1975), isNaN(y) ? 'Enter the year your house was built.' : (y < 1975 ? 'Built ' + y + '. We are not currently taking on houses older than 1975.' : 'Built ' + y + '. Good to go.'));
    var c = rule('walk', !w || wh, !w ? 'No walkout planned.' : (wh ? 'Walkout with a full finish. Good to go.' : 'We only build walkouts when we are also finishing the whole basement.'));
    var names = rooms.map(function (r) { return NAMES[r].toLowerCase(); }); if (names[0]) names[0] = names[0].charAt(0).toUpperCase() + names[0].slice(1);
    var sum = rooms.length ? list(names) + ' in about ' + fmt(s) + ' sq ft' + (w ? ', with a walkout' : '') + '.' : 'Pick a few rooms to start your plan.';
    if (!(a && b && c)) sum += ' One of our rules doesn’t fit yet. Call us and we’ll talk it through.';
    pl.querySelector('[data-pl-sum]').textContent = sum;
  }
  pl.addEventListener('input', update); pl.addEventListener('change', update); update();
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
