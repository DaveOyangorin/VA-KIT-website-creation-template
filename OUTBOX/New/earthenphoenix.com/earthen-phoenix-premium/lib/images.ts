import { asset } from './site';

/** Every photograph is Earthen Phoenix's own, carried over from the current site. */
export type ImageName =
  | 'mountain-meadow'
  | 'mountain-meadow-ridge'
  | 'yoga-assisted-fold'
  | 'massage-head-neck'
  | 'reiki-crystals-candles'
  | 'sound-tuning-forks'
  | 'sarga-barefoot-strap'
  | 'miquelle-portrait'
  | 'armature-aurora-body-oil'
  | 'armature-smooth-sailing-face-oil'
  | 'ms-secret-body-butter'
  | 'earthen-phoenix-logo';

type Variant = { w: number; h: number; file: string };

const V = (name: string, w: number, h: number, w2?: number, h2?: number): Variant[] => {
  const out: Variant[] = [{ w, h, file: `img/${name}-800.webp` }];
  if (w2 && h2) out.push({ w: w2, h: h2, file: `img/${name}-1600.webp` });
  return out;
};

export const IMAGES: Record<ImageName, Variant[]> = {
  'mountain-meadow': V('mountain-meadow', 800, 533, 1600, 1067),
  'mountain-meadow-ridge': V('mountain-meadow-ridge', 800, 533, 1600, 1067),
  'yoga-assisted-fold': V('yoga-assisted-fold', 800, 533, 1600, 1067),
  'massage-head-neck': V('massage-head-neck', 800, 1200, 1200, 1800),
  'reiki-crystals-candles': V('reiki-crystals-candles', 800, 450, 1600, 900),
  'sound-tuning-forks': V('sound-tuning-forks', 800, 450, 1600, 900),
  'sarga-barefoot-strap': [{ w: 750, h: 1334, file: 'img/sarga-barefoot-strap-800.webp' }],
  'miquelle-portrait': [{ w: 360, h: 640, file: 'img/miquelle-portrait-800.webp' }],
  'armature-aurora-body-oil': V('armature-aurora-body-oil', 800, 1067, 1350, 1800),
  'armature-smooth-sailing-face-oil': V('armature-smooth-sailing-face-oil', 800, 600, 1600, 1200),
  'ms-secret-body-butter': V('ms-secret-body-butter', 800, 796, 1070, 1064),
  'earthen-phoenix-logo': V('earthen-phoenix-logo', 800, 467, 1600, 933),
};

export function imgSrc(name: ImageName, large = false) {
  const v = IMAGES[name];
  return asset((large && v[1] ? v[1] : v[0]).file);
}

export function imgSet(name: ImageName) {
  const v = IMAGES[name];
  return {
    src: asset(v[0].file),
    srcSet: v.length > 1 ? v.map((x) => `${asset(x.file)} ${x.w}w`).join(', ') : undefined,
    width: v[0].w,
    height: v[0].h,
  };
}
