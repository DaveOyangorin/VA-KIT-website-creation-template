'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';
import Img from '@/components/ui/Img';
import { href } from '@/lib/site';
import { Arr } from '@/components/ui/Arrow';

const WORDS = 'I believe in all modalities that work for you. By working with the practitioner and modalities that call to you, you innately empower your own ability to heal.'.split(' ');

/** Scene 4. Miquelle. Her portrait rises and grows beside a wide photo of her table while her own words light up. */
export default function Miquelle() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    if (reduced) return;
    const q = gsap.utils.selector(el);
    gsap.timeline({ scrollTrigger: { trigger: el, start: 'top top', end: 'bottom bottom', scrub: 0.7 } })
      .fromTo(q('[data-portrait]'), { clipPath: 'inset(38% 20% 38% 20% round 24px)' }, { clipPath: 'inset(0% 0% 0% 0% round 24px)', ease: 'power2.out', duration: 0.45 }, 0)
      .fromTo(q('[data-portrait] img'), { scale: 1.4 }, { scale: 1, ease: 'power2.out', duration: 0.6 }, 0)
      .fromTo(q('[data-wide]'), { yPercent: 30, autoAlpha: 0 }, { yPercent: -10, autoAlpha: 1, ease: 'none', duration: 1 }, 0)
      .fromTo(q('[data-word]'), { opacity: 0.14 }, { opacity: 1, stagger: 0.02, ease: 'none', duration: 0.1 }, 0.1)
      .fromTo(q('[data-facts] > *'), { y: 30, autoAlpha: 0 }, { y: 0, autoAlpha: 1, stagger: 0.05, duration: 0.15 }, 0.75);
  });
  return (
    <section ref={ref} className="relative h-[260svh] motion-reduce:h-auto bg-forest text-chalk" aria-labelledby="miq-h">
      <div className="sticky top-0 h-[100svh] overflow-hidden wrap grid md:grid-cols-[minmax(0,5fr)_minmax(0,6fr)] gap-6 md:gap-[clamp(32px,5vw,90px)] items-center pt-[calc(var(--hdr)+8px)] pb-6">
        <div className="relative h-[42svh] md:h-[78svh]">
          <div data-wide className="absolute right-0 top-[4%] w-[62%] h-[46%] overflow-hidden rounded-[22px] bg-moss">
            <Img name="sound-tuning-forks" alt="Tuning forks beside a client on the massage table" className="cover" pos="45% 50%" sizes="30vw" />
          </div>
          <div data-portrait className="absolute left-0 bottom-0 h-full aspect-[9/16] max-w-[62%] overflow-hidden rounded-[24px] bg-moss shadow-[0_40px_80px_-40px_rgba(29,33,28,.5)]">
            <Img name="miquelle-portrait" alt="Miquelle, founder of Earthen Phoenix, smiling at sunset on the water" className="cover" sizes="360px" />
          </div>
        </div>
        <div>
          <p className="kicker text-saffron">Meet Miquelle</p>
          <h2 id="miq-h" className="sr-only">Meet Miquelle</h2>
          <blockquote className="mt-5 font-display text-[clamp(1.7rem,3.3vw,3.4rem)] leading-[1.08] tracking-[-0.02em]">
            {WORDS.map((w, i) => <span key={i}><span data-word className={i > 16 && i < 21 ? 'italic text-saffron' : undefined}>{w}</span>{' '}</span>)}
          </blockquote>
          <div data-facts className="mt-6 md:mt-10 grid grid-cols-3 gap-4 border-t border-chalk/20 pt-5 text-sm">
            <p><span className="block font-display text-2xl md:text-3xl">2011</span><span className="text-chalk/75">Started with Reiki</span></p>
            <p><span className="block font-display text-2xl md:text-3xl">2012</span><span className="text-chalk/75">Utah College of Massage Therapy</span></p>
            <p><span className="block font-display text-2xl md:text-3xl">Master</span><span className="text-chalk/75">Reiki practitioner</span></p>
            <a href={href('/about')} className="col-span-3 btn btn-flame justify-self-start mt-2">Her story <Arr /></a>
          </div>
        </div>
      </div>
    </section>
  );
}
