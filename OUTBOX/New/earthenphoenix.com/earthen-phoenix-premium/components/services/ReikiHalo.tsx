'use client';
import { useEffect, useRef, useState } from 'react';
import type { Service } from '@/lib/content';
import { prefersReduced } from '@/lib/anim';
import Img from '@/components/ui/Img';
import SigCopy from './SigCopy';

/**
 * Reiki: hands on or near the clothed body, never pressing. A warm, clear circle of light follows your hand
 * across her photograph without touching anything; the rest of the room stays dim and soft.
 * Left alone, the light rests in turn at the head, the shoulder and beside the tuning forks.
 * "Hands near" lifts it: wider, softer, and slower to follow.
 */
const RESTS: [number, number][] = [[0.44, 0.42], [0.74, 0.46], [0.56, 0.74]];

export default function ReikiHalo({ s }: { s: Service }) {
  const fig = useRef<HTMLDivElement>(null);
  const [near, setNear] = useState(false);
  const nearRef = useRef(near);
  nearRef.current = near;

  useEffect(() => {
    const el = fig.current;
    if (!el) return;
    const cur = { x: RESTS[0][0], y: RESTS[0][1], r: 0 };
    const target = { x: RESTS[0][0], y: RESTS[0][1] };
    let last = 0, rest = 0, raf = 0, visible = true;
    const reduced = prefersReduced();
    const apply = () => {
      el.style.setProperty('--x', `${cur.x * 100}%`);
      el.style.setProperty('--y', `${cur.y * 100}%`);
      el.style.setProperty('--r', `${cur.r}px`);
    };
    const tick = (t: number) => {
      raf = requestAnimationFrame(tick);
      if (!visible) return;
      if (t - last > 3200) { // no pointer for a while: the hands move to the next resting place
        last = t;
        rest = (rest + 1) % RESTS.length;
        target.x = RESTS[rest][0]; target.y = RESTS[rest][1];
      }
      const n = nearRef.current;
      const k = n ? 0.025 : 0.06;
      cur.x += (target.x - cur.x) * k;
      cur.y += (target.y - cur.y) * k;
      const R = Math.min(el.clientWidth, 900) * (n ? 0.46 : 0.32) * (1 + Math.sin(t / 1400) * 0.04);
      cur.r += (R - cur.r) * 0.05;
      apply();
    };
    if (reduced) { cur.r = el.clientWidth * 0.3; apply(); return; }
    const move = (e: PointerEvent) => {
      const r = el.getBoundingClientRect();
      target.x = (e.clientX - r.left) / r.width;
      target.y = (e.clientY - r.top) / r.height;
      last = performance.now() + 2500;
    };
    const io = new IntersectionObserver(([en]) => { visible = en.isIntersecting; });
    io.observe(el);
    el.addEventListener('pointermove', move);
    el.addEventListener('pointerdown', move);
    raf = requestAnimationFrame(tick);
    return () => { cancelAnimationFrame(raf); io.disconnect(); el.removeEventListener('pointermove', move); el.removeEventListener('pointerdown', move); };
  }, []);

  const soft = near ? 0.45 : 0.25;
  return (
    <section className="sec bg-night text-chalk" aria-labelledby="sig-h">
      <div className="wrap grid gap-14 lg:grid-cols-[minmax(0,4fr)_minmax(0,7fr)] items-center">
        <SigCopy s={s}>
          <div className="seg" role="group" aria-label="Hands">
            <button type="button" aria-pressed={!near} onClick={() => setNear(false)}>Hands on</button>
            <button type="button" aria-pressed={near} onClick={() => setNear(true)}>Hands near</button>
          </div>
        </SigCopy>
        <figure className="m-0">
          <div ref={fig} data-mask="centre" className="relative aspect-[16/10] overflow-hidden rounded-[28px] bg-moss touch-pan-y select-none cursor-none"
            style={{ ['--x' as string]: '44%', ['--y' as string]: '42%', ['--r' as string]: '0px' }}>
            <Img name={s.img} alt={s.alt} className="cover [filter:brightness(.55)_saturate(.6)_blur(3px)] scale-[1.02]" pos="50% 50%" sizes="(max-width: 1023px) 92vw, 60vw" />
            <div className="absolute inset-0" aria-hidden
              style={{ WebkitMaskImage: `radial-gradient(circle var(--r) at var(--x) var(--y), #000 ${100 - soft * 100}%, transparent)`, maskImage: `radial-gradient(circle var(--r) at var(--x) var(--y), #000 ${100 - soft * 100}%, transparent)` }}>
              <Img name={s.img} alt="" className="cover [filter:brightness(1.12)_saturate(1.08)]" pos="50% 50%" sizes="(max-width: 1023px) 92vw, 60vw" />
              <div className="absolute inset-0 mix-blend-soft-light bg-[radial-gradient(circle_var(--r)_at_var(--x)_var(--y),rgba(255,190,120,.55),transparent)]" />
            </div>
            <span className="pointer-events-none absolute size-3 -ml-1.5 -mt-1.5 rounded-full border border-chalk/70" style={{ left: 'var(--x)', top: 'var(--y)' }} aria-hidden />
          </div>
          <figcaption className="mt-4 text-sm text-chalk/55">Her photograph: tuning forks beside a client on the table. The light never touches; it only rests.</figcaption>
        </figure>
      </div>
    </section>
  );
}
