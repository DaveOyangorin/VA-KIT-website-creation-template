'use strict';
/*
  Novarte VA - tests.  node test\run-tests.js      exit 0 = every case passed

  Builds a throw-away kit folder under %TEMP%, starts server.js against it on a free port,
  and checks the whole contract: what it serves, what it refuses, the hours sheet, the task
  status rules, and that nothing can reach a file outside the kit. Touches no real file.
*/
const fs = require('fs');
const os = require('os');
const path = require('path');
const http = require('http');
const { spawn } = require('child_process');

const APP = path.resolve(__dirname, '..');
const PORT = 5581;
const BASE = 'http://127.0.0.1:' + PORT;
const KIT = path.join(os.tmpdir(), 'novarte-va-test-' + Date.now().toString(36));
let pass = 0, fail = 0, child = null;

function ok(name, cond, detail) {
  if (cond) { pass++; console.log('PASS ' + name); }
  else { fail++; console.log('FAIL ' + name + (detail ? '\n     ' + detail : '')); }
}
function eq(name, got, want) { ok(name, JSON.stringify(got) === JSON.stringify(want), 'expected ' + JSON.stringify(want) + ', got ' + JSON.stringify(got)); }
function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

function req(method, p, { body, token, headers } = {}) {
  return new Promise((resolve) => {
    const data = body === undefined ? null : Buffer.from(JSON.stringify(body));
    const r = http.request(BASE + p, {
      method,
      headers: Object.assign({ Accept: 'application/json' },
        data ? { 'Content-Type': 'application/json', 'Content-Length': data.length } : {},
        token ? { 'X-VA-Token': token } : {}, headers || {})
    }, (res) => {
      let s = '';
      res.on('data', c => { s += c; });
      res.on('end', () => { let j = null; try { j = JSON.parse(s); } catch (_) { /* not json */ } resolve({ status: res.statusCode, json: j, text: s, headers: res.headers }); });
    });
    r.on('error', () => resolve({ status: 0, json: null, text: '', headers: {} }));
    if (data) r.write(data);
    r.end();
  });
}

function buildKit() {
  fs.mkdirSync(path.join(KIT, 'INBOX', 'testco'), { recursive: true });
  fs.mkdirSync(path.join(KIT, 'OUTBOX', '_approved'), { recursive: true });
  fs.writeFileSync(path.join(KIT, 'INBOX', 'testco_backlinks-brief_2026-09-16.md'), '# Claim the listings\n\nDo the free ones first.\n');
  fs.writeFileSync(path.join(KIT, 'INBOX', 'testco', 'nap.txt'), 'Testco\n1 Main St\n');
  fs.writeFileSync(path.join(KIT, 'INBOX', 'README.md'), 'readme - must not be listed\n');
  fs.writeFileSync(path.join(KIT, 'OUTBOX', '2026-09-16_testco_tracker.csv'), 'a,b\n1,2\n');
  fs.writeFileSync(path.join(KIT, 'OUTBOX', '_approved', '2026-09-15_testco_profile.md'), '# ok\n');
  fs.writeFileSync(path.join(KIT, 'WORKLOG.csv'), 'date,start,end,hours,client,job,what_i_did,files,notes\n2026-09-15,,,0,example,setup,"Example row - delete it.",,\n');
  fs.writeFileSync(path.join(KIT, 'tasks.json'), JSON.stringify({
    tasks: [
      { id: 't1', at: '2026-09-16T08:00:00.000Z', slug: 'testco', client: 'Testco', job: 'backlinks', title: 'Claim the listings', due: '', status: 'open', brief: 'testco_backlinks-brief_2026-09-16.md', files: [], by: 'owner' },
      { id: 't2', at: '2026-09-10T08:00:00.000Z', slug: 'testco', client: 'Testco', job: 'gbp', title: 'Old closed task', due: '', status: 'approved', brief: 'x.md', files: [], by: 'owner' },
      { id: 't3', at: '2026-09-09T08:00:00.000Z', slug: 'testco', client: 'Testco', job: 'gbp', title: 'Cancelled one', due: '', status: 'cancelled', brief: 'y.md', files: [], by: 'owner' }
    ]
  }, null, 2));
  fs.writeFileSync(path.join(os.tmpdir(), 'va-outside-secret.txt'), 'must never be served\n');
}

async function start() {
  child = spawn(process.execPath, [path.join(APP, 'server.js')], {
    cwd: APP, env: Object.assign({}, process.env, { VA_KIT: KIT, VA_PORT: String(PORT) }), windowsHide: true, stdio: ['ignore', 'pipe', 'pipe']
  });
  child.stdout.on('data', () => {});
  child.stderr.on('data', (b) => console.log('[server] ' + String(b).trim()));
  for (let i = 0; i < 60; i++) { const r = await req('GET', '/api/state'); if (r.status === 200) return true; await sleep(250); }
  return false;
}
function stop() { if (child && !child.killed) { try { process.kill(child.pid); } catch (_) { /* gone */ } } }

async function main() {
  buildKit();
  if (!await start()) { console.log('FAIL server did not start'); process.exit(2); }

  /* --- the page and its assets --- */
  const page = await req('GET', '/');
  ok('GET / serves the page', page.status === 200 && /Novarte VA/.test(page.text));
  ok('GET / has a fresh token (no {{TOKEN}} left)', !/\{\{TOKEN\}\}/.test(page.text));
  ok('GET / sets a strict CSP', /default-src 'self'/.test(String(page.headers['content-security-policy'] || '')));
  const token = (page.text.match(/name="va-token" content="([a-f0-9]+)"/) || [])[1] || '';
  ok('token is a long random string', token.length >= 32, 'got ' + token.length + ' chars');
  ok('GET /app.js serves the app', (await req('GET', '/app.js')).status === 200);

  /* --- state --- */
  const s = (await req('GET', '/api/state')).json;
  ok('state: kit folder found', s.kitOk === true);
  eq('state: open + closed tasks listed, cancelled hidden', s.tasks.map(t => t.id), ['t1', 't2']);
  eq('state: he may set only these statuses', s.statuses, ['open', 'in progress', 'submitted']);
  ok('state: the brief is listed in INBOX', s.inbox.some(f => f.name === 'testco_backlinks-brief_2026-09-16.md'));
  ok('state: a document in a client folder is listed', s.inbox.some(f => f.name === 'testco/nap.txt'));
  ok('state: README.md is not listed', !s.inbox.some(f => /README/.test(f.name)));
  ok('state: OUTBOX draft listed', s.outbox.some(f => f.name === '2026-09-16_testco_tracker.csv'));
  ok('state: approved file is not in the waiting list', !s.outbox.some(f => /_approved/.test(f.name)));
  ok('state: approved file has its own list', s.approved.some(f => f.name === '2026-09-15_testco_profile.md'));
  eq('state: the example WORKLOG row is ignored', s.hours.rows.length, 0);

  /* --- reading a file --- */
  const brief = await req('GET', '/file?p=' + encodeURIComponent('INBOX/testco_backlinks-brief_2026-09-16.md'));
  ok('GET /file reads a brief', brief.status === 200 && /Claim the listings/.test(brief.text));
  ok('GET /file serves .md as plain text (never as a page)', /text\/plain/.test(String(brief.headers['content-type'])));
  eq('GET /file refuses ..\\ escapes', (await req('GET', '/file?p=' + encodeURIComponent('../va-outside-secret.txt'))).status, 400);
  eq('GET /file refuses an absolute path', (await req('GET', '/file?p=' + encodeURIComponent(path.join(os.tmpdir(), 'va-outside-secret.txt')))).status, 400);
  fs.writeFileSync(path.join(KIT, 'INBOX', 'evil.js'), 'alert(1)\n');
  eq('GET /file refuses a runnable type that really is in the folder', (await req('GET', '/file?p=' + encodeURIComponent('INBOX/evil.js'))).status, 400);
  eq('GET /file refuses an .html page', (await req('GET', '/file?p=' + encodeURIComponent('INBOX/page.html'))).status, 400);
  eq('GET /file 404s a missing file', (await req('GET', '/file?p=' + encodeURIComponent('INBOX/nope.md'))).status, 404);

  /* --- posting needs the page token --- */
  eq('POST without the token is refused', (await req('POST', '/api/hours', { body: { hours: 1, what: 'x' } })).status, 403);
  eq('POST with a wrong token is refused', (await req('POST', '/api/hours', { body: { hours: 1, what: 'x' }, token: 'deadbeef' })).status, 403);

  /* --- hours --- */
  const good = await req('POST', '/api/hours', { body: { date: '2026-09-16', hours: 2.5, client: 'testco', job: 'backlinks', what: 'Claimed Yelp and Bing', notes: 'waiting on a postcard' }, token });
  ok('POST /api/hours saves a row', good.status === 200 && good.json.ok === true);
  const sheet = fs.readFileSync(path.join(KIT, 'WORKLOG.csv'), 'utf8');
  ok('the row is in WORKLOG.csv', /2026-09-16,,,2.5,testco,backlinks,Claimed Yelp and Bing/.test(sheet), sheet);
  eq('hours: 0 is refused', (await req('POST', '/api/hours', { body: { hours: 0, what: 'x' }, token })).status, 400);
  eq('hours: 99 is refused', (await req('POST', '/api/hours', { body: { hours: 99, what: 'x' }, token })).status, 400);
  eq('hours: an empty comment is refused', (await req('POST', '/api/hours', { body: { hours: 1, what: '   ' }, token })).status, 400);
  const withComma = await req('POST', '/api/hours', { body: { hours: 1, what: 'fixed name, address, phone', client: 'testco' }, token });
  ok('a comment with commas stays one row', withComma.status === 200 && /"fixed name, address, phone"/.test(fs.readFileSync(path.join(KIT, 'WORKLOG.csv'), 'utf8')));
  const s2 = (await req('GET', '/api/state')).json;
  eq('state: hours add up', s2.hours.summary.all, 3.5);
  ok('state: hours per client', s2.hours.summary.byClient.some(b => b.client === 'testco' && b.hours === 3.5));

  /* --- task status --- */
  const moved = await req('POST', '/api/task/t1/status', { body: { status: 'in progress' }, token });
  ok('he can set "in progress"', moved.status === 200 && moved.json.task.status === 'in progress');
  ok('the change is written to tasks.json', /in progress/.test(fs.readFileSync(path.join(KIT, 'tasks.json'), 'utf8')));
  ok('the change records who did it', JSON.parse(fs.readFileSync(path.join(KIT, 'tasks.json'), 'utf8')).tasks[0].updatedBy === 'assistant');
  eq('he cannot approve his own task', (await req('POST', '/api/task/t1/status', { body: { status: 'approved' }, token })).status, 400);
  eq('he cannot cancel a task', (await req('POST', '/api/task/t1/status', { body: { status: 'cancelled' }, token })).status, 400);
  eq('a closed (approved) task cannot be reopened', (await req('POST', '/api/task/t2/status', { body: { status: 'in progress' }, token })).status, 409);
  eq('unknown task id is 404', (await req('POST', '/api/task/nope/status', { body: { status: 'open' }, token })).status, 404);
  const other = JSON.parse(fs.readFileSync(path.join(KIT, 'tasks.json'), 'utf8')).tasks;
  eq('other tasks are untouched', [other[1].status, other[2].status], ['approved', 'cancelled']);

  /* --- website photos (no real download: links are refused before any network call) --- */
  const site = path.join(KIT, 'OUTBOX', 'testco-site');
  fs.mkdirSync(path.join(site, 'blog'), { recursive: true });
  fs.writeFileSync(path.join(site, 'index.html'),
    '<h1>Hi</h1>\n<img src="https://testco.example/a.jpg?x=1&amp;y=2" alt="Van" data-local="images/van-sandy.webp" width="800" height="600">\n' +
    '<img src="https://badge.example/seal.png" alt="seal">\n<img src="images/logo.png" alt="logo">\n' +
    '<img src="http://testco.example/old.jpg" alt="Old" data-local="images/old.webp">\n<img alt="Ip" data-local="images/ip.webp" src="https://127.0.0.1/x.jpg"/>\n');
  fs.writeFileSync(path.join(site, 'blog', 'post.html'), '<img alt="Van again" src="https://testco.example/a.jpg?x=1&amp;y=2" data-local="images/van-sandy.webp">\n');
  fs.writeFileSync(path.join(site, '_preview.html'), '<img src="https://testco.example/a.jpg?x=1&amp;y=2" alt="Van" data-local="images/van-sandy.webp">\n');
  const sp = (await req('GET', '/api/state')).json.sites.find(x => x.site === 'testco-site');
  ok('state: the site folder is listed with its linked photos', sp && sp.linked === 3 && sp.saved === 0, JSON.stringify(sp));
  eq('photos: POST needs the token', (await req('POST', '/api/photos/fetch', { body: { site: 'testco-site' } })).status, 403);
  eq('photos: a bad site name is refused', (await req('POST', '/api/photos/fetch', { body: { site: '../INBOX' }, token })).status, 400);
  eq('photos: a missing site is 404', (await req('POST', '/api/photos/fetch', { body: { site: 'nope-site' }, token })).status, 404);

  const { collectPhotos, sniff, publicHttps } = require(path.join(APP, 'server.js'));
  const found = collectPhotos(site);
  eq('photos: one entry per URL, data-local only', found.list.map(p => p.name), ['van-sandy', 'old', 'ip']);
  eq('photos: &amp; in a link is decoded for the download', found.list[0].url, 'https://testco.example/a.jpg?x=1&y=2');
  eq('photos: both pages that use a photo are known', found.list[0].pages.sort(), ['blog/post.html', 'index.html']);
  eq('photos: a web picture without data-local is left alone', found.other, 1);
  ok('photos: http, IP and localhost links are refused', !publicHttps('http://testco.example/a.jpg') && !publicHttps('https://127.0.0.1/x.jpg') && !publicHttps('https://localhost/x.jpg') && !publicHttps('https://u:p@testco.example/x.jpg') && !!publicHttps('https://testco.example/a.jpg'));
  const webp = Buffer.concat([Buffer.from('RIFF'), Buffer.alloc(4), Buffer.from('WEBPVP8 '), Buffer.alloc(20)]);
  eq('photos: file type comes from the bytes', [sniff(Buffer.from([0xff, 0xd8, 0xff, 0, 0, 0, 0, 0, 0, 0, 0, 0])), sniff(webp), sniff(Buffer.from('<html><body>not a photo</body></html>'))], ['.jpg', '.webp', '']);

  /* pretend step 1 downloaded the van photo, then send the WebP the browser would make */
  fs.mkdirSync(path.join(site, 'images', '_orig'), { recursive: true });
  fs.writeFileSync(path.join(site, 'images', '_orig', 'van-sandy.jpg'), Buffer.from([0xff, 0xd8, 0xff, 0xe0]));
  fs.writeFileSync(path.join(site, '_photos.json'), JSON.stringify({ 'https://testco.example/a.jpg?x=1&amp;y=2': { name: 'van-sandy', url: 'https://testco.example/a.jpg?x=1&y=2', orig: 'images/_orig/van-sandy.jpg' } }));
  eq('photos: a non-WebP upload is refused', (await req('POST', '/api/photos/webp', { body: { site: 'testco-site', name: 'van-sandy', data: Buffer.from('<svg></svg>').toString('base64'), width: 10, height: 10 }, token })).status, 400);
  eq('photos: an unknown photo name is 404', (await req('POST', '/api/photos/webp', { body: { site: 'testco-site', name: 'nope', data: webp.toString('base64'), width: 10, height: 10 }, token })).status, 404);
  const wr = await req('POST', '/api/photos/webp', { body: { site: 'testco-site', name: 'van-sandy', data: webp.toString('base64'), width: 1600, height: 900 }, token });
  ok('photos: the WebP is saved in images/', wr.status === 200 && fs.existsSync(path.join(site, 'images', 'van-sandy.webp')), JSON.stringify(wr.json));
  const lk = await req('POST', '/api/photos/link', { body: { site: 'testco-site' }, token });
  ok('photos: link updates both pages', lk.status === 200 && lk.json.linked === 2 && lk.json.pages === 2, JSON.stringify(lk.json));
  const idx = fs.readFileSync(path.join(site, 'index.html'), 'utf8');
  ok('photos: the page now uses the local file', /<img src="images\/van-sandy\.webp" alt="Van" data-local="images\/van-sandy\.webp" width="800" height="450">/.test(idx), idx);
  ok('photos: other pictures are untouched', /src="https:\/\/badge\.example\/seal\.png"/.test(idx) && /src="images\/logo\.png"/.test(idx) && /src="http:\/\/testco\.example\/old\.jpg"/.test(idx));
  const post = fs.readFileSync(path.join(site, 'blog', 'post.html'), 'utf8');
  ok('photos: a page in a sub-folder gets ../images/', /src="\.\.\/images\/van-sandy\.webp"/.test(post) && /width="1600" height="900"/.test(post), post);
  ok('photos: _preview.html keeps its full URL', /src="https:\/\/testco\.example/.test(fs.readFileSync(path.join(site, '_preview.html'), 'utf8')));
  ok('photos: images/_orig is removed after linking', !fs.existsSync(path.join(site, 'images', '_orig')));
  eq('photos: 2 links to the old website are left (http + IP)', lk.json.left, 2);

  /* --- nothing else exists --- */
  eq('unknown GET is 404', (await req('GET', '/api/whatever')).status, 404);
  eq('unknown POST is 404', (await req('POST', '/api/whatever', { body: {}, token })).status, 404);
  eq('PUT is refused', (await req('PUT', '/api/hours', { body: {}, token })).status, 405);

  console.log('\n' + pass + ' passed, ' + fail + ' failed');
  stop();
  try { fs.rmSync(KIT, { recursive: true, force: true }); } catch (_) { /* leave it */ }
  try { fs.rmSync(path.join(os.tmpdir(), 'va-outside-secret.txt'), { force: true }); } catch (_) { /* leave it */ }
  process.exit(fail ? 1 : 0);
}

process.on('SIGINT', () => { stop(); process.exit(130); });
main().catch((e) => { console.error(e); stop(); process.exit(2); });
