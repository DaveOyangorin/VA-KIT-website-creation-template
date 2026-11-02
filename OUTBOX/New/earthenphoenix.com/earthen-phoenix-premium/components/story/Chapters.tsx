'use client';
import { useRef } from 'react';
import { gsap, ScrollTrigger, useGsap } from '@/lib/anim';
import { REGISTER, SERVICE, type ServiceKey } from '@/lib/content';
import { REVEALS } from '@/lib/reveals';
import { BOOK, href } from '@/lib/site';
import Img from '@/components/ui/Img';
import { Arr } from '@/components/ui/Arrow';

/**
 * Scene 3. One full-screen chapter per session. Each chapter pins while you scroll, and the scroll plays that
 * session's own motion on its photograph (lib/reveals.ts), scrubbed forward and back with your hand:
 * Reiki widens a circle of light, Swedish sweeps one long stroke, lymphatic drains to the collarbone, deep tissue
 * pushes in, Thai presses in bands, Sarga climbs in weighted steps, Zen opens a letterbox, yoga flows into
 * stillness, the reading turns a card, and herbalism fills with colour.
 */
const ORDER: { key: ServiceKey; group: string }[] = REGISTER.flatMap((g) => g.keys.map((key) => ({ key, group: g.title })));

function Chapter({ k, i, group }: { k: ServiceKey; i: number; group: string }) {
  const s = SERVICE[k];
  const flip = i % 2 === 1;
  return (
    <article id={`ch-${k}`} data-chapter={k} className="relative h-[230svh] motion-reduce:h-auto" aria-labelledby={`ch-${k}-h`}>
      <div className={`sticky top-0 h-[100svh] overflow-hidden grid grid-rows-[62%_38%] md:grid-rows-1 ${flip ? 'md:grid-cols-[minmax(0,1fr)_minmax(0,1.45fr)]' : 'md:grid-cols-[minmax(0,1.45fr)_minmax(0,1fr)]'}`}>
        <div className={`relative md:h-full p-3 md:p-5 md:pt-[calc(var(--hdr)+12px)] ${flip ? 'md:order-2' : ''}`}>
          <div data-frame className="relative h-full overflow-hidden rounded-[26px] bg-moss">
            <Img name={s.img} alt={s.alt} className="cover" pos={s.pos} sizes="(max-width: 767px) 100vw, 60vw" />
          </div>
        </div>
        <div className={`relative flex flex-col justify-center px-[var(--gutter)] md:px-[clamp(28px,4vw,72px)] ${flip ? 'md:order-1' : ''}`}>
          <div data-text>
            <p className="flex items-center gap-4 text-sm text-ink-2">
              <span className="font-display italic text-3xl md:text-5xl text-flame leading-none">{String(i + 1).padStart(2, '0')}</span>
              <span className="uppercase tracking-[.2em] text-xs">{group}</span>
            </p>
            <h2 id={`ch-${k}-h`} className="font-display text-[clamp(2.6rem,6.2vw,6.4rem)] leading-[0.92] tracking-[-0.035em] mt-3 md:mt-6">{s.name}</h2>
            <p className="mt-3 md:mt-6 text-ink-2 md:text-lg max-w-[34ch]">{s.line}.</p>
            <p className="mt-4 md:mt-8 flex flex-wrap items-center gap-x-6 gap-y-3">
              <span className="font-display text-2xl md:text-3xl tabular-nums">{s.price}</span>
              <span className="text-ink-2 text-sm">{s.length}</span>
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
    el.querySelectorAll<HTMLElement>('[data-chapter]').forEach((ch) => {
      const k = ch.dataset.chapter as ServiceKey;
      const frame = ch.querySelector<HTMLElement>('[data-frame]')!;
      const img = frame.querySelector('img');
      const reveal = REVEALS[k](frame, img);
      reveal.pause(0);
      const text = ch.querySelector('[data-text]');
      const drift = gsap.fromTo(img, { yPercent: 0 }, { yPercent: -4, ease: 'none', paused: true });
      ScrollTrigger.create({
        trigger: ch, start: 'top 85%', end: 'bottom bottom', scrub: 0.6,
        onUpdate: (self) => {
          const p = self.progress;
          reveal.progress(Math.min(1, p / 0.6));
          drift.progress(Math.max(0, (p - 0.6) / 0.4));
        },
      });
      gsap.fromTo(text, { y: 60, autoAlpha: 0 }, { y: 0, autoAlpha: 1, ease: 'power2.out', scrollTrigger: { trigger: ch, start: 'top 60%', end: 'top top', scrub: 0.6 } });
    });
  });

  return (
    <section ref={ref} className="relative bg-mist" aria-label="Every session, one chapter each">
      {ORDER.map(({ key, group }, i) => <Chapter key={key} k={key} i={i} group={group} />)}
    </section>
  );
}
