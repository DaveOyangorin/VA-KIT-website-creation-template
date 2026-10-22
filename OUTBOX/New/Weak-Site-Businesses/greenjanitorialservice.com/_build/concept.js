/* concept: the service finder. Two chip groups (space, kind of clean); the card lists the GJS services that fit, in their own words,
   each linking to its service page. Nothing is sent anywhere. */
(function () {
  var f = document.querySelector('[data-finder]'); if (!f) return;
  var data = JSON.parse(f.querySelector('[data-fd-data]').textContent);
  var list = f.querySelector('[data-fd-list]'), head = f.querySelector('[data-fd-h]');
  var sp = Array.prototype.slice.call(f.querySelectorAll('[data-sp]')), nd = Array.prototype.slice.call(f.querySelectorAll('[data-nd]'));
  function cur(g, a) { var b = g.filter(function (x) { return x.getAttribute('aria-pressed') === 'true'; })[0]; return b.getAttribute(a); }
  function draw() {
    var s = cur(sp, 'data-sp'), n = cur(nd, 'data-nd');
    var ks = data.m[s + '|' + n] || [];
    head.textContent = sp.filter(function (x) { return x.getAttribute('data-sp') === s; })[0].textContent + ' · ' + nd.filter(function (x) { return x.getAttribute('data-nd') === n; })[0].textContent;
    list.innerHTML = ks.map(function (k) { var v = data.sv[k]; return '<a class="fd-i" href="' + v.href + '"><b>' + v.t + '</b><span>' + v.d + '</span></a>'; }).join('');
  }
  [sp, nd].forEach(function (g) {
    g.forEach(function (b) { b.addEventListener('click', function () { g.forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); }); draw(); }); });
  });
  draw();
})();
