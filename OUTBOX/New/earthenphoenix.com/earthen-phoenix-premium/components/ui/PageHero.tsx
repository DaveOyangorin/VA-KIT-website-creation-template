'use client';
import { useRef, type ReactNode } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import { REVEALS } from '@/lib/reveals';
import type { ServiceKey } from '@/lib/content';
import type { ImageName } from '@/lib/images';
import { href } from '@/lib/site';
import Img from './Img';

/**
 * Inner-page hero: a full-bleed photograph. On a session page it arrives with that session's own reveal
 * (lib/reveals.ts); elsewhere it opens like a slow letterbox. Scrolling pushes the photo gently away.
 */
export default function PageHero({ img, alt, pos, kicker, title, answer, spec, ctas, trail, reveal }: {
  img: ImageName; alt: string; pos?: string; kicker: string; title: string; answer: string;
  spec?: [string, string][]; ctas?: ReactNode; trail: [string, string][]; reveal?: ServiceKey;
}) {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    const frame = el.querySelector<HTMLElement>('[data-frame]')!;
    const image = frame.querySelector('img');
    const words = el.querySelectorAll<HTMLElement>('[data-w]');
    if (reduced) return;
    const tl = gsap.timeline({ delay: 0.1, paused: true });
    Promise.race([document.fonts?.ready, new Promise((r) => setTimeout(r, 1200))]).then(() => { gsap.set('[data-h1]', { visibility: 'visible' }); tl.play(); });
    tl.add(reveal ? REVEALS[reveal](frame, image) : gsap.fromTo(frame, { clipPath: 'inset(40% 0% 40% 0%)' }, { clipPath: 'inset(0% 0% 0% 0%)', duration: 1.8, ease: 'expo.inOut' }), 0)
      .fromTo(words, { yPercent: 115, y: 0 }, { yPercent: 0, y: 0, duration: 1.5, stagger: 0.08, ease: 'expo.out' }, 0.7)
      .fromTo('[data-in]', { y: 24, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 1.2, stagger: 0.08, ease: 'expo.out' }, 1);
    gsap.timeline({ scrollTrigger: { trigger: el, start: 'top top', end: 'bottom top', scrub: 0.5 } })
      .to('[data-push]', { yPercent: 14, scale: 1.06, ease: 'none' }, 0)
      .to('[data-copy]', { y: -50, autoAlpha: 0.2, ease: 'none' }, 0);
  }, [reveal]);

  return (
    <section ref={ref} className="relative min-h-[100svh] lg:min-h-[94svh] flex items-start overflow-hidden bg-night text-chalk" aria-labelledby="page-h">
      <div data-push className="absolute inset-0">
        <div data-frame className="absolute inset-0 overflow-hidden">
          <Img name={img} alt={alt} eager className="cover" pos={pos} />
        </div>
      </div>
      <div className="absolute inset-0 bg-gradient-to-t from-night/95 via-night/45 to-night/35 pointer-events-none" />
      <div data-copy className="wrap relative pt-[calc(var(--hdr)+clamp(40px,16svh,170px))] pb-[clamp(36px,6vw,80px)]">
        <ol className="flex flex-wrap gap-2 text-sm text-chalk/70" aria-label="Breadcrumb" data-in>
          {trail.map(([name, p], i) => (
            <li key={p} className="flex items-center gap-2">
              {i < trail.length - 1 ? <><a className="ulink" href={href(p)}>{name}</a><span aria-hidden>/</span></> : <span aria-current="page" className="text-chalk">{name}</span>}
            </li>
          ))}
        </ol>
        <p className="kicker text-chalk/85 mt-8" data-in>{kicker}</p>
        <h1 id="page-h" data-h1 className="display h1 mt-5 max-w-[12ch]">
          {title.split(' ').map((w, i) => (
            <span key={i}><span className="sw"><span data-w>{w}</span></span>{' '}</span>
          ))}
        </h1>
        <div className="mt-8 grid gap-8 lg:grid-cols-[minmax(0,1fr)_auto] items-end">
          <p className="lede max-w-[46ch] text-chalk/85" data-in>{answer}</p>
          {spec && (
            <dl className="flex flex-wrap gap-x-10 gap-y-4" data-in>
              {spec.map(([k, v]) => (
                <div key={k} className="border-l border-chalk/25 pl-4">
                  <dt className="text-xs uppercase tracking-[.18em] text-chalk/60">{k}</dt>
                  <dd className="mt-1 font-display text-2xl tracking-[-0.01em]">{v}</dd>
                </div>
              ))}
            </dl>
          )}
        </div>
        {ctas && <div className="mt-9 flex flex-wrap gap-3" data-in>{ctas}</div>}
      </div>
    </section>
  );
}
