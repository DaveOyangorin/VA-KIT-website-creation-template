import PageHero from '@/components/ui/PageHero';
import Shelf from '@/components/home/Shelf';
import Split from '@/components/ui/Split';
import JsonLd from '@/components/ui/JsonLd';
import { Arr } from '@/components/ui/Arrow';
import { PRODUCTS } from '@/lib/content';
import { BUSINESS, crumbsLd, graph, pageMeta } from '@/lib/seo';
import { PHONE, SITE_URL, STORE, absolute, href } from '@/lib/site';

const TITLE = 'Body Oil, Face Oil & Body Butter | Earthen Phoenix';
const DESC = 'Take the care home: Armature Aurora Signature Body Oil ($44), Armature Smooth Sailing Face Oil ($55) and M’s Secret Body Butter ($44) from Earthen Phoenix in Salt Lake City.';

export const metadata = pageMeta({ title: TITLE, desc: DESC, path: '/products', og: 'armature-aurora-body-oil' });

export default function Products() {
  const trail: [string, string][] = [['Home', '/'], ['Products', '/products']];
  return (
    <>
      <JsonLd data={graph(
        BUSINESS, { '@type': 'WebPage', url: absolute('/products'), name: TITLE, description: DESC }, crumbsLd(trail),
        ...PRODUCTS.map((p) => ({ '@type': 'Product', name: p.name, image: absolute(`/img/${p.img}-800.webp`),
          offers: { '@type': 'Offer', price: p.price.slice(1), priceCurrency: 'USD', url: STORE[p.store], seller: { '@id': SITE_URL + '/#business' } } })),
      )} />
      <PageHero img="armature-aurora-body-oil" alt="Amber bottles of body oil on a white shell dish" pos="50% 60%" kicker="Oils and butter" title="Take it home."
        answer="Two Armature oils and M’s Secret Body Butter, from $44. Checkout happens in the Earthen Phoenix online store."
        spec={[['From', '$44'], ['Products', '3'], ['Checkout', 'Online store']]} trail={trail}
        ctas={<a href="#shelf" className="btn btn-flame">See the shelf <Arr /></a>} />
      <section id="shelf" className="sec bg-mist" aria-labelledby="shelf-h">
        <div className="wrap">
          <p className="kicker" data-reveal>The shelf</p>
          <Split as="h2" id="shelf-h" className="h2 mt-6 mb-14" text="Oils _and butter._" />
          <Shelf store />
          <p className="mt-14 text-ink-2" data-reveal>Need help choosing? <a className="underline underline-offset-4" href={href('/contact')}>Contact us</a> or call {PHONE}.</p>
        </div>
      </section>
    </>
  );
}
