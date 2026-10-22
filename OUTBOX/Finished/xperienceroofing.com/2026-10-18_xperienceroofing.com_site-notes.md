# xperienceroofing.com redesign: notes for Angelo

Draft, 18 Oct 2026. Nothing is live. Client: **Xperience Roofing**, Midvale, UT.

- `site/`: the files to put live. Same URLs and canonicals as today (`https://xperienceroofing.com/services/roof-repair`, no trailing slash; the host must serve each page from its folder), the client's **GA4 tag (G-J6XPDS3KLB) kept**.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source (`build.py`, `cfg.py`, `pages.py`, `p_blog.py`, `illus.py`, `engine.py`, `migrate.py`, `clean.py`, `qa.py`; old pages in `_build/src/`).
- `2026-10-17_xperienceroofing.com_report.html`: the website plan report.

## ⚠ Please check first

- **Every photo on the current site is stock** (Freepik / Unsplash style), including European houses and a Dutch scaffolding sign ("Steigerbouw Floren"), and many carry invented local captions such as "Standing seam metal — Draper, UT" or "Commercial TPO — Murray, UT". That presents stock as their own work. The draft uses **no photos**; the design runs on type and original drawings. Ask the client for real job photos with cities.
- **NAP:** Xperience Roofing, 8034 S State St Suite B, Midvale, UT 84047 (the Google profile writes "Ste B"), (385) 402-6364, service@xperienceroofing.com. Hours Mon–Sat 9:00am–8:30pm, Sunday closed (contact page).
- **Rating:** the site says "4.9★ average rating"; the Google profile shows 4.9 from 365 reviews. Kept as the client states it. Confirm before go-live.

## What was done

- **37 pages, same URLs:** home, about, services (+6), systems (+5), materials (+3), process, locations (+10), contact, privacy, terms, a new `/blog` with one post, and a 404 page.
- **Report applied:** home targets "roofing company midvale" (title, H1, first sentence); every service page names Midvale in its title, H1 and opening paragraph.
- **All pages keep the client's own text** (cleaned out of the Next.js markup), with a new title, meta and opening paragraph where needed. Dropped: the stock-photo captions with city names, lifespan and warranty-length figures in the system specs ("25–50 years", "50–70 years", "lifetime"), and form blocks.
- **Kept from the client:** family-run, Midvale, since 2019, licensed and insured (their claim), free inspections, the five signature systems with materials, tiers and palettes, the Installer's Standard, the six-step process, the "what we believe" points, storm documentation (they document; the owner files), solar detach and reset, the 10 location pages.
- **QA:** 0 real issues. The checker flags one item on the home page because its canonical is `https://xperienceroofing.com` with no trailing slash (as on the live site); that's the checker, not the page. JSON-LD valid, no broken links, no sideways scrolling at 390 or 1440 px.

## Design v2 (redone 21 Oct 2026 after review)

Version 1 ran on type and drawings only (the client's own photos were all stock and were removed), and read as not premium enough. Version 2, **"Built for the Wasatch"**, keeps the catalogue concept and sets it against the weather every valley roof answers to.

- **Hero:** a full-height photo of Lone Peak in winter beside the dark catalogue panel.
  - The headline rises in line by line.
  - The standing-seam profile drawing sits on a glass plate over the photo.
- **Panorama band:** the snow-covered Wasatch seen from the valley, carrying the client's own line, "Built for Utah snow, wind and sun."
- **CTA:** a snowy Emigration Canyon photo behind the free-estimate panel.
- **Kept:** "The Collection" system selector (the signature), the Installer's Standard, materials, process, services and FAQ.
- **Photos: openly licensed landscapes, credited on the page as atmosphere, never presented as Xperience jobs.**
  - "Lone Peak Summit in the Winter" by Derrellwilliams (CC BY-SA 4.0)
  - "Wasatch Mountains SLV pano4" by Leon7 (CC BY-SA 3.0)
  - "Wasatch Range from Emigration Canyon" by Kepler Sticka-Jones (CC BY-SA 4.0)
  - All via Wikimedia Commons, lightly graded (brightness, contrast, color).
  - **Real job photos from the client would still be better.**
- **References** (alongside the original Aesop and Le Labo, and Vitsoe catalogues): Dwell and Kinfolk (screenshotted 21 Oct 2026) for photography-led editorial pacing.
- **Motion:** parallax on all three photos. It stops for visitors who choose reduced motion.

## Design (premium, site-specific)

- **Concept, "The Collection":** the client already writes like a catalogue, so the site is laid out like a product collection: a **system selector** (five tabs, each with an original profile drawing of the system, its material, tier and palette as swatch chips), the **Material World** layer stack drawn exploded with the client's own XP-MAT codes, the **Installer's Standard** as six numbered plates, the six-step process as a timeline, and "Edition 02" as a nod to their "Edition 01".
- **References:** Aesop and Le Labo catalogues (restraint, serif display), Vitsoe product pages (spec tables, one accent), architectural detail sheets.
- **Colors:** the brand's warm black and charcoal, bone paper, the logo amber (#ffb000). **Fonts:** Gloock (display), Sora (text), Martian Mono (specs). Verified loading.
- Logo: the client's own SVG, with a light version made for the dark header (same file, text color changed).

## New journal post (1,080 words)

`/blog/how-to-read-a-roofing-estimate`, "How to Read a Roofing Estimate: The Line Items That Matter".

- **Main phrase:** "how to read a roofing estimate" (informational). Search volume: not in our data. It builds on the client's promise of "written estimates with clear line items" and targets no service keyword; it links to replacement, inspections and the process page.
- **Sources (linked):** Utah Admin. Code R156-55a-301 (S280 Roofing Contractor scope); Utah Division of Professional Licensing (license lookup); FTC "Hiring a Contractor" (several written estimates, lowest isn't always best, current license, permits).
- No prices. Byline "Xperience Roofing". [[NEEDS: author]]

## robots.txt, sitemap, schema

- robots.txt allows everything and the AI search bots; sitemap (36 URLs).
- Schema: RoofingContractor (name, phone, email, address, hours, founding date 2019, 10 cities) on every page; Breadcrumb on every inner page; FAQPage on home and the post; BlogPosting on the post; ContactPage on contact.

## Before go-live

- Connect the estimate form (name, phone, email, ZIP, service, message, SMS consent) to the client's handler.
- Re-test speed (it was 98/100; keep it there).
