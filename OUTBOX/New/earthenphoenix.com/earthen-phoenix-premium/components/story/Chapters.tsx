'use client';
import { useRef, type CSSProperties } from 'react';
import { gsap, ScrollTrigger, useGsap } from '@/lib/anim';
import { REGISTER, SERVICE, type ServiceKey } from '@/lib/content';
import { REVEALS } from '@/lib/reveals';
import { BOOK, href } from '@/lib/site';
import Img from '@/components/ui/Img';
import { Arr } from '@/components/ui/Arrow';

/**
 * Scene 3. One full-screen chapter per session, each on its own bold colour from her logo.
 * Chapters stack like cards: the next one slides up over the last while it stays pinned.
 * Inside each chapter, scroll plays that session's own motion on its photograph (lib/reveals.ts),
 * the name rises letter by letter, and a colour block drifts behind the photo for depth.
 */
const ORDER: { key: ServiceKey; group: string }[] = REGISTER.flatMap((g) => g.keys.map((key) => ({ key, group: g.title })));

const COLOR: Record<ServiceKey, { bg: string; fg: string; block: string }> = {
  reiki: { bg: 'var(--color-saffron)', fg: 'var(--color-ink)', block: 'var(--color-tangerine)' },
  swedish: { bg: 'var(--color-rose)', fg: 'var(--color-ink)', block: 'var(--color-poppy)' },
  lymph: { bg: 'var(--color-tangerine)', fg: 'var(--color-ink)', block: 'var(--color-saffron)' },
  deep: { bg: 'var(--color-poppy)', fg: 'var(--color-chalk)', block: 'var(--color-cacao)' },
  thai: { bg: 'var(--color-forest)', fg: 'var(--color-chalk)', block: 'var(--color-saffron)' },
  sarga: { bg: 'var(--color-cacao)', fg: 'var(--color-chalk)', block: 'var(--color-poppy)' },
  zen: { bg: 'var(--color-meadow)', fg: 'var(--color-ink)', block: 'var(--color-forest)' },
  yoga: { bg: 'var(--color-saffron)', fg: 'var(--color-ink)', block: 'var(--color-forest)' },
  astro: { bg: 'var(--color-tangerine)', fg: 'var(--color-ink)', block: 'var(--color-cacao)' },
  herbs: { bg: 'var(--color-forest)', fg: 'var(--color-chalk)', block: 'var(--color-tangerine)' },
};

function Chapter({ k, i, group }: { k: ServiceKey; i: number; group: string }) {
  const s = SERVICE[k];
  const c = COLOR[k];
  const flip = i % 2 === 1;
  return (
    <article id={`ch-${k}`} data-chapter={k} className={`relative h-[230svh] motion-reduce:h-auto ${i ? '-mt-[100svh] motion-reduce:mt-0' : ''}`}
      style={{ zIndex: i + 1, '--fg': c.fg } as CSSProperties} aria-labelledby={`ch-${k}-h`}>
      <div className={`sticky top-0 h-[100svh] overflow-hidden grid grid-rows-[60%_40%] md:grid-rows-1 rounded-t-[28px] shadow-[0_-30px_60px_-30px_rgba(29,33,28,.35)] text-[var(--fg)] ${flip ? 'md:grid-cols-[minmax(0,1fr)_minmax(0,1.45fr)]' : 'md:grid-cols-[minmax(0,1.45fr)_minmax(0,1fr)]'}`}
        style={{ background: c.bg }}>
        <div className={`relative md:h-full p-3 md:p-6 md:pt-[calc(var(--hdr)+16px)] ${flip ? 'md:order-2' : ''}`}>
          <div data-block aria-hidden className={`absolute top-[18%] bottom-[8%] w-[46%] rounded-[26px] ${flip ? 'left-[4%]' : 'right-[4%]'}`} style={{ background: c.block }} />
          <div data-frame className="relative h-full overflow-hidden rounded-[26px] bg-moss shadow-[0_40px_80px_-40px_rgba(0,0,0,.45)]">
            <Img name={s.img} alt={s.alt} className="cover" pos={s.pos} sizes="(max-width: 767px) 100vw, 60vw" />
          </div>
        </div>
        <div className={`relative flex flex-col justify-center px-[var(--gutter)] md:px-[clamp(28px,4vw,72px)] ${flip ? 'md:order-1' : ''}`}>
          <span data-num aria-hidden className="pointer-events-none absolute -top-[4%] md:top-[8%] right-[6%] font-display italic leading-none opacity-15 text-[clamp(8rem,22vw,20rem)]">{String(i + 1).padStart(2, '0')}</span>
          <div data-text className="relative">
            <p className="uppercase tracking-[.22em] text-xs opacity-80">{String(i + 1).padStart(2, '0')} · {group}</p>
            <h2 id={`ch-${k}-h`} className="font-display text-[clamp(2.6rem,6.2vw,6.4rem)] leading-[0.92] tracking-[-0.035em] mt-3 md:mt-6">
              {s.name.split(' ').map((w, wi) => (
                <span key={wi} className="inline-block whitespace-nowrap mr-[0.25em]">
                  {w.split('').map((ch, ci) => <span key={ci} className="inline-block overflow-clip pb-[0.08em] -mb-[0.08em]"><span data-ch className="inline-block">{ch}</span></span>)}
                </span>
              ))}
            </h2>
            <p className="mt-3 md:mt-6 md:text-lg max-w-[34ch] opacity-85">{s.line}.</p>
            <p className="mt-4 md:mt-8 flex flex-wrap items-baseline gap-x-5 gap-y-2">
              <span className="font-display text-3xl md:text-4xl tabular-nums">{s.price}</span>
              <span className="text-sm opacity-75">{s.length}</span>
            </p>
            <p className="mt-4 md:mt-8 flex flex-wrap gap-3">
              <a href={href('/' + s.slug)} className="btn btn-ink !min-h-[44px] md:!min-h-[52px]">How it works <Arr /></a>
              <a href={BOOK} className="btn btn-ghost !min-h-[44px] md:!min-h-[52px] max-sm:hidden">Book</a>
            </p>
          </div>
        </div>
      </div>
    </article>
  );
}

export default function Chapters() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    if (reduced) return;
    const all = el.querySelectorAll<HTMLElement>('[data-chapter]');
    all.forEach((ch, i) => {
      const k = ch.dataset.chapter as ServiceKey;
      const frame = ch.querySelector<HTMLElement>('[data-frame]')!;
      const img = frame.querySelector('img');
      const reveal = REVEALS[k](frame, img);
      reveal.pause(0);
      const drift = gsap.fromTo(img, { yPercent: 0 }, { yPercent: -4, ease: 'none', paused: true });
      ScrollTrigger.create({
        trigger: ch, start: i ? 'top 40%' : 'top 85%', end: 'bottom bottom', scrub: 0.6,
        onUpdate: (self) => {
          const p = self.progress;
          reveal.progress(Math.min(1, p / 0.6));
          drift.progress(Math.max(0, (p - 0.6) / 0.4));
        },
      });
      const enter = { trigger: ch, start: i ? 'top 70%' : 'top 60%', end: i ? 'top top' : 'top 10%', scrub: 0.6 };
      gsap.fromTo(ch.querySelectorAll('[data-ch]'), { yPercent: 110, rotate: 8, y: 0 }, { yPercent: 0, rotate: 0, y: 0, stagger: 0.02, ease: 'power3.out', scrollTrigger: enter });
      gsap.fromTo(ch.querySelector('[data-text]'), { y: 50, autoAlpha: 0 }, { y: 0, autoAlpha: 1, ease: 'power2.out', scrollTrigger: enter });
      gsap.fromTo(ch.querySelector('[data-num]'), { yPercent: 40, opacity: 0 }, { yPercent: -20, opacity: 0.15, ease: 'none', scrollTrigger: { trigger: ch, start: 'top 80%', end: 'bottom bottom', scrub: true } });
      gsap.fromTo(ch.querySelector('[data-block]'), { yPercent: 25, rotate: -6 }, { yPercent: -15, rotate: 4, ease: 'none', scrollTrigger: { trigger: ch, start: 'top bottom', end: 'bottom bottom', scrub: true } });
      // the card being covered sinks back slightly as the next one slides over it
      const next = all[i + 1];
      if (next) gsap.to(ch.querySelector(':scope > div'), { scale: 0.94, filter: 'brightness(.92)', ease: 'none', scrollTrigger: { trigger: next, start: 'top bottom', end: 'top top', scrub: true } });
    });
  });

  return (
    <section ref={ref} className="relative bg-mist" aria-label="Every session, one chapter each">
      {ORDER.map(({ key, group }, i) => <Chapter key={key} k={key} i={i} group={group} />)}
    </section>
  );
}
