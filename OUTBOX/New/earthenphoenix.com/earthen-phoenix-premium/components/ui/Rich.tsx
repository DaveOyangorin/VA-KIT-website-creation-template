import { Fragment } from 'react';
import { BOOK, href } from '@/lib/site';

/** Renders plain copy with [text](/path) links. "BOOK" as a path means the booking calendar. */
export default function Rich({ text }: { text: string }) {
  const parts = text.split(/(\[[^\]]+\]\([^)]+\))/g);
  return (
    <>
      {parts.map((p, i) => {
        const m = p.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
        if (!m) return <Fragment key={i}>{p}</Fragment>;
        const to = m[2] === 'BOOK' ? BOOK : href(m[2]);
        return <a key={i} href={to}>{m[1]}</a>;
      })}
    </>
  );
}
