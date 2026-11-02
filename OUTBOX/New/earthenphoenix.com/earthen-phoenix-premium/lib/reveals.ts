'use client';
/**
 * One photographic reveal per session. Each acts on a clipped frame and the photo inside it,
 * and each one moves the way that session meets the body:
 *
 *  reiki    a soft circle of light widens from the centre and the photo comes into focus (hands near, nothing pressed)
 *  swedish  one long diagonal stroke crosses the frame, carrying a sheen of oil
 *  lymph    the frame clears from every edge toward one point at the collarbone (drainage paths)
 *  deep     a small window opens while the photo pushes slowly in (beneath the surface)
 *  thai     vertical bands press up on a beat, feet to hips, then the photo is drawn long
 *  sarga    the photo climbs in six weighted steps, settling after each one
 *  zen      a letterbox opens like a view widening, and the scene slows from a drift
 *  yoga     an organic shape flows and then settles into stillness
 *  astro    a card turns over
 *  herbs    colour fills from below behind a moving liquid surface
 */
import { gsap } from './anim';
import type { ServiceKey } from './content';

type Reveal = (frame: HTMLElement, img: HTMLElement | null) => gsap.core.Timeline;

const pct = (n: number) => `${(n * 100).toFixed(2)}%`;

export function combPolygon(tops: number[]) {
  const n = tops.length;
  const pts: string[] = [];
  tops.forEach((t, i) => {
    const x0 = pct(i / n), x1 = pct((i + 1) / n), y = pct(t);
    pts.push(`${x0} 100%`, `${x0} ${y}`, `${x1} ${y}`, `${x1} 100%`);
  });
  return `polygon(${pts.join(',')})`;
}

export function wavePolygon(level: number, amp: number, phase: number, waves = 1.6) {
  const pts: string[] = [];
  const steps = 28;
  for (let i = 0; i <= steps; i++) {
    const x = i / steps;
    const y = level + Math.sin(x * Math.PI * 2 * waves + phase) * amp;
    pts.push(`${pct(x)} ${pct(y)}`);
  }
  pts.push('100% 100%', '0% 100%');
  return `polygon(${pts.join(',')})`;
}

/** Everything visible except a rectangular hole that shrinks onto (cx, cy). k = 1 hides all, k = 0 shows all. */
export function holePolygon(k: number, cx: number, cy: number) {
  const l = cx - k * (cx + 0.02), r = cx + k * (1 - cx + 0.02);
  const t = cy - k * (cy + 0.02), b = cy + k * (1 - cy + 0.02);
  return `polygon(evenodd, 0% 0%, 100% 0%, 100% 100%, 0% 100%, 0% 0%, ${pct(l)} ${pct(t)}, ${pct(l)} ${pct(b)}, ${pct(r)} ${pct(b)}, ${pct(r)} ${pct(t)}, ${pct(l)} ${pct(t)})`;
}

const done = (frame: HTMLElement) => () => { frame.style.clipPath = 'inset(0% 0% 0% 0%)'; };

export const REVEALS: Record<ServiceKey, Reveal> = {
  reiki(frame, img) {
    const tl = gsap.timeline({ onComplete: done(frame) });
    tl.fromTo(frame, { clipPath: 'circle(0% at 50% 48%)' }, { clipPath: 'circle(78% at 50% 48%)', duration: 2, ease: 'expo.inOut' });
    if (img) tl.fromTo(img, { filter: 'blur(14px) brightness(1.35)', scale: 1.06 }, { filter: 'blur(0px) brightness(1)', scale: 1, duration: 2.4, ease: 'power2.out', clearProps: 'filter' }, 0);
    return tl;
  },

  swedish(frame, img) {
    const p = { v: 0 };
    const sheen = document.createElement('i');
    sheen.setAttribute('aria-hidden', 'true');
    Object.assign(sheen.style, {
      position: 'absolute', inset: '-10% auto -10% 0', width: '22%', pointerEvents: 'none', zIndex: '2',
      background: 'linear-gradient(100deg, transparent, rgba(255,214,160,.38), transparent)', mixBlendMode: 'screen', transform: 'skewX(-14deg)',
    });
    frame.appendChild(sheen);
    const set = () => {
      const x = p.v * 1.35;
      frame.style.clipPath = `polygon(0% 0%, ${pct(x)} 0%, ${pct(x - 0.35)} 100%, 0% 100%)`;
      sheen.style.left = pct(x - 0.3);
    };
    const tl = gsap.timeline({ onComplete: () => { sheen.remove(); done(frame)(); } });
    tl.to(p, { v: 1, duration: 1.9, ease: 'power3.inOut', onUpdate: set, onStart: set });
    if (img) tl.fromTo(img, { scale: 1.08, xPercent: -2 }, { scale: 1, xPercent: 0, duration: 2.4, ease: 'power2.out' }, 0);
    return tl;
  },

  lymph(frame, img) {
    const p = { k: 1 };
    const cx = 0.6, cy = 0.5; // the collarbone, in her photograph
    const set = () => { frame.style.clipPath = holePolygon(p.k, cx, cy); };
    const tl = gsap.timeline({ onComplete: done(frame) });
    tl.to(p, { k: 0, duration: 2, ease: 'expo.inOut', onUpdate: set, onStart: set });
    if (img) tl.fromTo(img, { scale: 1.12, transformOrigin: '60% 50%' }, { scale: 1, duration: 2.4, ease: 'power3.out' }, 0);
    return tl;
  },

  deep(frame, img) {
    const tl = gsap.timeline({ onComplete: done(frame) });
    tl.fromTo(frame, { clipPath: 'inset(30% 32% 30% 32%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 2, ease: 'expo.inOut' });
    if (img) tl.fromTo(img, { scale: 1 }, { scale: 1.14, duration: 3.2, ease: 'power2.inOut' }, 0);
    return tl;
  },

  thai(frame, img) {
    const n = 8;
    const tops = Array.from({ length: n }, () => 1);
    const set = () => { frame.style.clipPath = combPolygon(tops); };
    set();
    const tl = gsap.timeline({ onComplete: done(frame), onUpdate: set });
    const beat = 0.16;
    for (let i = 0; i < n; i++) {
      const o = { v: 1 };
      tl.to(o, { v: 0.35, duration: beat, ease: 'power3.out', onUpdate: () => { tops[i] = o.v; } }, i * beat)
        .to(o, { v: 0, duration: beat * 2.2, ease: 'power2.inOut', onUpdate: () => { tops[i] = o.v; } }, i * beat + beat);
    }
    if (img) tl.fromTo(img, { scaleX: 1.09, scaleY: 1.02 }, { scaleX: 1, scaleY: 1, duration: 1.4, ease: 'expo.out' }, n * beat);
    return tl;
  },

  sarga(frame, img) {
    const steps = 6;
    const tl = gsap.timeline({ onComplete: done(frame) });
    gsap.set(frame, { clipPath: 'inset(100% 0% 0% 0%)' });
    for (let i = 1; i <= steps; i++) {
      tl.to(frame, { clipPath: `inset(${pct(1 - i / steps)} 0% 0% 0%)`, duration: 0.3, ease: 'power4.in' });
      if (img) tl.fromTo(img, { y: 0 }, { y: 8, duration: 0.09, ease: 'power2.out', yoyo: true, repeat: 1 }, '>-0.02');
      tl.to({}, { duration: 0.06 });
    }
    return tl;
  },

  zen(frame, img) {
    const tl = gsap.timeline({ onComplete: done(frame) });
    tl.fromTo(frame, { clipPath: 'inset(47% 0% 47% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 2.4, ease: 'expo.inOut' });
    if (img) tl.fromTo(img, { scale: 1.28, xPercent: -3 }, { scale: 1, xPercent: 0, duration: 3.4, ease: 'expo.out' }, 0);
    return tl;
  },

  yoga(frame, img) {
    const tl = gsap.timeline({ onComplete: done(frame) });
    tl.fromTo(frame, { clipPath: 'inset(32% 36% 32% 36% round 50% 50% 50% 50%)' },
      { clipPath: 'inset(14% 20% 10% 18% round 46% 54% 38% 62%)', duration: 0.9, ease: 'sine.inOut' })
      .to(frame, { clipPath: 'inset(6% 8% 12% 10% round 60% 40% 56% 44%)', duration: 0.8, ease: 'sine.inOut' })
      .to(frame, { clipPath: 'inset(0% 0% 0% 0% round 0% 0% 0% 0%)', duration: 1.2, ease: 'expo.out' });
    if (img) tl.fromTo(img, { scale: 1.1 }, { scale: 1, duration: 2.9, ease: 'sine.out' }, 0);
    return tl;
  },

  astro(frame, img) {
    const tl = gsap.timeline({ onComplete: () => { done(frame)(); gsap.set(frame, { clearProps: 'transform' }); } });
    tl.fromTo(frame, { rotateY: -88, transformPerspective: 1400, clipPath: 'inset(8% 30% 8% 30% round 18px)' },
      { rotateY: 0, duration: 1.1, ease: 'power3.out' })
      .to(frame, { clipPath: 'inset(0% 0% 0% 0% round 0px)', duration: 1.3, ease: 'expo.inOut' }, '-=0.2');
    if (img) tl.fromTo(img, { scale: 1.18 }, { scale: 1, duration: 2.2, ease: 'expo.out' }, 0.4);
    return tl;
  },

  herbs(frame, img) {
    const p = { level: 1.08, phase: 0 };
    const set = () => { frame.style.clipPath = wavePolygon(p.level, 0.035 * Math.min(1, p.level + 0.2), p.phase); };
    const tl = gsap.timeline({ onComplete: done(frame) });
    tl.to(p, { level: -0.08, phase: Math.PI * 4, duration: 2.4, ease: 'power2.inOut', onUpdate: set, onStart: set });
    if (img) tl.fromTo(img, { filter: 'saturate(0.2) brightness(1.2)' }, { filter: 'saturate(1) brightness(1)', duration: 2.6, ease: 'power2.out', clearProps: 'filter' }, 0);
    return tl;
  },
};
