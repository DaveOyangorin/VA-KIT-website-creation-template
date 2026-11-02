import { imgSet, type ImageName } from '@/lib/images';
import type { CSSProperties } from 'react';

/** Responsive <img> for her photos: 800w and 1600w sources, lazy unless `eager`. */
export default function Img({ name, alt, sizes = '100vw', eager, className, style, pos }: {
  name: ImageName; alt: string; sizes?: string; eager?: boolean; className?: string; style?: CSSProperties; pos?: string;
}) {
  const s = imgSet(name);
  return (
    // eslint-disable-next-line @next/next/no-img-element
    <img
      src={s.src} srcSet={s.srcSet} sizes={s.srcSet ? sizes : undefined} width={s.width} height={s.height} alt={alt}
      className={className} style={pos ? { objectPosition: pos, ...style } : style}
      loading={eager ? 'eager' : 'lazy'} decoding={eager ? 'sync' : 'async'} fetchPriority={eager ? 'high' : undefined}
    />
  );
}
