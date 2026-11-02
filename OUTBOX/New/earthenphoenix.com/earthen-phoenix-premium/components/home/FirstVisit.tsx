'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import Split from '@/components/ui/Split';
import { BOOK, PHONE, TEL, href } from '@/lib/site';

/** Three steps on a single line that draws itself as you read. */
export default function FirstVisit() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    if (reduced) return;
    const path = el.querySelector<SVGPathElement>('[data-path]')!;
    gsap.fromTo(path, { strokeDashoffset: 1 }, { strokeDashoffset: 0, ease: 'none', scrollTrigger: { trigger: el.querySelector('ol'), start: 'top 75%', end: 'bottom 60%', scrub: true } });
    el.querySelectorAll<HTMLElement>('[data-step]').forEach((s) => {
      gsap.fromTo(s.querySelector('[data-dot]'), { scale: 0 }, { scale: 1, duration: 0.8, ease: 'back.out(3)', scrollTrigger: { trigger: s, start: 'top 72%', once: true } });
    });
  });
  const steps = [
    { t: 'Choose, or ask', d: <>Pick a session. Not sure which? Call or text <a className="underline underline-offset-4" href={TEL}>{PHONE}</a> and Miquelle will help you choose.</> },
    { t: 'Book online or by phone', d: <>Use the <a className="underline underline-offset-4" href={BOOK}>booking page</a>, or call or text. First time? Mention it for 20% off your first service.</> },
    { t: 'A session built around you', d: <>Anything from light and relaxing to deep fascial work, based on your individual needs. <a className="underline underline-offset-4" href={href('/faq')}>Questions first?</a></> },
  ];
  return (
    <section ref={ref} className="sec bg-chalk" aria-labelledby="visit-h">
      <div className="wrap grid gap-14 lg:grid-cols-[minmax(0,4fr)_minmax(0,6fr)]">
        <div className="lg:sticky lg:top-[calc(var(--hdr)+40px)] self-start">
          <p className="kicker" data-reveal>Your first visit</p>
          <Split as="h2" id="visit-h" className="h2 mt-6" text="Three steps, _no guesswork._" />
        </div>
        <div className="relative">
          <svg className="absolute left-[19px] top-4 h-[calc(100%-32px)] w-2 overflow-visible" preserveAspectRatio="none" viewBox="0 0 2 100" aria-hidden>
            <path d="M1 0 V100" stroke="currentColor" strokeOpacity=".15" strokeWidth="1" vectorEffect="non-scaling-stroke" />
            <path data-path d="M1 0 V100" stroke="var(--color-flame)" strokeWidth="2" vectorEffect="non-scaling-stroke" pathLength={1} strokeDasharray="1" />
          </svg>
          <ol className="grid gap-16">
            {steps.map((s, i) => (
              <li key={s.t} data-step className="relative pl-16">
                <span data-dot className="absolute left-[9px] top-1 grid place-items-center size-[22px] rounded-full bg-flame text-[.7rem] font-semibold text-night">{i + 1}</span>
                <h3 className="h3">{s.t}</h3>
                <p className="mt-3 text-ink-2 measure">{s.d}</p>
              </li>
            ))}
          </ol>
        </div>
      </div>
    </section>
  );
}
