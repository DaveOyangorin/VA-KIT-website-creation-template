# stgeorgeconcreteleveling.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **St. George Concrete Leveling**, St. George, UT.

**"Check first" is on the outreach list, and the report found no Google profile.** The reviewer notes the name and domain read like a lead-generation site. **Confirm who owns it, and who answers 435-466-5545, before outreach.**

## Folders and files

- `site/`: the files to put live.
  - All 63 live pages, with the same canonicals (trailing slash).
  - A new blog post at `/blog/irrigation-leaks-sunken-concrete/`.
  - The live site has no tracking tag.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_v3.py`, `p_blog.py`, `illus.py`
  - the kit files
  - the styles: `theme.css`, `premium.css`, `concept.css`, `concept.js`
- `2026-10-19_stgeorgeconcreteleveling.com_report.html`: the website plan report.

## Please check first

- **Details used (the site's own contact page):** 169 W 2710 S Cir Suite 202-A, St. George, UT 84790; 435-466-5545; Monday to Friday, 8–5.
- **Left out until the client can back them up.** There's no Google profile to check against.
  - "Thousands of satisfied customers"
  - "Local and family owned"
  - "15+ years in business"
  - "Certified"
  - "Licensed under Utah's S260 classification"
  - the warranty
  - **customer anecdotes written into the pages**, e.g. "a Bloomington Hills client had a 1.25-inch lip". They read like generated filler.
- **Kept as the client states it:** licensed and insured; free quotes; the five-step process; the technical method (foam, ports, Blue Stakes 811, ADA guidance).
- **Report notes:**
  - The site grew from the 6 pages in the report to 63.
  - The near-duplicate surface pages (concrete lifting, slab lifting, driveway and sidewalk leveling) are kept at their URLs, but the home page presents them as a clear surface picker.
  - Foundation repair is the biggest gap. No page was invented.

## Photos

- **The live site's only photo** is a stock foam-lifting composite. **It is not used.**
- **Everything is drawn:**
  - the hero lip gauge
  - a small isometric drawing for each surface (driveway, sidewalk, patio, garage, pool deck, steps, porch, commercial), shown on every service and town page
- **One openly licensed landscape** is used for atmosphere: Snow Canyon State Park by pkinney62 (CC BY 2.0), credited.

## What was done

- **Text:** the client's own, cleaned.
  - Removed: the repeated trust-badge list, claim sentences and anecdotes, and the quote-form blocks.
  - The FAQs became real FAQs.
- **Report applied:** the home page targets "concrete leveling st george", and every service and town page keeps St. George or its town in the title and H1.
- **QA:**
  - 0 issues across 65 files.
  - No broken images, and no sideways scroll at phone width.
  - The mobile header check passed.
  - Speed should stay high (95 now).

## Design (premium)

- **Research (screenshotted 20 Oct 2026):** Linear, Stripe Press, Hilti.
- **Chosen three:**
  - **Linear** (linear.app): a dark, precise, instrument-like interface.
  - **Stripe Press** (stripe.press): editorial typography.
  - **Hilti** (hilti.com): one hard accent on a quiet ground.
- **Concept, "Measure the lip":**
  - The question every visitor has is "is this bad enough to fix?", and the client's own pages cite the ADA rules that answer it.
  - **The signature, the lip gauge in the hero:** drag the sunken slab and a caliper reads the lip in sixteenths of an inch. The panel names the 2010 ADA Standards rule it falls under: 303.2 vertical up to ¼ in.; 303.3 bevel from ¼ to ½ in.; 303.4 ramp above ½ in. The colour goes green, amber, then red.
  - **The rest:** the surface picker with drawings, a five-step process line, a Snow Canyon band, town chips, and the FAQ plus quote form.
- **Brand guide:**
  - instrument slate #20252B
  - safety yellow #FFCC33
  - concrete greys
  - red-rock soil #A3532F
  - green, amber and red for the gauge
- **Fonts:** Space Grotesk (display), Figtree (text), Space Mono (readouts).

## New blog post (1,054 words)

`/blog/irrigation-leaks-sunken-concrete/`, "Is Your Sprinkler System Sinking Your Concrete? Finding Irrigation Leaks Before They Wash Out a Slab".

- **No cannibalizing.** No page covers finding the water. The post links to pool deck, sidewalk and driveway leveling, void filling and soil stabilization.
- **Sources (linked), all EPA WaterSense:**
  - "Sprinkler Spruce-Up": 50% more outdoor water with clock timers; broken heads; leaky joints and pressure; valves that seep; pooling between cycles; heads aimed at hardscape.
  - "Fix a Leak Week": the two-hour meter test.
  - "Watering Tips": midday watering; clay soils; cycle and soak.
- **Pool-deck details** come from the client's own text.
- **No prices.**

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists every page except `/thank-you/` (noindex).
- **Schema:**
  - Business node (the contact-page address; hours; areas).
  - Breadcrumbs; Service on service and town pages.
  - FAQPage; BlogPosting.

## Before go-live

- Confirm ownership and the claims.
- Connect the quote form.
- Add real job photos if they exist.
- Set up a Google Business Profile.
