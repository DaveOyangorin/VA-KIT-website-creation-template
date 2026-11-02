'use client';
import { useRef } from 'react';
import { gsap, ScrollTrigger, useGsap } from '@/lib/anim';
import { REGISTER, SERVICE } from '@/lib/content';
import Img from '@/components/ui/Img';

/**
 * Scene 2. All ten sessions as one sideways reel: tall photographs that slide past as you scroll down,
 * each photo drifting inside its frame and easing up to full size as it reaches the middle.
 */
const KEYS = REGISTER.flatMap((g) => g.keys);

export default function Reel() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    if (reduced) return;
    const track = el.querySelector<HTMLElement>('[data-track]')!;
    const dist = () => track.scrollWidth - window.innerWidth;
    const move = gsap.to(track, {
      x: () => -dist(), ease: 'none',
      scrollTrigger: { trigger: el, start: 'top top', end: () => `+=${dist()}`, scrub: 0.8, pin: true, anticipatePin: 1, invalidateOnRefresh: true },
    });
    el.querySelectorAll<HTMLElement>('[data-panel]').forEach((panel) => {
      const img = panel.querySelector('img');
      gsap.fromTo(img, { xPercent: -12 }, { xPercent: 12, ease: 'none', scrollTrigger: { trigger: panel, containerAnimation: move, start: 'left right', end: 'right left', scrub: true } });
      gsap.fromTo(panel, { scale: 0.88 }, { scale: 1, ease: 'none', scrollTrigger: { trigger: panel, containerAnimation: move, start: 'left right', end: 'center center', scrub: true } });
    });
    ScrollTrigger.refresh();
  });

  return (
    <section ref={ref} className="relative bg-mist overflow-hidden" aria-labelledby="reel-h">
      <div className="h-[100svh] flex items-center">
        <div data-track className="flex items-center gap-[clamp(16px,2.4vw,36px)] pl-[var(--gutter)] pr-[12vw] will-change-transform">
          <div className="shrink-0 w-[min(80vw,520px)] pr-[4vw]">
            <p className="kicker text-lichen">Ten sessions</p>
            <h2 id="reel-h" className="font-display text-[clamp(3rem,7vw,7rem)] leading-[0.92] tracking-[-0.035em] mt-6">Ten ways <em>to ground.</em></h2>
            <p className="mt-6 text-ink-2 max-w-[34ch]">From hands that never touch to her full body weight, then out into the mountains.</p>
          </div>
          {KEYS.map((k, i) => {
            const s = SERVICE[k];
            return (
              <a key={k} href={`#ch-${s.key}`} data-panel
                className="group relative shrink-0 snap-center w-[78vw] sm:w-[52vw] lg:w-[34vw] h-[72svh] overflow-hidden rounded-[28px] bg-moss origin-center">
                <div className="absolute inset-y-0 -inset-x-[14%]"><Img name={s.img} alt={s.alt} className="cover transition-transform duration-[1200ms] ease-[cubic-bezier(.16,1,.3,1)] group-hover:scale-105" pos={s.pos} sizes="(max-width: 1023px) 80vw, 40vw" /></div>
                <div className="absolute inset-0 bg-gradient-to-t from-night/75 via-night/5 to-transparent" />
                <span className="absolute top-5 left-6 text-chalk/90 text-sm tabular-nums">{String(i + 1).padStart(2, '0')}</span>
                <span className="absolute top-5 right-6 text-chalk/90 text-xs uppercase tracking-[.2em]">{s.touch}</span>
                <span className="absolute left-6 right-6 bottom-6 text-chalk">
                  <span className="block font-display text-[clamp(2.2rem,3.6vw,3.6rem)] leading-[0.95] tracking-[-0.03em]">{s.name}</span>
                  <span className="mt-2 block text-sm text-chalk/85">{s.price} · {s.length}</span>
                </span>
              </a>
            );
          })}
        </div>
      </div>
    </section>
  );
}
