import PageHero from '@/components/ui/PageHero';
import SessionsIndex from '@/components/ui/SessionsIndex';
import Faq from '@/components/ui/Faq';
import Split from '@/components/ui/Split';
import JsonLd from '@/components/ui/JsonLd';
import { Arr } from '@/components/ui/Arrow';
import { SERVICES, SESSIONS_FAQ } from '@/lib/content';
import { BUSINESS, crumbsLd, faqLd, graph, pageMeta } from '@/lib/seo';
import { BOOK, absolute } from '@/lib/site';

const TITLE = 'Sessions & Prices: Massage, Bodywork, Reiki, Yoga | Earthen Phoenix';
const DESC = 'Every Earthen Phoenix session and price in Salt Lake City: Reiki $130, Swedish from $140, deep tissue and Thai from $150, lymphatic and Sarga $180, Zen mountain $200, yoga $140, readings $2/min.';

export const metadata = pageMeta({ title: TITLE, desc: DESC, path: '/sessions', og: 'yoga-assisted-fold' });

export default function Sessions() {
  const trail: [string, string][] = [['Home', '/'], ['Sessions & prices', '/sessions']];
  return (
    <>
      <JsonLd data={graph(
        BUSINESS,
        { '@type': 'WebPage', url: absolute('/sessions'), name: TITLE, description: DESC },
        { '@type': 'ItemList', name: 'Earthen Phoenix sessions', itemListElement: SERVICES.map((s, i) => ({ '@type': 'ListItem', position: i + 1, url: absolute('/' + s.slug), name: s.full })) },
        faqLd(SESSIONS_FAQ), crumbsLd(trail),
      )} />
      <PageHero img="yoga-assisted-fold" alt="Miquelle guiding a student into a forward bend on a grassy hillside" pos="60% 45%" kicker="Ten sessions" title="Sessions and prices."
        answer="Ten kinds of session with Miquelle, from $130 Reiki to the $200 Zen mountain massage. Readings are $2 a minute." spec={[['From', '$130'], ['Sessions', '10'], ['First visit', '20% off']]}
        trail={trail} ctas={<><a href="#prices" className="btn btn-flame">See every price <Arr /></a><a href={BOOK} className="btn btn-ghost">Book</a></>} />
      <section id="prices" className="sec bg-mist" aria-labelledby="prices-h">
        <div className="wrap">
          <div className="grid gap-8 lg:grid-cols-2 items-end mb-16">
            <div>
              <p className="kicker" data-reveal>As listed on the booking page</p>
              <Split as="h2" id="prices-h" className="h2 mt-6" text="Every price, _one list._" />
            </div>
            <p className="text-ink-2 measure" data-reveal>Ordered from hands that hover to her full body weight, then the sessions beyond the table. Open any one to see how it works. New clients: mention it when you book for 20% off your first service.</p>
          </div>
          <SessionsIndex />
          <p className="mt-10 text-ink-2 measure" data-reveal>Herbal remedy prices vary with the consultation and the cost of herbs at the time of purchase.</p>
        </div>
      </section>
      <section className="sec bg-chalk" aria-labelledby="faq-h">
        <div className="wrap grid gap-12 lg:grid-cols-[minmax(0,4fr)_minmax(0,7fr)]">
          <div>
            <p className="kicker" data-reveal>Before you book</p>
            <Split as="h2" id="faq-h" className="h2 mt-6" text="Asked _and answered._" />
          </div>
          <div data-reveal><Faq items={SESSIONS_FAQ} /></div>
        </div>
      </section>
    </>
  );
}
