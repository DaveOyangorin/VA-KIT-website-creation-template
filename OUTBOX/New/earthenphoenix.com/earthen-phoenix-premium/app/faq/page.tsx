import PageHero from '@/components/ui/PageHero';
import Faq from '@/components/ui/Faq';
import JsonLd from '@/components/ui/JsonLd';
import { Arr } from '@/components/ui/Arrow';
import { ALL_FAQ } from '@/lib/content';
import { BUSINESS, crumbsLd, faqLd, graph, pageMeta } from '@/lib/seo';
import { BOOK, absolute, href } from '@/lib/site';

const TITLE = 'Questions about Massage, Reiki & Yoga | Earthen Phoenix';
const DESC = 'Answers about Earthen Phoenix in Salt Lake City: booking, the 20% first-visit discount, massage, Sarga, Reiki, yoga, readings, herbal remedies and Miquelle’s training.';

export const metadata = pageMeta({ title: TITLE, desc: DESC, path: '/faq', og: 'sound-tuning-forks' });

export default function FaqPage() {
  const trail: [string, string][] = [['Home', '/'], ['Questions', '/faq']];
  return (
    <>
      <JsonLd data={graph(BUSINESS, { '@type': 'WebPage', url: absolute('/faq'), name: TITLE, description: DESC }, faqLd(ALL_FAQ.flatMap((g) => g.items)), crumbsLd(trail))} />
      <PageHero img="sound-tuning-forks" alt="Tuning forks resting beside a client on the massage table" pos="40% 50%" kicker="Questions" title="Good questions."
        answer="Short answers about booking, prices, what each session feels like, and Miquelle’s training." trail={trail}
        ctas={<><a href={BOOK} className="btn btn-flame">Get an appointment <Arr /></a><a href={href('/contact')} className="btn btn-ghost">Ask your own</a></>} />
      <section className="sec bg-mist">
        <div className="wrap grid gap-20">
          {ALL_FAQ.map((g, i) => (
            <div key={g.title} className="grid gap-8 lg:grid-cols-[minmax(0,4fr)_minmax(0,7fr)]" data-reveal>
              <div className="lg:sticky lg:top-[calc(var(--hdr)+32px)] self-start">
                <span className="font-display italic text-3xl text-clay">{['i', 'ii', 'iii', 'iv', 'v'][i]}.</span>
                <h2 className="h3 mt-3">{g.title}</h2>
              </div>
              <Faq items={g.items} />
            </div>
          ))}
        </div>
      </section>
    </>
  );
}
