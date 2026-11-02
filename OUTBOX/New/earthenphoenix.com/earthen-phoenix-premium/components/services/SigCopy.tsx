import type { ReactNode } from 'react';
import { Hand } from 'lucide-react';
import type { Service } from '@/lib/content';
import Split from '@/components/ui/Split';

/** The words beside each signature piece: what the session is, then how to interact with the photograph. */
export default function SigCopy({ s, children, className = '' }: { s: Service; children?: ReactNode; className?: string }) {
  return (
    <div className={className}>
      <p className="kicker text-lichen" data-reveal>{s.signature.kicker}</p>
      <Split as="h2" id="sig-h" className="h2 mt-6" text={s.signature.title} />
      <div className="mt-8 grid gap-5 text-ink-2 measure" data-reveal data-delay="1">
        {s.signature.body.map((p) => <p key={p}>{p}</p>)}
      </div>
      {children && <div className="mt-8" data-reveal data-delay="2">{children}</div>}
      {s.signature.hint && (
        <p className="mt-8 inline-flex items-center gap-3 text-sm text-ink-2" data-reveal data-delay="3">
          <Hand size={16} strokeWidth={1.5} aria-hidden /> {s.signature.hint}
        </p>
      )}
    </div>
  );
}
