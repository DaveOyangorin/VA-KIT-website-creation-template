import type { ReactNode } from 'react';
import type { Service } from '@/lib/content';
import { BOOK, PHONE, TEL, href } from '@/lib/site';
import Img from '@/components/ui/Img';
import Split from '@/components/ui/Split';
import { Arr } from '@/components/ui/Arrow';
import { ReadingCost, YogaSplit } from './Calculators';

/** The practical part of each session page: lengths and prices, plus what is specific to that session. */
function Prices({ s }: { s: Service }) {
  if (!s.offers.length) return null;
  return (
    <dl className="grid grid-cols-2 gap-px bg-ink/10 rounded-[22px] overflow-hidden" data-reveal>
      {s.offers.map((o) => (
        <div key={o.label} className="bg-chalk p-6 sm:p-8 last:odd:col-span-2">
          <dt className="text-sm text-ink-2">{o.label}</dt>
          <dd className="mt-2 font-display text-[clamp(2.6rem,5vw,4rem)] leading-none tracking-[-0.03em] tabular-nums">${o.price}{s.key === 'astro' && <span className="text-xl text-ink-2"> / min</span>}</dd>
        </div>
      ))}
    </dl>
  );
}

function Note({ title, children }: { title: string; children: ReactNode }) {
  return (
    <div className="mt-8 rounded-[22px] border border-ink/12 p-6 sm:p-7" data-reveal>
      <p className="font-display text-xl">{title}</p>
      <div className="rich mt-2 text-ink-2">{children}</div>
    </div>
  );
}

function Shell({ kicker, title, left, right }: { kicker: string; title: string; left?: ReactNode; right: ReactNode }) {
  return (
    <section className="sec bg-mist" aria-label={kicker}>
      <div className="wrap grid gap-14 lg:grid-cols-2 items-start">
        <div>
          <p className="kicker" data-reveal>{kicker}</p>
          <Split as="h2" className="h2 mt-6" text={title} />
          {left && <div className="mt-8 lede text-ink-2 measure" data-reveal>{left}</div>}
        </div>
        <div>{right}</div>
      </div>
    </section>
  );
}

const Book = ({ label = 'Book this session' }: { label?: string }) => (
  <div className="mt-10 flex flex-wrap gap-3" data-reveal>
    <a href={BOOK} className="btn btn-ink">{label} <Arr /></a>
    <a href={TEL} className="btn btn-ghost">Call or text {PHONE}</a>
  </div>
);

export default function Details({ s }: { s: Service }) {
  switch (s.key) {
    case 'reiki':
      return <Shell kicker="Her training" title="Since _2011._"
        left={<p>Miquelle started with Reiki in 2011 and is now a Master Reiki practitioner. Sound therapy and breath-work are part of her training too.</p>}
        right={<><Prices s={s} /><Note title="Do I stay clothed?">Yes. Hands are placed gently on or near your clothed body.</Note><Book /></>} />;
    case 'swedish':
      return <Shell kicker="Choose your length" title="An hour, _or ninety minutes._"
        left={<p>Swedish can include sound therapy, meditation and breathwork, for stress relief and relaxation.</p>}
        right={<><Prices s={s} /><Note title="Want more pressure?">Swedish stays light to medium. For deep pressure with stretching, book <a href={href('/deep-tissue-massage')}>deep tissue</a>.</Note><Book /></>} />;
    case 'lymph':
      return <Shell kicker="One slow treatment" title="Ninety minutes, _six steps._"
        left={<p>The booking page describes it as a treatment for skin firming and for reducing bloating, water retention and inflammation. Choose it for a slow, full-body treatment rather than a pressure-focused massage.</p>}
        right={<><Prices s={s} /><Book /></>} />;
    case 'deep':
      return <Shell kicker="Choose your length" title="Deep, and _never painful._"
        left={<p>Tell Miquelle how much pressure you want and she adjusts. You leave with stretching guidance so the results last.</p>}
        right={<><Prices s={s} /><Note title="Is there anything deeper?"><a href={href('/sarga-bodywork')}>Sarga bodywork</a> goes deep into the fascia and suits old injuries. You need to be very comfortable with deep pressure.</Note><Book /></>} />;
    case 'thai':
      return (
        <section className="sec bg-mist" aria-label="Certified">
          <div className="wrap grid gap-14 lg:grid-cols-2 items-center">
            <div data-mask="up" className="relative aspect-[4/5] overflow-hidden rounded-[28px] bg-moss">
              <div data-parallax="0.12" className="absolute -inset-y-[8%] inset-x-0"><Img name="mountain-meadow" alt="Miquelle and a student in a mountain meadow" className="cover" pos="30% 50%" sizes="(max-width: 1023px) 92vw, 45vw" /></div>
            </div>
            <div>
              <p className="kicker" data-reveal>Certified</p>
              <Split as="h2" className="h2 mt-6" text="One of many ways _she works._" />
              <p className="lede mt-8 text-ink-2 measure" data-reveal>Miquelle is certified in Thai bodywork, alongside Sarga, lymphatic work, cupping, cranial-sacral therapy, sound therapy, reflexology, yoga, Reiki and breath-work.</p>
              <div className="mt-10"><Prices s={s} /></div>
              <Book />
            </div>
          </div>
        </section>
      );
    case 'sarga':
      return <Shell kicker="Honest about intensity" title="Is it _for you?_"
        left={<p>“Must be very comfortable with deep pressure to receive this.” Sarga can be somewhat uncomfortable during the session.</p>}
        right={<><Prices s={s} /><Note title="Deep work, less intensity">Try <a href={href('/deep-tissue-massage')}>deep tissue massage</a>: deep pressure with breathwork and stretching, never painful.</Note><Book /></>} />;
    case 'zen':
      return <Shell kicker="One private session" title="Ninety minutes _outside._"
        left={<p>A private massage beside a peaceful mountain river, combining therapeutic massage with nature for relaxation and a reset.</p>}
        right={<><Prices s={s} /><Note title="Location and season">Call or text <a href={TEL}>{PHONE}</a> and ask Miquelle where and when.</Note>
          <div className="mt-10 flex flex-wrap gap-3" data-reveal><a href={TEL} className="btn btn-ink">Ask about location and season <Arr /></a><a href={BOOK} className="btn btn-ghost">Booking page</a></div></>} />;
    case 'yoga':
      return <Shell kicker="Private or split" title="One price, _shared how you like._"
        left={<p>Book the hour for yourself, or split it between group participants. The session is $140 either way.</p>}
        right={<div className="rounded-[26px] bg-chalk p-7 sm:p-10" data-reveal><YogaSplit /><Book label="Book private yoga" /></div>} />;
    case 'astro':
      return <Shell kicker="Priced by the minute" title="$2 _a minute._"
        left={<><p>Astrology offers a unique understanding of our conscious and subconscious selves, primarily through our birth charts. A reading uses your full birth chart.</p><p className="mt-4">Tarot and oracle readings are about the present moment.</p></>}
        right={<div className="rounded-[26px] bg-chalk p-7 sm:p-10" data-reveal><ReadingCost /><Book label="Book a reading" /></div>} />;
    case 'herbs':
      return (
        <section className="sec bg-mist" aria-label="How it works">
          <div className="wrap">
            <p className="kicker" data-reveal>How it works</p>
            <Split as="h2" className="h2 mt-6 max-w-[16ch]" text="From a conversation _to a remedy._" />
            <ol className="mt-14 grid gap-px bg-ink/10 rounded-[24px] overflow-hidden sm:grid-cols-2 lg:grid-cols-4">
              {[['A consultation', 'You and Miquelle talk through what you need.'], ['Herbs are ordered', 'From Mountain Rose Herbs in Oregon.'], ['One to two weeks', 'Allow that long for the herbs to arrive.'], ['Your remedy', 'Made for you: a tea, a rollie or a tincture.']].map(([t, d], i) => (
                <li key={t} className="bg-chalk p-7" data-reveal data-delay={i}>
                  <span className="font-display italic text-3xl text-clay">{['i', 'ii', 'iii', 'iv'][i]}.</span>
                  <h3 className="h3 mt-6">{t}</h3>
                  <p className="mt-2 text-ink-2">{d}</p>
                </li>
              ))}
            </ol>
            <div className="mt-10 grid gap-8 lg:grid-cols-[auto_1fr] items-end" data-reveal>
              <p className="font-display text-[clamp(2.6rem,5vw,4rem)] leading-none tracking-[-0.03em]">$40–$100</p>
              <p className="text-ink-2 max-w-[60ch]">Approximate. Customization, consultation and pricing vary with time and herb prices at the time of purchase.</p>
            </div>
            <div className="mt-10 flex flex-wrap gap-3" data-reveal><a href={BOOK} className="btn btn-ink">Book a consultation <Arr /></a><a href={href('/contact')} className="btn btn-ghost">Ask about herbs</a></div>
          </div>
        </section>
      );
  }
}
