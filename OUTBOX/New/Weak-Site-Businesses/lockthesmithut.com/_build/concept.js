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
