# Earthen Phoenix: "Rise & Rest"

A new website for Earthen Phoenix (Miquelle, Salt Lake City), built 2 November 2026 with Next.js 16, React 19, TypeScript, Tailwind CSS 4, GSAP + ScrollTrigger, Motion for React, Lenis and Lucide icons.

Only the words, prices and photographs come from her current site and booking page. The concept, palette, type, layout, components, animation and code are all new. Nothing is reused from the earlier drafts (strata/breath/bowl, sand garden, "Release", Ember, Atlas).

## The concept

Her mark rises out of the earth: a phoenix over the ground, with the line "Ground your soul." On the home page the headline sits **behind her real Wasatch ridge**. The sky was cut out of her own meadow photograph, so the words climb out from behind the mountains on arrival (the phoenix rising) and sink back behind them as you scroll (grounding).

The sessions are then ordered by **how her hands meet the body**, from her own descriptions: hands near (Reiki), hands that glide (Swedish, lymphatic), hands that press (deep tissue, Thai), full weight (Sarga), then beyond the table (Zen mountain, yoga, readings, herbs). Every session animates **her actual photograph** the way that session works.

## Design system

- **Colour:** moss-night `#0d1410`, mountain mist `#eaeef0` (sampled from her own sky), chalk `#f6f7f4`, lichen `#aab79c`, flame `#ec6a3f` (CTA), clay `#9c3a1b` (accent on light), amber `#f2a65a`. All text pairs pass WCAG AA (5.9:1 or better).
- **Type:** Fraunces (soft optical serif, self-hosted by next/font) and Hanken Grotesk.
- **Tokens:** `app/globals.css` (`@theme`), base styles in `@layer base`, components in `@layer components`.

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
