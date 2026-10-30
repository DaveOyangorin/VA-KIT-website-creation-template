/* Earthen Phoenix, site-wide behaviour that ep.js (header, reveals, home motion) doesn't cover:
   the five-band page transition, the services menu, the contact form, the yoga split and the Sarga comfort check. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches, root = document.documentElement;

  // ---------- page transition ----------
  // Browsers with cross-document View Transitions use the CSS @view-transition rule; others get the five bands.
  var native = 'CSSViewTransitionRule' in window;
  var veil = document.querySelector('.veil');
  if (veil && !reduce && !native) {
    try { if (sessionStorage.getItem('ep-veil')) { sessionStorage.removeItem('ep-veil'); root.classList.add('arriving'); requestAnimationFrame(function () { requestAnimationFrame(function () { root.classList.add('arrived'); root.classList.remove('arriving'); }); }); } } catch (e) {}
    document.addEventListener('click', function (e) {
      var a = e.target.closest('a[href]'); if (!a || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target || a.hasAttribute('download')) return;
      var url = new URL(a.href, location.href); if (url.origin !== location.origin || !/\.html$|\/$/.test(url.pathname) || (url.pathname === location.pathname && url.hash)) return;
      e.preventDefault(); root.classList.remove('arrived'); root.classList.add('leaving');
      try { sessionStorage.setItem('ep-veil', '1'); } catch (er) {}
      setTimeout(function () { location.href = a.href; }, 700);
    });
    addEventListener('pageshow', function (e) { if (e.persisted) root.classList.remove('leaving', 'arriving', 'arrived'); });
  }

  // ---------- the first-visit cairn: stones settle one on another when it comes into view ----------
  var cairn = document.getElementById('cairn');
  if (cairn) { if (reduce || !('IntersectionObserver' in window)) cairn.classList.add('in'); else { var co = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { cairn.classList.add('in'); co.disconnect(); } }, { threshold: .4 }); co.observe(cairn); } }

  // ---------- services menu: one open at a time, closes on outside click or Escape ----------
  var dd = document.querySelector('.bar nav details');
  if (dd) {
    document.addEventListener('click', function (e) { if (dd.open && !dd.contains(e.target)) dd.open = false; });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && dd.open) { dd.open = false; dd.querySelector('summary').focus(); } });
  }

  // ---------- yoga: one price, split however the group likes ----------
  var people = document.querySelectorAll('.people button'), split = document.getElementById('splitOut');
  people.forEach(function (b) { b.addEventListener('click', function () {
    people.forEach(function (o) { o.setAttribute('aria-pressed', String(o === b)); });
    var n = +b.dataset.n, each = 140 / n;
    split.textContent = n === 1 ? '$140 for your private hour' : '$140 shared by ' + n + ': about $' + (Math.round(each * 100) / 100).toFixed(each % 1 ? 2 : 0) + ' each';
  }); });

  // ---------- Sarga: are you comfortable with deep pressure? ----------
  var ask = document.getElementById('comfort');
  if (ask) ask.querySelectorAll('button').forEach(function (b) { b.addEventListener('click', function () {
    var out = ask.querySelector('.ans');
    out.innerHTML = b.dataset.a === 'yes'
      ? 'Then Sarga may be for you. <a class="link" href="https://earthenphoenix.com/appointment-8682">Book a 90-minute session</a>'
      : 'Start with something gentler: <a class="link" href="swedish-massage.html">Swedish massage</a> or <a class="link" href="reiki.html">Reiki</a>. Or <a class="link" href="tel:+18016094263">call Miquelle</a> and ask.';
  }); });

  // ---------- contact form: no server needed; it writes the message into the visitor's own email or text app ----------
  var form = document.getElementById('note');
  if (form) {
    var err = form.querySelector('.err');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(form), name = (d.get('name') || '').trim(), reply = (d.get('reply') || '').trim(), msg = (d.get('message') || '').trim(), svc = d.get('service') || '', how = d.get('how') || 'email';
      if (!name || !reply || !msg) { err.textContent = 'Please add your name, how to reach you, and a short message.'; (!name ? form.name : !reply ? form.reply : form.message).focus(); return; }
      err.textContent = '';
      var body = 'Hi Miquelle,\n\n' + msg + '\n\n' + (svc ? 'Interested in: ' + svc + '\n' : '') + (d.get('first') ? 'This is my first visit.\n' : '') + 'Best way to reach me: ' + reply + '\n\n' + name;
      if (how === 'text') location.href = 'sms:+18016094263?&body=' + encodeURIComponent(body);
      else location.href = 'mailto:info@earthenphoenix.com?subject=' + encodeURIComponent('Question from ' + name + (svc ? ' about ' + svc : '')) + '&body=' + encodeURIComponent(body);
      form.querySelector('.sent').hidden = false;
    });
  }
})();
