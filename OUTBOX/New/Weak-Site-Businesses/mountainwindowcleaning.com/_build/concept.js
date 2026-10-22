/* concept: (1) the hero glass: a canvas of hard-water haze and mineral spots over the valley photo; dragging squeegees it clear, one
   stroke plays on load, "Clean the glass" clears it all (and is the only motion under reduced motion). (2) the quote-page estimator: their
   published prices, a range where the price is a range, and the $150 visit minimum. Nothing is sent anywhere. */
(function () {
  var hero = document.querySelector('[data-glass]'); if (!hero) return;
  var cv = hero.querySelector('[data-haze]'), ctx = cv.getContext('2d'), reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var W = 0, H = 0, dpr = Math.min(2, window.devicePixelRatio || 1), seed = 7;
  function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
  function paint() {
    var r = hero.getBoundingClientRect(); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.globalCompositeOperation = 'source-over'; seed = 7;
    var x0 = W < 640 ? 0 : W * .38, g = ctx.createLinearGradient(x0, 0, W, H);
    g.addColorStop(0, 'rgba(226,236,240,0)'); g.addColorStop(.18, 'rgba(226,236,240,.5)'); g.addColorStop(1, 'rgba(214,226,232,.62)');
    ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
    for (var i = 0; i < Math.round(W * H / 2600); i++) {
      var x = x0 + rnd() * (W - x0), y = rnd() * H, s = 1.5 + rnd() * 6;
      ctx.beginPath(); ctx.arc(x, y, s, 0, 6.283); ctx.fillStyle = 'rgba(255,255,255,' + (.25 + rnd() * .45) + ')'; ctx.fill();
      ctx.lineWidth = .8; ctx.strokeStyle = 'rgba(170,150,120,' + (.18 + rnd() * .25) + ')'; ctx.stroke();
    }
    hero.classList.remove('clean');
  }
  var last = null, wiped = 0;
  function wipe(x, y) {
    ctx.globalCompositeOperation = 'destination-out'; ctx.lineCap = 'round'; ctx.lineJoin = 'round'; ctx.lineWidth = Math.max(70, Math.min(140, W * .08));
    ctx.beginPath(); ctx.moveTo(last ? last[0] : x, last ? last[1] : y); ctx.lineTo(x, y); ctx.stroke(); last = [x, y];
    if (++wiped > 40) hero.classList.add('clean');
  }
  function pos(e) { var r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; }
  var down = false;
  cv.addEventListener('pointerdown', function (e) { down = true; last = null; var p = pos(e); wipe(p[0], p[1]); });
  cv.addEventListener('pointermove', function (e) { if (!down && e.pointerType !== 'mouse') return; if (e.pointerType === 'mouse' && !down && e.buttons === 0) { var p = pos(e); if (last && Math.hypot(p[0] - last[0], p[1] - last[1]) > 120) last = null; wipe(p[0], p[1]); return; } var q = pos(e); wipe(q[0], q[1]); });
  window.addEventListener('pointerup', function () { down = false; last = null; });
  cv.addEventListener('pointerleave', function () { last = null; });
  hero.querySelector('[data-clean]').addEventListener('click', function () {
    if (hero.classList.contains('clean') && this.textContent === 'Fog it up again') { paint(); this.textContent = 'Clean the glass'; return; }
    if (reduce) { ctx.clearRect(0, 0, W, H); hero.classList.add('clean'); this.textContent = 'Fog it up again'; return; }
    var b = this, t0 = null, rows = 4;
    (function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 1600), row = Math.min(rows - 1, Math.floor(p * rows)), lp = p * rows - row;
      var y = H * (row + .5) / rows, x = row % 2 ? W * (1 - lp) : W * lp; if (lp < .03) last = null; wipe(x, y);
      if (p < 1) requestAnimationFrame(step); else { ctx.clearRect(0, 0, W, H); hero.classList.add('clean'); b.textContent = 'Fog it up again'; } })(performance.now());
  });
  paint();
  var rt; window.addEventListener('resize', function () { clearTimeout(rt); rt = setTimeout(function () { if (Math.abs(hero.getBoundingClientRect().width - W) > 40) paint(); }, 200); });
  if (!reduce) setTimeout(function () {
    var t0 = null, x1 = W < 640 ? W * .1 : W * .45, x2 = W * .95, y1 = H * .3, y2 = H * .52;
    (function step(t) { if (!t0) t0 = t; var p = Math.min(1, (t - t0) / 1100), e = p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
      wipe(x1 + (x2 - x1) * e, y1 + (y2 - y1) * e + Math.sin(e * 3.14) * -20); if (p < 1) requestAnimationFrame(step); else { last = null; wiped = 0; hero.classList.remove('clean'); } })(performance.now());
  }, 700);
})();

(function () {
  var es = document.querySelector('[data-est]'); if (!es) return;
  var NAMES = { ext: 'Outside windows', int: 'Inside windows', scr: 'Screens', trk: 'Window tracks', sol: 'Solar panels' };
  var CNT = { ext: 'panes', int: 'panes', scr: 'scr', trk: 'trk', sol: 'sol' };
  function n(k) { var i = es.querySelector('[data-cnt="' + k + '"] input'); return Math.max(0, Math.min(400, parseInt(i.value, 10) || 0)); }
  function money(v) { return '$' + Math.round(v).toLocaleString('en-US'); }
  function upd() {
    var lo = 0, hi = 0, lines = [], used = {};
    es.querySelectorAll('[data-es]').forEach(function (c) {
      var k = c.getAttribute('data-es'), q = n(CNT[k]); if (c.checked) used[CNT[k]] = 1;
      if (!c.checked || !q) return; var a = q * +c.getAttribute('data-lo'), b = q * +c.getAttribute('data-hi'); lo += a; hi += b;
      lines.push('<li><span>' + NAMES[k] + ' &times; ' + q + '</span><span>' + (a === b ? money(a) : money(a) + '&ndash;' + money(b)) + '</span></li>');
    });
    es.querySelectorAll('[data-cnt]').forEach(function (r) { r.classList.toggle('off', !used[r.getAttribute('data-cnt')]); });
    var min = 150, L = Math.max(lo, lo ? min : 0), Hh = Math.max(hi, hi ? min : 0);
    es.querySelector('[data-total]').textContent = !lo ? '$0' : (L === Hh ? money(L) : money(L) + '–' + money(Hh));
    es.querySelector('[data-range]').textContent = lo ? 'Estimate for a one-time clean' : 'Pick a service and add a count';
    es.querySelector('[data-lines]').innerHTML = lines.join('');
    es.querySelector('[data-min]').textContent = lo && lo < min ? 'Your total is below the $150 visit minimum, so the visit is $150.' : 'Every visit has a $150 minimum.';
  }
  es.addEventListener('click', function (e) {
    var b = e.target.closest('[data-inc],[data-dec]'); if (!b) return; var i = b.parentNode.querySelector('input');
    i.value = Math.max(0, Math.min(400, (parseInt(i.value, 10) || 0) + (b.hasAttribute('data-inc') ? 1 : -1))); upd();
  });
  es.addEventListener('input', upd); es.addEventListener('change', upd); upd();
})();
