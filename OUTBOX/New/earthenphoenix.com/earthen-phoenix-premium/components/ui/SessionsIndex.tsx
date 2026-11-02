'use client';
import { useRef, useState, type PointerEvent } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { REGISTER, SERVICE, type ServiceKey } from '@/lib/content';
import { imgSrc } from '@/lib/images';
import { href } from '@/lib/site';

/** Every session and price, grouped by how her hands meet the body. A photo of the session trails the pointer. */
export default function SessionsIndex() {
  const box = useRef<HTMLDivElement>(null);
  const [hover, setHover] = useState<ServiceKey | null>(null);
  const [pt, setPt] = useState({ x: 0, y: 0 });
  const move = (e: PointerEvent) => {
    const r = box.current?.getBoundingClientRect();
    if (r) setPt({ x: e.clientX - r.left, y: e.clientY - r.top });
  };
  return (
    <div ref={box} className="relative" onPointerMove={move} onPointerLeave={() => setHover(null)}>
      {REGISTER.map((g, gi) => (
        <div key={g.title} className="mt-16 first:mt-0" data-reveal>
          <p className="flex items-baseline gap-4 pb-4">
            <span className="font-display italic text-2xl text-clay">{['i', 'ii', 'iii', 'iv', 'v'][gi]}.</span>
            <span className="kicker !gap-0 before:!hidden">{g.title}</span>
            <span className="text-sm text-ink-2 hidden sm:inline">{g.note}</span>
          </p>
          <ul>
            {g.keys.map((k) => {
              const s = SERVICE[k];
              return (
                <li key={k} className="border-t border-ink/15">
                  <a href={href('/' + s.slug)} onPointerEnter={(e) => e.pointerType === 'mouse' && setHover(k)}
                    className="group grid grid-cols-[1fr_auto] md:grid-cols-[minmax(0,1.1fr)_minmax(0,1fr)_120px_150px] items-baseline gap-x-6 gap-y-2 py-6">
                    <span className="font-display text-[clamp(1.7rem,3vw,2.7rem)] leading-none tracking-[-0.025em] transition-transform duration-700 ease-[cubic-bezier(.16,1,.3,1)] group-hover:translate-x-3 group-hover:text-clay">{s.full}</span>
                    <span className="md:order-none order-3 col-span-2 md:col-span-1 text-ink-2">{s.line}</span>
                    <span className="hidden md:block text-ink-2 tabular-nums">{s.length}</span>
                    <span className="text-right tabular-nums font-medium">{s.price}</span>
                  </a>
                </li>
              );
            })}
          </ul>
        </div>
      ))}
      <AnimatePresence>
        {hover && (
          <motion.div key="peek" className="pointer-events-none absolute z-10 hidden md:block w-[240px] aspect-[4/5] overflow-hidden rounded-[18px] bg-moss shadow-2xl"
            initial={{ opacity: 0, scale: 0.85 }} animate={{ opacity: 1, scale: 1, x: pt.x - 120, y: pt.y - 330 }} exit={{ opacity: 0, scale: 0.85 }}
            transition={{ type: 'spring', stiffness: 160, damping: 22, mass: 0.6 }} style={{ left: 0, top: 0 }}>
            <AnimatePresence initial={false}>
              <motion.img key={hover} src={imgSrc(SERVICE[hover].img)} alt="" className="cover" style={{ objectPosition: SERVICE[hover].pos }}
                initial={{ clipPath: 'inset(100% 0% 0% 0%)' }} animate={{ clipPath: 'inset(0% 0% 0% 0%)' }} transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }} />
            </AnimatePresence>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
