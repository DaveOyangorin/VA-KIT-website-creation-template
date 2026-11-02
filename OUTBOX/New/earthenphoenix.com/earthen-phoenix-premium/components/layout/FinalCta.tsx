'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import Img from '@/components/ui/Img';
import { Arr } from '@/components/ui/Arrow';
import { BOOK, PHONE, TEL } from '@/lib/site';

/**
 * The closing scene on every page, the mirror of the opening: the meadow fills the screen, then folds back
 * into a small circle of light on linen as the invitation to book settles around it.
 */
export default function FinalCta() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    const q = gsap.utils.selector(el);
    if (reduced) { gsap.set(q('[data-circle]'), { clipPath: 'inset(0% 30% 40% 30% round 999px)' }); return; }
    gsap.timeline({ scrollTrigger: { trigger: el, start: 'top top', end: 'bottom bottom', scrub: 0.8 } })
      .fromTo(q('[data-circle]'), { clipPath: 'inset(0% 0% 0% 0% round 0px)' }, { clipPath: 'inset(16% 34% 38% 34% round 999px)', ease: 'power2.inOut' }, 0)
      .fromTo(q('[data-circle] img'), { scale: 1 }, { scale: 1.25, ease: 'none' }, 0)
      .fromTo(q('[data-copy] > *'), { y: 50, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.06, ease: 'power2.out', duration: 0.4 }, 0.5);
  });
  return (
    <section ref={ref} className="relative h-[220svh] motion-reduce:h-auto bg-mist" aria-labelledby="cta-h">
      <div className="sticky top-0 h-[100svh] overflow-hidden">
        <div data-circle className="absolute inset-0 overflow-hidden">
          <Img name="mountain-meadow" alt="" className="cover" pos="58% 40%" />
        </div>
        <div data-copy className="absolute inset-x-0 bottom-[7svh] text-center px-[var(--gutter)]">
          <p className="kicker !gap-0 before:!hidden text-lichen">First time with us?</p>
          <h2 id="cta-h" className="font-display text-[clamp(2.6rem,7vw,7rem)] leading-[0.92] tracking-[-0.035em] mt-4">
            Mention it when you book: <em className="text-flame">20% off.</em>
          </h2>
          <div className="mt-8 flex flex-wrap justify-center gap-3">
            <a href={BOOK} className="btn btn-flame">Get an appointment <Arr /></a>
            <a href={TEL} className="btn btn-ghost">Call or text {PHONE}</a>
          </div>
        </div>
      </div>
    </section>
  );
}
