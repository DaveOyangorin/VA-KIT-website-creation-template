'use client';
import { useEffect, useRef, useState } from 'react';
import type { Service } from '@/lib/content';
import { gsap, prefersReduced } from '@/lib/anim';
import Img from '@/components/ui/Img';
import SigCopy from './SigCopy';

/**
 * Private yoga: fun Vinyasa flow, then slow Yin holds. In flow, the frame around her photograph moves with a
 * quick breath: its edges swell and shift like a body moving through poses. In the hold, it comes to rest in one
 * calm shape and only breathes, slowly. The breath cue beneath follows along.
 */
const SHAPES = [
  'inset(4% 6% 6% 4% round 46% 54% 42% 58% / 52% 44% 56% 48%)',
  'inset(8% 2% 2% 8% round 58% 42% 54% 46% / 44% 56% 48% 52%)',
  'inset(2% 8% 8% 2% round 40% 60% 48% 52% / 56% 48% 52% 44%)',
  'inset(6% 4% 4% 6% round 52% 48% 60% 40% / 48% 52% 44% 56%)',
];
const HOLD = 'inset(5% 5% 5% 5% round 32px 32px 32px 32px / 32px 32px 32px 32px)';

export default function YogaFlow({ s }: { s: Service }) {
  const frame = useRef<HTMLDivElement>(null);
  const [mode, setMode] = useState<'flow' | 'hold'>('flow');
  const [cue, setCue] = useState('Inhale');

  useEffect(() => {
    const el = frame.current;
    if (!el) return;
    if (prefersReduced()) { el.style.clipPath = HOLD; setCue('Hold'); return; }
    const img = el.querySelector('img');
    const tl = gsap.timeline({ repeat: -1 });
    if (mode === 'flow') {
      SHAPES.forEach((shape, i) => {
        tl.to(el, { clipPath: shape, duration: 1.2, ease: 'sine.inOut', onStart: () => setCue(i % 2 ? 'Exhale' : 'Inhale') });
      });
      gsap.to(img, { scale: 1.06, rotate: 0.6, duration: 1.2, yoyo: true, repeat: -1, ease: 'sine.inOut' });
    } else {
      gsap.to(el, { clipPath: HOLD, duration: 2.2, ease: 'expo.out' });
      gsap.to(img, { rotate: 0, duration: 2, ease: 'expo.out' });
      tl.to(img, { scale: 1.03, duration: 5, ease: 'sine.inOut', onStart: () => setCue('Hold · breathe in') })
        .to(img, { scale: 1, duration: 5, ease: 'sine.inOut', onStart: () => setCue('Hold · breathe out') });
    }
    const io = new IntersectionObserver(([en]) => (en.isIntersecting ? tl.play() : tl.pause()));
    io.observe(el);
    return () => { io.disconnect(); tl.kill(); gsap.killTweensOf(img); gsap.killTweensOf(el); };
  }, [mode]);

  return (
    <section className="sec bg-mist text-ink" aria-labelledby="sig-h">
      <div className="wrap grid gap-14 lg:grid-cols-[minmax(0,7fr)_minmax(0,4fr)] items-center">
        <figure className="m-0 order-2 lg:order-1">
          <div ref={frame} className="relative aspect-[3/2] overflow-hidden bg-moss" style={{ clipPath: SHAPES[0] }}>
            <Img name={s.img} alt={s.alt} className="cover" pos={s.pos} sizes="(max-width: 1023px) 92vw, 60vw" />
          </div>
          <figcaption className="mt-4 flex items-center justify-between text-sm text-ink-2">
            <span>Her photograph: an assisted fold on the grass.</span>
            <span className="font-display italic text-lg text-clay" aria-live="polite">{cue}</span>
          </figcaption>
        </figure>
        <div className="order-1 lg:order-2">
          <SigCopy s={s}>
            <div className="seg" role="group" aria-label="Part of the practice">
              <button type="button" aria-pressed={mode === 'flow'} onClick={() => setMode('flow')}>Vinyasa flow</button>
              <button type="button" aria-pressed={mode === 'hold'} onClick={() => setMode('hold')}>Yin hold</button>
            </div>
          </SigCopy>
        </div>
      </div>
    </section>
  );
}
