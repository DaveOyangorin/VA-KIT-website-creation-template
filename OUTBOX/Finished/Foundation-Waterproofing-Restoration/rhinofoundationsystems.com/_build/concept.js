/* concept: "Drive the pier". The depth gauge drives a helical pier down through the drawn soil layers; each layer shows Rhino's own
   description of that soil; past the frost line the pier bears, the house rotates back to level and the wall crack closes. */
(function () {
  var P = document.querySelector('[data-pierdemo]'); if (!P) return;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var r = P.querySelector('.pr-range'), house = P.querySelector('[data-house]'), pier = P.querySelector('[data-pier]'), tip = P.querySelector('[data-tip]'), shaft = P.querySelector('[data-shaft]');
  var status = P.querySelector('[data-status]'), meter = P.querySelector('[data-meter]'), tx = P.querySelectorAll('.pr-tx');
  var bounds = [232, 302, 382, 450, 9999], names = ['Loam', 'Silt', 'Clay', 'Sand', 'Below the frost line'];
  var TOP = 236, BOT = 548, FROST = 462, TILT = 2.4, cur = -1, bearing = null, touched = false, anim = null;
  var draw = function (v) {
    var y = TOP + (BOT - TOP) * v / 100, i = 0; while (y > bounds[i]) i++;
    var bear = y >= FROST, ang = bear ? 0 : TILT, drop = (517 - 210) * Math.tan(ang * Math.PI / 180);
    house.style.transform = 'rotate(' + ang + 'deg)';
    pier.setAttribute('transform', 'translate(0 ' + drop.toFixed(1) + ')');
    tip.setAttribute('transform', 'translate(0 ' + (y - drop).toFixed(1) + ')'); shaft.setAttribute('y2', (y - drop - 4).toFixed(1));
    if (i !== cur) { cur = i; P.dataset.layer = i; tx.forEach(function (t) { t.classList.toggle('on', +t.dataset.i === i); }); r.setAttribute('aria-valuetext', names[i]); }
    if (bear !== bearing) { bearing = bear; P.dataset.bearing = bear ? '1' : '0'; status.textContent = bear ? 'BEARING: LEVEL' : 'SETTLING'; meter.textContent = bear ? 'Bearing, level' : 'Settling'; }
  };
  var stop = function () { if (anim) cancelAnimationFrame(anim); anim = null; };
  var tween = function (to, dur) { stop(); var from = +r.value, t0 = performance.now();
    var step = function (t) { var k = Math.min(1, (t - t0) / dur); k = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2; r.value = from + (to - from) * k; draw(+r.value); if (k < 1) anim = requestAnimationFrame(step); };
    anim = requestAnimationFrame(step); };
  r.addEventListener('input', function () { touched = true; stop(); draw(+r.value); });
  draw(0);
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { io.disconnect(); setTimeout(function () { if (!touched) tween(100, 6500); }, 600); } }, { threshold: .45 });
    io.observe(P);
  }
})();
