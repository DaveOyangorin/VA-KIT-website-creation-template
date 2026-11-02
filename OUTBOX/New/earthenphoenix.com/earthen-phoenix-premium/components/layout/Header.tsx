'use client';
import { useEffect, useRef, useState } from 'react';
import { usePathname } from 'next/navigation';
import { AnimatePresence, motion } from 'motion/react';
import { ChevronDown, Phone } from 'lucide-react';
import { SERVICES } from '@/lib/content';
import { BOOK, PHONE, TEL, asset, href } from '@/lib/site';
import { imgSrc } from '@/lib/images';
import { Arr } from '@/components/ui/Arrow';

const LINKS = [
  { path: '/sessions', label: 'Sessions', mega: true },
  { path: '/about', label: 'About' },
  { path: '/products', label: 'Products' },
  { path: '/faq', label: 'Questions' },
  { path: '/contact', label: 'Contact' },
];

const ease = [0.16, 1, 0.3, 1] as const;

export default function Header() {
  const raw = usePathname() || '/';
  const path = raw.replace(/\.html$/, '').replace(/\/index$/, '/') || '/';
  const isService = SERVICES.some((s) => '/' + s.slug === path);
  const isCurrent = (p: string) => path === p || (p === '/sessions' && isService);

  const [scrolled, setScrolled] = useState(false);
  const [menu, setMenu] = useState(false);
  const [mega, setMega] = useState(false);
  const [peek, setPeek] = useState(0);
  const megaTimer = useRef<number | undefined>(undefined);
  const burger = useRef<HTMLButtonElement>(null);

  // Home opens on her pale mountain sky, so its header starts in ink. Other pages open on a dark photo.
  const tone = path === '/' ? 'dark' : 'light';

  // Once scrolled, the header takes the tone of whatever lies beneath it: night over dark sections and photos,
  // mist over light ones, so it never sits as a hard bar across the page.
  const [over, setOver] = useState<'light' | 'dark'>('light');
  useEffect(() => {
    let raf = 0;
    const sample = () => {
      raf = 0;
      setScrolled(window.scrollY > 40);
      const y = (document.querySelector<HTMLElement>('.hdr')?.offsetHeight || 70) + 2;
      for (const el of document.elementsFromPoint(window.innerWidth / 2, y)) {
        if (el.closest('.hdr, #mega, #menu')) continue;
        if (el.tagName === 'IMG' || el.tagName === 'CANVAS') { setOver('dark'); return; }
        const m = getComputedStyle(el).backgroundColor.match(/[\d.]+/g);
        if (!m || (m[3] !== undefined && Number(m[3]) < 0.5)) continue;
        const [r, g, b] = m.map(Number);
        setOver(0.2126 * r + 0.7152 * g + 0.0722 * b < 128 ? 'dark' : 'light');
        return;
      }
    };
    const on = () => { if (!raf) raf = requestAnimationFrame(sample); };
    sample();
    window.addEventListener('scroll', on, { passive: true });
    window.addEventListener('resize', on);
    return () => { window.removeEventListener('scroll', on); window.removeEventListener('resize', on); cancelAnimationFrame(raf); };
  }, []);

  useEffect(() => {
    const html = document.documentElement;
    if (menu) { window.__lenis?.stop(); html.style.overflow = 'hidden'; }
    else { window.__lenis?.start(); html.style.overflow = ''; }
    const onKey = (e: KeyboardEvent) => { if (e.key === 'Escape') { setMenu(false); setMega(false); burger.current?.focus(); } };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [menu]);

  const openMega = () => { window.clearTimeout(megaTimer.current); setMega(true); };
  const closeMega = () => { megaTimer.current = window.setTimeout(() => setMega(false), 160); };

  return (
    <>
      <header className="hdr" data-over={mega ? 'light' : over} data-tone={tone} data-scrolled={scrolled || mega ? 'true' : 'false'} data-menu={menu ? 'true' : 'false'}>
        <a href={href('/')} className="flex items-center gap-3 shrink-0" aria-label="Earthen Phoenix, home">
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={asset('img/ep-mark.png')} alt="" width={38} height={38} className="size-9 md:size-[38px]" />
          <span className="font-display text-[1.4rem] leading-none tracking-[-0.02em]">
            Earthen <em className="italic">Phoenix</em>
          </span>
        </a>

        <nav className="nav ml-auto hidden lg:flex items-center gap-8" aria-label="Main">
          {LINKS.map((l) =>
            l.mega ? (
              <div key={l.path} className="relative flex items-center gap-1" onMouseEnter={openMega} onMouseLeave={closeMega}>
                <a href={href(l.path)} aria-current={isCurrent(l.path) ? 'page' : undefined}>{l.label}</a>
                <button type="button" className="p-1 -mr-1" aria-expanded={mega} aria-controls="mega" aria-label="Show all sessions"
                  onClick={() => setMega((m) => !m)} onFocus={openMega}>
                  <ChevronDown size={15} strokeWidth={1.75} className={`transition-transform duration-500 ${mega ? 'rotate-180' : ''}`} aria-hidden />
                </button>
              </div>
            ) : (
              <a key={l.path} href={href(l.path)} aria-current={isCurrent(l.path) ? 'page' : undefined}>{l.label}</a>
            ),
          )}
        </nav>

        <a href={BOOK} className="btn btn-flame hidden sm:inline-flex ml-auto lg:ml-4 !min-h-[46px] !px-5">Book a session <Arr /></a>

        <button ref={burger} type="button" className="lg:hidden ml-auto sm:ml-2 flex items-center gap-3 min-h-11 pl-3 font-medium text-[.95rem]"
          aria-expanded={menu} aria-controls="menu" onClick={() => setMenu((m) => !m)}>
          <span>{menu ? 'Close' : 'Menu'}</span>
          <span className="relative block w-6 h-3" aria-hidden>
            <i className={`absolute left-0 right-0 h-px bg-current transition-transform duration-500 ${menu ? 'top-1.5 rotate-45' : 'top-0'}`} />
            <i className={`absolute left-0 right-0 h-px bg-current transition-transform duration-500 ${menu ? 'top-1.5 -rotate-45' : 'top-3'}`} />
          </span>
        </button>
      </header>

      {/* Desktop sessions panel */}
      <AnimatePresence>
        {mega && (
          <motion.div id="mega" key="mega" onMouseEnter={openMega} onMouseLeave={closeMega}
            initial={{ clipPath: 'inset(0% 0% 100% 0%)' }} animate={{ clipPath: 'inset(0% 0% 0% 0%)' }} exit={{ clipPath: 'inset(0% 0% 100% 0%)' }}
            transition={{ duration: 0.7, ease }}
            className="fixed inset-x-0 z-50 hidden lg:block bg-mist text-ink shadow-[0_30px_60px_-30px_rgba(29,33,28,.25)]" style={{ top: 'var(--hdr)' }}>
            <div className="wrap grid grid-cols-[1fr_1fr_minmax(280px,30%)] gap-10 py-10">
              {[SERVICES.slice(0, 5), SERVICES.slice(5)].map((col, ci) => (
                <ul key={ci} className="grid content-start">
                  {col.map((s, i) => {
                    const idx = ci * 5 + i;
                    return (
                      <li key={s.key}>
                        <a href={href('/' + s.slug)} onMouseEnter={() => setPeek(idx)} onFocus={() => setPeek(idx)}
                          className="group flex items-baseline justify-between gap-4 py-3 border-b border-ink/10">
                          <span className="font-display text-2xl tracking-[-0.02em] transition-transform duration-500 group-hover:translate-x-2" style={{ fontVariationSettings: "'SOFT' 100" }}>{s.name}</span>
                          <span className="text-sm text-ink-2 tabular-nums">{s.price}</span>
                        </a>
                      </li>
                    );
                  })}
                </ul>
              ))}
              <div className="relative aspect-[4/5] overflow-hidden rounded-[22px] bg-moss">
                <AnimatePresence initial={false}>
                  <motion.img key={peek} src={imgSrc(SERVICES[peek].img)} alt="" className="cover" style={{ objectPosition: SERVICES[peek].pos }}
                    initial={{ opacity: 0, scale: 1.12 }} animate={{ opacity: 1, scale: 1 }} exit={{ opacity: 0 }} transition={{ duration: 0.9, ease }} />
                </AnimatePresence>
                <div className="absolute inset-x-0 bottom-0 p-5 text-chalk bg-gradient-to-t from-night/80 to-transparent">
                  <p className="text-xs uppercase tracking-[.2em] opacity-80">{SERVICES[peek].touch}</p>
                  <p className="text-[.95rem] mt-1">{SERVICES[peek].line}</p>
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Phone and tablet menu: opens directly below the header, which stays put. */}
      <AnimatePresence>
        {menu && (
          <motion.div id="menu" key="menu" role="dialog" aria-modal="true" aria-label="Menu"
            initial={{ clipPath: 'inset(0% 0% 100% 0%)' }} animate={{ clipPath: 'inset(0% 0% 0% 0%)' }} exit={{ clipPath: 'inset(0% 0% 100% 0%)' }}
            transition={{ duration: 0.75, ease }}
            className="fixed inset-x-0 bottom-0 z-50 bg-mist text-ink overflow-y-auto overscroll-contain lg:hidden" style={{ top: 'var(--hdr)' }}>
            <div className="wrap pt-6 pb-12 grid gap-10">
              <nav aria-label="Menu">
                <ul>
                  {[{ path: '/', label: 'Home' }, ...LINKS].map((l, i) => (
                    <motion.li key={l.path} initial={{ y: 40, opacity: 0 }} animate={{ y: 0, opacity: 1 }} transition={{ delay: 0.15 + i * 0.06, duration: 0.9, ease }}
                      className="border-b border-ink/10">
                      <a href={href(l.path)} aria-current={isCurrent(l.path) ? 'page' : undefined}
                        className="flex items-center justify-between py-3.5 font-display text-[2.1rem] leading-none tracking-[-0.02em]" style={{ fontVariationSettings: "'SOFT' 100" }}>
                        {l.label}
                        {isCurrent(l.path) && <span className="size-2 rounded-full bg-flame" aria-hidden />}
                      </a>
                    </motion.li>
                  ))}
                </ul>
              </nav>
              <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.5, duration: 0.8 }}>
                <p className="kicker text-lichen">Every session</p>
                <ul className="mt-4 grid grid-cols-1 sm:grid-cols-2 gap-x-8">
                  {SERVICES.map((s) => (
                    <li key={s.key}>
                      <a href={href('/' + s.slug)} className="flex justify-between gap-4 py-2.5 border-b border-ink/10 text-[1.02rem]">
                        <span>{s.name}</span><span className="text-ink-2 text-sm tabular-nums">{s.price}</span>
                      </a>
                    </li>
                  ))}
                </ul>
              </motion.div>
              <motion.div className="grid gap-4" initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.6, duration: 0.8, ease }}>
                <a href={BOOK} className="btn btn-flame justify-center">Book a session <Arr /></a>
                <a href={TEL} className="btn btn-ghost justify-center"><Phone size={17} strokeWidth={1.75} aria-hidden /> Call or text {PHONE}</a>
                <p className="text-sm text-ink-2">First time? Mention it when you book for 20% off your first service.</p>
              </motion.div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
