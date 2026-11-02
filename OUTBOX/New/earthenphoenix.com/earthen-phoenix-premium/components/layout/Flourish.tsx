'use client';
import { useEffect, useRef } from 'react';
import { gsap, ScrollTrigger, isTouch, prefersReduced } from '@/lib/anim';

/**
 * Two small site-wide touches:
 *  - a reading bar at the very top in the five bands of her logo, filling as you scroll the page;
 *  - magnetic buttons: on a mouse, every button leans gently toward the pointer and springs back.
 */
export default function Flourish() {
  const bar = useRef<HTMLDivElement>(null);
  useEffect(() => {
    if (prefersReduced()) return;
    const el = bar.current!;
    const st = ScrollTrigger.create({ start: 0, end: 'max', onUpdate: (s) => gsap.set(el, { scaleX: s.progress }) });

    if (isTouch()) return () => st.kill();
    const pull = (e: PointerEvent) => {
      const b = (e.target as HTMLElement).closest<HTMLElement>('.btn');
      if (!b) return;
      const r = b.getBoundingClientRect();
      gsap.to(b, { x: (e.clientX - r.left - r.width / 2) * 0.25, y: (e.clientY - r.top - r.height / 2) * 0.35, duration: 0.5, ease: 'power3.out' });
    };
    const release = (e: PointerEvent) => {
      const b = (e.target as HTMLElement).closest<HTMLElement>('.btn');
      if (b && !b.contains(e.relatedTarget as Node)) gsap.to(b, { x: 0, y: 0, duration: 0.9, ease: 'elastic.out(1, .4)' });
    };
    document.addEventListener('pointermove', pull);
    document.addEventListener('pointerout', release);
    return () => { st.kill(); document.removeEventListener('pointermove', pull); document.removeEventListener('pointerout', release); };
  }, []);
  return (
    <div ref={bar} aria-hidden className="fixed top-0 left-0 right-0 h-[3px] z-[70] origin-left scale-x-0 pointer-events-none motion-reduce:hidden"
      style={{ background: 'linear-gradient(90deg, var(--color-saffron) 0 20%, var(--color-tangerine) 20% 40%, var(--color-poppy) 40% 60%, var(--color-cacao) 60% 80%, var(--color-forest) 80% 100%)' }} />
  );
}
