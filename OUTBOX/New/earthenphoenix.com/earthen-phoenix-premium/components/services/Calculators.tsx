'use client';
import { useState } from 'react';
import { AnimatePresence, motion } from 'motion/react';

const roll = { initial: { y: '60%', opacity: 0 }, animate: { y: '0%', opacity: 1 }, exit: { y: '-60%', opacity: 0 }, transition: { duration: 0.45, ease: [0.16, 1, 0.3, 1] as const } };

/** Private yoga is $140 for the hour, private or split between group participants. */
export function YogaSplit() {
  const [n, setN] = useState(1);
  const each = 140 / n;
  return (
    <div className="grid gap-6">
      <label className="grid gap-3">
        <span className="flex justify-between text-sm"><span>People sharing the hour</span><output className="tabular-nums font-medium">{n === 1 ? 'Just you' : n}</output></span>
        <input className="range text-ink" type="range" min={1} max={6} step={1} value={n} onChange={(e) => setN(Number(e.target.value))} />
      </label>
      <p className="font-display text-[clamp(3rem,6vw,5rem)] leading-none tabular-nums overflow-hidden h-[1.05em]" aria-live="polite">
        <AnimatePresence mode="popLayout" initial={false}>
          <motion.span key={n} className="block" {...roll}>${Number.isInteger(each) ? each : each.toFixed(2)}</motion.span>
        </AnimatePresence>
      </p>
      <p className="text-ink-2 -mt-3">{n === 1 ? 'for your private hour' : `each, if ${n} of you split the $140 hour evenly`}</p>
    </div>
  );
}

/** Readings are $2 a minute. */
export function ReadingCost() {
  const [m, setM] = useState(30);
  return (
    <div className="grid gap-6">
      <div className="seg" role="group" aria-label="Reading length">
        {[15, 30, 45, 60].map((x) => <button key={x} type="button" aria-pressed={m === x} onClick={() => setM(x)}>{x} min</button>)}
      </div>
      <p className="font-display text-[clamp(3rem,6vw,5rem)] leading-none tabular-nums overflow-hidden h-[1.05em]" aria-live="polite">
        <AnimatePresence mode="popLayout" initial={false}>
          <motion.span key={m} className="block" {...roll}>${m * 2}</motion.span>
        </AnimatePresence>
      </p>
      <p className="text-ink-2 -mt-3">{m} minutes at $2 a minute</p>
    </div>
  );
}
