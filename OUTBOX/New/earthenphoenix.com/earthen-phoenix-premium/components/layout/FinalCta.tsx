'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import Img from '@/components/ui/Img';
import Split from '@/components/ui/Split';
import { Arr } from '@/components/ui/Arrow';
import { BOOK, PHONE, TEL } from '@/lib/site';

/** The last scene on every page: her meadow opens from a framed print to the full width as you arrive. */
export default function FinalCta() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced }) => {
    if (reduced) return;
    const frame = ref.current!.querySelector<HTMLElement>('[data-frame]')!;
    const img = frame.querySelector('img')!;
    gsap.timeline({ scrollTrigger: { trigger: ref.current, start: 'top bottom', end: 'top 15%', scrub: 1 } })
      .fromTo(frame, { clipPath: 'inset(10% 7% 10% 7% round 32px)' }, { clipPath: 'inset(0% 0% 0% 0% round 0px)', ease: 'none' })
      .fromTo(img, { scale: 1.25 }, { scale: 1.02, ease: 'none' }, 0);
  });
  return (
    <section ref={ref} className="relative min-h-[100svh] flex items-end text-chalk" aria-labelledby="cta-h">
      <div data-frame className="absolute inset-0 overflow-hidden bg-moss">
        <Img name="yoga-assisted-fold" alt="" className="cover" pos="62% 50%" />
        <div className="absolute inset-0 bg-gradient-to-t from-night via-night/45 to-night/10" />
      </div>
      <div className="wrap relative pb-[clamp(56px,9vw,120px)] pt-40">
        <p className="kicker text-lichen" data-reveal>First time with us?</p>
        <Split as="h2" id="cta-h" className="display text-[clamp(2.8rem,7.6vw,7.4rem)] mt-6 max-w-[14ch]" text="Mention it when you book: _20% off_ your first service." />
        <div className="mt-10 flex flex-wrap gap-3" data-reveal data-delay="2">
          <a href={BOOK} className="btn btn-flame">Get an appointment <Arr /></a>
          <a href={TEL} className="btn btn-ghost">Call or text {PHONE}</a>
        </div>
      </div>
    </section>
  );
}
