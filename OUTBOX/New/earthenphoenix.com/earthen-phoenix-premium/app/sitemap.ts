import type { MetadataRoute } from 'next';
import { SERVICES } from '@/lib/content';
import { absolute } from '@/lib/site';

export const dynamic = 'force-static';

export default function sitemap(): MetadataRoute.Sitemap {
  const paths = ['/', '/sessions', ...SERVICES.map((s) => '/' + s.slug), '/about', '/products', '/faq', '/contact'];
  return paths.map((p) => ({ url: absolute(p), lastModified: '2026-11-02', changeFrequency: 'monthly', priority: p === '/' ? 1 : p === '/sessions' ? 0.9 : 0.7 }));
}
