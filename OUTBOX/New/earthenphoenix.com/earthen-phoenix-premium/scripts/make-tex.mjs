// Inline copies of the session hero photos for the living photograph (components/three/LivingPhoto.tsx).
// A sandboxed preview can't upload the page's own <img> to WebGL, but a script-loaded data URL works anywhere.
import { readFileSync, writeFileSync, mkdirSync, existsSync } from 'node:fs';
const names = ['sound-tuning-forks', 'massage-head-neck', 'reiki-crystals-candles', 'yoga-assisted-fold', 'sarga-barefoot-strap', 'mountain-meadow', 'armature-smooth-sailing-face-oil'];
mkdirSync('public/tex', { recursive: true });
for (const n of names) {
  const f = [`public/img/${n}-1600.webp`, `public/img/${n}-800.webp`].find(existsSync);
  const b64 = readFileSync(f).toString('base64');
  writeFileSync(`public/tex/${n}.js`, `(window.__EPTEX=window.__EPTEX||{})[${JSON.stringify(n)}]="data:image/webp;base64,${b64}";\n`);
  console.log(n, Math.round(b64.length / 1024) + 'KB');
}
