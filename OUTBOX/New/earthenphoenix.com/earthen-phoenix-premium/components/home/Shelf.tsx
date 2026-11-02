import { PRODUCTS } from '@/lib/content';
import { STORE, href } from '@/lib/site';
import Img from '@/components/ui/Img';
import { Arr } from '@/components/ui/Arrow';

/** Her oils and butter. On hover the photo lifts off the shelf, its shadow deepens and it eases in closer. */
function Product({ p, store, i }: { p: (typeof PRODUCTS)[number]; store: boolean; i: number }) {
  return (
    <a href={store ? STORE[p.store] : href('/products')} className="group block" data-reveal data-delay={i}>
      <div className="relative aspect-[4/5] overflow-hidden rounded-[22px] bg-moss transition-[transform,box-shadow] duration-700 ease-[cubic-bezier(.16,1,.3,1)] group-hover:-translate-y-2 group-hover:shadow-[0_40px_70px_-35px_rgba(13,20,16,.6)]">
        <Img name={p.img} alt={p.alt} className="cover transition-transform duration-[1400ms] ease-[cubic-bezier(.16,1,.3,1)] group-hover:scale-[1.07]" sizes="(max-width: 767px) 90vw, 30vw" />
      </div>
      <div className="mt-5 flex items-baseline justify-between gap-4">
        <h3 className="font-display text-[1.5rem] leading-tight tracking-[-0.015em]">{p.name}</h3>
        <span className="tabular-nums">{p.price}</span>
      </div>
      {store && <p className="mt-2 inline-flex items-center gap-2 text-sm text-clay">Buy in the online store <Arr out /></p>}
    </a>
  );
}

export default function Shelf({ store = false }: { store?: boolean }) {
  return (
    <div className="grid gap-12 md:grid-cols-3 md:gap-8">
      {PRODUCTS.map((p, i) => <Product key={p.name} p={p} store={store} i={i} />)}
    </div>
  );
}
