'use client';
import { useEffect, useRef, useState } from 'react';
import type { Service } from '@/lib/content';
import { prefersReduced } from '@/lib/anim';
import { imgSrc } from '@/lib/images';
import Img from '@/components/ui/Img';
import SigCopy from './SigCopy';

/**
 * Swedish: long strokes and essential oils. Drag across the photograph and each stroke leaves a warm, glossy
 * trace that lifts the photo out of shadow and then slowly sinks back, like oil being worked in.
 * Left alone, a long demonstration stroke travels the length of the frame. Light or medium changes the width.
 */
export default function SwedishStroke({ s }: { s: Service }) {
  const wrap = useRef<HTMLDivElement>(null);
  const canvas = useRef<HTMLCanvasElement>(null);
  const [pressure, setPressure] = useState<'light' | 'medium'>('light');
  const pRef = useRef(pressure);
  pRef.current = pressure;

  useEffect(() => {
    const el = wrap.current, cv = canvas.current;
    if (!el || !cv) return;
    const ctx = cv.getContext('2d')!;
    const mask = document.createElement('canvas');
    const mctx = mask.getContext('2d')!;
    const img = new Image();
    img.src = imgSrc(s.img, true);
    let W = 0, H = 0, dpr = 1, raf = 0, visible = true, ready = false;
    let lastInput = -1e9, demoT = 0;
    let prev: { x: number; y: number } | null = null;

    const size = () => {
      dpr = Math.min(2, window.devicePixelRatio || 1);
      W = el.clientWidth; H = el.clientHeight;
      for (const c of [cv, mask]) { c.width = W * dpr; c.height = H * dpr; }
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      mctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    };
    const cover = () => { // draw the photo object-fit: cover, matching the <img> beneath
      const s2 = Math.max(W / img.width, H / img.height);
      const w = img.width * s2, h = img.height * s2;
      ctx.drawImage(img, (W - w) / 2, (H - h) * 0.3, w, h);
    };
    const stroke = (a: { x: number; y: number }, b: { x: number; y: number }) => {
      const wdt = (pRef.current === 'light' ? 0.09 : 0.14) * Math.max(W, 420);
      mctx.globalCompositeOperation = 'source-over';
      mctx.lineCap = 'round'; mctx.lineJoin = 'round';
      mctx.strokeStyle = 'rgba(0,0,0,.6)';
      mctx.shadowColor = 'rgba(0,0,0,1)'; mctx.shadowBlur = wdt * 0.5;
      mctx.lineWidth = wdt;
      mctx.beginPath(); mctx.moveTo(a.x, a.y); mctx.lineTo(b.x, b.y); mctx.stroke();
    };
    const demoPoint = (t: number) => ({ // one long stroke, down the length of the frame and back
      x: W * (0.08 + 0.84 * (0.5 - 0.5 * Math.cos(t * Math.PI))),
      y: H * (0.32 + 0.22 * Math.sin(t * Math.PI * 1.3)),
    });

    const frame = (t: number) => {
      raf = requestAnimationFrame(frame);
      if (!visible || !ready) return;
      // the oil slowly works in: the trace fades
      mctx.globalCompositeOperation = 'destination-out';
      mctx.shadowBlur = 0;
      mctx.fillStyle = 'rgba(0,0,0,.007)';
      mctx.fillRect(0, 0, W, H);
      if (t - lastInput > 2600) {
        const p0 = demoPoint(demoT % 2 > 1 ? 2 - (demoT % 2) : demoT % 2);
        demoT += 0.0045;
        const p1 = demoPoint(demoT % 2 > 1 ? 2 - (demoT % 2) : demoT % 2);
        stroke(p0, p1);
      }
      ctx.clearRect(0, 0, W, H);
      ctx.globalCompositeOperation = 'source-over';
      ctx.filter = 'brightness(1.3) saturate(1.2) sepia(.14)';
      cover();
      ctx.filter = 'none';
      ctx.globalCompositeOperation = 'destination-in';
      ctx.drawImage(mask, 0, 0, W, H);
      ctx.globalCompositeOperation = 'lighter'; // a faint sheen where the oil is
      ctx.globalAlpha = 0.12;
      ctx.drawImage(mask, 0, 0, W, H);
      ctx.globalAlpha = 1;
    };

    const pos = (e: PointerEvent) => { const r = el.getBoundingClientRect(); return { x: e.clientX - r.left, y: e.clientY - r.top }; };
    const down = (e: PointerEvent) => { prev = pos(e); lastInput = performance.now(); el.setPointerCapture(e.pointerId); };
    const move = (e: PointerEvent) => {
      if (!prev && e.pointerType !== 'mouse') return;
      const p = pos(e);
      if (prev) stroke(prev, p);
      prev = e.buttons || e.pointerType === 'mouse' ? p : null;
      lastInput = performance.now();
    };
    const up = () => { prev = null; };
    const leave = () => { prev = null; };

    size();
    const ro = new ResizeObserver(size); ro.observe(el);
    const io = new IntersectionObserver(([en]) => { visible = en.isIntersecting; }); io.observe(el);
    img.onload = () => {
      ready = true;
      if (prefersReduced()) { // draw one finished stroke, still
        for (let i = 0; i < 60; i++) stroke(demoPoint(i / 60), demoPoint((i + 1) / 60));
        frame(0); cancelAnimationFrame(raf);
      }
    };
    el.addEventListener('pointerdown', down);
    el.addEventListener('pointermove', move);
    el.addEventListener('pointerup', up);
    el.addEventListener('pointerleave', leave);
    if (!prefersReduced()) raf = requestAnimationFrame(frame);
    return () => {
      cancelAnimationFrame(raf); ro.disconnect(); io.disconnect();
      el.removeEventListener('pointerdown', down); el.removeEventListener('pointermove', move);
      el.removeEventListener('pointerup', up); el.removeEventListener('pointerleave', leave);
    };
  }, [s.img]);

  return (
    <section className="sec bg-mist text-ink" aria-labelledby="sig-h">
      <div className="wrap grid gap-14 lg:grid-cols-[minmax(0,7fr)_minmax(0,4fr)] items-center">
        <figure className="m-0 order-2 lg:order-1">
          <div ref={wrap} data-mask="left" className="relative aspect-[4/5] sm:aspect-[16/11] overflow-hidden rounded-[28px] bg-moss touch-pan-y select-none cursor-crosshair">
            <Img name={s.img} alt={s.alt} className="cover [filter:brightness(.42)_saturate(.65)]" pos="50% 30%" sizes="(max-width: 1023px) 92vw, 60vw" />
            <canvas ref={canvas} className="absolute inset-0 w-full h-full" aria-hidden />
          </div>
          <figcaption className="mt-4 text-sm text-ink-2">Her photograph. Each stroke you draw lifts the warmth back into it, then slowly works in.</figcaption>
        </figure>
        <div className="order-1 lg:order-2">
          <SigCopy s={s}>
            <div className="seg" role="group" aria-label="Pressure">
              <button type="button" aria-pressed={pressure === 'light'} onClick={() => setPressure('light')}>Light</button>
              <button type="button" aria-pressed={pressure === 'medium'} onClick={() => setPressure('medium')}>Medium</button>
            </div>
          </SigCopy>
        </div>
      </div>
    </section>
  );
}
