'use client';
import { useState } from 'react';
import { motion, useReducedMotion } from 'motion/react';
import type { Service } from '@/lib/content';
import { imgSrc } from '@/lib/images';
import SigCopy from './SigCopy';

/**
 * Astrology & tarot. Four cards lie face down: one for each thing she says tarot helps you do. Turn a card and its
 * face is a quarter of her candlelit photograph; turn all four and the whole picture is there.
 */
const CARDS = [
  ['Consider a problem', 'Bring the question you are carrying.'],
  ['Give a voice to it', 'Say it out loud, with the cards.'],
  ['Work it through', 'Together, at your pace.'],
  ['See the blocks', 'Where things might be stuck.'],
] as const;

function Back() {
  return (
    <svg viewBox="0 0 100 160" className="absolute inset-0 w-full h-full" aria-hidden>
      <rect x="5" y="5" width="90" height="150" rx="6" fill="none" stroke="#ec6a3f" strokeOpacity=".6" />
      <rect x="10" y="10" width="80" height="140" rx="4" fill="none" stroke="#f6f7f4" strokeOpacity=".18" />
      {[34, 24, 14].map((r) => <circle key={r} cx="50" cy="80" r={r} fill="none" stroke="#f6f7f4" strokeOpacity={0.12 + (34 - r) / 120} />)}
      {Array.from({ length: 12 }, (_, i) => {
        const a = (i / 12) * Math.PI * 2;
        return <line key={i} x1={50 + Math.cos(a) * 16} y1={80 + Math.sin(a) * 16} x2={50 + Math.cos(a) * 32} y2={80 + Math.sin(a) * 32} stroke="#f2a65a" strokeOpacity=".35" strokeWidth=".6" />;
      })}
      <circle cx="50" cy="80" r="4" fill="#ec6a3f" />
      {[[22, 28], [78, 30], [20, 132], [80, 128], [50, 26], [50, 136]].map(([x, y]) => <circle key={`${x}${y}`} cx={x} cy={y} r=".9" fill="#f6f7f4" opacity=".6" />)}
    </svg>
  );
}

export default function TarotDraw({ s }: { s: Service }) {
  const [up, setUp] = useState<boolean[]>([false, false, false, false]);
  const reduce = useReducedMotion();
  const src = imgSrc(s.img, true);
  const flip = (i: number) => setUp((u) => u.map((v, j) => (j === i ? !v : v)));
  const all = up.every(Boolean);

  return (
    <section className="sec bg-night text-chalk" aria-labelledby="sig-h">
      <div className="wrap grid gap-14 lg:grid-cols-[minmax(0,4fr)_minmax(0,7fr)] items-center">
        <SigCopy s={s}>
          <button type="button" className="btn btn-ghost" onClick={() => setUp(all ? [false, false, false, false] : [true, true, true, true])}>
            {all ? 'Lay them face down' : 'Turn all four'}
          </button>
        </SigCopy>
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 sm:gap-4 [perspective:1400px]">
          {CARDS.map(([t, d], i) => (
            <button key={t} type="button" onClick={() => flip(i)} aria-pressed={up[i]} aria-label={`${t}: ${d}${up[i] ? ' (turned over)' : ''}`}
              className="relative aspect-[5/8] text-left" data-reveal data-delay={i}>
              <motion.span className="absolute inset-0 [transform-style:preserve-3d]" animate={{ rotateY: up[i] ? 180 : 0, y: up[i] ? -8 : 0 }}
                transition={reduce ? { duration: 0 } : { duration: 0.9, ease: [0.16, 1, 0.3, 1] }}>
                <span className="absolute inset-0 rounded-[18px] bg-moss overflow-hidden [backface-visibility:hidden] shadow-[0_30px_60px_-30px_rgba(0,0,0,.8)]">
                  <Back />
                  <span className="absolute inset-x-0 bottom-4 text-center text-[.7rem] uppercase tracking-[.2em] text-chalk/60">{['i', 'ii', 'iii', 'iv'][i]}</span>
                </span>
                <span className="absolute inset-0 rounded-[18px] overflow-hidden [backface-visibility:hidden] [transform:rotateY(180deg)] bg-moss">
                  {/* one quarter of her photograph per card */}
                  <span className="absolute inset-0" style={{ backgroundImage: `url(${src})`, backgroundSize: '400% auto', backgroundPosition: `${(i / 3) * 100}% 50%` }} />
                  <span className="absolute inset-0 bg-gradient-to-t from-night/90 via-night/10 to-transparent" />
                  <span className="absolute inset-x-3 bottom-3">
                    <b className="block font-display font-normal text-[1.05rem] leading-tight">{t}</b>
                    <span className="block text-[.78rem] text-chalk/70 mt-1">{d}</span>
                  </span>
                </span>
              </motion.span>
            </button>
          ))}
        </div>
      </div>
    </section>
  );
}
