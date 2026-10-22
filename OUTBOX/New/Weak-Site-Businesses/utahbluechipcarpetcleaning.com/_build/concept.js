/* concept: tap-your-rooms floor plan. Each room is a keyboard-operable checkbox; the count (1-10, hallway included) looks up Blue Chip's
   published online price, adds a duct package and pet treatment, and points the book button at the matching package page. Nothing is sent. */
(function () {
  var SLUG = ['1-room-and-hallway', '2-rooms-and-hallway', '3-rooms-and-hallway', '4-rooms-and-hallway', '5-rooms-and-hallway', '6-rooms-and-hallway', '7-rooms-and-hallway', '8-rooms-and-hallway', '9-rooms-and-hallway', '10-rooms-and-hallway'];
  document.querySelectorAll('[data-plan]').forEach(function (pl) {
    var prices = pl.getAttribute('data-prices').split(',').map(Number), rooms = pl.querySelectorAll('[data-room]'), book = pl.querySelector('[data-book]');
    var h0 = book.getAttribute('href'), base = h0.slice(0, h0.indexOf('booking-calendar/') + 17), suf = /index\.html$/.test(h0) ? '/index.html' : '';
    function m(v) { return '$' + v.toFixed(2); }
    function upd() {
      var n = Array.prototype.filter.call(rooms, function (r) { return r.getAttribute('aria-checked') === 'true'; }).length;
      var c = n ? prices[n - 1] : 0, d = +pl.querySelector('[data-duct]').value, p = pl.querySelector('[data-pet]').checked ? 100 : 0;
      pl.querySelector('[data-n]').textContent = n; pl.querySelector('[data-carpet]').textContent = n ? m(c) : '$0.00';
      pl.querySelector('[data-total]').textContent = m(c + d + p);
      book.hidden = !n; if (n) book.setAttribute('href', base + SLUG[n - 1] + suf);
    }
    function tog(r) { r.setAttribute('aria-checked', r.getAttribute('aria-checked') === 'true' ? 'false' : 'true'); upd(); }
    rooms.forEach(function (r) {
      r.addEventListener('click', function () { tog(r); });
      r.addEventListener('keydown', function (e) { if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); tog(r); } });
    });
    pl.addEventListener('change', upd); upd();
  });
})();
