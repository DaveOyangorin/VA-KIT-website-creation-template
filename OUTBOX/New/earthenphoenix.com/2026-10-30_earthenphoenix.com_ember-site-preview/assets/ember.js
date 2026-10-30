/* EMBER — site behaviour. The ember swarm itself lives in swarm.js. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches, root = document.documentElement, hasIO = 'IntersectionObserver' in window;
  var yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();
  requestAnimationFrame(function () { root.classList.add('ready'); });

  // ---------- header capsule ----------
  var cap = document.querySelector('.cap');
  function onScroll() { if (cap) cap.classList.toggle('on', scrollY > 40 || root.classList.contains('menu-open')); }
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // ---------- full-screen menu ----------
  var burger = document.querySelector('.burger'), menu = document.getElementById('menu');
  function setMenu(o) {
    root.classList.toggle('menu-open', o); root.classList.toggle('locked', o); burger.setAttribute('aria-expanded', String(o)); burger.querySelector('span').textContent = o ? 'Close' : 'Menu';
    menu.setAttribute('aria-hidden', String(!o)); if ('inert' in menu) menu.inert = !o;
    if (o) setTimeout(function () { var f = menu.querySelector('a'); if (f) f.focus({ preventScroll: true }); }, 250); onScroll();
  }
  if (burger && menu) {
    if ('inert' in menu) menu.inert = true;
    burger.addEventListener('click', function () { setMenu(!root.classList.contains('menu-open')); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); burger.focus(); } });
  }

  // ---------- page transition: an ember iris opens from the click ----------
  if (!reduce) {
    try { if (sessionStorage.getItem('ep-iris')) { sessionStorage.removeItem('ep-iris'); requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('came'); root.classList.remove('come'); }); }); } } catch (e) { root.classList.remove('come'); }
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]'); if (!a || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target || a.hasAttribute('download')) return;
      var u = new URL(a.href, location.href); if (u.origin !== location.origin || !/(\.html|\/)$/.test(u.pathname) || (u.pathname === location.pathname && u.hash)) return;
      e.preventDefault(); root.style.setProperty('--x', e.clientX + 'px'); root.style.setProperty('--y', e.clientY + 'px');
      root.classList.remove('came'); root.classList.add('go'); try { sessionStorage.setItem('ep-iris', '1'); } catch (er) {}
      setTimeout(function () { location.href = a.href; }, 640);
    });
    addEventListener('pageshow', function (e) { if (e.persisted) root.classList.remove('go', 'come', 'came'); });
  }

  // ---------- reveals ----------
  var rise = document.querySelectorAll('[data-rise]');
  if (hasIO && !reduce) { var io = new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }); }, { threshold: .15, rootMargin: '0px 0px -6% 0px' }); rise.forEach(function (el) { io.observe(el); }); }
  else rise.forEach(function (el) { el.classList.add('in'); });

  // headlines arrive word by word
  document.querySelectorAll('[data-split]').forEach(function (h) {
    var w = 0;
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (c) {
        if (c.nodeType === 3) {
          var frag = document.createDocumentFragment();
          c.textContent.split(/(\s+)/).forEach(function (part) {
            if (!part) return; if (/^\s+$/.test(part)) { frag.appendChild(document.createTextNode(part)); return; }
            var o = document.createElement('span'); o.className = 'split-word'; var i = document.createElement('span'); i.style.setProperty('--w', w++); i.textContent = part; o.appendChild(i); frag.appendChild(o);
          });
          node.replaceChild(frag, c);
        } else if (c.nodeType === 1 && c.tagName !== 'BR') walk(c);
      });
    })(h);
    h.setAttribute('aria-label', h.textContent.replace(/\s+/g, ' ').trim());
  });

  // ---------- ignite: words heat as you read ----------
  document.querySelectorAll('.ignite').forEach(function (p) {
    var hot = (p.dataset.hot || '').split('|');
    var words = p.textContent.trim().split(/\s+/); p.textContent = '';
    words.forEach(function (w, i) { var s = document.createElement('span'); s.className = 'w' + (hot.some(function (h) { return h && w.toLowerCase().indexOf(h) === 0; }) ? ' hot' : ''); s.textContent = w; p.appendChild(s); if (i < words.length - 1) p.appendChild(document.createTextNode(' ')); });
    if (reduce) return;
    var spans = p.querySelectorAll('.w');
    function upd() { var r = p.getBoundingClientRect(), f = (innerHeight * .82 - r.top) / (r.height + innerHeight * .35); var n = Math.round(Math.max(0, Math.min(1, f)) * spans.length); spans.forEach(function (s, i) { s.classList.toggle('lit', i < n); }); }
    addEventListener('scroll', upd, { passive: true }); upd();
  });

  // ---------- counters ----------
  document.querySelectorAll('[data-count]').forEach(function (b) {
    var to = +b.dataset.count, suf = b.dataset.suffix || ''; if (reduce || !hasIO) { b.textContent = to + suf; return; }
    var from = +(b.dataset.from || 0); b.textContent = from + suf;
    var o = new IntersectionObserver(function (es) { if (!es[0].isIntersecting) return; o.disconnect(); var t0 = performance.now();
      (function step(n) { var f = Math.min(1, (n - t0) / 1600), e = 1 - Math.pow(1 - f, 3); b.textContent = Math.round(from + (to - from) * e) + suf; if (f < 1) requestAnimationFrame(step); })(t0); }, { threshold: .6 });
    o.observe(b);
  });

  // ---------- gallery: drag to scroll ----------
  document.querySelectorAll('.strip').forEach(function (s) {
    var down = false, x0 = 0, l0 = 0, moved = 0;
    s.addEventListener('pointerdown', function (e) { if (e.pointerType !== 'mouse') return; down = true; moved = 0; x0 = e.clientX; l0 = s.scrollLeft; s.classList.add('drag'); });
    addEventListener('pointermove', function (e) { if (!down) return; moved = Math.abs(e.clientX - x0); s.scrollLeft = l0 - (e.clientX - x0); });
    addEventListener('pointerup', function () { down = false; s.classList.remove('drag'); });
    s.addEventListener('click', function (e) { if (moved > 6) e.preventDefault(); }, true);
  });

  // ---------- client words ----------
  document.querySelectorAll('.voices').forEach(function (v) {
    var qs = v.querySelectorAll('blockquote'), ticks = v.parentNode.querySelectorAll('.ticks button'), i = 0, tm;
    function show(n) {
      i = n; qs.forEach(function (q, j) { q.classList.toggle('on', j === n); q.setAttribute('aria-hidden', String(j !== n)); });
      ticks.forEach(function (t, j) { t.classList.remove('on', 'done'); if (j < n) t.classList.add('done'); }); if (ticks[n]) { void ticks[n].offsetWidth; ticks[n].classList.add('on'); }
      clearTimeout(tm); if (!reduce) tm = setTimeout(function () { show((i + 1) % qs.length); }, 7000);
    }
    ticks.forEach(function (t, j) { t.addEventListener('click', function () { show(j); }); });
    show(0);
  });

  // ---------- tarot deck: the four steps, one card at a time ----------
  var deck = document.querySelectorAll('.deck button');
  deck.forEach(function (c) { c.addEventListener('click', function () { var o = !c.classList.contains('on'); c.classList.toggle('on', o); c.setAttribute('aria-pressed', String(o)); }); });
  if (deck.length && hasIO && !reduce) { var dio = new IntersectionObserver(function (es) { if (!es[0].isIntersecting) return; dio.disconnect(); deck.forEach(function (c, i) { setTimeout(function () { c.click(); }, 500 + i * 650); }); }, { threshold: .5 }); dio.observe(deck[0].parentNode); }
  else deck.forEach(function (c) { c.classList.add('on'); c.setAttribute('aria-pressed', 'true'); });

  // ---------- readings cost: $2 a minute ----------
  var mins = document.getElementById('mins');
  if (mins) { var cost = document.getElementById('cost'), mo = document.getElementById('minsOut'); var up = function () { cost.textContent = '$' + mins.value * 2; mo.textContent = mins.value + ' minutes'; }; mins.addEventListener('input', up); up(); }

  // ---------- yoga: one price, split how you like ----------
  var ppl = document.querySelectorAll('[data-n]'), so = document.getElementById('splitOut');
  ppl.forEach(function (b) { b.addEventListener('click', function () { ppl.forEach(function (o) { o.setAttribute('aria-pressed', String(o === b)); }); var n = +b.dataset.n, each = 140 / n; so.textContent = n === 1 ? '$140 for your private hour' : '$140 shared by ' + n + ': about $' + (each % 1 ? each.toFixed(2) : each) + ' each'; }); });

  // ---------- Sarga: are you comfortable with deep pressure? ----------
  var ask = document.getElementById('comfort');
  if (ask) ask.querySelectorAll('button').forEach(function (b) { b.addEventListener('click', function () {
    ask.querySelectorAll('button').forEach(function (o) { o.setAttribute('aria-pressed', String(o === b)); });
    ask.querySelector('.ans').innerHTML = b.dataset.a === 'yes' ? 'Then Sarga may be right for you. <a class="uline" href="' + ask.dataset.book + '">Book 90 minutes</a>.' : 'Start gentler: <a class="uline" href="swedish-massage.html">Swedish massage</a> or <a class="uline" href="reiki.html">Reiki</a>, or <a class="uline" href="tel:+18016094263">call Miquelle</a> and ask.';
  }); });

  // ---------- contact form: writes the message into your own email or text app ----------
  var form = document.getElementById('note');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    var d = new FormData(form), name = (d.get('name') || '').trim(), reply = (d.get('reply') || '').trim(), msg = (d.get('message') || '').trim(), svc = d.get('service') || '', err = form.querySelector('.err');
    if (!name || !reply || !msg) { err.textContent = 'Please add your name, how to reach you, and a short message.'; (!name ? form.elements.name : !reply ? form.elements.reply : form.elements.message).focus(); return; }
    err.textContent = '';
    var body = 'Hi Miquelle,\n\n' + msg + '\n\n' + (svc ? 'Asking about: ' + svc + '\n' : '') + (d.get('first') ? 'This will be my first visit.\n' : '') + 'Reach me at: ' + reply + '\n\n' + name;
    form.querySelector('.sent').hidden = false;
    location.href = d.get('how') === 'text' ? 'sms:+18016094263?&body=' + encodeURIComponent(body) : 'mailto:info@earthenphoenix.com?subject=' + encodeURIComponent('Question from ' + name + (svc ? ' about ' + svc : '')) + '&body=' + encodeURIComponent(body);
  });
})();
