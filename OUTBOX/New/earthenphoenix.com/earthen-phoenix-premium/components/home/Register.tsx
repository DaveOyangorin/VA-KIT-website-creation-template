'use client';
import { useEffect, useRef, useState } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { REGISTER, SERVICE, type ServiceKey } from '@/lib/content';
import { gsap, ScrollTrigger, prefersReduced, useGsap } from '@/lib/anim';
import { REVEALS } from '@/lib/reveals';
import { href } from '@/lib/site';
import Img from '@/components/ui/Img';
import Split from '@/components/ui/Split';
import { Arr } from '@/components/ui/Arrow';

/**
 * "The register of touch": every session, ordered from hands that hover to her full body weight, then beyond the table.
 * On large screens a sticky stage swaps photographs as you read, and each session enters with its own motion
 * (see lib/reveals.ts). On phones each session reveals its own photo inline, with the same motion.
 */
const ORDER: { key: ServiceKey; group: number }[] = REGISTER.flatMap((g, gi) => g.keys.map((key) => ({ key, group: gi })));

export default function Register() {
  const ref = useRef<HTMLElement>(null);
  const [active, setActive] = useState(0);
  const running = useRef<gsap.core.Timeline | null>(null);
  const z = useRef(10);
  const first = useRef(true);

  // Swap the stage photo with that session's own reveal.
  useEffect(() => {
    const stage = ref.current?.querySelector<HTMLElement>('[data-stage]');
    if (!stage) return;
    const layers = stage.querySelectorAll<HTMLElement>('[data-layer]');
    const frame = layers[active];
    if (first.current || prefersReduced()) {
      first.current = false;
      layers.forEach((l, i) => { l.style.visibility = i === active ? 'visible' : 'hidden'; l.style.clipPath = ''; });
      return;
    }
    running.current?.progress(1);
    if (z.current > 400) { layers.forEach((l) => { l.style.zIndex = '10'; }); z.current = 10; }
    frame.style.zIndex = String(++z.current);
    const tl = REVEALS[ORDER[active].key](frame, frame.querySelector('img'));
    tl.pause();
    tl.progress(0.001);
    frame.style.visibility = 'visible';
    tl.eventCallback('onComplete', () => {
      frame.style.clipPath = 'inset(0% 0% 0% 0%)';
      layers.forEach((l, i) => { if (i !== active) l.style.visibility = 'hidden'; });
    });
    tl.play();
    running.current = tl;
  }, [active]);

  useGsap(ref, ({ reduced, el }) => {
    const mm = gsap.matchMedia();
    mm.add('(min-width: 1024px)', () => {
      el.querySelectorAll<HTMLElement>('[data-row]').forEach((row, i) => {
        ScrollTrigger.create({ trigger: row, start: 'top 58%', end: 'bottom 58%', onToggle: (s) => s.isActive && setActive(i) });
      });
    });
    if (!reduced) {
      mm.add('(max-width: 1023px)', () => {
        el.querySelectorAll<HTMLElement>('[data-inline]').forEach((frame, i) => {
          frame.style.clipPath = 'inset(0% 0% 100% 0%)';
          ScrollTrigger.create({
            trigger: frame, start: 'top 82%', once: true,
            onEnter: () => REVEALS[ORDER[i].key](frame, frame.querySelector('img')),
          });
        });
      });
    }
    return () => mm.revert();
  });

  const cur = SERVICE[ORDER[active].key];
  const curGroup = ORDER[active].group;

  return (
    <section ref={ref} id="sessions" className="relative bg-night text-chalk sec" aria-labelledby="reg-h">
      <div className="wrap">
        <div className="grid gap-10 lg:grid-cols-[1fr_auto] items-end">
          <div>
            <p className="kicker text-lichen" data-reveal>Ten sessions</p>
            <Split as="h2" id="reg-h" className="h2 mt-6 max-w-[15ch]" text="From hands that hover _to her full weight._" />
          </div>
          <p className="lede text-chalk/70 max-w-[42ch]" data-reveal data-delay="2">
            Miquelle works anywhere “from light and relaxing to deep fascial work.” Here is every session in that order, then the ones that leave the table altogether.
          </p>
        </div>

        <div className="mt-[clamp(56px,8vw,110px)] grid lg:grid-cols-[minmax(0,5fr)_minmax(0,6fr)] gap-x-[clamp(32px,5vw,90px)]">
          {/* The list */}
          <ol className="relative">
            {ORDER.map(({ key, group }, i) => {
              const s = SERVICE[key];
              const newGroup = i === 0 || ORDER[i - 1].group !== group;
              const g = REGISTER[group];
              return (
                <li key={key} data-row className="lg:min-h-[64svh] lg:flex lg:flex-col lg:justify-center py-10 lg:py-0">
                  {newGroup && (
                    <p className="mb-8 flex items-baseline gap-4 text-lichen">
                      <span className="font-display italic text-2xl">{['i', 'ii', 'iii', 'iv', 'v'][group]}.</span>
                      <span className="kicker !gap-0 before:!hidden">{g.title}</span>
                      <span className="text-sm text-chalk/50 hidden sm:inline">{g.note}</span>
                    </p>
                  )}
                  <div className={`transition-opacity duration-700 ${i === active ? 'lg:opacity-100' : 'lg:opacity-35'}`}>
                    {/* Inline photo for phones and tablets */}
                    <div data-inline className="lg:hidden relative aspect-[4/3] mb-7 overflow-hidden rounded-[22px] bg-moss">
                      <Img name={s.img} alt={s.alt} className="cover" pos={s.pos} sizes="(max-width: 1023px) 92vw, 1px" />
                    </div>
                    <p className="text-sm text-chalk/55 tabular-nums">{String(i + 1).padStart(2, '0')} · {s.touch}</p>
                    <h3 className="mt-3 font-display text-[clamp(2.4rem,4.6vw,4.4rem)] leading-[0.95] tracking-[-0.03em] font-light" style={{ fontVariationSettings: "'SOFT' 100, 'opsz' 144" }}>
                      <a href={href('/' + s.slug)} className="hover:text-flame transition-colors duration-500">{s.name}</a>
                    </h3>
                    <p className="mt-4 text-chalk/75 max-w-[40ch]">{s.line}.</p>
                    <p className="mt-5 flex flex-wrap items-center gap-x-6 gap-y-3">
                      <span className="tabular-nums">{s.price} <span className="text-chalk/50">· {s.length}</span></span>
                      <a href={href('/' + s.slug)} className="inline-flex items-center gap-2 ulink text-flame">How it works <Arr /></a>
                    </p>
                  </div>
                </li>
              );
            })}
          </ol>

          {/* The sticky stage */}
          <div className="hidden lg:block">
            <div className="sticky top-[calc(var(--hdr)+20px)] h-[calc(100svh-var(--hdr)-40px)]">
              <div data-stage className="relative h-full overflow-hidden rounded-[28px] bg-moss">
                {ORDER.map(({ key }, i) => {
                  const s = SERVICE[key];
                  return (
                    <div key={key} data-layer className="absolute inset-0 overflow-hidden" style={{ visibility: i === 0 ? 'visible' : 'hidden' }}>
                      <Img name={s.img} alt="" className="cover" pos={s.pos} sizes="50vw" />
                    </div>
                  );
                })}
                <div className="absolute inset-0 z-[500] pointer-events-none bg-gradient-to-t from-night/75 via-transparent to-night/30" />

                {/* The scale of touch */}
                <ol className="absolute z-[501] top-6 right-6 grid gap-2 text-right text-[.78rem] tracking-[.14em] uppercase" aria-label="Scale of touch">
                  {REGISTER.map((g, gi) => (
                    <li key={g.title} className={`flex items-center justify-end gap-3 transition-all duration-700 ${gi === curGroup ? 'text-chalk' : 'text-chalk/40'}`}>
                      {g.title}
                      <span className={`block h-px bg-current transition-all duration-700 ${gi === curGroup ? 'w-10 !bg-flame' : 'w-4'}`} />
                    </li>
                  ))}
                </ol>

                <div className="absolute z-[501] left-7 right-7 bottom-6" aria-live="polite">
                  <AnimatePresence mode="wait" initial={false}>
                    <motion.div key={cur.key} initial={{ y: 16, opacity: 0 }} animate={{ y: 0, opacity: 1 }} exit={{ y: -10, opacity: 0 }} transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}>
                      <p className="kicker text-lichen">{cur.touch}</p>
                      <p className="mt-2 font-display text-3xl tracking-[-0.02em]">{cur.name}</p>
                    </motion.div>
                  </AnimatePresence>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
