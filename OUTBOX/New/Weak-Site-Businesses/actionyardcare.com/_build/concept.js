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
