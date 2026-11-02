'use client';
import { useEffect, useState } from 'react';
import { AnimatePresence, motion, useReducedMotion } from 'motion/react';
import { VOICES } from '@/lib/content';

/** The three client quotes from her current site, one at a time. */
export default function Voices() {
  const [i, setI] = useState(0);
  const [paused, setPaused] = useState(false);
  const reduce = useReducedMotion();
  useEffect(() => {
    if (paused || reduce) return;
    const t = window.setTimeout(() => setI((n) => (n + 1) % VOICES.length), 7000);
    return () => window.clearTimeout(t);
  }, [i, paused, reduce]);
  const v = VOICES[i];
  return (
    <section className="sec bg-night text-chalk" aria-labelledby="voices-h" onMouseEnter={() => setPaused(true)} onMouseLeave={() => setPaused(false)} onFocus={() => setPaused(true)}>
      <div className="wrap">
        <p id="voices-h" className="kicker text-lichen" data-reveal>Client words</p>
        <div className="relative mt-10 min-h-[9em] sm:min-h-[6em] lg:min-h-[4.1em] text-[clamp(1.9rem,4.4vw,4.2rem)]" aria-live="polite">
          <AnimatePresence mode="wait">
            <motion.figure key={i} className="absolute inset-0"
              initial={{ opacity: 0, y: 24, filter: 'blur(6px)' }} animate={{ opacity: 1, y: 0, filter: 'blur(0px)' }} exit={{ opacity: 0, y: -16, filter: 'blur(6px)' }}
              transition={{ duration: 0.9, ease: [0.16, 1, 0.3, 1] }}>
              <blockquote className="font-display font-light leading-[1.08] tracking-[-0.025em] max-w-[30ch]" style={{ fontVariationSettings: "'SOFT' 100, 'opsz' 120" }}>
                <span className="text-flame">“</span>{v.quote}<span className="text-flame">”</span>
              </blockquote>
              <figcaption className="mt-6 text-base tracking-[.18em] uppercase text-chalk/60">{v.name}</figcaption>
            </motion.figure>
          </AnimatePresence>
        </div>
        <div className="mt-10 flex gap-3" role="group" aria-label="Choose a quote">
          {VOICES.map((x, n) => (
            <button key={x.name} type="button" onClick={() => setI(n)} aria-label={`Words from ${x.name}`} aria-pressed={n === i} className="relative h-11 w-16">
              <span className="absolute left-0 right-0 top-1/2 h-px bg-chalk/25 overflow-hidden">
                <span key={n === i ? i : -1} className={`absolute inset-0 bg-flame origin-left ${n === i ? (paused || reduce ? 'scale-x-100' : 'animate-[fill_7s_linear_forwards]') : 'scale-x-0'}`} />
              </span>
            </button>
          ))}
        </div>
      </div>
    </section>
  );
}
