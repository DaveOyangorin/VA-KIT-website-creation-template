/* concept: the breaker panel. Each breaker toggles its circuit and shows that job; the main lights every circuit. */
(function () {
  var p = document.querySelector('[data-panel]');
  if (!p) return;
  var brks = [].slice.call(p.querySelectorAll('.brk[data-b]')), main = p.querySelector('[data-main]'), loads = p.querySelectorAll('.ld'), idle = p.querySelector('[data-ld="idle"]');
  var show = function (k) { loads.forEach(function (l) { l.classList.toggle('on', l.getAttribute('data-ld') === String(k)); }); };
  var sync = function (last) {
    var any = brks.some(function (b) { return b.classList.contains('on'); });
    p.classList.toggle('lit', any); main.classList.toggle('on', brks.every(function (b) { return b.classList.contains('on'); })); main.setAttribute('aria-pressed', main.classList.contains('on') ? 'true' : 'false');
    if (!any) { show('idle'); return; }
    if (last != null && brks[last].classList.contains('on')) show(last);
    else { var on = brks.filter(function (b) { return b.classList.contains('on'); }); show(on[on.length - 1].getAttribute('data-b')); }
  };
  brks.forEach(function (b, i) { b.addEventListener('click', function () { b.classList.toggle('on'); b.setAttribute('aria-pressed', b.classList.contains('on') ? 'true' : 'false'); sync(i); }); });
  brks[0].classList.add('on'); brks[0].setAttribute('aria-pressed', 'true'); sync(0);  // start with one circuit live so the panel reads as interactive
  main.addEventListener('click', function () {
    var to = !main.classList.contains('on');
    brks.forEach(function (b) { b.classList.toggle('on', to); b.setAttribute('aria-pressed', to ? 'true' : 'false'); });
    sync(to ? 0 : null);
  });
})();
