# aluminumlockroofing.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live. Client: **Aluminum Lock Roofing**, Salt Lake City.

- `site/`: the files to put live. Same URLs and canonicals as today, Google Analytics kept.
- `preview/`: the private review copy. No tracking, forms off, draft strip on top.
- `_build/`: the source (`build.py`, `pages.py`, `p_home.py`, `p_blog.py`, `qa.py`).
- `2026-10-16_aluminumlockroofing.com_report.html`: the website plan report.

## ⚠ Please decide first: the address

The report found that this business's Google profile uses **the same address as Custom Roofing LLC** (customroofs.biz): 1950 S 900 W Ste S2, Salt Lake City, UT 84104.

The client's own website shows **no street address**, only phone, email and "Utah". So the draft also leaves the street address out of every page and out of the schema (it says "Salt Lake City, UT" only). Nothing about the address conflict is baked in. Once you decide, the address can be added in one place (`S` in `_build/build.py`).

- Redesign (v2, 18 Oct 2026): "the interlock". Schibsted Grotesk + JetBrains Mono; graphite, brushed aluminum and the brand orange. Transparent header over the snow hero, an animated four-sided interlock graphic, a brushed-aluminum stat band, a working color picker (six finishes have a real client photo; Sierra Tan and Polar White say "sample on request"), photo doors for homeowners and roofers, an exploded 3D roof system, a gallery wall and Q&A cards. The top bar was removed.

## What was done

- **9 pages:**
  - Home, Services, About, FAQ and Contact, plus the privacy policy page.
  - A new blog index and blog post.
  - A 404 page.
  - URLs and canonicals are unchanged (`https://aluminumlockroofing.com/...`, no www).
- **Report applied:** Salt Lake City is named in the home title, H1 and first sentence ("roofing company salt lake city"), and in every page's title or H1.
- **No new service pages were invented.** The report marks 9 of 10 services as "ask client", so roof repair, metal roofing and the rest wait for the client's answers.
- **Images:** 21 local WebP files in `site/assets/img/`, all from the client's own gallery and logo, all under 150 KB, with width/height and alt text. No stock or AI images.
- **The 8 real shingle colors** are shown as color chips, with colors sampled from the client's color chart: Matte Black, Brick Red, Brown Stone, Classic Green, Copper Penny, Granite Gray, Sierra Tan, Polar White.
- **Speed (report: 60/100 on mobile):** plain HTML, one CSS file, no Elementor, small images lazy-loaded below the top. Re-test after go-live.

## Design direction

- **References actually reviewed:** Classic Metal Roofing Systems (classicmetalroofingsystems.com: old project photos shown as print snapshots with captions), DECRA (decra.com: full-bleed roof photography) and Englert (englertinc.com: dark angular sections). DaVinci Roofscapes blocked access.
- **Concept, "the roof archive":** the client's decades-spanning gallery photos (some carry film date stamps) shown as print snapshots with typed captions, plus brushed-aluminum bands and the color chips.
- **Colors:** near-black and aluminum gray, with a copper-orange accent close to their brand #FF6600.
- **Fonts:** Chivo (headings) and IBM Plex Sans (body). Verified loading. The old site used DM Sans.
- **Copy:** the client's own wording is careful and claim-free ("ask about written warranty coverage" and so on). I kept that tone and added no claims about years in business, warranties, prices or "free" estimates.

## New blog post (1,410 words)

`/blog/can-you-put-a-new-roof-over-an-old-roof/`, "Can You Put a New Roof Over an Old Roof?". This is the client's first post, and `/blog/` is new too.

- **Main phrase:** "can you put a new roof over an old roof" (informational, long-tail, blog only).
- **Long-tail phrases:** roof over vs tear off, how many layers of roofing are allowed, aluminum shingles over asphalt.
- **Why this topic:** the client's own FAQ answers the roof-over question, so the post builds on their real expertise. The report reserves "How long do roofs last in Utah?" for the future metal roofing page, so I avoided it here. It's also already used on another client's site.
- **Kept off this post on purpose:** "roofing company salt lake city" (home page) and "roof installation / roof replacement / metal roofing salt lake city" (pages the client still has to confirm). The post only links to the services page.
- **Sources (linked in the post):**
  - ICC: Utah adopted the 2021 IRC.
  - Town of Firestone, CO reroof checklist, quoting IRC R908.3.1.1: "Roof recover is not allowed" when there are already two layers.
  - Fine Homebuilding on ice barriers.
  - The client's own FAQ.
- **No prices.** Cost questions are left for a cost page once the client shares real prices.
- **Author:** the byline is "Aluminum Lock Roofing". [[NEEDS: author]]

## robots.txt, sitemap, schema

- **robots.txt:** allows everything, explicitly allows the AI search bots, and blocks the two builder URLs that were leaking into Google (below). Sitemap: `https://aluminumlockroofing.com/sitemap.xml`.
- **sitemap.xml** lists 7 URLs. The privacy page is left out until it has real text.
- **Schema:**
  - Business: RoofingContractor with name, phone, email, city (no street, see above) and a Facebook link.
  - Services page: two Services (installation, and materials for roofers) + Breadcrumb.
  - FAQ page: FAQPage built from the client's 8 visible FAQs.
  - About: AboutPage. Contact: ContactPage.
  - Blog post: BlogPosting + FAQPage.
  - Breadcrumbs everywhere. No rating markup.

## Problems found on the current site

1. **The sitemap exposes builder internals:** `/?elementskit_template=header` and `/metform-form/new-form-1768995728/`. They should be removed from the sitemap and noindexed.
2. **The privacy policy page has no policy.** It only says "We're currently making changes to our site". The site collects contact form data, so it needs real privacy text. The draft marks it noindex and shows a [[NEEDS]] placeholder.
3. **Missing meta descriptions** on About, Contact, FAQ and Privacy. New ones are written for the draft.

## Tracking (live build only)

- **Google Analytics 4: G-976GK1B0K7**, the same ID their Site Kit plugin uses.
- **Forms:** the contact form has new fields (name, phone, email, project location, current roof type, installation or materials, message), matching what the client asks people to send. It has **no endpoint**. Connect it before go-live.

## Questions for the client (via Angelo)

1. **The address** (see the top section). Is it shared with Custom Roofing LLC on purpose?
2. **Business name:** "Aluminum Lock Roofing" (site) or "Aluminum Lock Roofing Inc" (logo)? The Google profile adds "| Aluminum Shingles".
3. **Phone format:** the site shows (801) 484-3321 and the Google profile shows +1801-484-3321. OK to keep the site's format?
4. **Which services do they offer?** Roof repair, metal roofing, roof replacement, inspections, gutters, commercial, flat roofs, emergency repair. Only confirmed services get pages.
5. **Where do they install?** Their site says "serving customers nationwide" (materials) and asks people to confirm installation availability.
6. **Real prices** for a cost page (aluminum shingle and metal roof cost), plus **warranty terms** to state on the site.
7. **Privacy policy text.**
8. **Blog author:** name and role.
