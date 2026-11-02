import { Arr } from '@/components/ui/Arrow';
import Img from '@/components/ui/Img';
import { href } from '@/lib/site';

export const metadata = { title: 'Page not found | Earthen Phoenix', description: 'This page has moved or no longer exists.', robots: { index: false } };

export default function NotFound() {
  return (
    <section className="relative min-h-[100svh] grid place-items-center overflow-hidden bg-night text-chalk text-center">
      <div className="absolute inset-0 opacity-40"><Img name="mountain-meadow" alt="" className="cover" pos="50% 40%" /></div>
      <div className="absolute inset-0 bg-gradient-to-b from-night/70 to-night" />
      <div className="wrap relative pt-[var(--hdr)]">
        <p className="kicker text-lichen">404</p>
        <h1 className="display h1 mt-6">Off the <em>path.</em></h1>
        <p className="lede mt-6 text-chalk/75">This page has moved or no longer exists.</p>
        <div className="mt-10 flex flex-wrap justify-center gap-3">
          <a href={href('/')} className="btn btn-flame">Home <Arr /></a>
          <a href={href('/sessions')} className="btn btn-ghost">Sessions</a>
        </div>
      </div>
    </section>
  );
}
