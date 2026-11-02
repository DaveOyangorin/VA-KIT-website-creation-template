# Earthen Phoenix: a scroll-driven story

A new website for Earthen Phoenix (Miquelle, Salt Lake City), built 2 November 2026 with Next.js 16, React 19, TypeScript, Tailwind CSS 4, GSAP + ScrollTrigger, Motion for React, Lenis and Lucide icons.

Only the words, prices and photographs come from her current site and booking page. The concept, palette, type, layout, components, animation and code are all new. Nothing is reused from the earlier drafts (strata/breath/bowl, sand garden, "Release", Ember, Atlas).

## The concept (v2: a scroll-driven story)

The first version ("Rise & Rest", dark moss, headline behind the ridge) was rejected as too dark, too text-heavy and not "wow". This version tells the whole home page as one scroll-driven story of pinned, full-screen scenes (`components/story/`):

1. **Opening:** "Earthen" and "Phoenix" on linen with her meadow in a small window between them; scrolling parts the words and opens the window to full screen, then "Ground your soul."
2. **Reel:** all ten sessions slide past sideways as tall photo panels.
3. **Chapters:** one pinned full-screen chapter per session; scroll plays that session's own motion on its photo (`lib/reveals.ts`).
4. **Miquelle:** her portrait grows while her own words light up.
5. **Client words:** three quotes, one at a time, over the hillside.
6. **Shelf**, then the **closing scene** on every page: the meadow folds back into a circle around the invitation to book.

## Design system

- **Colour:** linen `#f6f3ee`, sand `#ece6dc`, ink `#1d211c`, sage `#5c6f50`/`#8a9b7c`, and the logo's sun `#e8a33d` and ember `#c4502a` (CTA, white text 4.7:1).
- **Type:** Bodoni Moda (display) and Manrope (text), loaded from Google Fonts so they also load inside sandboxed preview frames.

## Service-specific animation

| Session | On the home stage (`lib/reveals.ts`) | On its own page (`components/services/`) |
|---|---|---|
| Reiki | A soft circle of light widens and the photo comes into focus | `ReikiHalo`: a warm, clear light follows your hand without touching; "Hands on / Hands near" |
| Swedish | One long diagonal stroke with a sheen of oil | `SwedishStroke`: drag to leave warm, glossy strokes that slowly work in; Light / Medium |
| Lymphatic | The frame clears from every edge toward the collarbone | `LymphSequence`: pinned scroll through all six treatment steps on one photo |
| Deep tissue | A small window opens while the photo pushes in | `DeepLayers`: pinned scroll through four nested windows, one per part of the session |
| Thai | Bands press up on a beat, then the photo is drawn long | `ThaiRhythm`: the photo in ten bands that press on a beat, then stretch apart; tap to press |
| Sarga | Climbs in six weighted steps | `SargaSteps`: each step presses the photo down and the pressure ripples outward; the strap tightens |
| Zen mountain | A letterbox opens like a widening view | `ZenHorizon`: pinned scroll; a thin strip opens to full width while a clock counts 90 minutes |
| Private yoga | An organic shape flows, then settles | `YogaFlow`: the frame moves with a quick breath (Vinyasa), then rests and breathes slowly (Yin) |
| Astrology & tarot | A card turns over | `TarotDraw`: four cards, one per step of a tarot reading; each face is a quarter of her photo |
| Herbalism | Colour fills from below behind a liquid surface | `HerbSteep`: tea fills slowly, tincture drops fall and raise the level, a rollie rolls on one line |

Also: the hero ridge layering and grounding scroll (`components/home/Hero.tsx`), the sticky session stage with its scale of touch (`Register.tsx`), the indoor/outdoor pinned split (`TwoPlaces.tsx`), the layered portrait composition, a drawn first-visit line, the final CTA that opens from a framed print to full width, mask reveals and parallax (`components/layout/Animator.tsx`), a page curtain between pages, and a header that takes on the tone of the section beneath it.

Under `prefers-reduced-motion`, Lenis is off, nothing pins or scrubs, and every piece is drawn in its finished state.

## Pages (17)

`/`, `/sessions`, ten session pages (`/reiki`, `/swedish-massage`, `/lymphatic-firming-treatment`, `/deep-tissue-massage`, `/thai-bodywork`, `/sarga-bodywork`, `/zen-mountain-session`, `/private-yoga`, `/astrology-tarot`, `/herbalism`), `/about`, `/products`, `/faq`, `/contact`, and a 404. Also `sitemap.xml`, `robots.txt`, `llms.txt` (a plain summary for AI answer engines) and `_redirects` (old URLs to new ones, Netlify format).

Every page has its own title, description, canonical URL, Open Graph and Twitter tags, and JSON-LD: business, web page, breadcrumbs, service with offers, FAQ, products and item list.

## Editing

All words, prices and FAQs are in `lib/content.ts`. Contact details and the booking link are in `lib/site.ts`. Photos are in `public/img/`. `mountain-meadow-ridge-*.webp` is the meadow photo with the sky cut out; if the hero photo ever changes, that cutout must be remade, along with the ridge profile in `Hero.tsx`.

```
npm install
npm run dev              # http://localhost:3000
npm run build            # production static export -> out/
npm run build:preview    # flat, relative-path copy -> out-preview/ (works from any folder)
npm run typecheck
```

## Deploying (needs approval first)

`out/` is a fully static site. Upload it to Netlify, Cloudflare Pages, Vercel or any static host. On Netlify, `_redirects` works as is; on other hosts, recreate the redirects in their format. Do not point `earthenphoenix.com` at the new host until the booking calendar is sorted (see below).

## Before launch

1. **Booking calendar:** every "Book" button goes to the live GoHighLevel page `earthenphoenix.com/appointment-8682`. If the domain moves to a new host, that calendar needs a new URL first, or booking breaks.
2. **Yoga price:** the booking page says $140 for 60 minutes; her old home page said $120. This site uses $140. Confirm with Miquelle.
3. **Testimonials:** the three quotes (Sylvie, V, Megan) are from her current site. Confirm she is happy to keep them.
4. **Address and hours** are not shown because they are not published. Ask whether to add them.
5. **Contact form:** it opens the visitor's own email or text app with the note filled in. Nothing is stored. For a real inbox, connect Netlify Forms or the GoHighLevel form.
6. **More photos would help.** There are 7 session photos for 10 sessions, so some are shared (Swedish and deep tissue; Thai and yoga; lymphatic and readings; Zen and yoga). The herbalism page uses her Armature face-oil product photo.
7. **Portrait resolution:** her portrait is only 360×640, so it is kept small. A larger original would look sharper.
