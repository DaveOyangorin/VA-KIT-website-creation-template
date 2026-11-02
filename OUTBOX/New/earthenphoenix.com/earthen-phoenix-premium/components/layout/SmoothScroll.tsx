'use client';
import { useEffect } from 'react';
import Lenis from 'lenis';
import { gsap, ScrollTrigger, prefersReduced } from '@/lib/anim';

declare global {
  interface Window { __lenis?: Lenis }
}

/** Lenis smooth scrolling, driven by GSAP's ticker so ScrollTrigger stays in lockstep. Off under reduced motion. */
export default function SmoothScroll() {
  useEffect(() => {
    if (prefersReduced()) return;
    const lenis = new Lenis({ duration: 1.15, easing: (t) => 1 - Math.pow(1 - t, 4), touchMultiplier: 1.4 });
    window.__lenis = lenis;
    lenis.on('scroll', ScrollTrigger.update);
    const tick = (time: number) => lenis.raf(time * 1000);
    gsap.ticker.add(tick);
    gsap.ticker.lagSmoothing(0);

    // In-page anchors glide instead of jumping.
    const onClick = (e: MouseEvent) => {
      const a = (e.target as HTMLElement).closest('a');
      const h = a?.getAttribute('href');
      if (!a || !h || !h.startsWith('#') || h.length < 2) return;
      const target = document.getElementById(h.slice(1));
      if (!target) return;
      e.preventDefault();
      lenis.scrollTo(target, { offset: -70 });
    };
    document.addEventListener('click', onClick);
    return () => {
      document.removeEventListener('click', onClick);
      gsap.ticker.remove(tick);
      lenis.destroy();
      window.__lenis = undefined;
    };
  }, []);
  return null;
}
