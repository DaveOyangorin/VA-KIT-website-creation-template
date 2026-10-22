/* concept: the work-order tool (product + symptom -> printed ticket -> pre-filled booking form), reviews, service-area counties. */
(function () {
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var dg = document.querySelector('[data-diag]');
  if (dg) {
    var tabs = dg.querySelectorAll('.dg-tab'), groups = dg.querySelectorAll('.dg-sy'), paper = dg.querySelector('[data-tk]');
    var outApp = dg.querySelector('[data-tk-app]'), outSym = dg.querySelector('[data-tk-sym]'), state = { app: tabs[0].textContent, key: tabs[0].getAttribute('data-app'), sym: '' };
    var print = function () { if (reduce) return; paper.classList.remove('tk-pr'); void paper.offsetWidth; paper.classList.add('tk-pr'); };
    var render = function () { outApp.textContent = state.app; outSym.textContent = state.sym || 'Pick a symptom'; outSym.classList.toggle('empty', !state.sym); print(); };
    var pickApp = function (t) {
      tabs.forEach(function (x) { x.classList.toggle('on', x === t); x.setAttribute('aria-pressed', x === t ? 'true' : 'false'); });
      state.app = t.textContent; state.key = t.getAttribute('data-app'); state.sym = '';
      groups.forEach(function (g) { g.classList.toggle('on', g.getAttribute('data-for') === state.key); g.querySelectorAll('button').forEach(function (b) { b.classList.remove('on'); }); });
      render();
    };
    tabs.forEach(function (t) { t.addEventListener('click', function () { pickApp(t); }); });
    groups.forEach(function (g) { g.querySelectorAll('button').forEach(function (b) { b.addEventListener('click', function () { g.querySelectorAll('button').forEach(function (x) { x.classList.toggle('on', x === b); }); state.sym = b.getAttribute('data-sym'); render(); }); }); });
    render(); outSym.classList.add('empty');
    var fromHash = function () { var h = (location.hash || '').replace('#fix-', ''); if (!h || h === location.hash) return; var t = dg.querySelector('.dg-tab[data-app="' + h + '"]'); if (t) { pickApp(t); var sec = document.getElementById('diagnose'); if (sec) sec.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' }); } };
    window.addEventListener('hashchange', fromHash); fromHash();
    var book = dg.querySelector('[data-tk-book]');
    if (book) book.addEventListener('click', function () {
      var sel = document.querySelector('[data-prod]'), msg = document.querySelector('[data-msg]'), form = document.querySelector('#book .form');
      if (sel) [].forEach.call(sel.options, function (o) { if (o.textContent.toLowerCase().indexOf(state.app.toLowerCase().replace('television', 'television')) === 0) sel.value = o.value; });
      if (sel && state.key === 'tv') [].forEach.call(sel.options, function (o) { if (/^Television/.test(o.textContent)) sel.value = o.value; });
      if (msg && state.sym) msg.value = state.app + ': ' + state.sym.toLowerCase() + '.';
      if (form && !reduce) { form.classList.remove('flash'); void form.offsetWidth; form.classList.add('flash'); }
    });
  }
  var qs = document.querySelector('[data-quotes]');
  if (qs) {
    var q = qs.querySelectorAll('.q'), n = qs.querySelector('[data-q-n]'), i = 0;
    var go = function (k) { i = (k + q.length) % q.length; q.forEach(function (x, j) { x.classList.toggle('on', j === i); }); n.textContent = (i + 1) + ' / ' + q.length; };
    qs.querySelector('[data-q-prev]').addEventListener('click', function () { go(i - 1); }); qs.querySelector('[data-q-next]').addEventListener('click', function () { go(i + 1); });
  }
  var ar = document.querySelector('[data-area]');
  if (ar) {
    var at = ar.querySelectorAll('.ar-tab'), al = ar.querySelectorAll('.ar-list');
    at.forEach(function (t) { t.addEventListener('click', function () { var c = t.getAttribute('data-c'); at.forEach(function (x) { x.classList.toggle('on', x === t); }); al.forEach(function (l) { l.classList.toggle('on', l.getAttribute('data-cl') === c); }); }); });
  }
})();
