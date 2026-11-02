import { notFound } from 'next/navigation';
import type { ComponentType } from 'react';
import { SERVICES, bySlug, type Service, type ServiceKey } from '@/lib/content';
import { BUSINESS, crumbsLd, faqLd, graph, pageMeta, serviceLd } from '@/lib/seo';
import { BOOK, TEL, absolute } from '@/lib/site';
import PageHero from '@/components/ui/PageHero';
import Faq from '@/components/ui/Faq';
import MoreSessions from '@/components/ui/MoreSessions';
import JsonLd from '@/components/ui/JsonLd';
import Split from '@/components/ui/Split';
import { Arr } from '@/components/ui/Arrow';
import Details from '@/components/services/Details';
import ReikiHalo from '@/components/services/ReikiHalo';
import SwedishStroke from '@/components/services/SwedishStroke';
import LymphSequence from '@/components/services/LymphSequence';
import DeepLayers from '@/components/services/DeepLayers';
import ThaiRhythm from '@/components/services/ThaiRhythm';
import SargaSteps from '@/components/services/SargaSteps';
import ZenHorizon from '@/components/services/ZenHorizon';
import YogaFlow from '@/components/services/YogaFlow';
import TarotDraw from '@/components/services/TarotDraw';
import HerbSteep from '@/components/services/HerbSteep';

/** One signature piece per session: each animates her photograph the way that session works. */
const SIGNATURE: Record<ServiceKey, ComponentType<{ s: Service }>> = {
  reiki: ReikiHalo, swedish: SwedishStroke, lymph: LymphSequence, deep: DeepLayers, thai: ThaiRhythm,
  sarga: SargaSteps, zen: ZenHorizon, yoga: YogaFlow, astro: TarotDraw, herbs: HerbSteep,
};

export const dynamicParams = false;
export function generateStaticParams() {
  return SERVICES.map((s) => ({ service: s.slug }));
}

type Props = { params: Promise<{ service: string }> };

export async function generateMetadata({ params }: Props) {
  const s = bySlug((await params).service);
  if (!s) return {};
  return pageMeta({ title: s.seo.title, desc: s.seo.desc, path: '/' + s.slug, og: s.hero.img ?? s.img });
}

export default async function ServicePage({ params }: Props) {
  const s = bySlug((await params).service);
  if (!s) notFound();
  const Signature = SIGNATURE[s.key];
  const trail: [string, string][] = [['Home', '/'], ['Sessions', '/sessions'], [s.name, '/' + s.slug]];
  const ctas = s.key === 'zen'
    ? <><a href={TEL} className="btn btn-flame">Ask about location and season <Arr /></a><a href={BOOK} className="btn btn-ghost">Booking page</a></>
    : s.key === 'herbs'
      ? <><a href={BOOK} className="btn btn-flame">Book a consultation <Arr /></a><a href={TEL} className="btn btn-ghost">Call or text</a></>
      : <><a href={BOOK} className="btn btn-flame">Book this session <Arr /></a><a href={TEL} className="btn btn-ghost">Call or text</a></>;

  return (
    <>
      <JsonLd data={graph(
        BUSINESS,
        { '@type': 'WebPage', url: absolute('/' + s.slug), name: s.seo.title, description: s.seo.desc, inLanguage: 'en-US' },
        serviceLd(s), faqLd(s.faqs), crumbsLd(trail),
      )} />
      <PageHero img={s.hero.img ?? s.img} alt={s.hero.alt ?? s.alt} pos={s.hero.pos ?? s.pos} kicker={s.hero.kicker} title={s.hero.title}
        answer={s.hero.answer} spec={s.hero.spec} trail={trail} reveal={s.key} ctas={ctas} />
      <Signature s={s} />
      <Details s={s} />
      <section className="sec bg-chalk" aria-labelledby="faq-h">
        <div className="wrap grid gap-12 lg:grid-cols-[minmax(0,4fr)_minmax(0,7fr)]">
          <div>
            <p className="kicker" data-reveal>Before you book</p>
            <Split as="h2" id="faq-h" className="h2 mt-6" text="Asked _and answered._" />
          </div>
          <div data-reveal><Faq items={s.faqs} /></div>
        </div>
      </section>
      <MoreSessions keys={s.related} />
    </>
  );
}
