import { Fragment, createElement, type ElementType } from 'react';

/**
 * Wraps each word in a line mask so it can rise into place (see Animator).
 * Write _words_ to set them in italic.
 */
export default function Split({ text, as = 'h2', className, delay, id }: { text: string; as?: ElementType; className?: string; delay?: number; id?: string }) {
  const parts = text.split(/(_[^_]+_)/g).filter(Boolean);
  const nodes = parts.map((part, i) => {
    const italic = part.startsWith('_') && part.endsWith('_');
    const words = (italic ? part.slice(1, -1) : part).split(/(\s+)/);
    const inner = words.map((w, j) =>
      /^\s+$/.test(w) || !w ? <Fragment key={j}>{w}</Fragment> : (
        <span className="sw" key={j}><span>{w}</span></span>
      ),
    );
    return italic ? <em key={i}>{inner}</em> : <Fragment key={i}>{inner}</Fragment>;
  });
  return createElement(as, { className, id, 'data-split': '', 'data-delay': delay }, nodes);
}
