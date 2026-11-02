import Hero from '@/components/home/Hero';
import Statement from '@/components/home/Statement';
import Register from '@/components/home/Register';
import TwoPlaces from '@/components/home/TwoPlaces';
import Meet from '@/components/home/Meet';
import FirstVisit from '@/components/home/FirstVisit';
import Voices from '@/components/home/Voices';
import Shelf from '@/components/home/Shelf';
import Split from '@/components/ui/Split';
import JsonLd from '@/components/ui/JsonLd';
import { BUSINESS, graph, pageMeta } from '@/lib/seo';
import { absolute, href } from '@/lib/site';
import { SERVICES } from '@/lib/content';

const TITLE = 'Massage, Yoga & Reiki in Salt Lake City | Earthen Phoenix';
const DESC = 'Earthen Phoenix in Salt Lake City: massage, Thai and Sarga bodywork, Reiki, private yoga, astrology, tarot and herbal remedies with Miquelle. Ground your soul.';

export const metadata = pageMeta({ title: TITLE, desc: DESC, path: '/' });

export default function Home() {
  return (
    <>
      <JsonLd data={graph(
        BUSINESS,
        { '@type': 'WebSite', url: absolute('/'), name: 'Earthen Phoenix', inLanguage: 'en-US' },
        { '@type': 'WebPage', url: absolute('/'), name: TITLE, description: DESC },
        { '@type': 'ItemList', name: 'Earthen Phoenix sessions', itemListElement: SERVICES.map((s, i) => ({ '@type': 'ListItem', position: i + 1, url: absolute('/' + s.slug), name: s.full })) },
      )} />
      <Hero />
      <Statement />
      <Register />
      <TwoPlaces />
      <Meet />
      <FirstVisit />
      <Voices />
      <section className="sec bg-mist" aria-labelledby="shelf-h">
        <div className="wrap">
          <div className="flex flex-wrap items-end justify-between gap-6 mb-14">
            <div>
              <p className="kicker" data-reveal>Take the care home</p>
              <Split as="h2" id="shelf-h" className="h2 mt-6" text="Oils _and butter._" />
            </div>
            <a href={href('/products')} className="ulink" data-reveal>All products</a>
          </div>
          <Shelf />
        </div>
      </section>
    </>
  );
}
