'use client';
import { useEffect } from 'react';
import { gsap, ScrollTrigger, prefersReduced } from '@/lib/anim';

/**
 * Page-wide scroll motion, declared with data attributes so server components stay static:
 *  data-split            heading words rise out of their line masks
 *  data-reveal           copy settles up into place (data-delay="1" staggers)
 *  data-mask="up|left|centre"   a photo is uncovered by a clip, while the photo inside eases back from a zoom
 *  data-parallax="0.12"  the element drifts against the scroll (inside a clipped frame)
 * The hidden starting states live in CSS under html.anim, so nothing flashes before hydration.
 */
export default function Animator() {
  useEffect(() => {
    const root = document.documentElement;
    if (prefersReduced()) { root.classList.remove('anim'); return; }

    const ctx = gsap.context(() => {
      gsap.utils.toArray<HTMLElement>('[data-split]').forEach((el) => {
        const words = el.querySelectorAll<HTMLElement>('.sw > span');
        gsap.fromTo(words, { yPercent: 110, y: 0 }, {
          yPercent: 0, y: 0, duration: 1.3, stagger: 0.07, ease: 'expo.out', delay: Number(el.dataset.delay || 0) * 0.12,
          scrollTrigger: { trigger: el, start: 'top 88%', once: true },
        });
      });

      gsap.utils.toArray<HTMLElement>('[data-reveal]').forEach((el) => {
        gsap.fromTo(el, { y: 28, autoAlpha: 0 }, {
          y: 0, autoAlpha: 1, duration: 1.2, ease: 'expo.out', delay: Number(el.dataset.delay || 0) * 0.12,
          scrollTrigger: { trigger: el, start: 'top 90%', once: true },
        });
      });

      const FROM: Record<string, string> = {
        up: 'inset(100% 0% 0% 0%)',
        left: 'inset(0% 100% 0% 0%)',
        centre: 'inset(48% 48% 48% 48%)',
      };
      gsap.utils.toArray<HTMLElement>('[data-mask]').forEach((el) => {
        const from = FROM[el.dataset.mask || 'up'] || FROM.up;
        const inner = el.querySelector('img');
        const tl = gsap.timeline({ scrollTrigger: { trigger: el, start: 'top 85%', once: true } });
        tl.fromTo(el, { clipPath: from }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.6, ease: 'expo.inOut' });
        if (inner) tl.fromTo(inner, { scale: 1.3 }, { scale: 1, duration: 2.2, ease: 'expo.out' }, 0.1);
      });

      gsap.utils.toArray<HTMLElement>('[data-parallax]').forEach((el) => {
        const amt = Number(el.dataset.parallax || 0.12) * 100;
        gsap.fromTo(el, { yPercent: -amt / 2 }, {
          yPercent: amt / 2, ease: 'none',
          scrollTrigger: { trigger: el.parentElement || el, start: 'top bottom', end: 'bottom top', scrub: true },
        });
      });
    });

    // Late layout shifts (fonts, images) move trigger points: refresh once everything is in.
    const refresh = () => ScrollTrigger.refresh();
    window.addEventListener('load', refresh);
    document.fonts?.ready.then(refresh);
    return () => { window.removeEventListener('load', refresh); ctx.revert(); };
  }, []);
  return null;
}
