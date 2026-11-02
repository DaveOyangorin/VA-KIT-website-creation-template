'use client';
import { useEffect, useRef } from 'react';
import { gsap, prefersReduced } from '@/lib/anim';

const KEY = 'ep-curtain';

/** A night-coloured curtain that falls when you follow an internal link and lifts on the next page. */
export default function PageCurtain() {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const el = ref.current;
    if (!el || prefersReduced()) return;
    let arriving = false;
    try { arriving = sessionStorage.getItem(KEY) === '1'; sessionStorage.removeItem(KEY); } catch {}
    if (arriving) {
      gsap.set(el, { scaleY: 1, transformOrigin: 'top' });
      gsap.to(el, { scaleY: 0, duration: 0.9, ease: 'expo.inOut', delay: 0.05 });
    }

    const onClick = (e: MouseEvent) => {
      if (e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      const a = (e.target as HTMLElement).closest('a');
      if (!a || a.target === '_blank' || a.hasAttribute('download')) return;
      const raw = a.getAttribute('href') || '';
      if (!raw || raw.startsWith('#') || /^[a-z]+:/i.test(raw) && !raw.startsWith(location.origin)) return;
      const url = new URL(a.href, location.href);
      if (url.origin !== location.origin) return;
      if (url.pathname === location.pathname && url.hash) return;
      e.preventDefault();
      try { sessionStorage.setItem(KEY, '1'); } catch {}
      gsap.set(el, { transformOrigin: 'bottom' });
      gsap.to(el, { scaleY: 1, duration: 0.55, ease: 'expo.in', onComplete: () => { location.href = url.href; } });
    };
    document.addEventListener('click', onClick);
    // Back/forward cache: never come back to a closed curtain.
    const onShow = (ev: PageTransitionEvent) => { if (ev.persisted) gsap.set(el, { scaleY: 0 }); };
    window.addEventListener('pageshow', onShow);
    return () => { document.removeEventListener('click', onClick); window.removeEventListener('pageshow', onShow); };
  }, []);

  return <div ref={ref} className="curtain" aria-hidden="true" />;
}
