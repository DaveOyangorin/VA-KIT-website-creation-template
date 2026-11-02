import { SERVICES } from '@/lib/content';
import { BOOK, EMAIL, PHONE, TEL, asset, href } from '@/lib/site';
import FinalCta from './FinalCta';

export default function Footer() {
  const body = SERVICES.filter((s) => ['swedish', 'deep', 'thai', 'lymph', 'sarga', 'zen'].includes(s.key));
  const more = SERVICES.filter((s) => ['reiki', 'yoga', 'astro', 'herbs'].includes(s.key));
  const col = 'grid content-start gap-2.5 text-[.98rem]';
  return (
    <footer className="bg-night text-chalk">
      <FinalCta />
      <div className="wrap pt-24 pb-10">
        <div className="grid gap-14 lg:grid-cols-[1.4fr_1fr_1fr_1fr]">
          <div>
            <p className="display text-[clamp(3rem,6vw,5.6rem)]">Ground<br /><em className="text-flame">your soul.</em></p>
            <p className="mt-6 max-w-[36ch] text-chalk/70">Massage, bodywork, Reiki, yoga, readings and herbal remedies with Miquelle in Salt Lake City, Utah.</p>
            <a href={BOOK} className="btn btn-flame mt-8">Book a session</a>
          </div>
          <nav aria-label="Massage and bodywork" className={col}>
            <p className="kicker text-lichen mb-3">Massage &amp; bodywork</p>
            {body.map((s) => <a key={s.key} className="ulink justify-self-start" href={href('/' + s.slug)}>{s.name}</a>)}
          </nav>
          <nav aria-label="More sessions" className={col}>
            <p className="kicker text-lichen mb-3">More sessions</p>
            {more.map((s) => <a key={s.key} className="ulink justify-self-start" href={href('/' + s.slug)}>{s.name}</a>)}
            <a className="ulink justify-self-start" href={href('/sessions')}>All sessions &amp; prices</a>
            <a className="ulink justify-self-start" href={href('/products')}>Products</a>
          </nav>
          <div className={col}>
            <p className="kicker text-lichen mb-3">Visit</p>
            <a className="ulink justify-self-start" href={href('/about')}>About Miquelle</a>
            <a className="ulink justify-self-start" href={href('/faq')}>Questions</a>
            <a className="ulink justify-self-start" href={href('/contact')}>Contact</a>
            <a className="ulink justify-self-start" href={TEL}>{PHONE}</a>
            <a className="ulink justify-self-start" href={`mailto:${EMAIL}`}>{EMAIL}</a>
            <p className="text-chalk/60 mt-2">Salt Lake City, Utah</p>
          </div>
        </div>
        <div className="mt-20 pt-6 border-t border-chalk/10 flex flex-wrap items-center justify-between gap-4 text-sm text-chalk/55">
          <span className="flex items-center gap-3">
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={asset('img/ep-mark.png')} alt="" width={26} height={26} loading="lazy" />
            © 2026 Earthen Phoenix · Salt Lake City, Utah
          </span>
          <span>All photographs are Earthen Phoenix’s own.</span>
        </div>
      </div>
    </footer>
  );
}
