import { CalendarDays, Mail, MessageSquare, Phone } from 'lucide-react';
import PageHero from '@/components/ui/PageHero';
import NoteForm from '@/components/ui/NoteForm';
import Split from '@/components/ui/Split';
import JsonLd from '@/components/ui/JsonLd';
import { Arr } from '@/components/ui/Arrow';
import { BUSINESS, crumbsLd, graph, pageMeta } from '@/lib/seo';
import { BOOK, EMAIL, PHONE, SMS, TEL, absolute } from '@/lib/site';

const TITLE = 'Contact & Booking | Earthen Phoenix, Salt Lake City';
const DESC = 'Book Earthen Phoenix online, call or text 801-609-4263, or email info@earthenphoenix.com. Massage, Reiki, yoga and readings in Salt Lake City. 20% off your first service.';

export const metadata = pageMeta({ title: TITLE, desc: DESC, path: '/contact', og: 'reiki-crystals-candles' });

const WAYS = [
  { icon: CalendarDays, label: 'Book online', value: 'Booking page', to: BOOK },
  { icon: Phone, label: 'Call', value: PHONE, to: TEL },
  { icon: MessageSquare, label: 'Text', value: PHONE, to: SMS },
  { icon: Mail, label: 'Email', value: EMAIL, to: `mailto:${EMAIL}` },
];

export default function Contact() {
  const trail: [string, string][] = [['Home', '/'], ['Contact', '/contact']];
  return (
    <>
      <JsonLd data={graph(BUSINESS, { '@type': 'ContactPage', url: absolute('/contact'), name: TITLE, description: DESC }, crumbsLd(trail))} />
      <PageHero img="reiki-crystals-candles" alt="Lit candles and crystals around a client on the massage table" pos="45% 50%" kicker="Contact and booking" title="Reach out."
        answer="Feel free to contact me with any questions anytime. Book online, call or text 801-609-4263, or email info@earthenphoenix.com."
        spec={[['Phone', PHONE], ['Where', 'Salt Lake City'], ['First visit', '20% off']]} trail={trail}
        ctas={<><a href={BOOK} className="btn btn-flame">Get an appointment <Arr /></a><a href={TEL} className="btn btn-ghost">Call or text</a></>} />
      <section className="sec bg-mist text-ink" aria-labelledby="ways-h">
        <div className="wrap grid gap-14 lg:grid-cols-2 items-start">
          <div>
            <p className="kicker text-lichen" data-reveal>Ways in</p>
            <Split as="h2" id="ways-h" className="h2 mt-6" text="Call, text, _or write._" />
            <ul className="mt-12">
              {WAYS.map(({ icon: Icon, label, value, to }, i) => (
                <li key={label} className="border-t border-ink/12 last:border-b" data-reveal data-delay={i}>
                  <a href={to} className="group flex items-center gap-5 py-6">
                    <span className="grid place-items-center size-12 rounded-full border border-ink/20 transition-colors duration-500 group-hover:bg-flame group-hover:border-flame group-hover:text-chalk"><Icon size={19} strokeWidth={1.5} aria-hidden /></span>
                    <span className="grid">
                      <span className="text-xs uppercase tracking-[.2em] text-ink-2">{label}</span>
                      <span className="text-[clamp(1.2rem,2vw,1.6rem)] font-medium tracking-[-0.01em] transition-transform duration-700 group-hover:translate-x-2">{value}</span>
                    </span>
                  </a>
                </li>
              ))}
            </ul>
            <p className="mt-8 text-ink-2 measure" data-reveal>Earthen Phoenix is in Salt Lake City, Utah. The Zen mountain session happens outdoors beside a mountain river; ask Miquelle about its location and season.</p>
          </div>
          <div data-reveal data-delay="1"><NoteForm /></div>
        </div>
      </section>
    </>
  );
}
