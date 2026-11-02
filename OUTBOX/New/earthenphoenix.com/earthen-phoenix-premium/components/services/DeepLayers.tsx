'use client';
import { useRef, useState } from 'react';
import type { Service } from '@/lib/content';
import { ScrollTrigger, useGsap } from '@/lib/anim';
import Img from '@/components/ui/Img';
import SigCopy from './SigCopy';

/**
 * Deep tissue: beneath the surface. Four windows sit one inside another on her photograph, each looking closer
 * in on her hands. Scrolling carries you through them, one layer per part of the session:
 * deep pressure, breathwork, stretching and movement, take-home stretches.
 */
const STEPS = [
  ['Deep pressure', 'At the depth you ask for. Therapeutic, and never painful.'],
  ['Breathwork', 'The work follows your breathing.'],
  ['Stretching and movement', 'To restore balance.'],
  ['Take-home stretches', 'Guidance so the results last.'],
] as const;
const N = STEPS.length;
const FX = 0.26, FY = 0.6; // her hands, in the photograph

export default function DeepLayers({ s }: { s: Service }) {
  const ref = useRef<HTMLElement>(null);
  const [step, setStep] = useState(0);

  useGsap(ref, ({ reduced, el }) => {
    const layers = el.querySelectorAll<HTMLElement>('[data-layer]');
    const render = (t: number) => {
      layers.forEach((layer, i) => {
        const f = Math.min(1, Math.max(0, 1 - (i - t) * 0.36));
        const inset = (a: number) => `${(a * (1 - f) * 100).toFixed(2)}%`;
        layer.style.clipPath = f <= 0 ? 'inset(50%)' : `inset(${inset(FY)} ${inset(1 - FX)} ${inset(1 - FY)} ${inset(FX)} round ${Math.round(18 * (1 - f) + 2)}px)`;
        layer.style.setProperty('--edge', String(f >= 1 ? 0 : 0.7));
        const img = layer.querySelector<HTMLElement>('img')!;
        const sc = (1 + i * 0.42) * (1 + Math.max(0, t - i) * 0.18);
        img.style.transform = `scale(${sc.toFixed(4)})`;
      });
    };
    if (reduced) { render(0); return; }
    render(0);
    const st = ScrollTrigger.create({
      ...(window.matchMedia('(min-width: 1024px)').matches
        ? { trigger: el.querySelector('[data-track]'), start: 'top top', end: 'bottom bottom' }
        : { trigger: el.querySelector('figure'), start: 'top 75%', end: 'bottom 25%' }), scrub: 0.6,
      onUpdate: (self) => { const t = self.progress * (N - 1); render(t); setStep(Math.round(t)); },
    });
    return () => st.kill();
  });

  return (
    <section ref={ref} className="bg-mist text-ink" aria-labelledby="sig-h">
      <div data-track className="relative lg:h-[340svh]">
        <div className="lg:sticky lg:top-0 lg:h-[100svh] wrap grid gap-12 lg:grid-cols-[minmax(0,5fr)_minmax(0,6fr)] items-center py-[clamp(88px,12vw,160px)] lg:py-[calc(var(--hdr)+24px)]">
          <div>
            <SigCopy s={s} />
            <ol className="mt-10 grid gap-1" aria-label="The parts of a deep tissue session">
              {STEPS.map(([t, d], i) => (
                <li key={t} className={`grid grid-cols-[2.2rem_1fr] gap-3 py-3 border-t border-ink/10 transition-opacity duration-500 ${i === step ? 'opacity-100' : 'lg:opacity-40'}`}>
                  <span className={`font-display italic text-xl ${i === step ? 'text-flame' : ''}`}>{['i', 'ii', 'iii', 'iv'][i]}</span>
                  <span><b className="font-medium">{t}</b><span className="block text-sm text-ink-2 mt-0.5">{d}</span></span>
                </li>
              ))}
            </ol>
          </div>
          <figure className="m-0">
            <div className="relative aspect-[4/5] max-h-[78svh] mx-auto overflow-hidden rounded-[28px] bg-moss" role="img" aria-label="Her photograph shown as four windows, each one looking closer in on her hands at a client's neck and shoulders">
              {STEPS.map((_, i) => (
                <div key={i} data-layer className="absolute inset-0 overflow-hidden" style={{ zIndex: i + 1 }}>
                  <Img name={s.img} alt="" className="cover will-change-transform" pos={`${FX * 100}% ${FY * 100}%`} sizes="(max-width: 1023px) 92vw, 46vw"
                    style={{ transformOrigin: `${FX * 100}% ${FY * 100}%` }} />
                  <span className="absolute inset-0 rounded-[inherit] pointer-events-none" style={{ boxShadow: 'inset 0 0 0 1px rgba(246,247,244,var(--edge,0))' }} />
                </div>
              ))}
              <span className="absolute z-10 left-5 bottom-5 text-xs uppercase tracking-[.2em] text-ink-2">Layer {step + 1} of {N}</span>
            </div>
          </figure>
        </div>
      </div>
    </section>
  );
}
