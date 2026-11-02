'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import { VOICES } from '@/lib/content';
import Img from '@/components/ui/Img';

/** Scene 5. Her clients' words, one at a time, over the hillside as it slowly pulls back. */
export default function Voices() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    if (reduced) return;
    const q = gsap.utils.selector(el);
    const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: 'top top', end: 'bottom bottom', scrub: 0.7 } });
    tl.fromTo(q('[data-bg]'), { scale: 1.3 }, { scale: 1, ease: 'none', duration: 3 }, 0);
    q('[data-quote]').forEach((node, i) => {
      tl.fromTo(node, { autoAlpha: 0, y: 50 }, { autoAlpha: 1, y: 0, duration: 0.35 }, i)
        .to(node, { autoAlpha: 0, y: -40, duration: 0.3 }, i + 0.75);
    });
  });
  return (
    <section ref={ref} className="relative h-[320svh] motion-reduce:h-auto" aria-label="Client words">
      <div className="sticky top-0 h-[100svh] overflow-hidden text-chalk motion-reduce:static motion-reduce:h-auto motion-reduce:py-32">
        <div data-bg className="absolute inset-0"><Img name="yoga-assisted-fold" alt="" className="cover" pos="60% 50%" /></div>
        <div className="absolute inset-0 bg-night/55" />
        <p className="absolute top-[calc(var(--hdr)+24px)] left-[var(--gutter)] kicker">Client words</p>
        {VOICES.map((v) => (
          <figure key={v.name} data-quote className="absolute inset-0 grid place-items-center px-[var(--gutter)] text-center motion-safe:opacity-0 motion-reduce:relative motion-reduce:py-12">
            <div>
              <blockquote className="font-display text-[clamp(2rem,5.2vw,5.4rem)] leading-[1.04] tracking-[-0.025em] max-w-[22ch] mx-auto font-medium [text-shadow:0_2px_30px_rgba(0,0,0,.35)]">“{v.quote}”</blockquote>
              <figcaption className="mt-8 text-sm uppercase tracking-[.25em] text-chalk/85">{v.name}</figcaption>
            </div>
          </figure>
        ))}
      </div>
    </section>
  );
}
