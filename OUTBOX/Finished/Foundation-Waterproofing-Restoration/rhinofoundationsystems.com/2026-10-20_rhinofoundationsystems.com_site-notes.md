# rhinofoundationsystems.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **Rhino Foundation Systems**, American Fork, UT (serves all of Utah).

## Read this first: where the content came from

- **The live site can't be reached from our network.** The connection times out, which looks like an IP block. Both a plain fetch and a browser failed.
- **So every page was rebuilt from the Internet Archive's captures of July to September 2025:**
  - 30 pages: the site's page sitemap plus the main nav
  - 3 service-area hub URLs that are in the sitemap but were never captured, rebuilt as simple link hubs
- **The report (5 Oct 2026) counts 96 pages, so the site has grown since September 2025.** Pages added after that aren't in this draft.
- **Best fix:** ask the client for the current page list or a site export, then add the missing pages before go-live.

## Folders and files

- `site/`: the files to put live.
  - 35 pages at the same URLs and canonicals as the archived site (trailing slash).
  - A new blog post at `/blog/radon-foundation-cracks/`.
  - Google Tag Manager GTM-PKK38W6K is kept as on the live site.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_r.py`, `p_blog.py`
  - the kit files
  - `theme.css`, `concept.css`, `concept.js`
  - the archived pages in `src/`
- `2026-10-19_rhinofoundationsystems.com_report.html`: the website plan report.

## Please check first

- **Phone and address:**
  - The site shows **801-509-5344** (used everywhere) and office@rhinofoundationsystems.com.
  - A quote banner also shows 801-492-3503.
  - The Google profile (report) says **+1435-660-5182** and **35 Barratt Ave, American Fork, UT 84003**.
  - The site shows no street address, so none is shown. **Ask which phone is main, and whether to show the address.**
- **Reviews:** 4.7 stars from 290 (Google, per the report). **Not shown as a number** until the client confirms.
- **Left out until the client can back them up:**
  - "over 40 years", "Trusted since 1985"
  - "thousands of customers/projects", "hundreds of 5-star reviews"
  - "certified", warranties
  - "no subcontractors", "Utah's leading" / "a leading"
  - the named-family "case studies" on the American Fork and Alpine pages
- **Kept as the client states it:** "licensed and insured"; free consultations and estimates.
- **Testimonials:** the three on the site, quoted word for word with the names and towns shown there.
- **A copy-paste error on the live site was dropped:** the "Advantages of Helical Piers" section opened with a paragraph about crawl space encapsulation.
- **Ad landing pages:** the 4 landing pages (basement, concrete repair, Vuba Stone, leveling-2) keep their URLs and forms, but are set to noindex and left out of the sitemap.
- **Report applied:**
  - The home page targets "foundation repair american fork" in the title, H1 and first sentence.
  - Service pages keep their own Salt Lake City titles, as on the site.
  - American Fork now appears on the home page and the city pages.

## Photos

- **Only the client's own photos are used:**
  - the branded Rhino truck at a job
  - helical piers on a crate
  - an excavator driving push piers
  - a finished basement waterproofing install
  - tape-measured slab lips
  - a settled sidewalk
  - two crack photos used as warning-sign examples, not presented as Rhino jobs
- **Not used:** the live site's stock files (Depositphotos, Adobe "240_F", iStock, product renders, cartoon illustrations).
- **Logo:** the site's own white rhino logo, plus a black version made from it.

## Design (premium)

- **Research (screenshotted 20 Oct 2026):** Rivian, STIHL, Carhartt. Caterpillar, YETI, John Deere and Ram blocked the screenshot.
- **Chosen three:**
  - **Rivian** (rivian.com): oversized type on a quiet ground, one hero object.
  - **STIHL** (stihlusa.com): one hard brand colour over working photography.
  - **Carhartt** (carhartt.com): rugged and plain-spoken.
- **Concept, "Down to solid ground":** a rhino doesn't move, and neither should a foundation. Rhino's own pages explain how clay, silt, sand and loam behave under a house, and that helical piers anchor below the frost line.
- **Signature, "Drive the pier":**
  - A drawn section through the ground under a settling house, with a crack in the wall.
  - Drag the depth gauge and a helical pier goes down through loam, silt, clay and sand. Each layer reads back Rhino's own description of that soil.
  - Past the frost line the status turns to "Bearing, level", the house rotates back to level and the crack closes.
  - It plays once when scrolled into view (not for visitors who choose reduced motion). It's labelled as an illustration.
- **The rest:**
  - a dark hero with the real truck photo framed by a depth ruler
  - a Rhino-blue proof band
  - the warning signs as a numbered list
  - a services mosaic with their photos
  - a commercial split with the push-pier job
  - an editorial testimonial row
  - a county-by-county service area grid
  - a FAQ, the quote form, and a soil-strata stripe above the footer
- **Brand guide:**
  - Rhino blue #1478A2 (their banners), navy #0D1620, bone paper #F1EEE8
  - soil strata: loam #4B3A2B, silt #A38C6B, clay #9A5B3E, sand #D4BF92, bearing #59606A
- **Fonts:** Archivo at full width (display), Public Sans (text), JetBrains Mono (readouts).

## New blog post (1,230 words)

`/blog/radon-foundation-cracks/`, "Radon and Foundation Cracks: What Utah Homeowners Should Know".

- **No cannibalizing.** No page covers radon. The post links to foundation repair, basement waterproofing and crawl space encapsulation.
- **It does not claim Rhino tests for or mitigates radon.** It tells readers to test, and points to the EPA's guidance.
- **Sources (linked, all U.S. EPA):**
  - "What is Radon?": it enters through cracks and gaps.
  - "What is EPA's Action Level for Radon": 4 pCi/L action level; consider fixing from 2 to 4; 1.3 indoor and 0.4 outdoor averages.
  - "Health Risk of Radon": number one cause of lung cancer in non-smokers; about 21,000 deaths a year, about 2,900 among people who never smoked; the 2005 Surgeon General advisory.
- **No Utah radon statistics** (the state sources couldn't be reached to check). **No prices.**

## QA

- 0 issues across 35 pages.
- No broken images, and no sideways scroll at phone width.
- The mobile header and menu check passed.
- No JavaScript errors.

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists every indexable page (landing pages excluded).
- **Schema:**
  - Business node (phone, email, areas served; no street address)
  - Breadcrumbs; Service on service and city pages
  - FAQPage; BlogPosting

## Before go-live

- Get the current page list and add the missing pages.
- Confirm the phone, address and claims.
- Connect the forms.
