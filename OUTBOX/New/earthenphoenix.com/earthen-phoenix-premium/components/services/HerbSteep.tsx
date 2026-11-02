'use client';
import { useEffect, useRef, useState } from 'react';
import type { Service } from '@/lib/content';
import { gsap, prefersReduced } from '@/lib/anim';
import { wavePolygon } from '@/lib/reveals';
import Img from '@/components/ui/Img';
import SigCopy from './SigCopy';

/**
 * Herbalism: teas, rollies and tinctures. Her photograph starts pale, like water, and the colour comes into it
 * the way each remedy is made:
 *  tea       colour fills slowly from the bottom behind a gently moving surface
 *  tincture  drops fall one at a time; each one raises the level and rings outward
 *  rollie    a single rolled line of colour, exactly where it is put
 */
type Kind = 'tea' | 'tincture' | 'rollie';

export default function HerbSteep({ s }: { s: Service }) {
  const box = useRef<HTMLDivElement>(null);
  const [kind, setKind] = useState<Kind>('tea');
  const level = useRef({ v: 1.05, phase: 0, roll: 0 });
  const dropRef = useRef<(x?: number) => void>(() => {});

  useEffect(() => {
    const el = box.current;
    if (!el) return;
    const top = el.querySelector<HTMLElement>('[data-colour]')!;
    const L = level.current;
    const reduced = prefersReduced();
    gsap.killTweensOf(L);
    let raf = 0, visible = true;

    const draw = () => {
      if (kind === 'rollie') {
        // a diagonal band of colour that rolls across and stays put
        const w = 0.16, x = L.roll * 1.3 - 0.15;
        top.style.clipPath = `polygon(${(x - w) * 100}% 100%, ${x * 100}% 100%, ${(x + 0.35) * 100}% 0%, ${(x + 0.35 - w) * 100}% 0%)`;
        top.style.clipPath = L.roll >= 1 ? 'polygon(0% 100%, 115% 100%, 150% 0%, 35% 0%)' : top.style.clipPath;
      } else {
        top.style.clipPath = wavePolygon(L.v, 0.025 * Math.min(1, Math.max(0.15, L.v + 0.2)), L.phase, 1.4);
      }
    };
    const tick = () => { raf = requestAnimationFrame(tick); if (!visible) return; L.phase += 0.025; draw(); };

    if (reduced) { L.v = -0.1; L.roll = 1; draw(); return; }

    if (kind === 'tea') {
      L.v = 1.05;
      gsap.to(L, { v: -0.06, duration: 7, ease: 'sine.inOut', repeat: -1, repeatDelay: 2.4, yoyo: false });
    } else if (kind === 'tincture') {
      L.v = 1.05;
    } else {
      L.roll = 0;
      gsap.to(L, { roll: 1, duration: 3.2, ease: 'power2.inOut', repeat: -1, repeatDelay: 2 });
    }

    dropRef.current = (x = 0.3 + Math.random() * 0.4) => {
      if (kind !== 'tincture') return;
      const d = document.createElement('span');
      d.className = 'absolute size-3 -ml-1.5 rounded-full bg-amber shadow-[0_0_12px_rgba(242,166,90,.8)] pointer-events-none';
      d.style.left = `${x * 100}%`; d.style.top = '0%';
      el.appendChild(d);
      const surface = Math.max(0.05, L.v);
      gsap.to(d, { top: `${surface * 100}%`, duration: 0.7, ease: 'power2.in', onComplete: () => {
        d.remove();
        const ring = document.createElement('span');
        ring.className = 'absolute rounded-full border border-amber/80 pointer-events-none';
        Object.assign(ring.style, { left: `${x * 100}%`, top: `${surface * 100}%`, width: '24px', height: '10px', marginLeft: '-12px', marginTop: '-5px' });
        el.appendChild(ring);
        gsap.fromTo(ring, { scale: 0.5, opacity: 1 }, { scale: 7, opacity: 0, duration: 1.4, ease: 'expo.out', onComplete: () => ring.remove() });
        gsap.to(L, { v: L.v <= 0 ? 1.05 : L.v - 0.14, duration: L.v <= 0 ? 1.2 : 0.9, ease: 'expo.out' });
      } });
    };
    const auto = kind === 'tincture' ? window.setInterval(() => visible && dropRef.current(), 1500) : 0;
    const io = new IntersectionObserver(([en]) => { visible = en.isIntersecting; });
    io.observe(el);
    raf = requestAnimationFrame(tick);
    return () => { cancelAnimationFrame(raf); window.clearInterval(auto); io.disconnect(); gsap.killTweensOf(L); };
  }, [kind]);

  return (
    <section className="sec bg-mist text-ink" aria-labelledby="sig-h">
      <div className="wrap grid gap-14 lg:grid-cols-[minmax(0,4fr)_minmax(0,7fr)] items-center">
        <SigCopy s={s}>
          <div className="seg" role="group" aria-label="Remedy">
            {(['tea', 'tincture', 'rollie'] as Kind[]).map((k) => (
              <button key={k} type="button" aria-pressed={kind === k} onClick={() => setKind(k)}>{{ tea: 'Teas', tincture: 'Tinctures', rollie: 'Rollies' }[k]}</button>
            ))}
          </div>
        </SigCopy>
        <figure className="m-0">
          <div ref={box} data-mask="up" className="relative aspect-[4/3] overflow-hidden rounded-[28px] bg-moss cursor-pointer select-none"
            onPointerDown={(e) => { const r = e.currentTarget.getBoundingClientRect(); dropRef.current((e.clientX - r.left) / r.width); }}>
            <Img name={s.img} alt={s.alt} className="cover [filter:grayscale(1)_brightness(1.35)_contrast(.7)]" pos={s.pos} sizes="(max-width: 1023px) 92vw, 60vw" />
            <div data-colour className="absolute inset-0" style={{ clipPath: 'inset(100% 0 0 0)' }}>
              <Img name={s.img} alt="" className="cover" pos={s.pos} sizes="(max-width: 1023px) 92vw, 60vw" />
            </div>
          </div>
          <figcaption className="mt-4 text-sm text-ink-2">{kind === 'tincture' ? 'Tap the photograph to add a drop.' : 'An Armature oil beside fresh rosemary, from the Earthen Phoenix shop.'}</figcaption>
        </figure>
      </div>
    </section>
  );
}
