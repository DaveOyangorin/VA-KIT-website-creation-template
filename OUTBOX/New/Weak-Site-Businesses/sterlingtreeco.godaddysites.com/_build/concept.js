/* concept: the tree check. ISA's tree risk checklist as yes/no buttons; a "yes" lights the matching zone of the drawn tree (canopy,
   branch unions, trunk, roots and site). Any yes shows ISA's advice to have the tree examined by an ISA Certified Arborist and the ways
   an arborist may manage the risk. Nothing is sent anywhere. */
(function () {
  var c = document.querySelector('[data-tc]'); if (!c) return;
  var btns = Array.prototype.slice.call(c.querySelectorAll('[data-q]'));
  var ans = {}, zones = {};
  var yesN = c.querySelector('[data-tc-yes]'), ansN = c.querySelector('[data-tc-ans]');
  var h = c.querySelector('[data-tc-h]'), p = c.querySelector('[data-tc-p]'), more = c.querySelector('[data-tc-more]');
  var total = btns.length / 2;
  function draw() {
    var keys = Object.keys(ans), yes = keys.filter(function (k) { return ans[k].v === 'yes'; });
    yesN.textContent = yes.length; ansN.textContent = keys.length;
    var lit = {}; yes.forEach(function (k) { lit[ans[k].z] = 1; });
    ['canopy', 'union', 'trunk', 'roots'].forEach(function (z) {
      var g = c.querySelector('.z-' + z), t = c.querySelector('.t-' + z);
      if (g) g.classList.toggle('on', !!lit[z]); if (t) t.classList.toggle('on', !!lit[z]);
    });
    if (yes.length) {
      h.textContent = yes.length === 1 ? 'One sign worth a closer look' : yes.length + ' signs worth a closer look';
      p.textContent = 'ISA’s advice: if you answered yes to any question on the checklist, your tree should be examined by an ISA Certified Arborist.';
      more.hidden = false;
    } else if (keys.length === total) {
      h.textContent = 'No warning signs flagged';
      p.textContent = 'Good news. Mature trees still benefit from routine care, and regular care by an ISA Certified Arborist is a chance to catch defects early.';
      more.hidden = true;
    } else {
      h.textContent = keys.length ? 'Keep going' : 'Answer the questions above';
      p.textContent = 'Look at one tree at a time. Based on the ISA’s tree risk checklist.';
      more.hidden = true;
    }
  }
  btns.forEach(function (b) {
    b.addEventListener('click', function () {
      var q = b.getAttribute('data-q');
      btns.filter(function (x) { return x.getAttribute('data-q') === q; }).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      ans[q] = { v: b.getAttribute('data-v'), z: b.getAttribute('data-z') };
      draw();
    });
  });
  draw();
})();
