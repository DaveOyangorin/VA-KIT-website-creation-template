import Img from '@/components/ui/Img';
import Split from '@/components/ui/Split';
import { CERTS } from '@/lib/content';
import { href } from '@/lib/site';

/** A layered composition: her portrait over a wider photo of the table, each drifting at its own depth. */
export default function Meet() {
  return (
    <section className="sec bg-mist overflow-hidden" aria-labelledby="meet-h">
      <div className="wrap grid gap-16 lg:grid-cols-[minmax(0,5fr)_minmax(0,6fr)] items-center">
        <div className="relative h-[min(118vw,680px)] lg:h-[720px]">
          <div data-mask="left" className="absolute right-0 top-0 w-[82%] h-[64%] overflow-hidden rounded-[24px] bg-moss">
            <div data-parallax="0.14" className="absolute -inset-y-[10%] inset-x-0">
              <Img name="sound-tuning-forks" alt="Tuning forks beside a client on the massage table" className="cover" pos="40% 50%" sizes="(max-width: 1023px) 80vw, 36vw" />
            </div>
          </div>
          <div data-mask="up" className="absolute left-0 bottom-0 w-[54%] max-w-[330px] aspect-[9/16] overflow-hidden rounded-[20px] bg-moss shadow-[0_40px_80px_-30px_rgba(13,20,16,.5)]">
            <Img name="miquelle-portrait" alt="Miquelle, founder of Earthen Phoenix, smiling at sunset on the water" className="cover" sizes="330px" />
          </div>
          <p className="absolute right-0 bottom-[6%] w-[38%] text-sm text-ink-2" data-reveal>Miquelle teaches and practises yoga and meditation too.</p>
        </div>
        <div>
          <p className="kicker" data-reveal>Meet Miquelle</p>
          <Split as="h2" id="meet-h" className="h2 mt-6" text="Everyone is _extremely unique._" />
          <p className="lede mt-8 measure text-ink-2" data-reveal>“I have worked with many different people, backgrounds, and bodies. I base my work off individual needs; and can accommodate anything from light and relaxing to deep fascial work.”</p>
          <div className="mt-10" data-reveal>
            <p className="kicker text-ink-2">Certified in</p>
            <ul className="mt-5 flex flex-wrap gap-2">
              {CERTS.map((c) => (
                <li key={c.name}>
                  {c.path ? (
                    <a href={href(c.path)} className="inline-flex min-h-10 items-center rounded-full border border-ink/20 px-4 text-[.92rem] transition-colors duration-500 hover:bg-ink hover:text-chalk">{c.name}</a>
                  ) : (
                    <span className="inline-flex min-h-10 items-center rounded-full border border-ink/10 px-4 text-[.92rem] text-ink-2">{c.name}</span>
                  )}
                </li>
              ))}
            </ul>
          </div>
          <div className="mt-10" data-reveal><a href={href('/about')} className="btn btn-ink">Her story and training</a></div>
        </div>
      </div>
    </section>
  );
}
