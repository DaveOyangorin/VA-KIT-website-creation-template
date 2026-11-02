'use client';
import { useEffect, useRef, useState, type ReactNode } from 'react';
import { Pause, Play } from 'lucide-react';
import { gsap } from '@/lib/anim';
import type { ServiceKey } from '@/lib/content';

/**
 * Animated illustrations of what happens in each session. They loop on their own (no scrolling needed),
 * pause when off screen, and have a pause button (WCAG 2.2.2). Lines use currentColor; --acc is the accent fill.
 * They are small, contained loops with no parallax or flashing, so they keep playing under reduced motion.
 */

type Build = (svg: SVGSVGElement, tl: gsap.core.Timeline) => void;
const sel = (svg: SVGSVGElement, s: string) => svg.querySelectorAll<SVGElement>(s);
const one = (svg: SVGSVGElement, s: string) => svg.querySelector<SVGElement>(s)!;
/** Rounded so server and browser render identical coordinates. */
const r2 = (n: number) => Math.round(n * 100) / 100;

/* ---------- shared drawing: a client lying face down on the table ---------- */
const BODY = 'M96 160 C120 148 170 146 210 150 C250 154 300 156 336 166 C342 170 342 182 336 186 C300 192 250 192 210 190 C170 190 120 190 96 186 C88 180 88 166 96 160 Z';
function Table({ towel = true }: { towel?: boolean }) {
  return (
    <g>
      <line x1="40" y1="198" x2="362" y2="198" strokeWidth="3" />
      <line x1="76" y1="198" x2="70" y2="246" /><line x1="326" y1="198" x2="332" y2="246" />
      <g data-body>
        <path d={BODY} fill="color-mix(in oklab, currentColor 10%, transparent)" />
        <circle cx="74" cy="172" r="16" fill="color-mix(in oklab, currentColor 10%, transparent)" />
        {towel && <path d="M262 156 C290 158 318 160 338 168 C344 172 344 182 338 188 C318 192 290 192 262 191 Z" fill="var(--acc)" opacity=".55" />}
      </g>
    </g>
  );
}
const Hand = ({ id, x = 0, y = 0, flip = false }: { id: string; x?: number; y?: number; flip?: boolean }) => (
  <g data-hand={id} transform={`translate(${x} ${y})`}>
    <g transform={flip ? 'scale(-1 1)' : undefined}>
      <path d="M-16 0 C-16 -9 16 -9 18 -2 C19 3 14 6 8 6 L-12 6 C-15 6 -16 3 -16 0 Z" fill="var(--acc)" />
      <path d="M-14 -3 L-30 -10" strokeWidth="5" strokeLinecap="round" />
    </g>
  </g>
);

/* ---------- the ten scenes ---------- */
const SCENES: Record<ServiceKey, { label: string; draw: ReactNode; build: Build }> = {
  reiki: {
    label: 'Two hands hover just above the client and move from head to heart to belly; soft rings of energy spread down into the body without touching it.',
    draw: (<>
      <Table />
      {[0, 1, 2].map((i) => <ellipse key={i} data-ring cx="110" cy="150" rx="22" ry="6" fill="none" strokeWidth="1.5" />)}
      {[0, 1, 2, 3, 4, 5].map((i) => <circle key={i} data-spark cx={110 + i * 8} cy="150" r="2.2" fill="var(--acc)" stroke="none" />)}
      <g data-pair transform="translate(110 108)"><Hand id="a" x={-18} /><Hand id="b" x={18} flip /></g>
    </>),
    build: (svg, tl) => {
      const pair = one(svg, '[data-pair]'), rings = sel(svg, '[data-ring]'), sparks = sel(svg, '[data-spark]');
      [110, 200, 280].forEach((x, k) => {
        const at = k * 3;
        tl.to(pair, { attr: { transform: `translate(${x} 108)` }, duration: 1, ease: 'sine.inOut' }, at)
          .to(pair, { y: -6, duration: 1, yoyo: true, repeat: 1, ease: 'sine.inOut' }, at + 1)
          .fromTo(rings, { attr: { cx: x, rx: 8, ry: 2 }, opacity: 0.9 }, { attr: { rx: 46, ry: 12 }, opacity: 0, duration: 1.6, stagger: 0.4, ease: 'sine.out' }, at + 0.9)
          .fromTo(sparks, { attr: { cx: (i: number) => x - 20 + i * 8, cy: 152 }, opacity: 0 }, { attr: { cy: 112 }, opacity: 1, duration: 1.2, stagger: 0.12, ease: 'sine.out', yoyo: true, repeat: 1 }, at + 1);
      });
      tl.to(one(svg, '[data-body] path'), { opacity: 0.6, duration: 4.5, yoyo: true, repeat: 1, ease: 'sine.inOut' }, 0);
    },
  },

  swedish: {
    label: 'Oil drips onto the back, then one hand glides the whole length of the back in a long stroke, leaving a warm trail, and lifts to begin again.',
    draw: (<>
      <Table />
      <path data-trail d="M100 154 C150 146 200 148 240 152 C280 156 310 158 332 166" fill="none" stroke="var(--acc)" strokeWidth="6" strokeLinecap="round" pathLength={1} strokeDasharray="1" strokeDashoffset="1" opacity=".9" />
      <g data-bottle transform="translate(150 46) rotate(-30)">
        <rect x="-7" y="-20" width="14" height="24" rx="4" fill="var(--acc)" /><rect x="-3" y="-27" width="6" height="7" rx="2" />
      </g>
      {[0, 1, 2].map((i) => <path key={i} data-drop d="M0 -5 C3 0 4 3 0 5 C-4 3 -3 0 0 -5 Z" fill="var(--acc)" stroke="none" transform="translate(160 60)" opacity="0" />)}
      <Hand id="s" x={100} y={146} />
    </>),
    build: (svg, tl) => {
      const hand = one(svg, '[data-hand="s"]'), trail = one(svg, '[data-trail]');
      sel(svg, '[data-drop]').forEach((d, i) => {
        tl.fromTo(d, { attr: { transform: `translate(${160 + i * 22} 62)` }, opacity: 1 }, { attr: { transform: `translate(${160 + i * 22} 150)` }, duration: 0.6, ease: 'power2.in' }, i * 0.25)
          .to(d, { opacity: 0, duration: 0.15 }, i * 0.25 + 0.6);
      });
      tl.set(trail, { attr: { 'stroke-dashoffset': 1 }, opacity: 0.9 }, 0)
        .fromTo(hand, { attr: { transform: 'translate(100 146)' } }, { attr: { transform: 'translate(330 160)' }, duration: 2.6, ease: 'sine.inOut' }, 1.2)
        .to(trail, { attr: { 'stroke-dashoffset': 0 }, duration: 2.6, ease: 'sine.inOut' }, 1.2)
        .to(hand, { attr: { transform: 'translate(215 110)' }, duration: 0.8, ease: 'sine.inOut' }, 3.9)
        .to(hand, { attr: { transform: 'translate(100 146)' }, duration: 0.8, ease: 'sine.inOut' }, 4.7)
        .to(trail, { opacity: 0, duration: 1.2 }, 4.2);
    },
  },

  lymph: {
    label: 'Light, dotted drainage paths run along the body, and small drops of fluid flow along them to the node at the collarbone, which gently pulses.',
    draw: (<>
      <Table />
      {['M330 172 C280 168 200 166 104 167', 'M300 183 C250 185 180 183 106 174', 'M300 158 C250 153 180 151 106 160'].map((d) => (
        <path key={d} data-path d={d} fill="none" strokeWidth="1.6" strokeDasharray="2 6" />
      ))}
      {Array.from({ length: 9 }, (_, i) => <circle key={i} data-flow r="3.2" fill="var(--acc)" stroke="none" cx="-10" cy="-10" />)}
      <circle data-node cx="100" cy="167" r="7" fill="var(--acc)" />
    </>),
    build: (svg, tl) => {
      const paths = [...sel(svg, '[data-path]')] as SVGPathElement[];
      tl.to(paths, { attr: { 'stroke-dashoffset': 32 }, duration: 3, ease: 'none' }, 0);
      sel(svg, '[data-flow]').forEach((dot, i) => {
        const p = paths[i % 3], L = p.getTotalLength(), o = { t: 0 };
        tl.fromTo(o, { t: 0 }, { t: 1, duration: 3, ease: 'sine.in', onUpdate: () => {
          const pt = p.getPointAtLength(o.t * L); dot.setAttribute('cx', String(pt.x)); dot.setAttribute('cy', String(pt.y));
          dot.setAttribute('opacity', String(o.t < 0.9 ? 1 : (1 - o.t) * 10));
        } }, (i % 3) * 0.4 + Math.floor(i / 3) * 1);
      });
      tl.fromTo(one(svg, '[data-node]'), { attr: { r: 6 } }, { attr: { r: 10 }, duration: 0.5, yoyo: true, repeat: 5, ease: 'sine.inOut' }, 0.8);
    },
  },

  deep: {
    label: 'A forearm sinks slowly into one knot as the client breathes out, pressure rings spread deep into the muscle, then it lifts and moves to the next knot.',
    draw: (<>
      <Table />
      {[0, 1].map((i) => <ellipse key={i} data-ring cx="150" cy="156" rx="6" ry="2" fill="none" strokeWidth="1.6" />)}
      <ellipse data-dent cx="150" cy="153" rx="14" ry="0" fill="currentColor" opacity=".25" stroke="none" />
      <g data-arm transform="translate(150 100)"><line x1="0" y1="0" x2="60" y2="-60" strokeWidth="18" strokeLinecap="round" stroke="var(--acc)" /><circle cx="0" cy="0" r="9" fill="var(--acc)" stroke="none" /></g>
      <text data-breath x="200" y="40" textAnchor="middle" fontSize="15" fill="currentColor" stroke="none" style={{ fontStyle: 'italic' }}>breathe out</text>
    </>),
    build: (svg, tl) => {
      const arm = one(svg, '[data-arm]'), rings = sel(svg, '[data-ring]'), dent = one(svg, '[data-dent]'), word = one(svg, '[data-breath]');
      [150, 210, 270].forEach((x, k) => {
        const at = k * 3.2;
        tl.set([dent], { attr: { cx: x } }, at)
          .to(arm, { attr: { transform: `translate(${x} 100)` }, duration: 0.7, ease: 'sine.inOut' }, at)
          .call(() => { word.textContent = 'breathe in'; }, [], at)
          .call(() => { word.textContent = 'breathe out'; }, [], at + 0.8)
          .to(arm, { attr: { transform: `translate(${x} 150)` }, duration: 1.4, ease: 'power2.inOut' }, at + 0.8)
          .to(dent, { attr: { ry: 5 }, duration: 1.4, ease: 'power2.inOut' }, at + 0.8)
          .fromTo(rings, { attr: { cx: x, rx: 6, ry: 2 }, opacity: 1 }, { attr: { rx: 40, ry: 12 }, opacity: 0, duration: 1.2, stagger: 0.35 }, at + 1.6)
          .to(arm, { attr: { transform: `translate(${x} 100)` }, duration: 0.8, ease: 'sine.inOut' }, at + 2.4)
          .to(dent, { attr: { ry: 0 }, duration: 0.8 }, at + 2.4);
      });
    },
  },

  thai: {
    label: 'Two palms press on a steady beat, alternating, along the legs; then the whole body is drawn out in a long stretch and released.',
    draw: (<>
      <Table towel={false} />
      <g data-palms>
        <Hand id="l" x={230} y={146} /><Hand id="r" x={262} y={150} flip />
      </g>
      <path data-arrow d="M120 120 L320 120 M308 112 L320 120 L308 128 M132 112 L120 120 L132 128" fill="none" strokeWidth="2" opacity="0" />
    </>),
    build: (svg, tl) => {
      const l = one(svg, '[data-hand="l"]'), r = one(svg, '[data-hand="r"]'), body = one(svg, '[data-body]');
      const xs = [190, 230, 270, 300];
      xs.forEach((x, k) => {
        const at = k * 0.9;
        tl.set(l, { attr: { transform: `translate(${x} 140)` } }, at).set(r, { attr: { transform: `translate(${x + 26} 140)` } }, at)
          .to(l, { attr: { transform: `translate(${x} 152)` }, duration: 0.2, yoyo: true, repeat: 1, ease: 'power2.in' }, at)
          .to(r, { attr: { transform: `translate(${x + 26} 154)` }, duration: 0.2, yoyo: true, repeat: 1, ease: 'power2.in' }, at + 0.45)
          .to(body, { scaleY: 0.97, transformOrigin: '50% 100%', duration: 0.2, yoyo: true, repeat: 3 }, at);
      });
      tl.to(one(svg, '[data-palms]'), { opacity: 0, duration: 0.3 }, 3.7)
        .to(body, { scaleX: 1.07, transformOrigin: '20% 50%', duration: 1.4, ease: 'sine.inOut' }, 4)
        .to(one(svg, '[data-arrow]'), { opacity: 1, duration: 0.5 }, 4.1)
        .to(body, { scaleX: 1, duration: 1.2, ease: 'power3.inOut' }, 6)
        .to(one(svg, '[data-arrow]'), { opacity: 0, duration: 0.4 }, 6)
        .to(one(svg, '[data-palms]'), { opacity: 1, duration: 0.3 }, 7);
    },
  },

  sarga: {
    label: 'Holding a bar and strap overhead, a bare foot steps along the back, one place at a time; each step presses down and the pressure spreads wide.',
    draw: (<>
      <line data-bar x1="60" y1="26" x2="340" y2="26" strokeWidth="5" strokeLinecap="round" />
      <line data-strap x1="150" y1="26" x2="150" y2="96" strokeWidth="3" stroke="var(--acc)" />
      <Table />
      {[0, 1].map((i) => <ellipse key={i} data-ring cx="150" cy="156" rx="8" ry="2" fill="none" strokeWidth="1.6" />)}
      <g data-foot transform="translate(150 110)">
        <line x1="0" y1="-14" x2="0" y2="-80" strokeWidth="12" strokeLinecap="round" stroke="var(--acc)" />
        <path d="M-12 -6 C-12 -18 10 -20 16 -10 C20 -2 14 4 2 4 L-8 4 C-12 4 -12 0 -12 -6 Z" fill="var(--acc)" />
      </g>
    </>),
    build: (svg, tl) => {
      const foot = one(svg, '[data-foot]'), strap = one(svg, '[data-strap]'), rings = sel(svg, '[data-ring]'), body = one(svg, '[data-body]');
      [150, 205, 260].forEach((x, k) => {
        const at = k * 2.4;
        tl.to(foot, { attr: { transform: `translate(${x} 110)` }, duration: 0.6, ease: 'sine.inOut' }, at)
          .to(strap, { attr: { x1: x - 30, x2: x + 4 }, duration: 0.6, ease: 'sine.inOut' }, at)
          .to(foot, { attr: { transform: `translate(${x} 152)` }, duration: 0.55, ease: 'power3.in' }, at + 0.7)
          .to(strap, { attr: { y2: 120 }, duration: 0.55, ease: 'power3.in' }, at + 0.7)
          .to(body, { scaleY: 0.94, transformOrigin: `${(x - 60) / 2.8}% 100%`, duration: 0.4, yoyo: true, repeat: 1 }, at + 1.2)
          .fromTo(rings, { attr: { cx: x, rx: 8, ry: 2 }, opacity: 1 }, { attr: { rx: 70, ry: 14 }, opacity: 0, duration: 1.2, stagger: 0.3 }, at + 1.25)
          .to(foot, { attr: { transform: `translate(${x} 110)` }, duration: 0.5, ease: 'sine.out' }, at + 1.9)
          .to(strap, { attr: { y2: 96 }, duration: 0.5 }, at + 1.9);
      });
    },
  },

  zen: {
    label: 'A river winds down through a mountain meadow while the sun rises and clouds drift; a massage table waits by the water.',
    draw: (<>
      <circle data-sun cx="290" cy="110" r="22" fill="var(--acc)" stroke="none" />
      <g data-cloud><path d="M60 50 C60 40 76 36 84 44 C90 34 108 38 108 50 Z" fill="color-mix(in oklab, currentColor 12%, transparent)" /></g>
      <path d="M0 150 L70 80 L120 125 L180 60 L250 130 L310 85 L400 150 Z" fill="color-mix(in oklab, currentColor 18%, transparent)" />
      <path d="M0 170 L90 120 L160 160 L230 115 L300 158 L360 130 L400 160 L400 260 L0 260 Z" fill="color-mix(in oklab, currentColor 10%, transparent)" />
      {[0, 1].map((i) => <path key={i} data-river d="M200 140 C170 170 250 180 210 205 C175 228 260 240 230 262" fill="none" stroke="var(--acc)" strokeWidth={i ? 3 : 10} strokeLinecap="round" strokeDasharray={i ? '6 14' : undefined} opacity={i ? 1 : 0.45} />)}
      <g transform="translate(270 200)"><line x1="0" y1="0" x2="70" y2="0" strokeWidth="3" /><line x1="8" y1="0" x2="6" y2="18" /><line x1="62" y1="0" x2="64" y2="18" /><path d="M10 -2 C30 -10 50 -10 66 -4 L66 0 L10 0 Z" fill="var(--acc)" /><circle cx="6" cy="-6" r="5" /></g>
    </>),
    build: (svg, tl) => {
      tl.to(one(svg, '[data-river]:last-of-type'), { attr: { 'stroke-dashoffset': -80 }, duration: 6, ease: 'none' }, 0)
        .fromTo(one(svg, '[data-sun]'), { attr: { cy: 120 } }, { attr: { cy: 70 }, duration: 6, ease: 'sine.inOut' }, 0)
        .fromTo(one(svg, '[data-cloud]'), { x: -40 }, { x: 240, duration: 6, ease: 'none' }, 0);
    },
  },

  yoga: {
    label: 'A figure flows from standing, to a forward fold, to downward dog, then rests in a long, still hold while a circle breathes slowly.',
    draw: (<>
      <circle data-breath cx="200" cy="140" r="70" fill="var(--acc)" opacity=".25" stroke="none" />
      <line x1="80" y1="220" x2="320" y2="220" strokeWidth="3" />
      <g data-fig strokeWidth="7" strokeLinecap="round" strokeLinejoin="round">
        <line data-limb="spine" /><line data-limb="armL" /><line data-limb="armR" /><line data-limb="legL" /><line data-limb="legR" /><circle data-head r="11" fill="var(--acc)" />
      </g>
    </>),
    build: (svg, tl) => {
      type P = { head: [number, number]; neck: [number, number]; hip: [number, number]; hands: [number, number]; feet: [number, number] };
      const POSES: P[] = [
        { head: [200, 72], neck: [200, 90], hip: [200, 150], hands: [200, 34], feet: [200, 218] },     // standing, arms up
        { head: [212, 186], neck: [210, 168], hip: [200, 140], hands: [220, 216], feet: [200, 218] },  // forward fold
        { head: [168, 180], neck: [178, 162], hip: [222, 112], hands: [146, 216], feet: [262, 218] },  // downward dog
        { head: [150, 196], neck: [168, 186], hip: [236, 190], hands: [118, 214], feet: [262, 218] },  // child's pose (hold)
      ];
      const cur = { ...POSES[0] };
      const L = (n: string) => one(svg, `[data-limb="${n}"]`);
      const draw = () => {
        const set = (el: SVGElement, a: number[], b: number[]) => { el.setAttribute('x1', String(a[0])); el.setAttribute('y1', String(a[1])); el.setAttribute('x2', String(b[0])); el.setAttribute('y2', String(b[1])); };
        set(L('spine'), cur.neck, cur.hip);
        set(L('armL'), cur.neck, [cur.hands[0] - 6, cur.hands[1]]); set(L('armR'), cur.neck, [cur.hands[0] + 6, cur.hands[1]]);
        set(L('legL'), cur.hip, [cur.feet[0] - 8, cur.feet[1]]); set(L('legR'), cur.hip, [cur.feet[0] + 8, cur.feet[1]]);
        const h = one(svg, '[data-head]'); h.setAttribute('cx', String(cur.head[0])); h.setAttribute('cy', String(cur.head[1]));
      };
      draw();
      const go = (p: P, at: number, d: number) => {
        const from = { ...cur }, o = { t: 0 };
        tl.fromTo(o, { t: 0 }, { t: 1, duration: d, ease: 'sine.inOut', onStart: () => Object.assign(from, cur), onUpdate: () => {
          (Object.keys(p) as (keyof P)[]).forEach((k) => { cur[k] = [from[k][0] + (p[k][0] - from[k][0]) * o.t, from[k][1] + (p[k][1] - from[k][1]) * o.t]; });
          draw();
        } }, at);
      };
      go(POSES[1], 0.6, 1.1); go(POSES[2], 1.9, 1.1); go(POSES[0], 3.2, 1.3); go(POSES[1], 4.7, 1); go(POSES[3], 6, 1.4); go(POSES[0], 11.4, 1.4);
      tl.fromTo(one(svg, '[data-breath]'), { attr: { r: 60 } }, { attr: { r: 84 }, duration: 2.2, yoyo: true, repeat: 1, ease: 'sine.inOut' }, 7.2);
    },
  },

  astro: {
    label: 'A ring of zodiac stars turns slowly while three cards turn over one by one to show the sun, the moon and a star.',
    draw: (<>
      <g data-zodiac>{Array.from({ length: 12 }, (_, i) => { const a = (i / 12) * Math.PI * 2; return <circle key={i} cx={r2(200 + Math.cos(a) * 112)} cy={r2(132 + Math.sin(a) * 112)} r={i % 3 ? 2.4 : 4} fill="var(--acc)" stroke="none" />; })}<circle cx="200" cy="132" r="112" fill="none" strokeWidth="1" opacity=".35" /></g>
      {[0, 1, 2].map((i) => (
        <g key={i} transform={`translate(${130 + i * 70} 132) rotate(${(i - 1) * 8})`}>
          <g data-card>
            <rect x="-28" y="-46" width="56" height="92" rx="7" fill="color-mix(in oklab, currentColor 8%, transparent)" strokeWidth="2.5" />
            <g data-back><path d="M-16 -30 L16 30 M16 -30 L-16 30" strokeWidth="1" opacity=".5" /><circle r="9" fill="none" /></g>
            <g data-face opacity="0">
              {i === 0 && <><circle r="11" fill="var(--acc)" />{Array.from({ length: 8 }, (_, k) => { const a = (k / 8) * Math.PI * 2; return <line key={k} x1={r2(Math.cos(a) * 15)} y1={r2(Math.sin(a) * 15)} x2={r2(Math.cos(a) * 21)} y2={r2(Math.sin(a) * 21)} strokeWidth="2" />; })}</>}
              {i === 1 && <path d="M6 -16 A16 16 0 1 0 6 16 A12 12 0 1 1 6 -16 Z" fill="var(--acc)" />}
              {i === 2 && <path d="M0 -18 L5 -5 L18 -5 L8 3 L12 17 L0 8 L-12 17 L-8 3 L-18 -5 L-5 -5 Z" fill="var(--acc)" />}
            </g>
          </g>
        </g>
      ))}
    </>),
    build: (svg, tl) => {
      tl.to(one(svg, '[data-zodiac]'), { rotate: 60, svgOrigin: '200 132', duration: 9, ease: 'none' }, 0);
      sel(svg, '[data-card]').forEach((card, i) => {
        const at = 0.6 + i * 1.6;
        tl.to(card, { scaleX: 0, duration: 0.35, ease: 'power2.in', transformOrigin: '50% 50%' }, at)
          .set(card.querySelector('[data-back]'), { opacity: 0 }, at + 0.35).set(card.querySelector('[data-face]'), { opacity: 1 }, at + 0.35)
          .to(card, { scaleX: 1, y: -10, duration: 0.45, ease: 'power2.out' }, at + 0.35);
      });
      sel(svg, '[data-card]').forEach((card, i) => {
        tl.to(card, { scaleX: 0, duration: 0.3, ease: 'power2.in' }, 7.4 + i * 0.15)
          .set(card.querySelector('[data-back]'), { opacity: 1 }, 7.7 + i * 0.15).set(card.querySelector('[data-face]'), { opacity: 0 }, 7.7 + i * 0.15)
          .to(card, { scaleX: 1, y: 0, duration: 0.35 }, 7.7 + i * 0.15);
      });
    },
  },

  herbs: {
    label: 'Herb leaves drop into a cup of water, which slowly steeps to a warm colour and steams; beside it a dropper fills a tincture bottle drop by drop.',
    draw: (<>
      <defs><clipPath id="cupClip"><path d="M110 120 L230 120 L222 210 C220 222 210 228 198 228 L142 228 C130 228 120 222 118 210 Z" /></clipPath></defs>
      <rect data-tea x="100" y="150" width="140" height="90" clipPath="url(#cupClip)" fill="var(--acc)" opacity=".25" stroke="none" />
      <path d="M110 120 L230 120 L222 210 C220 222 210 228 198 228 L142 228 C130 228 120 222 118 210 Z" fill="none" strokeWidth="3" />
      <path d="M230 140 C258 140 258 186 226 188" fill="none" strokeWidth="3" />
      {[0, 1, 2].map((i) => <path key={i} data-steam d={`M${140 + i * 30} 112 C${130 + i * 30} 96 ${150 + i * 30} 86 ${140 + i * 30} 68`} fill="none" strokeWidth="2" strokeLinecap="round" pathLength={1} strokeDasharray="1" strokeDashoffset="1" />)}
      {[0, 1, 2, 3].map((i) => <path key={i} data-leaf d="M0 -9 C7 -5 7 5 0 9 C-7 5 -7 -5 0 -9 Z M0 -9 L0 9" fill="var(--acc)" transform={`translate(${135 + i * 22} 30)`} />)}
      <g transform="translate(316 0)">
        <rect x="-20" y="150" width="40" height="78" rx="8" fill="none" strokeWidth="3" /><rect x="-8" y="138" width="16" height="12" rx="2" />
        <rect data-fill x="-17" y="225" width="34" height="0" fill="var(--acc)" stroke="none" />
        <line x1="0" y1="70" x2="0" y2="112" strokeWidth="4" /><rect x="-7" y="54" width="14" height="18" rx="5" fill="var(--acc)" />
        <path data-drip d="M0 116 C3 121 4 124 0 126 C-4 124 -3 121 0 116 Z" fill="var(--acc)" stroke="none" />
      </g>
    </>),
    build: (svg, tl) => {
      sel(svg, '[data-leaf]').forEach((leaf, i) => {
        tl.fromTo(leaf, { attr: { transform: `translate(${135 + i * 22} 30) rotate(0)` }, opacity: 1 }, { attr: { transform: `translate(${140 + i * 20} 160) rotate(${i % 2 ? 160 : -140})` }, duration: 1.4, ease: 'sine.in' }, i * 0.3)
          .to(leaf, { opacity: 0, duration: 0.6 }, i * 0.3 + 1.4);
      });
      tl.fromTo(one(svg, '[data-tea]'), { opacity: 0.18, attr: { y: 150 } }, { opacity: 0.9, attr: { y: 140 }, duration: 3.5, ease: 'sine.inOut' }, 1.4)
        .fromTo(sel(svg, '[data-steam]'), { attr: { 'stroke-dashoffset': 1 }, opacity: 1 }, { attr: { 'stroke-dashoffset': -1 }, opacity: 0, duration: 2.4, stagger: 0.5, ease: 'sine.inOut', repeat: 1 }, 2.4);
      const drip = one(svg, '[data-drip]'), fill = one(svg, '[data-fill]');
      for (let k = 0; k < 5; k++) {
        const at = k * 1.3;
        tl.fromTo(drip, { y: 0, opacity: 1 }, { y: 100 - k * 8, duration: 0.5, ease: 'power2.in' }, at).set(drip, { opacity: 0 }, at + 0.5)
          .to(fill, { attr: { y: 225 - (k + 1) * 12, height: (k + 1) * 12 }, duration: 0.4 }, at + 0.5);
      }
      tl.to(fill, { attr: { y: 225, height: 0 }, duration: 0.8 }, 7.6).to(one(svg, '[data-tea]'), { opacity: 0.18, attr: { y: 150 }, duration: 0.8 }, 7.6);
    },
  },
};

export default function ServiceAnim({ k, className = '', tone = 'ink', title = true }: { k: ServiceKey; className?: string; tone?: 'ink' | 'chalk'; title?: boolean }) {
  const ref = useRef<SVGSVGElement>(null);
  const tlRef = useRef<gsap.core.Timeline | null>(null);
  const [paused, setPaused] = useState(false);
  const pausedRef = useRef(false);
  pausedRef.current = paused;

  useEffect(() => {
    const svg = ref.current;
    if (!svg) return;
    const ctx = gsap.context(() => {
      const tl = gsap.timeline({ repeat: -1, repeatDelay: 0.6, paused: true });
      SCENES[k].build(svg, tl);
      tlRef.current = tl;
    }, svg);
    const io = new IntersectionObserver(([en]) => {
      const tl = tlRef.current;
      if (!tl) return;
      if (en.isIntersecting && !pausedRef.current) tl.play(); else tl.pause();
    }, { threshold: 0.15 });
    io.observe(svg);
    return () => { io.disconnect(); ctx.revert(); };
  }, [k]);

  const toggle = () => {
    const tl = tlRef.current;
    setPaused((p) => { if (tl) (p ? tl.play() : tl.pause()); return !p; });
  };

  const sc = SCENES[k];
  return (
    <figure className={`relative m-0 ${tone === 'chalk' ? 'text-chalk' : 'text-ink'} ${className}`}>
      <svg ref={ref} viewBox="0 0 400 260" className="block w-full h-auto overflow-visible" role="img" aria-label={sc.label}
        fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
        {title && <title>{sc.label}</title>}
        {sc.draw}
      </svg>
      <button type="button" onClick={toggle} aria-label={paused ? 'Play animation' : 'Pause animation'}
        className="absolute bottom-1 right-1 grid place-items-center size-9 rounded-full bg-current/10 hover:bg-current/20 transition-colors">
        {paused ? <Play size={15} strokeWidth={2} aria-hidden /> : <Pause size={15} strokeWidth={2} aria-hidden />}
      </button>
    </figure>
  );
}
