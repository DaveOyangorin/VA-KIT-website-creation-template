/**
 * Site-wide constants and URL helpers.
 *
 * Two build targets share this code:
 *  - production (`npm run build`): clean URLs (/about) and root-absolute assets.
 *  - preview (`npm run build:preview`): every page is a flat .html file in one folder,
 *    linked by relative paths, so the export works inside a sub-folder or a sandboxed host.
 */
export const PREVIEW = process.env.NEXT_PUBLIC_EP_PREVIEW === '1';

export const SITE_URL = 'https://earthenphoenix.com';
export const BOOK = 'https://earthenphoenix.com/appointment-8682'; // live GoHighLevel calendar: see README before moving domains
export const PHONE = '801-609-4263';
export const TEL = 'tel:+18016094263';
export const SMS = 'sms:+18016094263';
export const EMAIL = 'info@earthenphoenix.com';

export const STORE = {
  aurora: 'https://earthenphoenix.com/product-details/product/67916113fbd2be1e2cb402bd',
  sailing: 'https://earthenphoenix.com/product-details/product/67916315fbd2be5dd0b40c2f',
  butter: 'https://earthenphoenix.com/product-details/product/6791441ef36f6cdd3681daa7',
};

/** Internal link: '/' | '/about' | '/about#faq' | '#prices' */
export function href(path: string): string {
  if (!PREVIEW || path.startsWith('#') || /^[a-z]+:/i.test(path)) return path;
  const [p, hash] = path.split('#');
  const base = p === '/' || p === '' ? 'index.html' : p.replace(/^\//, '') + '.html';
  return hash ? `${base}#${hash}` : base;
}

/** Public asset path: asset('img/x.webp') */
export function asset(p: string): string {
  return (PREVIEW ? '' : '/') + p.replace(/^\//, '');
}

export const absolute = (p: string) => SITE_URL + (p.startsWith('/') ? p : '/' + p);
