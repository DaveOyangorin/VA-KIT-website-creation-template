'use client';
import { useRef, useState } from 'react';
import type { Service } from '@/lib/content';
import { gsap, ScrollTrigger, useGsap } from '@/lib/anim';
import Img from '@/components/ui/Img';
import SigCopy from './SigCopy';

/**
 * Lymphatic firming: the six steps of the 90-minute treatment, played on one photograph as you scroll.
 *  1 Dry brushing        long sweeping strokes draw toward the heart
 *  2 Lymphatic massage   dotted drainage paths flow in from the edges to the collarbone
 *  3 Heated body wrap    warmth closes in around the body
 *  4 Hot towel cleanse   steam rises, then clears
 *  5 Head and neck       the light gathers at her head and neck
 *  6 Firming cream       everything clears, with a last sheen
 */
const STEPS = [
  ['Dry brushing', 'Long sweeps toward the heart.'],
  ['Lymphatic massage', 'Light and manual.'],
  ['Heated body wrap', 'Wrapped and warmed.'],
  ['Hot towel cleanse', 'The wrap comes off.'],
  ['Head and neck', 'A head and neck treatment.'],
  ['Firming cream', 'Eminence Coconut Firming.'],
] as const;

// Collarbone in the photograph (viewBox 0..160 x 0..90)
const CB = { x: 98, y: 48 };
const PATHS = [
  'M2 70 C 30 66, 60 58, 98 48', 'M10 88 C 40 74, 70 60, 98 48', 'M60 89 C 70 72, 84 58, 98 48',
  'M158 86 C 140 70, 118 56, 98 48', 'M158 30 C 138 38, 118 44, 98 48', 'M120 2 C 112 18, 104 34, 98 48',
];
const BRUSH = ['M8 40 C 40 34, 70 40, 92 44', 'M14 60 C 44 52, 72 52, 94 48', 'M30 80 C 56 66, 78 58, 96 50'];

export default function LymphSequence({ s }: { s: Service }) {
  const ref = useRef<HTMLElement>(null);
  const [step, setStep] = useState(0);

  useGsap(ref, ({ reduced, el }) => {
    const q = gsap.utils.selector(el);
    const tl = gsap.timeline({ paused: true, defaults: { ease: 'none' } });
    // 1 dry brushing
    tl.fromTo(q('[data-brush] path'), { strokeDashoffset: 1 }, { strokeDashoffset: 0, stagger: 0.15, duration: 0.7 }, 0)
      .to(q('[data-brush]'), { opacity: 0, duration: 0.3 }, 0.85)
    // 2 drainage paths
      .fromTo(q('[data-flow]'), { opacity: 0 }, { opacity: 1, duration: 0.25 }, 1)
      .fromTo(q('[data-flow] path'), { strokeDashoffset: 0 }, { strokeDashoffset: -40, duration: 1 }, 1)
      .fromTo(q('[data-node]'), { scale: 0, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.4, transformOrigin: 'center' }, 1.3)
      .to(q('[data-flow], [data-node]'), { opacity: 0, duration: 0.3 }, 1.85)
    // 3 heated wrap
      .fromTo(q('[data-wrap]'), { opacity: 0 }, { opacity: 1, duration: 0.5 }, 2)
      .fromTo(q('[data-img]'), { filter: 'saturate(1) sepia(0) brightness(1)' }, { filter: 'saturate(1.2) sepia(.25) brightness(1.04)', duration: 0.5 }, 2)
      .to(q('[data-wrap]'), { opacity: 0, duration: 0.3 }, 2.85)
    // 4 hot towel: steam rises, clears
      .fromTo(q('[data-steam]'), { opacity: 0, yPercent: 30 }, { opacity: 1, yPercent: 0, duration: 0.45 }, 3)
      .to(q('[data-img]'), { filter: 'saturate(1.05) sepia(.08) brightness(1.06) blur(6px)', duration: 0.45 }, 3)
      .to(q('[data-steam]'), { opacity: 0, yPercent: -30, duration: 0.45 }, 3.5)
      .to(q('[data-img]'), { filter: 'saturate(1) sepia(0) brightness(1) blur(0px)', duration: 0.45 }, 3.5)
    // 5 head and neck
      .fromTo(q('[data-focus]'), { opacity: 0 }, { opacity: 1, duration: 0.4 }, 4)
      .to(q('[data-img]'), { scale: 1.12, duration: 0.8 }, 4)
      .to(q('[data-focus]'), { opacity: 0, duration: 0.3 }, 4.75)
    // 6 firming cream: clear, one sheen
      .to(q('[data-img]'), { scale: 1, filter: 'saturate(1.06) brightness(1.08)', duration: 0.6 }, 5)
      .fromTo(q('[data-sheen]'), { xPercent: -120 }, { xPercent: 260, duration: 0.8 }, 5.1);
    if (reduced) { tl.progress(1); return; }
    const st = ScrollTrigger.create({
      ...(window.matchMedia('(min-width: 1024px)').matches
        ? { trigger: el.querySelector('[data-track]'), start: 'top top', end: 'bottom bottom' }
        : { trigger: el.querySelector('figure'), start: 'top 75%', end: 'bottom 25%' }), scrub: 0.5,
      onUpdate: (self) => { tl.progress(self.progress); setStep(Math.min(5, Math.floor(self.progress * 6))); },
    });
    return () => { st.kill(); tl.kill(); };
  });

  return (
    <section ref={ref} className="bg-night text-chalk" aria-labelledby="sig-h">
      <div data-track className="relative lg:h-[420svh]">
        <div className="lg:sticky lg:top-0 lg:h-[100svh] wrap grid gap-12 lg:grid-cols-[minmax(0,4fr)_minmax(0,7fr)] items-center py-[clamp(88px,12vw,160px)] lg:py-[calc(var(--hdr)+24px)]">
          <div>
            <SigCopy s={s} />
            <ol className="mt-10 grid grid-cols-2 gap-x-6" aria-label="The six steps">
              {STEPS.map(([t, d], i) => (
                <li key={t} className={`py-3 border-t border-chalk/10 transition-all duration-500 ${i === step ? 'opacity-100' : 'lg:opacity-40'}`}>
                  <span className={`text-xs tabular-nums ${i === step ? 'text-flame' : 'text-chalk/50'}`}>0{i + 1}</span>
                  <b className="block font-medium mt-1">{t}</b>
                  <span className="block text-sm text-chalk/60">{d}</span>
                </li>
              ))}
            </ol>
          </div>
          <figure className="m-0">
            <div className="relative aspect-[16/9] overflow-hidden rounded-[28px] bg-moss" role="img" aria-label={`${s.alt}. The photograph changes with each step of the treatment.`}>
              <div data-img className="absolute inset-0" style={{ transformOrigin: '64% 42%' }}>
                <Img name={s.img} alt="" className="cover" pos="50% 50%" sizes="(max-width: 1023px) 92vw, 60vw" />
              </div>
              <svg viewBox="0 0 160 90" preserveAspectRatio="none" className="absolute inset-0 w-full h-full" aria-hidden>
                <g data-brush fill="none" stroke="rgba(246,247,244,.55)" strokeWidth="5" strokeLinecap="round" style={{ filter: 'blur(1.2px)' }}>
                  {BRUSH.map((d) => <path key={d} d={d} pathLength={1} strokeDasharray="1" />)}
                </g>
                <g data-flow fill="none" stroke="rgba(242,166,90,.9)" strokeWidth=".6" strokeLinecap="round" strokeDasharray="1.2 2.6" opacity="0">
                  {PATHS.map((d) => <path key={d} d={d} vectorEffect="non-scaling-stroke" style={{ strokeWidth: 2 }} />)}
                </g>
                <circle data-node cx={CB.x} cy={CB.y} r="2.4" fill="none" stroke="#f2a65a" strokeWidth=".5" opacity="0" />
              </svg>
              <div data-wrap className="absolute inset-0 opacity-0 pointer-events-none" style={{ background: 'radial-gradient(ellipse 70% 60% at 45% 55%, transparent 35%, rgba(236,106,63,.35) 75%, rgba(120,40,10,.55))' }} />
              <div data-steam className="absolute inset-0 opacity-0 pointer-events-none" style={{ background: 'linear-gradient(to top, rgba(246,247,244,.75), rgba(246,247,244,.25) 55%, transparent)' }} />
              <div data-focus className="absolute inset-0 opacity-0 pointer-events-none" style={{ background: 'radial-gradient(circle at 70% 40%, transparent 14%, rgba(13,20,16,.78) 46%)' }} />
              <div className="absolute inset-0 overflow-hidden pointer-events-none"><div data-sheen className="absolute inset-y-0 w-1/4 -translate-x-[120%] bg-gradient-to-r from-transparent via-white/25 to-transparent skew-x-[-16deg]" /></div>
              <span className="absolute left-5 bottom-5 text-xs uppercase tracking-[.2em] text-chalk/85">Step {step + 1} · {STEPS[step][0]}</span>
            </div>
          </figure>
        </div>
      </div>
    </section>
  );
}
