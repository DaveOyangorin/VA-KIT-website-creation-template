'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import Img from '@/components/ui/Img';
import { BOOK, href } from '@/lib/site';
import { Arr } from '@/components/ui/Arrow';

/**
 * Scene 1. Her name on linen, with her mountain meadow in a small window between the two words.
 * Scrolling pushes the words apart and opens the window until the meadow fills the screen,
 * then "Ground your soul." settles over it.
 */
export default function Opening() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    const q = gsap.utils.selector(el);
    if (reduced) { gsap.set(q('[data-window]'), { clipPath: 'inset(0% 0% 0% 0% round 0px)' }); gsap.set(q('[data-words]'), { autoAlpha: 0 }); return; }
    const mobile = window.matchMedia('(max-width: 767px)').matches;
    // The window rests between the two words: a tall pill between them on wide screens, a small one between the stacked words on phones.
    const REST = mobile ? 'inset(41% 28% 41% 28% round 999px)' : 'inset(30% 43.5% 30% 43.5% round 999px)';
    const intro = gsap.timeline({ paused: true });
    intro.fromTo(q('[data-window]'), { clipPath: 'inset(50% 50% 50% 50% round 999px)' }, { clipPath: REST, duration: 1.8, ease: 'expo.out' }, 0.1)
      .fromTo(q('[data-letter]'), { yPercent: 110, y: 0 }, { yPercent: 0, y: 0, duration: 1.6, stagger: 0.035, ease: 'expo.out' }, 0.2)
      .fromTo(q('[data-in]'), { y: 20, autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 1.2, stagger: 0.1, ease: 'expo.out' }, 0.9)
      .fromTo(q('[data-sun]'), { y: '40vh', autoAlpha: 0 }, { y: 0, autoAlpha: 1, duration: 3, ease: 'expo.out' }, 0);
    Promise.race([document.fonts?.ready, new Promise((r) => setTimeout(r, 1200))]).then(() => intro.play());

    gsap.timeline({ scrollTrigger: { trigger: el, start: 'top top', end: 'bottom bottom', scrub: 0.8 } })
      .to(q('[data-left]'), mobile ? { yPercent: -160, autoAlpha: 0, ease: 'none' } : { xPercent: -120, autoAlpha: 0, ease: 'none' }, 0)
      .to(q('[data-right]'), mobile ? { yPercent: 160, autoAlpha: 0, ease: 'none' } : { xPercent: 120, autoAlpha: 0, ease: 'none' }, 0)
      .to(q('[data-in]'), { autoAlpha: 0, duration: 0.15 }, 0)
      .fromTo(q('[data-window]'), { clipPath: REST }, { clipPath: 'inset(0% 0% 0% 0% round 0px)', ease: 'power2.inOut', immediateRender: false }, 0)
      .fromTo(q('[data-window] img'), { scale: 1.35 }, { scale: 1, ease: 'power1.out' }, 0)
      .to(q('[data-sun]'), { y: '-30vh', autoAlpha: 0, ease: 'power1.in', duration: 0.45 }, 0)
      .fromTo(q('[data-veil]'), { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.3 }, 0.55)
      .fromTo(q('[data-ground] [data-gw]'), { yPercent: 110, y: 0 }, { yPercent: 0, y: 0, stagger: 0.04, duration: 0.3, ease: 'power3.out' }, 0.62)
      .fromTo(q('[data-ground-cta]'), { autoAlpha: 0, y: 30 }, { autoAlpha: 1, y: 0, duration: 0.25 }, 0.8);
  });

  const word = (w: string) => w.split('').map((c, i) => <span key={i} className="inline-block overflow-clip pb-[0.06em] -mb-[0.06em]"><span data-letter className="inline-block">{c}</span></span>);

  return (
    <section ref={ref} className="relative h-[300svh] motion-reduce:h-auto bg-mist" aria-labelledby="open-h">
      <div className="sticky top-0 h-[100svh] overflow-hidden">
        {/* Her logo's sun: five bands, rising behind the window like the phoenix */}
        <div data-sun aria-hidden className="absolute left-1/2 -translate-x-1/2 top-[76%] md:top-[64%] size-[min(120vw,900px)] md:size-[min(70vw,1000px)] rounded-full overflow-hidden"
          style={{ background: 'linear-gradient(180deg, var(--color-saffron) 0 20%, var(--color-tangerine) 20% 40%, var(--color-poppy) 40% 60%, var(--color-cacao) 60% 80%, var(--color-forest) 80% 100%)' }} />
        <div data-window className="absolute inset-0 overflow-hidden" style={{ clipPath: 'inset(30% 43.5% 30% 43.5% round 999px)' }}>
          <Img name="mountain-meadow" alt="Miquelle and a student greeting each other in a mountain meadow below the Wasatch peaks" eager className="cover" pos="62% 45%" />
          <div data-veil className="absolute inset-0 bg-gradient-to-t from-night/70 via-night/10 to-transparent opacity-0" />
        </div>

        <h1 id="open-h" data-words className="absolute inset-0 grid place-items-center pointer-events-none">
          <span className="sr-only">Earthen Phoenix: massage, bodywork, Reiki and yoga in Salt Lake City. Ground your soul.</span>
          <span aria-hidden className="w-full flex flex-col md:flex-row items-center justify-between md:px-[var(--gutter)] gap-[24svh] md:gap-0 font-display text-ink leading-none tracking-[-0.04em] text-[clamp(4.2rem,21vw,7rem)] md:text-[clamp(5rem,11vw,13rem)]">
            <span data-left className="block text-cacao">{word('Earthen')}</span>
            <span data-right className="block italic text-poppy">{word('Phoenix')}</span>
          </span>
        </h1>

        <p data-in className="absolute left-1/2 -translate-x-1/2 top-[calc(var(--hdr)+5svh)] kicker !gap-0 before:!hidden text-ink-2 whitespace-nowrap">Ground your soul</p>
        <p data-in className="absolute left-1/2 -translate-x-1/2 bottom-[5svh] z-[1] text-center text-sm text-ink font-medium w-[min(90vw,520px)]">
          Massage, bodywork, Reiki, yoga, readings and herbal remedies with Miquelle in Salt Lake City, Utah.
          <span className="mt-5 flex justify-center items-center gap-3 text-xs uppercase tracking-[.22em]"><span className="block w-px h-8 bg-ink/30 overflow-hidden relative"><span className="absolute inset-x-0 top-0 h-1/2 bg-ink animate-[drop_2.4s_ease-in-out_infinite]" /></span>Scroll</span>
        </p>

        <div data-ground className="absolute inset-x-0 bottom-0 wrap pb-[clamp(36px,7svh,80px)] text-chalk pointer-events-none">
          <p className="font-display leading-[0.92] tracking-[-0.035em] text-[clamp(3.4rem,10vw,10rem)]" aria-hidden>
            <span className="inline-block overflow-clip"><span data-gw className="inline-block">Ground</span></span>{' '}
            <span className="inline-block overflow-clip"><span data-gw className="inline-block italic">your soul.</span></span>
          </p>
          <div data-ground-cta className="mt-8 flex flex-wrap items-center gap-3 pointer-events-auto opacity-0">
            <a href={BOOK} className="btn btn-flame">Book a session <Arr /></a>
            <a href={href('/sessions')} className="btn btn-ghost">Every session</a>
            <span className="text-sm text-chalk/85 ml-2">First visit: 20% off</span>
          </div>
        </div>
      </div>
    </section>
  );
}
