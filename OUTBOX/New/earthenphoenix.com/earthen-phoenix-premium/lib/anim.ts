'use client';
import { useEffect, useLayoutEffect, type DependencyList, type RefObject } from 'react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

if (typeof window !== 'undefined') {
  gsap.registerPlugin(ScrollTrigger);
  gsap.defaults({ ease: 'expo.out', duration: 1.2 });
}

export { gsap, ScrollTrigger };

export const prefersReduced = () =>
  typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

export const isTouch = () => typeof window !== 'undefined' && window.matchMedia('(hover: none)').matches;

const useIso = typeof window !== 'undefined' ? useLayoutEffect : useEffect;

/** Runs GSAP code scoped to a ref and reverts it on unmount. Skipped entirely under reduced motion unless `always`. */
export function useGsap(
  scope: RefObject<HTMLElement | null>,
  fn: (ctx: { reduced: boolean; el: HTMLElement }) => void | (() => void),
  deps: DependencyList = [],
) {
  useIso(() => {
    const el = scope.current;
    if (!el) return;
    let cleanup: void | (() => void);
    const ctx = gsap.context(() => {
      cleanup = fn({ reduced: prefersReduced(), el });
    }, el);
    return () => {
      if (typeof cleanup === 'function') cleanup();
      ctx.revert();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, deps);
}
