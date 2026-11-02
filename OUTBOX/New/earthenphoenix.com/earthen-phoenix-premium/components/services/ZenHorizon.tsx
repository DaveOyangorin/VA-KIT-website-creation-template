'use client';
import { useRef, useState } from 'react';
import type { Service } from '@/lib/content';
import { gsap, ScrollTrigger, useGsap } from '@/lib/anim';
import Img from '@/components/ui/Img';
import SigCopy from './SigCopy';

/**
 * Zen mountain: ninety minutes outside. Her mountain photograph starts as a thin strip, like a view through a gap
 * in the trees, and opens to the full width the longer you stay. The drift slows as it opens, and a clock counts
 * the session's ninety minutes.
 */
export default function ZenHorizon({ s }: { s: Service }) {
  const ref = useRef<HTMLElement>(null);
  const [mins, setMins] = useState(0);

  useGsap(ref, ({ reduced, el }) => {
    const frame = el.querySelector<HTMLElement>('[data-frame]')!;
    const img = frame.querySelector('img')!;
    if (reduced) { setMins(90); return; }
    const tl = gsap.timeline({ paused: true, defaults: { ease: 'none' } })
      .fromTo(frame, { clipPath: 'inset(44% 8% 44% 8% round 999px)' }, { clipPath: 'inset(0% 0% 0% 0% round 0px)', ease: 'power2.inOut', duration: 1 }, 0)
      .fromTo(img, { scale: 1.45, xPercent: -6 }, { scale: 1, xPercent: 0, ease: 'power3.out', duration: 1 }, 0)
      .fromTo(el.querySelectorAll('[data-line]'), { autoAlpha: 0, y: 20 }, { autoAlpha: 1, y: 0, stagger: 0.18, duration: 0.2 }, 0.35);
    const st = ScrollTrigger.create({
      trigger: el.querySelector('[data-track]'), start: 'top top', end: 'bottom bottom', scrub: 1.2,
      onUpdate: (self) => { tl.progress(self.progress); setMins(Math.round(self.progress * 90)); },
    });
    return () => { st.kill(); tl.kill(); };
  });

  return (
    <section ref={ref} className="bg-night text-chalk" aria-labelledby="sig-h">
      <div className="sec wrap pb-0">
        <SigCopy s={s} />
      </div>
      <div data-track className="relative h-[260svh] mt-16">
        <div className="sticky top-0 h-[100svh] overflow-hidden">
          <div data-frame className="absolute inset-0 overflow-hidden">
            <Img name={s.img} alt={s.alt} className="cover" pos="50% 40%" sizes="100vw" />
            <div className="absolute inset-0 bg-gradient-to-t from-night/70 via-transparent to-night/30" />
          </div>
          <div className="relative h-full wrap flex flex-col justify-end pb-[clamp(32px,6vw,72px)]">
            <div className="flex flex-wrap items-end justify-between gap-8">
              <p className="font-display font-light text-[clamp(2.2rem,5.5vw,5rem)] leading-[0.95] tracking-[-0.03em]">
                <span data-line className="block">Mountain air.</span>
                <span data-line className="block">A peaceful river.</span>
                <span data-line className="block italic text-amber">Ninety minutes.</span>
              </p>
              <p className="text-right" aria-live="off">
                <span className="block font-display text-[clamp(3rem,7vw,6rem)] leading-none tabular-nums">{mins}</span>
                <span className="text-xs uppercase tracking-[.2em] text-chalk/70">of 90 minutes</span>
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
