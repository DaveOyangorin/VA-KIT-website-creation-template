'use client';
import { useRef } from 'react';
import { gsap, useGsap } from '@/lib/anim';

const WORDS = 'I believe in all modalities that work for you. By working with the practitioner and modalities that call to you, you innately empower your own ability to heal.';
const LIT = new Set(['call', 'to', 'you,', 'heal.']);

/** Her own words, lit one at a time as you read down the page. */
export default function Statement() {
  const ref = useRef<HTMLElement>(null);
  useGsap(ref, ({ reduced, el }) => {
    if (reduced) return;
    gsap.fromTo(el.querySelectorAll('[data-word]'), { opacity: 0.16 }, {
      opacity: 1, stagger: 0.08, ease: 'none',
      scrollTrigger: { trigger: el.querySelector('blockquote'), start: 'top 78%', end: 'bottom 45%', scrub: true },
    });
  });
  const words = WORDS.split(' ');
  return (
    <section ref={ref} className="sec bg-mist" aria-label="In Miquelle’s words">
      <div className="wrap grid gap-12 lg:grid-cols-[minmax(180px,1fr)_4fr]">
        <div className="flex lg:flex-col gap-6 lg:gap-3 text-sm text-ink-2" data-reveal>
          <p className="kicker text-ink">In her words</p>
          <p>Miquelle,<br />founder of Earthen Phoenix</p>
        </div>
        <blockquote>
          <p className="font-display font-light text-[clamp(2rem,4.4vw,4.3rem)] leading-[1.06] tracking-[-0.025em]" style={{ fontVariationSettings: "'SOFT' 100, 'opsz' 120" }}>
            {words.map((w, i) => (
              <span key={i}>
                <span data-word className={LIT.has(w) && i > 10 ? 'italic text-clay' : undefined}>{w}</span>{i < words.length - 1 ? ' ' : ''}
              </span>
            ))}
          </p>
          <footer className="mt-12 grid sm:grid-cols-3 gap-6 border-t border-ink/15 pt-6 text-[.95rem]" data-reveal>
            <p><span className="block font-display text-3xl">2011</span><span className="text-ink-2">Started with Reiki</span></p>
            <p><span className="block font-display text-3xl">2012</span><span className="text-ink-2">Utah College of Massage Therapy</span></p>
            <p><span className="block font-display text-3xl">Master</span><span className="text-ink-2">Reiki practitioner</span></p>
          </footer>
        </blockquote>
      </div>
    </section>
  );
}
