# Earthen Phoenix: "The Earthen Atlas" website

An original design for Earthen Phoenix (Miquelle, Salt Lake City), built 31 Oct 2026. Only the words, prices and photographs come from her current site and booking page. The concept, layout, type, colour, animation and code are all new. Nothing from the earlier drafts (Ember, the full-site preview, the sand-garden home) is reused.

## The concept

**Tension is drawn as elevation.** The five bands in the Earthen Phoenix mark (yellow, orange, red, brown, green) run like the colours of a relief map, so the site uses them as its map key: yellow and orange peaks are tension, brown is settling, green is ground. Her tagline, "Ground your soul", becomes literal: every session is shown as a terrain, and each one brings the ground level in its own way.

## Design system

- **Colour:** survey paper `#eee6d8`, dark earth `#1a1612`, plus the five bands from her mark: `#f3bd47` `#e5842f` `#c4432f` `#8f5c34` `#5f7d45`. Call-to-action red `#a8361f`.
- **Type:** Gloock (display serif), Albert Sans (text), Martian Mono (map labels and readouts). All from Google Fonts.
- **Layout devices:** full-bleed photo headers, a pinned sideways "atlas" of ten live plates, an offset field-photo collage, a trail elevation profile for her training, dashed "route" steps, and map labels with leader lines.

## Service animations (`assets/terrain.js`)

| Session | What the terrain shows | Visitor can |
|---|---|---|
| Home hero | Peaks over the shoulders and lower back; a long stroke passes and they level; tension slowly returns; scrolling grounds it | Scroll |
| Swedish | One long stroke per pass; peaks soften as it crosses | Drag to stroke; light or medium; add sound (ripples), meditation (slower), breathwork (the field breathes) |
| Deep tissue | One point sinks into one knot on each out-breath, then moves to the next | Choose depth |
| Thai | Presses on a beat from feet to hips, then the ground is stretched long | Tap to press |
| Lymphatic | A broad swelling drains as flow dots travel the paths to the collarbone | Watch |
| Sarga | Footprints step up the back; each hollow spreads wide | Tap to step |
| Reiki | No pressing: the whole field evens out toward balance | Hands on or near; tap to move hands |
| Zen mountain | Real mountains and a river that slows the longer you stay | Move fast to stir it |
| Private yoga | Waves during Vinyasa, stillness and slow breath in Yin | Tap to flow again |
| Astrology | Your sun sign's stars (stylised) over a dark horizon | Pick your birthday |
| Herbalism | An infusion spreading: tea, tincture drops, or a rollie line | Choose; tap to add a drop |

Also: the logo's five bands sweep across between pages, headings rise word by word, photos reveal like a survey scan, and the footer terrain sits at ground level and only breathes. With reduced motion on, every terrain is drawn still and nothing pins or sweeps.

## Pages (17)

`index.html`, `sessions.html`, ten session pages, `about.html`, `products.html`, `faq.html`, `contact.html`, `404.html`. Also `sitemap.xml`, `robots.txt`, `llms.txt` (plain summary for AI answer engines) and `_redirects` (old URLs to new pages, Netlify format). Every page has its own title, description, canonical, Open Graph tags and JSON-LD (business, breadcrumbs, services with offers, FAQs, products).

## Editing

All words live in `_src/build.py`. Change them there, then run:

```
python _src/build.py
```

Styles are in `assets/atlas.css`, page behaviour in `assets/site.js`, and the terrain engine in `assets/terrain.js`. No framework, no build tools and no dependencies.

## Deploying

It is a static site: upload the folder (minus `_src` and this README if you like) to any static host.

- **Netlify:** drag the folder onto app.netlify.com/drop, or connect the repo with no build command and the folder as the publish directory. `_redirects` works as is.
- **Cloudflare Pages / Vercel / GitHub Pages:** same, no build step. On hosts other than Netlify, recreate the redirects in their format.
- Point `earthenphoenix.com` at the new host only after the booking calendar is sorted (below).

## Before launch (flags)

1. **Booking calendar:** every "Book" button links to the live GoHighLevel page `earthenphoenix.com/appointment-8682`. If the domain moves to a new host, that calendar must move or get a new URL first, or booking breaks.
2. **Yoga price:** the booking page says $140 for 60 minutes; her old home page said $120. This site uses $140. Confirm with Miquelle.
3. **Testimonials:** the three quotes (Sylvie, V, Megan) are from her current site. Confirm she is happy to keep using them.
4. **Address and hours:** not shown, because they are not published. Ask whether to add them.
5. **Contact form:** it opens the visitor's own email or text app with the note filled in. Nothing is stored. For a true form inbox, connect Netlify Forms or the GoHighLevel form.
6. **Star patterns** on the astrology page are stylised and labelled as such.
