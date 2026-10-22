/* concept: Plan your basement. Chosen rooms are laid into the basement of the section drawing (widths follow a rough share of the floor),
   the dimension line shows the size, and RWK's three project rules are checked live. Works without motion; nothing is sent anywhere. */
(function () {
  var pl = document.querySelector('[data-planner]'); if (!pl) return;
  var NS = 'http://www.w3.org/2000/svg';
  var NAMES = { family: 'Family room', theater: 'Theater', bed: 'Bedroom', bath: 'Bathroom', gym: 'Home gym', play: 'Playroom', office: 'Office', bar: 'Kitchenette', store: 'Storage' };
  var SHARE = { family: 3, theater: 2.6, bed: 1.6, bath: 1, gym: 1.6, play: 1.8, office: 1.2, bar: 1.2, store: 1 };
  var COL = { family: '#f2b705', theater: '#ffd23f', bed: '#e9e5dc', bath: '#c9d6df', gym: '#f6c94a', play: '#ffe08a', office: '#d9d4c8', bar: '#f0d27a', store: '#bdb7aa' };
  var sq = pl.querySelector('[data-pl-sq]'), yr = pl.querySelector('[data-pl-yr]'), walk = pl.querySelector('[data-pl-walk]'), whole = pl.querySelector('[data-pl-whole]');
  var g = pl.querySelector('[data-sx-rooms]'), base = pl.querySelector('.sx-base'), dim = pl.querySelector('[data-sx-dim]');
  var fmt = function (n) { return n.toLocaleString('en-US'); };
  var prev = '';
  function list(a) { return a.length < 2 ? a.join('') : a.slice(0, -1).join(', ') + ' and ' + a[a.length - 1]; }
  function draw(rooms, s) {
    var key = rooms.join() + '|' + s; if (key === prev) return; prev = key;
    while (g.firstChild) g.removeChild(g.firstChild);
    var w = Math.round(420 * Math.sqrt(s / 3000)), x0 = 110, y = 222, h = 116;
    base.setAttribute('width', w); pl.style.setProperty('--bw', w);
    pl.querySelector('.sx-door').setAttribute('x', x0 + w - 8);
    pl.querySelector('.sx-dim path').setAttribute('d', 'M110 372H' + (x0 + w) + 'M110 364v16M' + (x0 + w) + ' 364v16');
    dim.setAttribute('x', x0 + w / 2); dim.textContent = fmt(s) + ' SQ FT';
    var tot = rooms.reduce(function (t, r) { return t + SHARE[r]; }, 0), x = x0 + 8, inner = w - 16;
    rooms.forEach(function (r, i) {
      var rw = inner * SHARE[r] / tot, grp = document.createElementNS(NS, 'g'); grp.setAttribute('class', 'sx-room'); grp.style.animationDelay = (i * 60) + 'ms';
      var re = document.createElementNS(NS, 'rect'); re.setAttribute('x', x); re.setAttribute('y', y); re.setAttribute('width', Math.max(4, rw - 2)); re.setAttribute('height', h); re.setAttribute('fill', COL[r]);
      grp.appendChild(re);
      if (rw > 44) { var t = document.createElementNS(NS, 'text'); t.setAttribute('x', x + rw / 2 - 1); t.setAttribute('y', y + h / 2 + 4); t.setAttribute('text-anchor', 'middle');
        t.textContent = rw > 70 ? NAMES[r] : NAMES[r].slice(0, 4) + '.'; grp.appendChild(t); }
      g.appendChild(grp); x += rw;
    });
  }
  function rule(name, ok, msg) { var li = pl.querySelector('[data-rule="' + name + '"]'); li.classList.toggle('no', !ok); pl.querySelector('[data-r-' + name + ']').textContent = msg; return ok; }
  function update() {
    var rooms = Array.prototype.map.call(pl.querySelectorAll('input[name="room"]:checked'), function (c) { return c.value; });
    var s = +sq.value, y = parseInt(yr.value, 10), w = walk.checked, wh = whole.checked;
    pl.querySelector('[data-pl-sqv]').textContent = fmt(s); pl.classList.toggle('walk', w);
    draw(rooms, s);
    var a = rule('size', s >= 500, s >= 500 ? fmt(s) + ' sq ft. Good to go.' : fmt(s) + ' sq ft. Basements need to be at least 500 sq ft.');
    var b = rule('year', !(y < 1975), isNaN(y) ? 'Enter the year your house was built.' : (y < 1975 ? 'Built ' + y + '. We are not currently taking on houses older than 1975.' : 'Built ' + y + '. Good to go.'));
    var c = rule('walk', !w || wh, !w ? 'No walkout planned.' : (wh ? 'Walkout with a full finish. Good to go.' : 'We only build walkouts when we are also finishing the whole basement.'));
    var names = rooms.map(function (r) { return NAMES[r].toLowerCase(); }); if (names[0]) names[0] = names[0].charAt(0).toUpperCase() + names[0].slice(1);
    var sum = rooms.length ? list(names) + ' in about ' + fmt(s) + ' sq ft' + (w ? ', with a walkout' : '') + '.' : 'Pick a few rooms to start your plan.';
    if (!(a && b && c)) sum += ' One of our rules doesn’t fit yet. Call us and we’ll talk it through.';
    pl.querySelector('[data-pl-sum]').textContent = sum;
  }
  pl.addEventListener('input', update); pl.addEventListener('change', update); update();
})();
