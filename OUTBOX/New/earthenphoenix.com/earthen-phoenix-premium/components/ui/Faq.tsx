'use client';
import { useState } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import { Plus } from 'lucide-react';
import type { QA } from '@/lib/content';
import Rich from './Rich';

/** Accessible accordion: real buttons, aria-expanded, and the answer's height animated by Motion. */
export default function Faq({ items, dark }: { items: QA[]; dark?: boolean }) {
  const [open, setOpen] = useState<number | null>(0);
  return (
    <div className={dark ? 'text-chalk' : ''}>
      {items.map(([q, a], i) => {
        const isOpen = open === i;
        const id = `faq-${q.replace(/[^a-z0-9]+/gi, '-').toLowerCase()}`;
        return (
          <div key={q} className="faq-item">
            <h3>
              <button type="button" aria-expanded={isOpen} aria-controls={id} onClick={() => setOpen(isOpen ? null : i)}
                className="group w-full flex items-center justify-between gap-6 py-6 text-left font-display text-[clamp(1.25rem,1.9vw,1.6rem)] leading-snug tracking-[-0.01em]">
                <span className="transition-transform duration-500 group-hover:translate-x-1">{q}</span>
                <span className={`shrink-0 grid place-items-center size-10 rounded-full border transition-all duration-500 ${isOpen ? 'rotate-45 bg-flame border-flame text-chalk' : 'border-current/25'}`} aria-hidden>
                  <Plus size={18} strokeWidth={1.5} />
                </span>
              </button>
            </h3>
            <AnimatePresence initial={false}>
              {isOpen && (
                <motion.div id={id} key="a" initial={{ height: 0, opacity: 0 }} animate={{ height: 'auto', opacity: 1 }} exit={{ height: 0, opacity: 0 }}
                  transition={{ duration: 0.55, ease: [0.16, 1, 0.3, 1] }} className="overflow-hidden">
                  <p className={`rich pb-7 max-w-[62ch] ${dark ? 'text-chalk/75' : 'text-ink-2'}`}><Rich text={a} /></p>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        );
      })}
    </div>
  );
}
