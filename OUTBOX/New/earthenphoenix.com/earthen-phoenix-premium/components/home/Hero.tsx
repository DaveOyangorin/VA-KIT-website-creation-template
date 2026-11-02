'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import { imgSet } from '@/lib/images';
import { BOOK, href } from '@/lib/site';
import { Arr } from '@/components/ui/Arrow';

/**
 * "Rise & Rest". Her meadow photograph is split in two: the sky, and everything below the ridge (cut from the same
 * photo). The headline lives between them, so it rises from behind the real Wasatch ridge on arrival (the phoenix)
 * and sinks back behind it as you scroll (ground your soul).
 */

// Height of the ridge across the photo (fraction of image height), sampled from the cutout at 41 points.
const RIDGE = [0.141, 0.162, 0.188, 0.209, 0.269, 0.31, 0.304, 0.294, 0.292, 0.296, 0.294, 0.307, 0.306, 0.292, 0.289, 0.278, 0.293, 0.301, 0.306, 0.311, 0.291, 0.309, 0.317, 0.322, 0.313, 0.311, 0.281, 0.257, 0.234, 0.213, 0.177, 0.172, 0.142, 0.129, 0.13, 0.132, 0.137, 0.134, 0.136, 0.154, 0.142];
const ridgeAt = (fx: number) => {
  const t = Math.min(40, Math.max(0, fx * 40));
  const i = Math.floor(t), f = t - i;
  return RIDGE[i] * (1 - f) + RIDGE[Math.min(40, i + 1)] * f;
};
const IW = 1600, IH = 1067;

export default function Hero() {
  const ref = useRef<HTMLElement>(null);
  const base = imgSet('mountain-meadow');
  const ridge = imgSet('mountain-meadow-ridge');

  useGsap(ref, ({ reduced, el }) => {
    const scene = el.querySelector<HTMLElement>('[data-scene]')!;
    const zoom = el.querySelector<HTMLElement>('[data-zoom]')!;
    const title = el.querySelector<HTMLElement>('[data-title]')!;
    const sink = el.querySelector<HTMLElement>('[data-sink]')!;
    const words = title.querySelectorAll<HTMLElement>('[data-w]');

    // Seat the headline on the ridge for this viewport: its last line's lower fifth tucks behind the mountains.
    const seat = () => {
      const W = scene.clientWidth, H = scene.clientHeight;
      const cs = getComputedStyle(scene);
      const px = parseFloat(cs.getPropertyValue('--px')) / 100 || 0.5;
      const py = parseFloat(cs.getPropertyValue('--py')) / 100 || 0.5;
      const s = Math.max(W / IW, H / IH);
      const wi = IW * s, hi = IH * s, x0 = (W - wi) * px, y0 = (H - hi) * py;
      const left = title.offsetLeft, width = title.offsetWidth;
      // Ridge height under the right two-thirds of the headline (the left edge meets a steep slope).
      const samples: number[] = [];
      for (let i = 0; i <= 12; i++) {
        const sx = left + width * (0.33 + (0.67 * i) / 12);
        samples.push(y0 + ridgeAt((sx - x0) / wi) * hi);
      }
      samples.sort((a, b) => a - b);
      const ridgeY = samples[Math.floor(samples.length / 2)];
      const fs = parseFloat(getComputedStyle(title).fontSize);
      title.style.top = `${ridgeY - title.offsetHeight + fs * 0.1}px`;
    };
    seat();
    const ro = new ResizeObserver(seat);
    ro.observe(scene);
    document.fonts?.ready.then(seat);

    if (reduced) { gsap.set([words, '[data-in]'], { clearProps: 'all' }); return () => ro.disconnect(); }

    // Arrival: slow cinematic settle of the whole scene; the words climb out from behind the ridge.
    const intro = gsap.timeline({ delay: 0.15, paused: true });
    Promise.race([document.fonts?.ready, new Promise((r) => setTimeout(r, 1200))]).then(() => { seat(); intro.play(); });
    intro
      .fromTo(zoom, { scale: 1.14 }, { scale: 1, duration: 3.2, ease: 'expo.out' }, 0)
      .fromTo(words, { yPercent: 135, y: 0 }, { yPercent: 0, y: 0, duration: 2, stagger: 0.12, ease: 'expo.out' }, 0.35)
      .fromTo('[data-in]', { y: 26, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 1.3, stagger: 0.1, ease: 'expo.out' }, 1.1);

    // Scroll: the headline sinks behind the mountains while the land drifts more slowly: grounding.
    const fs = () => parseFloat(getComputedStyle(title).fontSize);
    gsap.timeline({ scrollTrigger: { trigger: el, start: 'top top', end: 'bottom top', scrub: 0.6 } })
      .to(sink, { y: () => fs() * 1.9, ease: 'none' }, 0)
      .to(scene, { yPercent: 12, ease: 'none' }, 0)
      .to('[data-copy]', { y: -60, autoAlpha: 0, ease: 'none' }, 0);

    // A little depth under the pointer: only the headline moves, so the two photo layers never part.
    const move = (e: PointerEvent) => {
      if (e.pointerType !== 'mouse') return;
      const nx = e.clientX / window.innerWidth - 0.5;
      gsap.to(title, { x: nx * -14, duration: 1.6, ease: 'power3.out' });
    };
    el.addEventListener('pointermove', move);
    return () => { ro.disconnect(); el.removeEventListener('pointermove', move); };
  });

  const layer = 'absolute inset-0 w-full h-full object-cover [object-position:var(--px)_var(--py)] [mask-image:linear-gradient(to_bottom,transparent_0,#000_10%)]';

  return (
    <section ref={ref} className="relative h-[100svh] min-h-[620px] max-h-[1100px] overflow-hidden bg-[#ebeff2]" aria-labelledby="hero-h">
      {/* The sky, extended upward from the photo's own colour so the headline has room. */}
      <div className="absolute inset-0 bg-gradient-to-b from-[#e2e8ec] to-[#ebeff2]" />

      <div data-scene className="absolute inset-x-0 bottom-0 top-[30svh] md:top-[22svh] [--px:84%] [--py:40%] md:[--px:50%] md:[--py:38%] min-[1600px]:[--py:16%] will-change-transform">
        <div data-zoom className="absolute inset-0 origin-[50%_42%]">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={base.src} srcSet={base.srcSet} sizes="100vw" width={base.width} height={base.height} alt="Miquelle and a student greeting each other in a mountain meadow below the Wasatch peaks"
            className={layer} fetchPriority="high" decoding="async" />
          <div data-sink className="absolute inset-0 will-change-transform">
            <h1 id="hero-h" data-title className="display absolute left-[var(--gutter)] text-ink text-[clamp(3.6rem,19vw,6.4rem)] md:text-[clamp(5rem,9.6vw,10rem)] leading-[0.86] whitespace-nowrap">
              <span className="block"><span data-w className="inline-block">Ground</span></span>{' '}
              <span className="block"><span data-w className="inline-block">your</span><br className="md:hidden" /><span className="hidden md:inline"> </span><em data-w className="inline-block text-clay">soul.</em></span>
            </h1>
          </div>
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={ridge.src} srcSet={ridge.srcSet} sizes="100vw" width={ridge.width} height={ridge.height} alt="" aria-hidden className={layer} fetchPriority="high" decoding="async" />
        </div>
      </div>

      <p data-in className="kicker absolute left-[var(--gutter)] top-[calc(var(--hdr)+22px)] md:top-[calc(var(--hdr)+28px)] text-ink/75 z-[2]">
        Salt Lake City · Massage · Bodywork · Reiki · Yoga
      </p>

      <div className="absolute inset-x-0 bottom-0 h-[52%] bg-gradient-to-t from-night/85 via-night/40 to-transparent pointer-events-none" />

      <div data-copy className="px-[var(--gutter)] absolute inset-x-0 bottom-0 pb-[clamp(28px,5vw,64px)] flex flex-wrap items-end justify-between gap-8 text-chalk">
        <div className="max-w-[540px]">
          <p data-in className="lede">Massage, bodywork, Reiki, private yoga, readings and herbal remedies with Miquelle in Salt Lake City, Utah.</p>
          <div data-in className="mt-7 flex flex-wrap gap-3">
            <a href={BOOK} className="btn btn-flame">Get an appointment <Arr /></a>
            <a href={href('/sessions')} className="btn btn-ghost">See every session</a>
          </div>
        </div>
        <p data-in className="hidden md:flex items-center gap-3 text-sm text-chalk/80">
          <span className="relative block w-px h-12 bg-chalk/30 overflow-hidden"><span className="absolute inset-x-0 top-0 h-1/2 bg-chalk animate-[drop_2.4s_ease-in-out_infinite]" /></span>
          Scroll to ground
        </p>
      </div>
    </section>
  );
}
