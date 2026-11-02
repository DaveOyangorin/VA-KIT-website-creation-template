'use client';
import { useRef } from 'react';
import type { Service } from '@/lib/content';
import { gsap, useGsap } from '@/lib/anim';
import { imgSet } from '@/lib/images';
import SigCopy from './SigCopy';

/**
 * Thai bodywork: rhythmic compressions, then full-body stretching. Her photograph is cut into ten upright bands.
 * Palms press on a steady beat, alternating, from one side to the other; then the whole picture is drawn long,
 * the bands opening apart, before it settles. Tap anywhere to add a press of your own.
 */
const N = 10;

export default function ThaiRhythm({ s }: { s: Service }) {
  const ref = useRef<HTMLDivElement>(null);
  const pic = imgSet(s.img);

  useGsap(ref, ({ reduced, el }) => {
    const bands = gsap.utils.toArray<HTMLElement>(el.querySelectorAll('[data-band]'));
    if (reduced) return;
    const press = (i: number, at: number, tl: gsap.core.Timeline, depth = 0.9) => {
      tl.to(bands[i], { scaleY: depth, filter: 'brightness(.82)', duration: 0.14, ease: 'power3.out' }, at)
        .to(bands[i], { scaleY: 1, filter: 'brightness(1)', duration: 0.5, ease: 'elastic.out(1, .5)' }, at + 0.14);
    };
    const loop = gsap.timeline({ repeat: -1, repeatDelay: 0.6, paused: true });
    const beat = 0.42;
    for (let b = 0; b < N; b++) { // alternating palms, walking across the body
      const i = b % 2 === 0 ? b : b;
      press(i, b * beat, loop);
      if (i + 1 < N) press(i + 1, b * beat + beat / 2, loop, 0.95);
    }
    const end = N * beat + 0.3;
    // the stretch: drawn long, bands opening apart, then a slow release
    loop.to(bands, { x: (i) => (i - (N - 1) / 2) * 7, scaleX: 1.03, duration: 1.4, ease: 'sine.inOut' }, end)
      .to(el.querySelector('[data-strip]'), { scaleX: 1.05, duration: 1.4, ease: 'sine.inOut' }, end)
      .to(bands, { x: 0, scaleX: 1, duration: 1.6, ease: 'power3.inOut' }, end + 2.2)
      .to(el.querySelector('[data-strip]'), { scaleX: 1, duration: 1.6, ease: 'power3.inOut' }, end + 2.2);

    const io = new IntersectionObserver(([en]) => (en.isIntersecting ? loop.play() : loop.pause()), { threshold: 0.3 });
    io.observe(el);

    const tap = (e: PointerEvent) => {
      const r = el.getBoundingClientRect();
      const i = Math.min(N - 1, Math.max(0, Math.floor(((e.clientX - r.left) / r.width) * N)));
      const tl = gsap.timeline();
      for (let d = 0; d < N; d++) { // the press spreads outward from where you touched
        if (i - d >= 0) press(i - d, d * 0.06, tl, 0.88 + d * 0.012);
        if (d && i + d < N) press(i + d, d * 0.06, tl, 0.88 + d * 0.012);
      }
    };
    el.addEventListener('pointerdown', tap);
    return () => { io.disconnect(); loop.kill(); el.removeEventListener('pointerdown', tap); };
  });

  return (
    <section className="sec bg-[color-mix(in_oklab,var(--tint,var(--color-mist))_24%,var(--color-mist))] text-ink" aria-labelledby="sig-h">
      <div className="wrap grid gap-14 lg:grid-cols-[minmax(0,4fr)_minmax(0,7fr)] items-center">
        <SigCopy s={s} />
        <figure className="m-0">
          <div ref={ref} data-mask="up" className="relative aspect-[3/2] cursor-pointer select-none" role="img" aria-label={`${s.alt}, cut into bands that press on a beat and then stretch apart`}>
            <div data-strip className="absolute inset-0 flex">
              {Array.from({ length: N }, (_, i) => (
                <div key={i} data-band className="relative h-full overflow-hidden origin-bottom first:rounded-l-[24px] last:rounded-r-[24px]" style={{ width: `${100 / N}%` }}>
                  {/* eslint-disable-next-line @next/next/no-img-element */}
                  <img src={pic.src} srcSet={pic.srcSet} sizes="(max-width: 1023px) 92vw, 60vw" alt="" loading="lazy"
                    className="absolute top-0 h-full max-w-none object-cover" style={{ width: `${N * 100}%`, left: `${-i * 100}%`, objectPosition: s.pos }} />
                </div>
              ))}
            </div>
          </div>
          <figcaption className="mt-4 text-sm text-ink-2">Her photograph: an assisted stretch on the hillside.</figcaption>
        </figure>
      </div>
    </section>
  );
}
