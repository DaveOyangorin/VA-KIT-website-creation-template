/* Novarte VA - the assistant's app. Plain JS, no libraries; it only talks to its own server. */
(function () {
  'use strict';
  var TOKEN = (document.querySelector('meta[name="va-token"]') || {}).content || '';
  var S = { data: null, tab: 'tasks', busy: false, form: {}, open: {}, photos: {} };
  var TABS = [
    { key: 'tasks', label: 'My tasks' },
    { key: 'time', label: 'My time' },
    { key: 'drafts', label: 'My drafts' }
  ];

  /* ------------------------------------------------------------ tiny helpers */
  function h(tag, attrs) {
    var el = document.createElement(tag);
    attrs = attrs || {};
    Object.keys(attrs).forEach(function (k) {
      var v = attrs[k];
      if (v === null || v === undefined) return;
      if (k === 'text') { el.textContent = v; return; }
      if (k.slice(0, 2) === 'on' && typeof v === 'function') { el.addEventListener(k.slice(2), v); return; }
      el.setAttribute(k, v);
    });
    for (var i = 2; i < arguments.length; i++) add(el, arguments[i]);
    return el;
  }
  function add(el, kid) {
    if (kid === null || kid === undefined || kid === false) return;
    if (Array.isArray(kid)) { kid.forEach(function (k) { add(el, k); }); return; }
    el.appendChild(kid.nodeType ? kid : document.createTextNode(String(kid)));
  }
  function clear(el) { while (el.firstChild) el.removeChild(el.firstChild); return el; }
  function toast(msg, bad) {
    var t = document.getElementById('toast');
    t.textContent = msg; t.className = 'toast' + (bad ? ' bad' : ''); t.hidden = false;
    clearTimeout(toast.t); toast.t = setTimeout(function () { t.hidden = true; }, 3500);
  }
  function hrs(n) { return String(Math.round(Number(n || 0) * 100) / 100); }
  function when(iso) {
    if (!iso) return '';
    var d = new Date(iso); if (isNaN(d)) return String(iso).slice(0, 16);
    return d.toLocaleString(undefined, { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' });
  }
  function size(b) { return b > 1048576 ? (b / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(b / 1024)) + ' KB'; }
  function get(path) { return fetch(path, { headers: { Accept: 'application/json' } }).then(function (r) { return r.json(); }); }
  function post(path, body) {
    return fetch(path, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-VA-Token': TOKEN, Accept: 'application/json' },
      body: JSON.stringify(body || {})
    }).then(function (r) { return r.json().then(function (j) { return { ok: r.ok, data: j }; }); });
  }

  /* ---------------------------------------------------------------- loading */
  function load() {
    return get('/api/state').then(function (d) {
      if (d && d.error) { toast(d.error, true); return; }
      S.data = d; render();
    }).catch(function () { toast('The app is not running. Close the window and start it again.', true); });
  }

  /* ----------------------------------------------------------------- render */
  function render() {
    var tabs = clear(document.getElementById('tabs'));
    TABS.forEach(function (t) {
      tabs.appendChild(h('button', {
        class: 'tab' + (t.key === S.tab ? ' on' : ''), type: 'button',
        onclick: function () { S.tab = t.key; render(); }
      }, t.label));
    });
    var view = clear(document.getElementById('view'));
    if (!S.data) { view.appendChild(h('div', { class: 'empty', text: 'Loading...' })); return; }
    if (!S.data.kitOk) { view.appendChild(h('div', { class: 'panel', text: 'The shared folder is missing. Ask Angelo to re-share it.' })); return; }
    if (S.tab === 'tasks') return renderTasks(view);
    if (S.tab === 'time') return renderTime(view);
    if (S.tab === 'drafts') return renderDrafts(view);
  }

  /* ------------------------------------------------------------------ tasks */
  function chip(status) {
    var cls = status === 'in progress' ? 'progress' : status === 'submitted' ? 'submitted' : status === 'approved' ? 'approved' : 'open';
    return h('span', { class: 'chip ' + cls, text: status });
  }
  function renderTasks(view) {
    var d = S.data;
    var tasks = d.tasks || [];
    view.appendChild(h('h1', { text: 'My tasks' }));
    view.appendChild(h('p', { class: 'muted small', text: 'Angelo sends these. Open the brief, do the work, then set the status.' }));

    if (!tasks.length) view.appendChild(h('div', { class: 'panel empty', text: 'No task right now.' }));

    tasks.forEach(function (t) {
      var brief = (d.inbox || []).filter(function (f) { return f.name === t.brief || f.rel.split('/').pop() === t.brief; })[0];
      var panel = h('div', { class: 'panel col' },
        h('div', { class: 'row between' },
          h('div', {}, h('b', { text: t.title }), ' ', chip(t.status)),
          h('span', { class: 'muted small', text: (t.client || '') + (t.due ? ' - due ' + t.due : '') })),
        h('div', { class: 'muted small', text: 'job: ' + (t.job || 'other') + ' - sent ' + when(t.at) }));

      if (brief) {
        panel.appendChild(h('div', { class: 'row' },
          h('a', { class: 'btn small ghost', href: '/file?p=' + encodeURIComponent(brief.rel), target: '_blank', rel: 'noopener', text: 'Open the brief' }),
          h('button', {
            class: 'btn small ghost', type: 'button',
            onclick: function () {
              if (S.open[t.id]) { delete S.open[t.id]; render(); return; }
              fetch('/file?p=' + encodeURIComponent(brief.rel)).then(function (r) { return r.text(); }).then(function (txt) {
                S.open[t.id] = txt; render();
              });
            }
          }, S.open[t.id] ? 'Hide it here' : 'Read it here')));
        if (S.open[t.id]) panel.appendChild(h('pre', { class: 'mono', style: 'white-space:pre-wrap', text: S.open[t.id] }));
      } else {
        panel.appendChild(h('div', { class: 'muted small', text: 'Brief file: ' + (t.brief || '(none)') + ' - not synced yet.' }));
      }

      var mine = d.statuses || [];
      panel.appendChild(h('div', { class: 'row' },
        h('span', { class: 'muted small', text: 'Set status:' }),
        mine.filter(function (s) { return s !== t.status; }).map(function (s) {
          return h('button', {
            class: 'btn small' + (s === 'submitted' ? '' : ' ghost'), type: 'button', disabled: S.busy ? 'disabled' : null,
            onclick: function () {
              S.busy = true; render();
              post('/api/task/' + encodeURIComponent(t.id) + '/status', { status: s }).then(function (r) {
                S.busy = false;
                if (!r.ok) { toast(r.data.error || 'could not change it', true); render(); return; }
                toast('Marked "' + s + '"'); load();
              });
            }, text: s
          });
        })));
      view.appendChild(panel);
    });

    var files = (d.inbox || []).filter(function (f) { return f.name.indexOf('/') > 0; });
    if (files.length) {
      var box = h('div', { class: 'panel col' }, h('h2', { text: 'Files Angelo sent' }));
      files.slice(0, 40).forEach(function (f) {
        box.appendChild(h('div', { class: 'item row between' },
          h('a', { href: '/file?p=' + encodeURIComponent(f.rel), target: '_blank', rel: 'noopener', text: f.name }),
          h('span', { class: 'muted small', text: size(f.bytes) + ' - ' + when(f.mtime) })));
      });
      view.appendChild(box);
    }
  }

  /* ------------------------------------------------------------------- time */
  function renderTime(view) {
    var d = S.data; var sum = (d.hours && d.hours.summary) || {};
    var f = S.form;
    view.appendChild(h('h1', { text: 'My time' }));
    view.appendChild(h('div', { class: 'tiles' },
      h('div', { class: 'tile' }, h('b', { text: hrs(sum.week) }), h('span', { class: 'muted small', text: 'hours this week' })),
      h('div', { class: 'tile' }, h('b', { text: hrs(sum.month) }), h('span', { class: 'muted small', text: 'this month' })),
      h('div', { class: 'tile' }, h('b', { text: hrs(sum.all) }), h('span', { class: 'muted small', text: 'all time' }))));

    var clients = {};
    (d.tasks || []).forEach(function (t) { if (t.slug) clients[t.slug] = t.client || t.slug; });
    (d.hours.rows || []).forEach(function (r) { if (r.client && r.client !== 'internal') clients[r.client] = clients[r.client] || r.client; });
    var opts = Object.keys(clients);

    view.appendChild(h('div', { class: 'panel col' },
      h('h2', { text: 'Log my work' }),
      h('div', { class: 'row' },
        h('div', { class: 'field' }, h('label', { text: 'Date' }),
          h('input', { type: 'date', value: f.date || d.today, oninput: function (e) { f.date = e.target.value; } })),
        h('div', { class: 'field' }, h('label', { text: 'Hours' }),
          h('input', { type: 'number', step: '0.25', min: '0.25', max: '24', placeholder: 'e.g. 2.5', value: f.hours || '', oninput: function (e) { f.hours = e.target.value; } })),
        h('div', { class: 'field' }, h('label', { text: 'Client' }),
          h('select', { onchange: function (e) { f.client = e.target.value; } },
            [h('option', { value: 'internal', text: 'internal' })].concat(opts.map(function (k) {
              return h('option', { value: k, text: clients[k], selected: f.client === k ? 'selected' : null });
            })))),
        h('div', { class: 'field' }, h('label', { text: 'Job' }),
          h('select', { onchange: function (e) { f.job = e.target.value; } },
            (d.jobs || []).map(function (j) { return h('option', { value: j, text: j, selected: f.job === j ? 'selected' : null }); })))),
      h('div', {}, h('label', { text: 'What did you do?' }),
        h('textarea', { placeholder: 'In your own words. Example: claimed the Yelp and Bing listings, fixed the city on two profiles.', oninput: function (e) { f.what = e.target.value; } }, f.what || '')),
      h('div', {}, h('label', { text: 'Anything blocking you? (optional)' }),
        h('input', { value: f.notes || '', oninput: function (e) { f.notes = e.target.value; } })),
      h('div', { class: 'row between' },
        h('span', { class: 'muted small', text: 'One row per work session. Angelo reads this.' }),
        h('button', {
          class: 'btn', type: 'button', disabled: S.busy ? 'disabled' : null,
          onclick: function () {
            if (!f.hours || !String(f.what || '').trim()) { toast('Hours and the comment are required', true); return; }
            S.busy = true; render();
            post('/api/hours', {
              date: f.date || d.today, hours: Number(f.hours), client: f.client || 'internal',
              job: f.job || 'other', what: f.what, notes: f.notes || ''
            }).then(function (r) {
              S.busy = false;
              if (!r.ok) { toast(r.data.error || 'could not save', true); render(); return; }
              toast('Logged ' + hrs(f.hours) + ' hours'); S.form = {}; load();
            });
          }
        }, 'Log it'))));

    var rows = (d.hours && d.hours.rows) || [];
    var list = h('div', { class: 'panel col' }, h('h2', { text: 'What I logged' }));
    if (!rows.length) list.appendChild(h('div', { class: 'empty', text: 'Nothing yet.' }));
    rows.forEach(function (r) {
      list.appendChild(h('div', { class: 'item' },
        h('div', { class: 'row between' },
          h('div', {}, h('b', { text: r.date }), ' - ', hrs(r.hours) + ' h ', h('span', { class: 'chip', text: r.client || 'internal' })),
          h('span', { class: 'muted small', text: r.job || '' })),
        h('div', { text: r.what_i_did || '' }),
        r.notes ? h('div', { class: 'muted small', text: 'note: ' + r.notes }) : null));
    });
    view.appendChild(list);
  }

  /* ----------------------------------------------------------- site photos */
  /* The server downloads the photos; the browser makes each one a small WebP (canvas). */
  function toWebp(url) {
    return new Promise(function (resolve, reject) {
      var img = new Image();
      img.onload = function () {
        var w = img.naturalWidth, ht = img.naturalHeight;
        if (!w || !ht) { reject(new Error('empty picture')); return; }
        var k = Math.min(1, 1600 / w), cw = Math.round(w * k), ch = Math.round(ht * k);
        var c = document.createElement('canvas'); c.width = cw; c.height = ch;
        c.getContext('2d').drawImage(img, 0, 0, cw, ch);
        var qs = [0.82, 0.72, 0.62, 0.5];
        (function tryQ(i) {
          c.toBlob(function (b) {
            if (!b || b.type !== 'image/webp') { reject(new Error('use Chrome to make WebP')); return; }
            if (b.size > 150 * 1024 && i < qs.length - 1) { tryQ(i + 1); return; }
            var fr = new FileReader();
            fr.onload = function () { resolve({ data: String(fr.result).split(',')[1], width: cw, height: ch, bytes: b.size }); };
            fr.onerror = function () { reject(new Error('could not read the WebP')); };
            fr.readAsDataURL(b);
          }, 'image/webp', qs[i]);
        })(0);
      };
      img.onerror = function () { reject(new Error('could not open the photo')); };
      img.src = url;
    });
  }
  function savePhotos(site) {
    var msg = S.photos[site] = { busy: true, lines: ['Downloading the photos from the client\'s website...'] };
    S.busy = true; render();
    function say(t) { msg.lines.push(t); render(); }
    function done(t) { msg.busy = false; S.busy = false; if (t) say(t); load(); }
    post('/api/photos/fetch', { site: site }).then(function (r) {
      if (!r.ok) { done('Stopped: ' + (r.data.error || 'could not download')); return; }
      var list = r.data.photos || [];
      var good = list.filter(function (p) { return !p.error; });
      list.filter(function (p) { return p.error; }).forEach(function (p) { say('NOT saved: ' + p.name + ' - ' + p.error + ' (' + p.url + ')'); });
      say('Downloaded ' + good.length + ' of ' + list.length + '. Making them smaller (WebP)...');
      var chain = Promise.resolve();
      good.filter(function (p) { return p.convert; }).forEach(function (p) {
        chain = chain.then(function () {
          return toWebp('/file?p=' + encodeURIComponent(p.orig)).then(function (w) {
            return post('/api/photos/webp', { site: site, name: p.name, data: w.data, width: w.width, height: w.height }).then(function (x) {
              if (!x.ok) say('Kept the original for ' + p.name + ' - ' + (x.data.error || 'error'));
            });
          }).catch(function (e) { say('Kept the original for ' + p.name + ' - ' + e.message); });
        });
      });
      return chain.then(function () { return post('/api/photos/link', { site: site }); }).then(function (x) {
        if (!x.ok) { done('Stopped: ' + (x.data.error || 'could not update the pages')); return; }
        var t = 'Done. ' + x.data.linked + ' photo spots now use the saved files, in ' + x.data.pages + ' pages.';
        if (r.data.other) t += ' ' + r.data.other + ' other web pictures have no data-local, so they were left as they are.';
        if (x.data.left) t += ' ' + x.data.left + ' photos still link to the old website: send the list above to Angelo.';
        done(t);
      });
    }).catch(function () { done('Stopped: the app is not running.'); });
  }
  function renderPhotos(view) {
    var sites = S.data.sites || [];
    if (!sites.length) return;
    var box = h('div', { class: 'panel col' }, h('h2', { text: 'Website photos' }),
      h('p', { class: 'muted small', text: 'Saves the client\'s real photos into the website folder and makes them small WebP files. Use it after Claude has put the photos in the pages.' }));
    sites.forEach(function (s) {
      var m = S.photos[s.site];
      box.appendChild(h('div', { class: 'item col' },
        h('div', { class: 'row between' },
          h('div', {}, h('b', { text: s.site }), ' ',
            h('span', { class: 'muted small', text: s.linked + ' photos link to the old website, ' + s.saved + ' saved' })),
          h('button', {
            class: 'btn small', type: 'button', disabled: (S.busy || !s.linked) ? 'disabled' : null,
            onclick: function () { savePhotos(s.site); }
          }, m && m.busy ? 'Working...' : 'Save the photos')),
        m ? h('pre', { class: 'mono small', style: 'white-space:pre-wrap', text: m.lines.join('\n') }) : null));
    });
    view.appendChild(box);
  }

  /* ----------------------------------------------------------------- drafts */
  function renderDrafts(view) {
    var d = S.data;
    view.appendChild(h('h1', { text: 'My drafts' }));
    view.appendChild(h('p', { class: 'muted small', text: 'Everything your Claude wrote into OUTBOX. Angelo moves the good ones into "approved".' }));
    renderPhotos(view);
    var wait = h('div', { class: 'panel col' }, h('h2', { text: 'Waiting for Angelo' }));
    var outbox = d.outbox || [];
    if (!outbox.length) wait.appendChild(h('div', { class: 'empty', text: 'Nothing waiting.' }));
    outbox.forEach(function (f) {
      wait.appendChild(h('div', { class: 'item row between' },
        h('a', { href: '/file?p=' + encodeURIComponent(f.rel), target: '_blank', rel: 'noopener', text: f.name }),
        h('span', { class: 'muted small', text: size(f.bytes) + ' - ' + when(f.mtime) })));
    });
    view.appendChild(wait);

    var okList = d.approved || [];
    var done = h('div', { class: 'panel col' }, h('h2', { text: 'Approved - safe to use' }));
    if (!okList.length) done.appendChild(h('div', { class: 'empty', text: 'Nothing approved yet.' }));
    okList.forEach(function (f) {
      done.appendChild(h('div', { class: 'item row between' },
        h('a', { href: '/file?p=' + encodeURIComponent(f.rel), target: '_blank', rel: 'noopener', text: f.name }),
        h('span', { class: 'muted small', text: when(f.mtime) })));
    });
    view.appendChild(done);
  }

  /* ------------------------------------------------------------------- boot */
  document.getElementById('refresh').addEventListener('click', function () { load(); toast('Refreshed'); });
  load();
  setInterval(function () { if (!S.busy) load(); }, 30000);   /* OneDrive syncs in the background */
})();
