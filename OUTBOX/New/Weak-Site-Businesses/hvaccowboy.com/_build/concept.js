/* concept: the homeowner / business switch. Flipping it sets data-mode on the page wrapper (CSS shows the matching headline, services,
   job photos), and fills the quote form's "Homeowner or business" field. The choice is remembered for this visitor only. */
(function () {
  var c = document.querySelector('[data-crew]'); if (!c) return;
  var btns = Array.prototype.slice.call(c.querySelectorAll('[data-set]'));
  function set(m, save) {
    c.setAttribute('data-mode', m);
    btns.forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-set') === m ? 'true' : 'false'); });
    var f = document.getElementById('f-type'); if (f) f.value = m === 'biz' ? 'Business' : 'Homeowner';
    if (save) { try { localStorage.setItem('cowboy-mode', m); } catch (e) {} }
  }
  btns.forEach(function (b) { b.addEventListener('click', function () { set(b.getAttribute('data-set'), true); }); });
  var saved = null; try { saved = localStorage.getItem('cowboy-mode'); } catch (e) {}
  set(saved === 'biz' ? 'biz' : 'home', false);
})();
