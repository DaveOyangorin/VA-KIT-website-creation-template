import type { Metadata } from 'next';
import { EMAIL, PHONE, SITE_URL, absolute } from './site';
import type { QA, Service } from './content';
import type { ImageName } from './images';

const strip = (s: string) => s.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1');

export function pageMeta({ title, desc, path, og = 'mountain-meadow', noindex }: { title: string; desc: string; path: string; og?: ImageName; noindex?: boolean }): Metadata {
  const url = absolute(path === '/' ? '/' : path);
  const image = absolute(`/img/${og}-1600.webp`);
  return {
    title: { absolute: title },
    description: desc,
    alternates: { canonical: url },
    robots: noindex ? { index: false, follow: true } : { index: true, follow: true, 'max-image-preview': 'large' },
    openGraph: { type: 'website', siteName: 'Earthen Phoenix', title, description: desc, url, images: [{ url: image }], locale: 'en_US' },
    twitter: { card: 'summary_large_image', title, description: desc, images: [image] },
  };
}

export const BUSINESS = {
  '@type': 'HealthAndBeautyBusiness',
  '@id': SITE_URL + '/#business',
  name: 'Earthen Phoenix',
  url: SITE_URL + '/',
  slogan: 'Ground your soul',
  telephone: '+1-' + PHONE,
  email: EMAIL,
  image: absolute('/img/mountain-meadow-1600.webp'),
  logo: absolute('/img/earthen-phoenix-logo-800.webp'),
  address: { '@type': 'PostalAddress', addressLocality: 'Salt Lake City', addressRegion: 'UT', addressCountry: 'US' },
  areaServed: { '@type': 'City', name: 'Salt Lake City' },
  founder: {
    '@type': 'Person', name: 'Miquelle', jobTitle: 'Master Reiki practitioner, massage therapist and yoga teacher',
    alumniOf: { '@type': 'CollegeOrUniversity', name: 'Utah College of Massage Therapy' },
  },
};

export const graph = (...nodes: object[]) => ({ '@context': 'https://schema.org', '@graph': nodes });

export const faqLd = (qa: QA[]) => ({
  '@type': 'FAQPage',
  mainEntity: qa.map(([q, a]) => ({ '@type': 'Question', name: q, acceptedAnswer: { '@type': 'Answer', text: strip(a).replace('(BOOK)', '') } })),
});

export const crumbsLd = (trail: [string, string][]) => ({
  '@type': 'BreadcrumbList',
  itemListElement: trail.map(([name, p], i) => ({ '@type': 'ListItem', position: i + 1, name, item: absolute(p) })),
});

export const serviceLd = (s: Service) => ({
  '@type': 'Service',
  name: s.full,
  serviceType: s.full,
  description: s.seo.ld,
  provider: { '@id': SITE_URL + '/#business' },
  areaServed: { '@type': 'City', name: 'Salt Lake City' },
  url: absolute('/' + s.slug),
  ...(s.offers.length ? { offers: s.offers.map((o) => ({ '@type': 'Offer', price: o.price, priceCurrency: 'USD', description: o.label })) } : {}),
});
