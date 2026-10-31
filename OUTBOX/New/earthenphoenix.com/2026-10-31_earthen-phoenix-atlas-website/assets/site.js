/* THE EARTHEN ATLAS — page behaviour: header, menu, survey-line page transition, reveals, pinned atlas, trail, small tools. */
(() => {
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches, html = document.documentElement, $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();

  // header: transparent over photo headers, paper once scrolled
  const hdr = $('.hdr'), onScroll = () => hdr.classList.toggle('scrolled', scrollY > 30);
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  // menu: full-screen panel that starts below the header; page locked while open
  const burger = $('.burger'), menu = $('#menu');
  const setMenu = open => { burger.setAttribute('aria-expanded', open); menu.setAttribute('aria-hidden', !open); menu.inert = !open; html.classList.toggle('menu-open', open); if (open) $('a', menu).focus({ preventScroll: true }); };
  menu.inert = true;
  burger.addEventListener('click', () => setMenu(burger.getAttribute('aria-expanded') !== 'true'));
  addEventListener('keydown', e => { if (e.key === 'Escape' && html.classList.contains('menu-open')) { setMenu(false); burger.focus(); } });
  const mq = matchMedia('(min-width: 1101px)'); mq.addEventListener('change', () => mq.matches && setMenu(false));

  // page transition: survey lines sweep across, then the next page draws them back
  addEventListener('pageshow', e => { if (e.persisted) html.classList.remove('leaving', 'arriving'); });
  if (html.classList.contains('arriving')) requestAnimationFrame(() => setTimeout(() => html.classList.remove('arriving'), 30));
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href]'); if (!a || RM || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || a.target) return;
    const u = new URL(a.href, location.href); if (u.origin !== location.origin || !/\.html$/.test(u.pathname) || (u.pathname === location.pathname && u.hash)) return;
    e.preventDefault(); html.classList.add('leaving'); try { sessionStorage.setItem('ep-atlas', '1'); } catch (_) { }
    setTimeout(() => { location.href = a.href; }, 560);
  });

  // headline words rise; blocks reveal as they enter
  $$('[data-split]').forEach(h => {
    const walk = n => [...n.childNodes].forEach(c => {
      if (c.nodeType === 3) { const f = document.createDocumentFragment(); c.textContent.split(/(\s+)/).forEach(w => { if (!w) return; if (/^\s+$/.test(w)) f.append(w); else { const s = document.createElement('span'); s.className = 'w'; s.innerHTML = '<span></span>'; s.firstChild.textContent = w; f.append(s); } }); c.replaceWith(f); }
      else if (c.nodeType === 1 && c.tagName !== 'BR') walk(c);
    });
    walk(h); $$('.w > span', h).forEach((s, i) => s.style.transitionDelay = Math.min(i * 45 + 120, 900) + 'ms');
  });
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
  $$('[data-r],[data-split],.reveal-img,.route').forEach(el => io.observe(el));

  // scroll-linked: hero grounds as you leave it; pinned atlas runs sideways; trail draws; photos drift
  const heroT = $('.hero [data-terrain]'), atlas = $('.atlas'), track = atlas && $('.atlas-track', atlas), trail = $('.trail path.draw'), par = $$('[data-par]');
  const wide = matchMedia('(min-width: 900px)');
  function sizeAtlas() { if (!atlas) return; if (wide.matches && !RM) { atlas.style.height = (track.scrollWidth - innerWidth + innerHeight) + 'px'; atlas.classList.add('pinned'); } else { atlas.style.height = ''; atlas.classList.remove('pinned'); track.style.transform = ''; } }
  function frame() {
    if (heroT && heroT.terrain) heroT.terrain.sp = Math.min(1, Math.max(0, scrollY / (innerHeight * .8)));
    if (atlas && atlas.classList.contains('pinned')) {
      const r = atlas.getBoundingClientRect(), max = track.scrollWidth - innerWidth, p = Math.min(1, Math.max(0, -r.top / (r.height - innerHeight)));
      track.style.transform = `translate3d(${-p * max}px,0,0)`; atlas.style.setProperty('--p', p);
    }
    if (trail) { const r = trail.closest('svg').getBoundingClientRect(), p = Math.min(1, Math.max(0, (innerHeight * .95 - r.top) / (r.height + innerHeight * .3))); trail.style.strokeDashoffset = 1 - p; trail.closest('.trail').style.setProperty('--p', p); }
    if (!RM) par.forEach(el => { if (!wide.matches) { el.style.transform = ''; return; } const r = el.getBoundingClientRect(); el.style.transform = `translate3d(0,${((r.top + r.height / 2 - innerHeight / 2) * -(+el.dataset.par || .08)).toFixed(1)}px,0)`; });
  }
  let tick = false; addEventListener('scroll', () => { if (!tick) { tick = true; requestAnimationFrame(() => { frame(); tick = false; }); } }, { passive: true });
  addEventListener('resize', () => { sizeAtlas(); frame(); }); addEventListener('load', () => { sizeAtlas(); frame(); }); sizeAtlas(); frame();

  // client words: one at a time, paced slowly, pausable
  const vs = $('.voices'); if (vs) {
    const qs = $$('blockquote', vs), bs = $$('.vnav button'); let i = 0, hold = false;
    const show = n => { i = (n + qs.length) % qs.length; qs.forEach((q, j) => q.classList.toggle('on', j === i)); bs.forEach((b, j) => b.setAttribute('aria-current', j === i)); };
    bs.forEach((b, j) => b.addEventListener('click', () => show(j))); show(0);
    vs.addEventListener('mouseenter', () => hold = true); vs.addEventListener('mouseleave', () => hold = false); vs.addEventListener('focusin', () => hold = true);
    if (!RM) setInterval(() => { if (!hold) show(i + 1); }, 7000);
  }

  // deep tissue: depth slider label
  const depth = $('#depth'), dOut = $('#depthOut'); if (depth) { const f = () => dOut.textContent = ['Light', 'Medium', 'Deep'][depth.value]; depth.addEventListener('input', f); f(); }

  // astrology: birthday → sun sign, drawn in the sky
  const mo = $('#month'), da = $('#day'); if (mo) {
    const cut = [[1, 20, 'Capricorn', 'Aquarius'], [2, 19, 'Aquarius', 'Pisces'], [3, 21, 'Pisces', 'Aries'], [4, 20, 'Aries', 'Taurus'], [5, 21, 'Taurus', 'Gemini'], [6, 21, 'Gemini', 'Cancer'], [7, 23, 'Cancer', 'Leo'], [8, 23, 'Leo', 'Virgo'], [9, 23, 'Virgo', 'Libra'], [10, 23, 'Libra', 'Scorpio'], [11, 22, 'Scorpio', 'Sagittarius'], [12, 22, 'Sagittarius', 'Capricorn']];
    const days = () => { const n = new Date(2024, +mo.value, 0).getDate(), v = +da.value || 1; da.innerHTML = Array.from({ length: n }, (_, j) => `<option${j + 1 === Math.min(v, n) ? ' selected' : ''}>${j + 1}</option>`).join(''); };
    const sign = () => { const [, d, a, b] = cut[mo.value - 1], s = +da.value < d ? a : b, T = $('#t-astro')?.terrain; if (T) { T.p.sign = s; if (RM) { for (let k = 0; k < 90; k++) T.step(1 / 30); T.draw(); } } $('#signOut').textContent = 'Your sun sign: ' + s + '.'; };
    mo.value = 11; days(); da.value = 8; mo.addEventListener('change', () => { days(); sign(); }); da.addEventListener('change', sign); sign();
  }
  // readings: length → cost at $2 a minute
  $$('[data-mins]').forEach(b => b.addEventListener('click', () => { $$('[data-mins]').forEach(o => o.setAttribute('aria-pressed', o === b)); $('#cost').textContent = '$' + (b.dataset.mins * 2); $('#costNote').textContent = b.dataset.mins + ' minutes at $2 a minute'; }));
  // yoga: one price, shared
  const ppl = $('#people'); if (ppl) { const f = () => { const n = +ppl.value; $('#peopleOut').textContent = n === 1 ? 'Just you' : n + ' people'; $('#share').textContent = n === 1 ? '$140 for your private hour' : '$140 shared · about $' + (140 / n).toFixed(2).replace('.00', '') + ' each'; }; ppl.addEventListener('input', f); f(); }

  // contact: compose the note in the visitor's own email or text app (nothing stored here)
  const f = $('#note'); if (f) f.addEventListener('submit', e => {
    e.preventDefault(); const d = new FormData(f), err = $('.err', f), name = (d.get('name') || '').trim(), reply = (d.get('reply') || '').trim(), msg = (d.get('message') || '').trim();
    if (!name || !reply || !msg) { err.textContent = 'Please add your name, a way to reply and a message.'; (!name ? f.name : !reply ? f.reply : f.message).focus(); return; }
    err.textContent = ''; const body = `${msg}\n\n${d.get('service') ? 'Asking about: ' + d.get('service') + '\n' : ''}${d.get('first') ? 'This will be my first visit.\n' : ''}— ${name} (${reply})`;
    location.href = d.get('how') === 'text' ? 'sms:+18016094263?&body=' + encodeURIComponent(body) : 'mailto:info@earthenphoenix.com?subject=' + encodeURIComponent('A note from ' + name) + '&body=' + encodeURIComponent(body);
    $('.sent', f).hidden = false;
  });
})();
