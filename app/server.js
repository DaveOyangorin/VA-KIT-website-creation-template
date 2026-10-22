'use strict';
/*
  Novarte VA - the assistant's own little app.

  It runs on HIS computer, from inside the shared VA-KIT folder, and it touches nothing else:

      VA-KIT\tasks.json     the task list (Angelo's Desk writes the same file)
      VA-KIT\INBOX\         briefs and documents Angelo sent
      VA-KIT\OUTBOX\        the drafts he produced
      VA-KIT\WORKLOG.csv    his hours, one row per work session

  OneDrive keeps those files in step with Angelo's Novarte Desk. No client database, no money,
  no Claude, no key: it listens on 127.0.0.1 only, so only the person sitting at that PC can open
  it. Its one network call is "Save the photos": it downloads the client's real photos that a
  site page links with data-local="images/..." (https, picture files only) into that site folder.

  Start:  node server.js      (or double-click START-VA.cmd)   ->  http://localhost:5080
  Test:   node test\run-tests.js
*/
const fs = require('fs');
const http = require('http');
const path = require('path');
const crypto = require('crypto');

const APP = __dirname;
const KIT = process.env.VA_KIT ? path.resolve(process.env.VA_KIT) : path.resolve(APP, '..');
const PORT = Number(process.env.VA_PORT || 5080);
const PUBLIC = path.join(APP, 'public');
const TOKEN = crypto.randomBytes(24).toString('hex');   /* one per run: blocks other sites posting here */

const COLS = ['date', 'start', 'end', 'hours', 'client', 'job', 'what_i_did', 'files', 'notes'];
const JOBS = ['backlinks', 'website', 'gbp', 'emails', 'audit-review', 'revise', 'admin', 'learning', 'other'];
const STATUS = ['open', 'in progress', 'submitted', 'approved', 'cancelled'];
const MINE = ['open', 'in progress', 'submitted'];       /* the ones he may set himself */
const READABLE = new Set(['.md', '.txt', '.csv', '.pdf', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.avif', '.json']);
const TYPES = {
  '.md': 'text/plain; charset=utf-8', '.txt': 'text/plain; charset=utf-8', '.csv': 'text/csv; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.pdf': 'application/pdf', '.png': 'image/png',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.webp': 'image/webp', '.gif': 'image/gif', '.avif': 'image/avif',
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.css': 'text/css; charset=utf-8'
};

/* ------------------------------------------------------------------ helpers */
function isFile(p) { try { return fs.statSync(p).isFile(); } catch (_) { return false; } }
function isDir(p) { try { return fs.statSync(p).isDirectory(); } catch (_) { return false; } }
function today() { return new Date(Date.now() - new Date().getTimezoneOffset() * 60000).toISOString().slice(0, 10); }
function inKit(p) {
  const root = path.resolve(KIT); const abs = path.resolve(p);
  return abs === root || abs.startsWith(root + path.sep);
}
function kit(...rel) { return path.join(KIT, ...rel); }
function sendJson(res, obj, code = 200) {
  const body = Buffer.from(JSON.stringify(obj));
  res.writeHead(code, { 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff', 'Content-Length': body.length });
  res.end(body);
}
function sendFile(res, file, type, extra) {
  const body = fs.readFileSync(file);
  res.writeHead(200, Object.assign({ 'Content-Type': type, 'Cache-Control': 'no-store', 'X-Content-Type-Options': 'nosniff', 'Content-Length': body.length }, extra || {}));
  res.end(body);
}
function bad(msg, code = 400) { const e = new Error(msg); e.status = code; return e; }

/* ---------------------------------------------------------------- csv (hours) */
function splitCsvLine(line) {
  const out = []; let cur = ''; let q = false;
  for (let i = 0; i < line.length; i++) {
    const ch = line[i];
    if (q) { if (ch === '"') { if (line[i + 1] === '"') { cur += '"'; i++; } else q = false; } else cur += ch; }
    else if (ch === '"') q = true;
    else if (ch === ',') { out.push(cur); cur = ''; }
    else cur += ch;
  }
  out.push(cur); return out;
}
function csvCell(v) { const s = String(v == null ? '' : v); return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; }

function readHours() {
  const file = kit('WORKLOG.csv');
  if (!isFile(file)) return [];
  const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/).filter(l => l.trim());
  if (!lines.length) return [];
  const head = splitCsvLine(lines[0]).map(h => h.trim());
  const rows = [];
  for (let i = 1; i < lines.length; i++) {
    const cells = splitCsvLine(lines[i]);
    const row = {}; head.forEach((h, n) => { row[h] = (cells[n] || '').trim(); });
    if (String(row.client || '').toLowerCase() === 'example') continue;
    row.hours = Number(row.hours || 0) || 0;
    rows.push(row);
  }
  rows.sort((a, b) => (String(a.date) < String(b.date) ? 1 : -1));
  return rows;
}
function weekStart(d0) {
  const d = new Date(String(d0) + 'T00:00:00');
  if (isNaN(d)) return '';
  d.setDate(d.getDate() - ((d.getDay() + 6) % 7));
  return d.toISOString().slice(0, 10);
}
function hoursSummary(rows) {
  const w = weekStart(today()); const month = today().slice(0, 7);
  const byClient = {}; let week = 0, mtd = 0, all = 0;
  for (const r of rows) {
    all += r.hours;
    if (String(r.date).slice(0, 7) === month) mtd += r.hours;
    if (weekStart(r.date) === w) week += r.hours;
    byClient[r.client || 'internal'] = (byClient[r.client || 'internal'] || 0) + r.hours;
  }
  const round = (n) => Math.round(n * 100) / 100;
  return {
    week: round(week), month: round(mtd), all: round(all), weekStart: w,
    byClient: Object.keys(byClient).map(k => ({ client: k, hours: round(byClient[k]) })).sort((a, b) => b.hours - a.hours)
  };
}
function addHours(body) {
  const date = /^\d{4}-\d{2}-\d{2}$/.test(String(body.date || '')) ? String(body.date) : today();
  const hours = Math.round(Number(body.hours) * 100) / 100;
  if (!(hours > 0) || hours > 24) throw bad('hours must be a number between 0 and 24');
  const what = String(body.what || '').slice(0, 2000).trim();
  if (!what) throw bad('say what you did');
  const time = (s) => (/^\d{1,2}:\d{2}$/.test(String(s || '')) ? String(s) : '');
  const row = {
    date, start: time(body.start), end: time(body.end), hours,
    client: String(body.client || 'internal').toLowerCase().replace(/[^a-z0-9-]/g, '').slice(0, 40) || 'internal',
    job: JOBS.indexOf(String(body.job || '')) >= 0 ? String(body.job) : 'other',
    what_i_did: what, files: String(body.files || '').slice(0, 500).trim(), notes: String(body.notes || '').slice(0, 500).trim()
  };
  const file = kit('WORKLOG.csv');
  if (!isFile(file)) fs.writeFileSync(file, COLS.join(',') + '\n', 'utf8');
  const cur = fs.readFileSync(file, 'utf8');
  fs.appendFileSync(file, (!cur || cur.endsWith('\n') ? '' : '\n') + COLS.map(c => csvCell(row[c])).join(',') + '\n', 'utf8');
  return { ok: true, row };
}

/* ------------------------------------------------------------------- tasks */
function readTasks() {
  try { const j = JSON.parse(fs.readFileSync(kit('tasks.json'), 'utf8')); return Array.isArray(j.tasks) ? j.tasks : []; }
  catch (_) { return []; }
}
/* Both apps write this file through OneDrive, so re-read and change only this one task. */
function setStatus(id, status) {
  if (MINE.indexOf(status) < 0) throw bad('you can set: ' + MINE.join(', '));
  const tasks = readTasks();
  const t = tasks.find(x => x.id === id);
  if (!t) throw bad('no such task', 404);
  if (t.status === 'approved' || t.status === 'cancelled') throw bad('that task is closed - ask Angelo', 409);
  t.status = status; t.updated = new Date().toISOString(); t.updatedBy = 'assistant';
  fs.writeFileSync(kit('tasks.json'), JSON.stringify({ tasks }, null, 2), 'utf8');
  return t;
}

/* -------------------------------------------------------------- file lists */
function listDir(dir, depth = 0, out = [], base = dir) {
  let names = [];
  try { names = fs.readdirSync(dir, { withFileTypes: true }); } catch (_) { return out; }
  for (const n of names) {
    const p = path.join(dir, n.name);
    if (n.isDirectory()) { if (depth < 2) listDir(p, depth + 1, out, base); continue; }
    if (n.name === 'README.md') continue;
    let st = null; try { st = fs.statSync(p); } catch (_) { continue; }
    out.push({ name: path.relative(base, p).replace(/\\/g, '/'), rel: path.relative(KIT, p).replace(/\\/g, '/'), bytes: st.size, mtime: st.mtime.toISOString() });
  }
  return out;
}
function state() {
  const inbox = listDir(kit('INBOX')).sort((a, b) => (a.mtime < b.mtime ? 1 : -1));
  const outbox = listDir(kit('OUTBOX')).filter(f => !f.name.startsWith('_approved/')).sort((a, b) => (a.mtime < b.mtime ? 1 : -1));
  const approved = listDir(kit('OUTBOX/_approved')).sort((a, b) => (a.mtime < b.mtime ? 1 : -1));
  const rows = readHours();
  return {
    kit: KIT, kitOk: isDir(KIT), today: today(), jobs: JOBS, statuses: MINE,
    tasks: readTasks().filter(t => t.status !== 'cancelled'),
    inbox, outbox, approved, sites: sitesState(),
    hours: { rows: rows.slice(0, 300), summary: hoursSummary(rows) }
  };
}

/* ------------------------------------------------------------ site photos */
/* Claude in the kit has no shell, so it cannot save a picture. It links the client's real photos
   by full URL with data-local="images/<name>.webp". "Save the photos" finishes the job:
     1. /api/photos/fetch  downloads each linked photo into images/_orig/ (https, pictures only)
     2. the page turns each one into a small WebP in the browser (canvas) -> /api/photos/webp
     3. /api/photos/link   points every <img> at its local file and removes images/_orig/
   _photos.json in the site folder remembers which URL became which file. */
const MAX_PHOTO = 15 * 1024 * 1024;
const MAX_WEBP = 4 * 1024 * 1024;
const CONVERT = new Set(['.jpg', '.png', '.webp', '.avif']);
const IMG_TAG = /<img\b[^>]*>/gi;

function attr(tag, name) {
  const m = tag.match(new RegExp('\\s' + name + '\\s*=\\s*(?:"([^"]*)"|\'([^\']*)\')', 'i'));
  return m ? (m[1] != null ? m[1] : m[2]) : null;
}
function setAttr(tag, name, value) {
  const v = '"' + String(value).replace(/"/g, '&quot;') + '"';
  const re = new RegExp('(\\s' + name + '\\s*=\\s*)(?:"[^"]*"|\'[^\']*\')', 'i');
  if (re.test(tag)) return tag.replace(re, (m, a) => a + v);
  return tag.replace(/\s*(\/?)>$/, (m, slash) => ' ' + name + '=' + v + (slash ? ' />' : '>'));
}
function unescapeUrl(s) { return String(s).replace(/&amp;/g, '&').replace(/&#38;/g, '&'); }
function sniff(buf) {
  if (buf.length < 12) return '';
  if (buf[0] === 0xff && buf[1] === 0xd8 && buf[2] === 0xff) return '.jpg';
  if (buf.toString('hex', 0, 4) === '89504e47') return '.png';
  if (buf.toString('ascii', 0, 3) === 'GIF') return '.gif';
  if (buf.toString('ascii', 0, 4) === 'RIFF' && buf.toString('ascii', 8, 12) === 'WEBP') return '.webp';
  if (buf.toString('ascii', 4, 8) === 'ftyp' && /avi[fs]/.test(buf.toString('ascii', 8, 12))) return '.avif';
  const head = buf.toString('utf8', 0, Math.min(buf.length, 512)).trim().toLowerCase();
  if (/^(<\?xml[^>]*>\s*)?(<!--[\s\S]*?-->\s*)*<svg[\s>]/.test(head)) return '.svg';
  return '';
}
function publicHttps(raw) {
  let u; try { u = new URL(raw); } catch (_) { return null; }
  if (u.protocol !== 'https:' || u.username || u.password) return null;
  const host = u.hostname.toLowerCase();
  if (host === 'localhost' || host.endsWith('.local') || host.startsWith('[') || /^\d+\.\d+\.\d+\.\d+$/.test(host)) return null;
  return u;
}
function siteDir(site) {
  const s = String(site || '');
  if (!/^[A-Za-z0-9][A-Za-z0-9._-]{0,80}$/.test(s)) throw bad('bad site folder');
  const dir = kit('OUTBOX', s);
  if (!inKit(dir) || !isDir(dir)) throw bad('no such site folder', 404);
  return dir;
}
function listHtml(dir, depth = 0, out = []) {
  let names = [];
  try { names = fs.readdirSync(dir, { withFileTypes: true }); } catch (_) { return out; }
  for (const n of names) {
    if (n.name.startsWith('_') || n.name.startsWith('.')) continue;   /* _preview.html keeps its full URLs */
    const p = path.join(dir, n.name);
    if (n.isDirectory()) { if (depth < 4 && n.name !== 'images') listHtml(p, depth + 1, out); continue; }
    if (/\.html?$/i.test(n.name)) out.push(p);
  }
  return out;
}
function readManifest(dir) {
  try { const j = JSON.parse(fs.readFileSync(path.join(dir, '_photos.json'), 'utf8')); return j && typeof j === 'object' && !Array.isArray(j) ? j : {}; }
  catch (_) { return {}; }
}
function writeManifest(dir, man) { fs.writeFileSync(path.join(dir, '_photos.json'), JSON.stringify(man, null, 2), 'utf8'); }

/* every <img> with a full https src AND data-local, once per URL */
function collectPhotos(dir) {
  const bySrc = new Map(); const used = new Set(); let other = 0;
  for (const page of listHtml(dir)) {
    const html = fs.readFileSync(page, 'utf8');
    for (const tag of html.match(IMG_TAG) || []) {
      const src = attr(tag, 'src');
      if (!src || !/^https?:\/\//i.test(src)) continue;
      const local = attr(tag, 'data-local');
      if (!local) { other++; continue; }
      const rel = path.relative(dir, page).replace(/\\/g, '/');
      if (bySrc.has(src)) { const e = bySrc.get(src); if (e.pages.indexOf(rel) < 0) e.pages.push(rel); continue; }
      let base = path.basename(local).replace(/\.[^.]*$/, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 80) || 'photo';
      let name = base; let n = 2;
      while (used.has(name)) name = base + '-' + (n++);
      used.add(name);
      bySrc.set(src, { src, url: unescapeUrl(src), name, pages: [rel] });
    }
  }
  return { list: Array.from(bySrc.values()), other };
}
function sitesState() {
  const out = [];
  let names = [];
  try { names = fs.readdirSync(kit('OUTBOX'), { withFileTypes: true }); } catch (_) { return out; }
  for (const n of names) {
    if (!n.isDirectory() || n.name.startsWith('_') || n.name.startsWith('.')) continue;
    const dir = kit('OUTBOX', n.name);
    if (!listHtml(dir).length) continue;
    const man = readManifest(dir);
    out.push({ site: n.name, linked: collectPhotos(dir).list.length, saved: Object.values(man).filter(e => e && e.file).length });
  }
  return out;
}

async function download(raw) {
  const u = publicHttps(raw);
  if (!u) throw bad('only https links to a public website');
  const ctl = new AbortController(); const timer = setTimeout(() => ctl.abort(), 20000);
  try {
    const r = await fetch(u, { signal: ctl.signal, redirect: 'follow', headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) NovarteVA/1.0', Accept: 'image/avif,image/webp,image/*;q=0.9,*/*;q=0.5' } });
    if (!r.ok) throw bad('the website answered ' + r.status);
    if (!publicHttps(r.url)) throw bad('the link moved to a non-https address');
    if (Number(r.headers.get('content-length') || 0) > MAX_PHOTO) throw bad('the photo is over 15 MB');
    const buf = Buffer.from(await r.arrayBuffer());
    if (buf.length > MAX_PHOTO) throw bad('the photo is over 15 MB');
    const ext = sniff(buf);
    if (!ext) throw bad('that link is not a photo');
    return { buf, ext };
  } catch (e) {
    if (e && e.name === 'AbortError') throw bad('the website took too long');
    throw e;
  } finally { clearTimeout(timer); }
}

async function photosFetch(site) {
  const dir = siteDir(site);
  const found = collectPhotos(dir);
  const man = readManifest(dir);
  fs.mkdirSync(path.join(dir, 'images', '_orig'), { recursive: true });
  const photos = [];
  for (const p of found.list) {
    try {
      const { buf, ext } = await download(p.url);
      const orig = 'images/_orig/' + p.name + ext;
      fs.writeFileSync(path.join(dir, orig), buf);
      man[p.src] = { name: p.name, url: p.url, pages: p.pages, orig, bytes: buf.length };
      photos.push({ name: p.name, url: p.url, orig: path.relative(KIT, path.join(dir, orig)).replace(/\\/g, '/'), convert: CONVERT.has(ext), bytes: buf.length });
    } catch (e) {
      photos.push({ name: p.name, url: p.url, error: (e && e.message) || 'could not download' });
    }
  }
  writeManifest(dir, man);
  return { site, photos, other: found.other };
}

function photosWebp(body) {
  const dir = siteDir(body.site);
  const man = readManifest(dir);
  const entry = Object.values(man).find(e => e && e.name === String(body.name || ''));
  if (!entry) throw bad('unknown photo', 404);
  const buf = Buffer.from(String(body.data || ''), 'base64');
  if (sniff(buf) !== '.webp') throw bad('that is not a WebP picture');
  if (buf.length > MAX_WEBP) throw bad('the WebP is too big');
  const w = Math.round(Number(body.width)); const hgt = Math.round(Number(body.height));
  if (!(w > 0 && w <= 10000 && hgt > 0 && hgt <= 10000)) throw bad('bad width or height');
  entry.file = 'images/' + entry.name + '.webp';
  fs.writeFileSync(path.join(dir, entry.file), buf);
  entry.width = w; entry.height = hgt; entry.bytes = buf.length;
  writeManifest(dir, man);
  return { ok: true, file: entry.file, bytes: buf.length };
}

function photosLink(site) {
  const dir = siteDir(site);
  const man = readManifest(dir);
  /* a photo the browser could not turn into WebP (gif, svg, or an error) keeps its own format */
  for (const e of Object.values(man)) {
    if (!e || e.file || !e.orig || !isFile(path.join(dir, e.orig))) continue;
    e.file = 'images/' + e.name + path.extname(e.orig);
    fs.copyFileSync(path.join(dir, e.orig), path.join(dir, e.file));
  }
  let pages = 0, linked = 0;
  for (const page of listHtml(dir)) {
    const html = fs.readFileSync(page, 'utf8');
    const up = path.relative(path.dirname(page), dir).replace(/\\/g, '/');
    const prefix = up ? up + '/' : '';
    let n = 0;
    const next = html.replace(IMG_TAG, (tag) => {
      const src = attr(tag, 'src');
      const e = src && Object.prototype.hasOwnProperty.call(man, src) ? man[src] : null;
      if (!e || !e.file || !isFile(path.join(dir, e.file))) return tag;
      let t = setAttr(tag, 'src', prefix + e.file);
      if (e.width && e.height) {
        /* keep a width Claude chose for the layout; fix the height to the photo's real shape */
        const w = Number(attr(t, 'width')) > 0 ? Number(attr(t, 'width')) : e.width;
        t = setAttr(setAttr(t, 'width', w), 'height', Math.round(w * e.height / e.width));
      }
      n++; return t;
    });
    if (n) { fs.writeFileSync(page, next, 'utf8'); pages++; linked += n; }
  }
  fs.rmSync(path.join(dir, 'images', '_orig'), { recursive: true, force: true });
  writeManifest(dir, man);
  return { ok: true, pages, linked, left: collectPhotos(dir).list.length };
}

/* ------------------------------------------------------------------ server */
function indexHtml() {
  return fs.readFileSync(path.join(PUBLIC, 'index.html'), 'utf8').replace('{{TOKEN}}', TOKEN);
}
function readBody(req, limit = 200 * 1024) {
  return new Promise((resolve, reject) => {
    let size = 0; const chunks = [];
    req.on('data', (c) => { size += c.length; if (size > limit) { reject(bad('body too big')); req.destroy(); return; } chunks.push(c); });
    req.on('end', () => { try { resolve(chunks.length ? JSON.parse(Buffer.concat(chunks).toString('utf8')) : {}); } catch (_) { reject(bad('bad json')); } });
    req.on('error', reject);
  });
}

const server = http.createServer(async (req, res) => {
  let u;
  try { u = new URL(req.url, 'http://localhost'); } catch (_) { return sendJson(res, { error: 'bad url' }, 400); }
  const p = u.pathname;
  try {
    if (req.method === 'GET') {
      if (p === '/' || p === '/index.html') {
        const html = indexHtml();
        res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store', 'Content-Security-Policy': "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'" });
        return res.end(html);
      }
      if (p === '/app.js' || p === '/style.css') {
        const f = path.join(PUBLIC, path.basename(p));
        if (!isFile(f)) return sendJson(res, { error: 'not built' }, 404);
        return sendFile(res, f, TYPES[path.extname(f)]);
      }
      if (p === '/api/state') return sendJson(res, state());
      if (p === '/file') {
        const rel = String(u.searchParams.get('p') || '');
        if (!rel || rel.includes('..') || path.isAbsolute(rel)) throw bad('bad path');
        const abs = path.join(KIT, rel);
        /* type first, then existence: a file we would never serve gets the same answer either way */
        const ext = path.extname(abs).toLowerCase();
        if (!READABLE.has(ext)) throw bad('that file type does not open here');
        if (!inKit(abs) || !isFile(abs)) throw bad('no such file', 404);
        /* never let a file from the folder run as a page: text types are served as plain text */
        return sendFile(res, abs, TYPES[ext] || 'application/octet-stream', { 'Content-Disposition': 'inline; filename="' + path.basename(abs).replace(/"/g, '') + '"' });
      }
      return sendJson(res, { error: 'not found' }, 404);
    }
    if (req.method !== 'POST') return sendJson(res, { error: 'method not allowed' }, 405);
    if (req.headers['x-va-token'] !== TOKEN) return sendJson(res, { error: 'reload the page (token)' }, 403);
    const body = await readBody(req, p === '/api/photos/webp' ? 6 * 1024 * 1024 : undefined);
    if (p === '/api/hours') return sendJson(res, addHours(body));
    if (p === '/api/photos/fetch') return sendJson(res, await photosFetch(body.site));
    if (p === '/api/photos/webp') return sendJson(res, photosWebp(body));
    if (p === '/api/photos/link') return sendJson(res, photosLink(body.site));
    const m = p.match(/^\/api\/task\/([A-Za-z0-9_-]+)\/status$/);
    if (m) return sendJson(res, { task: setStatus(m[1], String(body.status || '')) });
    return sendJson(res, { error: 'not found' }, 404);
  } catch (e) {
    return sendJson(res, { error: (e && e.message) || 'error' }, (e && e.status) || 500);
  }
});

if (require.main === module) {
  if (!isDir(KIT)) { console.error('Novarte VA cannot start: the kit folder is missing: ' + KIT); process.exit(1); }
  for (const d of ['INBOX', 'OUTBOX']) { try { fs.mkdirSync(kit(d), { recursive: true }); } catch (_) { /* exists */ } }
  server.listen(PORT, '127.0.0.1', () => {
    console.log('Novarte VA  ->  http://localhost:' + PORT);
    console.log('folder      ->  ' + KIT);
    console.log('(close this window to stop)');
  });
  server.on('error', (e) => { console.error('cannot listen on ' + PORT + ': ' + e.message); process.exit(1); });
}

module.exports = { server, state, addHours, setStatus, readHours, hoursSummary, collectPhotos, photosLink, sniff, publicHttps, attr, setAttr, KIT, PORT, TOKEN };
