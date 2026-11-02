'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import Img from '@/components/ui/Img';
import { href } from '@/lib/site';

/** Pinned: the candlelit room gives way to the mountains as you scroll. Both are places her sessions happen. */
export default function TwoPlaces() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    if (reduced) { gsap.set(el.querySelector('[data-out]'), { clipPath: 'inset(0% 0% 0% 50%)' }); return; }
    const out = el.querySelector<HTMLElement>('[data-out]')!;
    const line = el.querySelector<HTMLElement>('[data-line]')!;
    const p = { v: 0 };
    const set = () => {
      const x = 100 - p.v * 100;
      out.style.clipPath = `inset(0% 0% 0% ${x}%)`;
      line.style.left = `${x}%`;
    };
    set();
    gsap.timeline({ scrollTrigger: { trigger: el, start: 'top top', end: '+=140%', scrub: 0.8, pin: true, anticipatePin: 1 } })
      .to(p, { v: 1, ease: 'none', onUpdate: set })
      .fromTo(el.querySelector('[data-in-img]'), { scale: 1 }, { scale: 1.12, ease: 'none' }, 0)
      .fromTo(out.querySelector('img'), { scale: 1.2, xPercent: 4 }, { scale: 1, xPercent: 0, ease: 'none' }, 0)
      .fromTo('[data-label-in]', { autoAlpha: 1 }, { autoAlpha: 0, ease: 'none', duration: 0.3 }, 0.55)
      .fromTo('[data-label-out]', { autoAlpha: 0 }, { autoAlpha: 1, ease: 'none', duration: 0.3 }, 0.6);
  });
  return (
    <section ref={ref} className="relative h-[100svh] overflow-hidden bg-night text-chalk" aria-labelledby="places-h">
      <div className="absolute inset-0 overflow-hidden">
        <div data-in-img className="absolute inset-0"><Img name="reiki-crystals-candles" alt="Candles and crystals around a client resting on the table" className="cover" pos="45% 50%" /></div>
      </div>
      <div data-out className="absolute inset-0 overflow-hidden" style={{ clipPath: 'inset(0% 0% 0% 100%)' }}>
        <Img name="mountain-meadow" alt="Miquelle with a student in a mountain meadow" className="cover" pos="62% 50%" />
      </div>
      <span data-line className="absolute top-0 bottom-0 w-px bg-chalk/70 left-full" aria-hidden />
      <div className="absolute inset-0 bg-gradient-to-b from-night/55 via-transparent to-night/70 pointer-events-none" />
      <div className="wrap relative h-full flex flex-col justify-between pt-[calc(var(--hdr)+40px)] pb-12">
        <div>
          <p className="kicker text-lichen">Two settings</p>
          <h2 id="places-h" className="h2 mt-5 max-w-[16ch]">Candlelight on the table. <em>A river in the mountains.</em></h2>
        </div>
        <div className="relative min-h-[140px]">
          <div data-label-in className="absolute bottom-0 max-w-[440px]">
            <p className="font-display text-3xl">Indoors</p>
            <p className="mt-2 text-chalk/80">Massage, bodywork, Reiki and body treatments, on the table with candles, crystals and essential oils.</p>
          </div>
          <div data-label-out className="absolute bottom-0 max-w-[440px] invisible">
            <p className="font-display text-3xl">Outdoors</p>
            <p className="mt-2 text-chalk/80">The <a className="underline underline-offset-4" href={href('/zen-mountain-session')}>Zen mountain session</a>: a private massage beside a peaceful mountain river.</p>
          </div>
        </div>
      </div>
    </section>
  );
}
