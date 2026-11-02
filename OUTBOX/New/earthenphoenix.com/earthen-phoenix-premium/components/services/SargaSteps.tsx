'use client';
import { useRef, useState } from 'react';
import type { Service } from '@/lib/content';
import { gsap, ScrollTrigger, prefersReduced, useGsap } from '@/lib/anim';
import { REVEALS } from '@/lib/reveals';
import Img from '@/components/ui/Img';
import SigCopy from './SigCopy';

/**
 * Sarga: barefoot, holding a strap overhead to control every ounce of weight. The photograph climbs into view in
 * six weighted steps. Each step you take presses the picture down and lets the pressure spread out wider than
 * the foot, then it settles; the strap line tightens with every step.
 */
export default function SargaSteps({ s }: { s: Service }) {
  const ref = useRef<HTMLDivElement>(null);
  const [steps, setSteps] = useState(0);

  useGsap(ref, ({ reduced, el }) => {
    const frame = el.querySelector<HTMLElement>('[data-frame]')!;
    if (reduced) return;
    frame.style.clipPath = 'inset(100% 0% 0% 0%)';
    const st = ScrollTrigger.create({ trigger: el, start: 'top 75%', once: true, onEnter: () => REVEALS.sarga(frame, frame.querySelector('img')) });
    return () => st.kill();
  });

  const step = (x = 0.5, y = 0.55) => {
    setSteps((n) => n + 1);
    const el = ref.current;
    if (!el || prefersReduced()) return;
    const img = el.querySelector('[data-weight]');
    const ring = document.createElement('span');
    ring.className = 'absolute rounded-full border border-chalk/70 pointer-events-none';
    Object.assign(ring.style, { left: `${x * 100}%`, top: `${y * 100}%`, width: '40px', height: '40px', marginLeft: '-20px', marginTop: '-20px' });
    el.querySelector('[data-frame]')!.appendChild(ring);
    gsap.timeline()
      .to(img, { y: 12, scale: 0.985, duration: 0.22, ease: 'power4.in' })
      .to(img, { y: 0, scale: 1, duration: 1.1, ease: 'elastic.out(1, .55)' });
    gsap.fromTo(ring, { scale: 0.4, opacity: 1 }, { scale: 9, opacity: 0, duration: 1.5, ease: 'expo.out', onComplete: () => ring.remove() });
    gsap.fromTo(el.querySelector('[data-strap]'), { scaleY: 1 }, { scaleY: 0.94, duration: 0.22, yoyo: true, repeat: 1, ease: 'power2.inOut', transformOrigin: 'top' });
  };

  return (
    <section className="sec bg-night text-chalk" aria-labelledby="sig-h">
      <div className="wrap grid gap-14 lg:grid-cols-[minmax(0,6fr)_minmax(0,5fr)] items-center">
        <figure className="m-0 order-2 lg:order-1">
          <div ref={ref} className="relative mx-auto max-w-[520px]">
            <span data-strap className="absolute -top-10 left-[7%] w-px h-[38%] bg-gradient-to-b from-transparent via-chalk/50 to-chalk/80" aria-hidden />
            <div data-frame className="relative aspect-[9/14] overflow-hidden rounded-[28px] bg-moss cursor-pointer"
              onPointerDown={(e) => { const r = e.currentTarget.getBoundingClientRect(); step((e.clientX - r.left) / r.width, (e.clientY - r.top) / r.height); }}>
              <div data-weight className="absolute inset-0">
                <Img name={s.img} alt={s.alt} className="cover scale-[1.05]" pos="50% 30%" sizes="(max-width: 1023px) 92vw, 520px" />
              </div>
            </div>
          </div>
          <figcaption className="mt-4 text-sm text-chalk/55 text-center">Her photograph. Tap it to place a step.</figcaption>
        </figure>
        <div className="order-1 lg:order-2">
          <SigCopy s={s}>
            <div className="flex items-center gap-5">
              <button type="button" className="btn btn-flame" onClick={() => step()}>Take a step</button>
              <span className="text-sm text-chalk/60 tabular-nums" aria-live="polite">{steps ? `${steps} step${steps > 1 ? 's' : ''}` : ''}</span>
            </div>
          </SigCopy>
        </div>
      </div>
    </section>
  );
}
