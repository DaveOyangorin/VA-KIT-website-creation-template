import type { ServiceKey } from './content';

/** Each session's colour, from the bands of her logo (used on the home chapters and as the tint of its own page). */
export const SESSION_COLOR: Record<ServiceKey, string> = {
  reiki: 'var(--color-saffron)', swedish: 'var(--color-rose)', lymph: 'var(--color-tangerine)', deep: 'var(--color-poppy)', thai: 'var(--color-forest)',
  sarga: 'var(--color-cacao)', zen: 'var(--color-meadow)', yoga: 'var(--color-saffron)', astro: 'var(--color-tangerine)', herbs: 'var(--color-forest)',
};
