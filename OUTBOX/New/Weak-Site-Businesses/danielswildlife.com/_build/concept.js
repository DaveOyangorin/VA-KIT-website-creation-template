/* concept: the clue matcher. Tick signs; each animal or service scores one point per matching sign (signs taken from Daniel's own service
   pages); the list ranks them, best match first, with a job photo, the page's own description and a link. Nothing is sent anywhere. */
(function () {
  var c = document.querySelector('[data-cm]'); if (!c) return;
  var d = JSON.parse(c.querySelector('[data-cm-data]').textContent);
  var boxes = Array.prototype.slice.call(c.querySelectorAll('.clue input'));
  var list = c.querySelector('[data-cm-list]'), empty = c.querySelector('[data-cm-empty]');
  function draw() {
    var on = boxes.filter(function (b) { return b.checked; }).map(function (b) { return b.value; });
    if (!on.length) { list.innerHTML = ''; empty.hidden = false; return; }
    var res = Object.keys(d.match).map(function (k) {
      var hit = d.match[k].filter(function (s) { return on.indexOf(s) >= 0; }).length;
      return { k: k, hit: hit };
    }).filter(function (r) { return r.hit > 0; }).sort(function (a, b) { return b.hit - a.hit; }).slice(0, 4);
    empty.hidden = true;
    list.innerHTML = '';
    res.forEach(function (r, i) {
      var li = document.createElement('li'); li.className = 'cm-i' + (i === 0 ? ' is-top' : '');
      var t = c.querySelector('template[data-img="' + r.k + '"]');
      var a = document.createElement('a'); a.href = d.href[r.k];
      if (t) a.appendChild(t.content.cloneNode(true));
      var box = document.createElement('div');
      box.innerHTML = '<span class="note">' + r.hit + ' of your ' + on.length + ' sign' + (on.length > 1 ? 's' : '') + '</span><b>' + d.label[r.k] + '</b><p></p><em>See how Daniel handles it →</em>';
      box.querySelector('p').textContent = d.why[r.k];
      a.appendChild(box); li.appendChild(a); list.appendChild(li);
    });
  }
  boxes.forEach(function (b) { b.addEventListener('change', draw); });
  c.querySelector('[data-cm-reset]').addEventListener('click', function () { boxes.forEach(function (b) { b.checked = false; }); draw(); });
  draw();
})();
