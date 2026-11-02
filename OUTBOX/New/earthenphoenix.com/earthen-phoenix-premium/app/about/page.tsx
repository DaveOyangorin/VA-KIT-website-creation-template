import PageHero from '@/components/ui/PageHero';
import Split from '@/components/ui/Split';
import Img from '@/components/ui/Img';
import JsonLd from '@/components/ui/JsonLd';
import { Arr } from '@/components/ui/Arrow';
import { ABOUT_WORDS, CERTS } from '@/lib/content';
import { BUSINESS, crumbsLd, graph, pageMeta } from '@/lib/seo';
import { BOOK, absolute, href } from '@/lib/site';

const TITLE = 'About Miquelle, Massage Therapist & Reiki Master | Earthen Phoenix';
const DESC = 'Meet Miquelle of Earthen Phoenix: Reiki since 2011, Utah College of Massage Therapy graduate 2012, Master Reiki practitioner, yoga teacher, certified in Sarga, Thai, lymphatic and more.';

export const metadata = pageMeta({ title: TITLE, desc: DESC, path: '/about', og: 'miquelle-portrait' });

export default function About() {
  const trail: [string, string][] = [['Home', '/'], ['About', '/about']];
  return (
    <>
      <JsonLd data={graph(BUSINESS, { '@type': 'AboutPage', url: absolute('/about'), name: TITLE, description: DESC }, crumbsLd(trail))} />
      <PageHero img="mountain-meadow" alt="Mountains above the meadow where Miquelle teaches" pos="62% 40%" kicker="Meet Miquelle" title="Individual needs."
        answer="Miquelle founded Earthen Phoenix in Salt Lake City. She started with Reiki in 2011, graduated from the Utah College of Massage Therapy in 2012 and is now a Master Reiki practitioner."
        spec={[['Since', '2011'], ['Years', '13+'], ['Certified in', '10']]} trail={trail}
        ctas={<><a href={BOOK} className="btn btn-flame">Get an appointment <Arr /></a><a href={href('/sessions')} className="btn btn-ghost">Her sessions</a></>} />

      <section className="sec bg-mist" aria-labelledby="words-h">
        <div className="wrap grid gap-16 lg:grid-cols-[minmax(0,4fr)_minmax(0,6fr)] items-start">
          <div className="lg:sticky lg:top-[calc(var(--hdr)+32px)]">
            <div data-mask="up" className="relative mx-auto max-w-[360px] aspect-[9/16] overflow-hidden rounded-[22px] bg-moss">
              <Img name="miquelle-portrait" alt="Miquelle, founder of Earthen Phoenix, smiling at sunset on the water" className="cover" sizes="360px" />
            </div>
          </div>
          <div>
            <p className="kicker" data-reveal>In her words</p>
            <Split as="h2" id="words-h" className="h2 mt-6" text="Everyone is _extremely unique._" />
            <div className="mt-10 grid gap-6 text-[1.15rem] leading-relaxed text-ink-2 measure">
              {ABOUT_WORDS.map((p) => <p key={p} data-reveal>{p}</p>)}
            </div>
            <ol className="mt-16 grid sm:grid-cols-3 gap-px bg-ink/10 rounded-[22px] overflow-hidden" aria-label="Her path">
              {[['2011', 'Started with Reiki'], ['2012', 'Utah College of Massage Therapy'], ['Today', 'Master Reiki practitioner']].map(([y, t], i) => (
                <li key={y} className="bg-chalk p-6" data-reveal data-delay={i}>
                  <span className="font-display text-4xl tracking-[-0.02em]">{y}</span>
                  <span className="block mt-2 text-ink-2">{t}</span>
                </li>
              ))}
            </ol>
            <p className="kicker mt-16" data-reveal>Certified in</p>
            <ul className="mt-6 flex flex-wrap gap-2" data-reveal>
              {CERTS.map((c) => (
                <li key={c.name}>
                  {c.path
                    ? <a href={href(c.path)} className="inline-flex min-h-11 items-center rounded-full border border-ink/20 px-5 transition-colors duration-500 hover:bg-ink hover:text-chalk">{c.name}</a>
                    : <span className="inline-flex min-h-11 items-center rounded-full border border-ink/10 px-5 text-ink-2">{c.name}</span>}
                </li>
              ))}
            </ul>
          </div>
        </div>
      </section>

      <section className="relative sec bg-night text-chalk overflow-hidden" aria-label="The name">
        <div className="absolute inset-0 opacity-35" data-mask="centre">
          <div data-parallax="0.18" className="absolute -inset-y-[12%] inset-x-0"><Img name="reiki-crystals-candles" alt="" className="cover" pos="30% 30%" /></div>
        </div>
        <div className="absolute inset-0 bg-gradient-to-r from-night via-night/80 to-night/30" />
        <div className="wrap relative">
          <p className="kicker text-lichen" data-reveal>The name</p>
          <Split as="p" className="display text-[clamp(2.4rem,6vw,5.6rem)] mt-8 max-w-[18ch]" text="“In the face of adversity, remember that you are _a phoenix rising from the ashes._”" />
        </div>
      </section>
    </>
  );
}
