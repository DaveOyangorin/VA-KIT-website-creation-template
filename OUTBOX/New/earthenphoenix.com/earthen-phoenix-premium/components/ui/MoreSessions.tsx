'use client';
import { useRef, useState, type PointerEvent } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { SERVICE, type ServiceKey } from '@/lib/content';
import { imgSrc } from '@/lib/images';
import { href } from '@/lib/site';
import { Arr } from './Arrow';

/**
 * Related sessions as an editorial index. On hover, a photo of the session follows the pointer;
 * on touch screens each row carries its own small photo instead.
 */
export default function MoreSessions({ keys, title = 'Other ways to ground.' }: { keys: ServiceKey[]; title?: string }) {
  const [hover, setHover] = useState<ServiceKey | null>(null);
  const box = useRef<HTMLDivElement>(null);
  const [pt, setPt] = useState({ x: 0, y: 0 });
  const move = (e: PointerEvent) => {
    const r = box.current?.getBoundingClientRect();
    if (r) setPt({ x: e.clientX - r.left, y: e.clientY - r.top });
  };
  return (
    <section className="sec bg-mist" aria-labelledby="more-h">
      <div className="wrap">
        <p className="kicker" data-reveal>Keep exploring</p>
        <h2 id="more-h" className="h2 mt-6" data-reveal>{title}</h2>
        <div ref={box} className="relative mt-14" onPointerMove={move} onPointerLeave={() => setHover(null)}>
          <ul>
            {keys.map((k) => {
              const s = SERVICE[k];
              return (
                <li key={k} className="border-t border-ink/15 last:border-b">
                  <a href={href('/' + s.slug)} onPointerEnter={(e) => e.pointerType === 'mouse' && setHover(k)}
                    className="group grid grid-cols-[64px_1fr_auto] md:grid-cols-[1fr_auto_auto] items-center gap-5 md:gap-10 py-6 md:py-8">
                    {/* eslint-disable-next-line @next/next/no-img-element */}
                    <img src={imgSrc(s.img)} alt="" loading="lazy" className="md:hidden size-16 rounded-xl object-cover" style={{ objectPosition: s.pos }} />
                    <span className="font-display text-[clamp(1.7rem,3.6vw,3.4rem)] leading-none tracking-[-0.025em] transition-transform duration-700 ease-[cubic-bezier(.16,1,.3,1)] group-hover:translate-x-3">{s.name}</span>
                    <span className="hidden md:block text-ink-2">{s.touch}</span>
                    <span className="flex items-center gap-3 tabular-nums text-ink-2 group-hover:text-clay transition-colors">{s.price}<span className="hidden sm:inline"><Arr /></span></span>
                  </a>
                </li>
              );
            })}
          </ul>
          <AnimatePresence>
            {hover && (
              <motion.div key="peek" className="pointer-events-none absolute z-10 hidden md:block w-[260px] aspect-[4/5] overflow-hidden rounded-[18px] bg-moss shadow-2xl"
                initial={{ opacity: 0, scale: 0.85 }} animate={{ opacity: 1, scale: 1, x: pt.x + 24, y: pt.y - 160 }} exit={{ opacity: 0, scale: 0.85 }}
                transition={{ type: 'spring', stiffness: 160, damping: 22, mass: 0.6 }} style={{ left: 0, top: 0 }}>
                <AnimatePresence initial={false}>
                  <motion.img key={hover} src={imgSrc(SERVICE[hover].img)} alt="" className="cover" style={{ objectPosition: SERVICE[hover].pos }}
                    initial={{ clipPath: 'inset(100% 0% 0% 0%)' }} animate={{ clipPath: 'inset(0% 0% 0% 0%)' }} transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }} />
                </AnimatePresence>
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </div>
    </section>
  );
}
