'use client';
import { useRef } from 'react';
import { gsap, ScrollTrigger, useGsap } from '@/lib/anim';
import { SERVICES } from '@/lib/content';

const TONES = ['text-poppy', 'text-forest', 'text-tangerine', 'text-cacao', 'text-saffron'];

/**
 * Between the reel and the chapters: two rows of giant session names in her logo colours, drifting in
 * opposite directions. Scroll speed pushes them faster and leans them into the motion; scrolling up reverses them.
 */
export default function Marquee() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    if (reduced) return;
    const rows = el.querySelectorAll<HTMLElement>('[data-row]');
    const loops = [...rows].map((row, i) =>
      gsap.fromTo(row, { xPercent: i ? -50 : 0 }, { xPercent: i ? 0 : -50, duration: 38, ease: 'none', repeat: -1 }),
    );
    let dir = 1;
    const st = ScrollTrigger.create({
      trigger: el, start: 'top bottom', end: 'bottom top',
      onUpdate: (self) => {
        const v = self.getVelocity();
        if (self.direction !== dir) { dir = self.direction; }
        const boost = 1 + Math.min(6, Math.abs(v) / 300);
        loops.forEach((l) => gsap.to(l, { timeScale: boost * dir, duration: 0.3, overwrite: true }));
        gsap.to(rows, { skewX: Math.max(-12, Math.min(12, -v / 180)), duration: 0.4, overwrite: 'auto' });
      },
    });
    const settle = () => {
      loops.forEach((l) => gsap.to(l, { timeScale: dir, duration: 1.2 }));
      gsap.to(rows, { skewX: 0, duration: 0.8 });
    };
    ScrollTrigger.addEventListener('scrollEnd', settle);
    return () => { st.kill(); ScrollTrigger.removeEventListener('scrollEnd', settle); loops.forEach((l) => l.kill()); };
  });

  const line = (offset: number) => [...SERVICES, ...SERVICES].map((s, i) => (
    <span key={i} className={`inline-flex items-center gap-[0.35em] pr-[0.35em] ${TONES[(i + offset) % TONES.length]}`}>
      <span className={i % 2 ? 'italic' : ''}>{s.name}</span>
      <span aria-hidden className="inline-block size-[0.28em] rounded-full bg-current opacity-80" />
    </span>
  ));

  return (
    <section ref={ref} className="relative overflow-hidden bg-mist py-[clamp(48px,8vw,110px)]" aria-hidden>
      <div className="font-display leading-[1.02] tracking-[-0.035em] text-[clamp(3.4rem,10vw,10rem)] whitespace-nowrap select-none">
        <div data-row className="inline-flex will-change-transform">{line(0)}</div>
        <br />
        <div data-row className="inline-flex will-change-transform">{line(2)}</div>
      </div>
    </section>
  );
}
