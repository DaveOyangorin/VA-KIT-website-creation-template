// Builds a self-contained preview copy in out-preview/: every page a flat .html file, linked by relative paths,
// so it works from any folder or sandboxed host (e.g. a private review link). Production uses `npm run build`.
import { execSync } from 'node:child_process';
import { existsSync, readdirSync, readFileSync, renameSync, rmSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const root = new URL('..', import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const out = join(root, 'out'), dest = join(root, 'out-preview');

execSync('npx next build', { cwd: root, stdio: 'inherit', env: { ...process.env, EP_PREVIEW: '1' } });
rmSync(dest, { recursive: true, force: true });
renameSync(out, dest);

// next/font writes url(./_next/static/media/...) into CSS that lives in _next/static/css/: point it at ../media/.
const walk = (d) => readdirSync(d, { withFileTypes: true }).flatMap((e) => (e.isDirectory() ? walk(join(d, e.name)) : [join(d, e.name)]));
let fixed = 0;
for (const f of walk(dest)) {
  if (!/\.(css|html|js)$/.test(f)) continue;
  const s = readFileSync(f, 'utf8');
  let t = s;
  if (f.endsWith('.css')) t = t.replaceAll('./_next/static/media/', '../media/').replaceAll('/_next/static/media/', '../media/');
  if (t !== s) { writeFileSync(f, t); fixed++; }
}
// Some preview hosts reserve names that start with "_": move _next/ to assets/ and rewrite every reference.
renameSync(join(dest, '_next'), join(dest, 'assets'));
for (const f of walk(dest)) {
  if (!/\.(css|html|js)$/.test(f)) continue;
  const s = readFileSync(f, 'utf8');
  const t = s.replaceAll('./_next/', './assets/').replaceAll('/_next/', '/assets/');
  if (t !== s) { writeFileSync(f, t); fixed++; }
}
// Build manifests and the RSC navigation payloads are never requested (all links are plain page loads).
for (const f of walk(dest)) {
  const name = f.split(/[\\/]/).pop();
  if (name.startsWith('_') && name !== '_redirects') rmSync(f);
}
if (!existsSync(join(dest, 'index.html'))) throw new Error('preview export missing index.html');
console.log(`preview ready in out-preview/ (${fixed} files patched)`);
