# m3industriesconcrete.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **M3 Industries**, concrete contractor, St. George, UT.

**"Check first" is on the outreach list, and the report found no Google profile at all.** Read the warning before outreach. Without a profile they can't show in map results (a Google profile job).

## Folders and files

- `site/`: the files to put live.
  - All 37 live URLs, with the same canonicals (Wix, no trailing slash).
  - One new post under `/post/`.
  - **Google Analytics 4 G-RM58WGPQMM** is kept.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_v3.py`, `p_blog.py`
  - the kit files
  - the styles: `theme.css`, `premium.css`, `concept.css`, `concept.js`
- `2026-10-19_m3industriesconcrete.com_report.html`: the website plan report.

## Please check first (important)

- **The live contact page is still the Wix template.**
  - It shows "500 Terry Francine St., San Francisco, CA", "123-456-7890" and "info@mysite.com", and some page footers repeat it.
  - The draft uses the client's real details from their own service pages everywhere: **(435) 701-0081**, **m3industriesconcrete@gmail.com** and **2570 South 3430 East, St. George, UT**.
- **Experience:** the home page meta says "25+ yrs", the foundation pages say "over 20 years", and a counter says "25+ Years". The draft uses "20+ years". Confirm.
- **Not shown:**
  - the "5.0, Based on Google Reviews" block, because no Google profile was found
  - the "200+ Projects" and "5-star average" counters
- **Reviews:** three of the four named customer quotes on the site (Scott Later, Tom Penne, Amy Adams) are shown verbatim, labelled "St. George, UT", with no Google label. One mentions "Merrill and his crew". Is Merrill the owner?
- **Coatings:** NexaNano SiO2 is kept as the sealer they use. These absolute product claims were left out until confirmed: "100% Oil & Stain Proof", "permanent hydrophobic barrier" and "protects … for a decade".
- **Report items:**
  - the cost, topic and FAQ parts come from foundation searches, so they were not used
  - concrete lifting is the biggest gap. No page was invented.

## Photos (important)

- **Many images on the live site look AI-generated:** red-rock scenes with workers, cleaning photos stamped with the M3 logo, patio and walkway renders, a dump truck scene and water-bead close-ups. **None are used.**
- **Used:** the client's own phone-camera job photos:
  - footings and forms in red dirt, a pour crew screeding, slabs at new homes
  - driveways, a stained driveway and steps, a retaining wall, sidewalk forms
- **Ask the client for more real photos,** especially of coatings and stamped work.

## What was done

- **Text:** the client's own, cleaned:
  - Wix booking junk ("1 hr", "1 US dollar") removed
  - typos fixed ("Craftsmenship", "commericial")
  - template placeholders removed
- **Report applied:**
  - The home page targets "concrete coatings st george" alongside their general concrete work.
  - Every service page names St. George in the title, H1 and opening line.
- **Speed (48/100 now):** plain HTML instead of Wix, with WebP photos. Re-test after go-live.
- **QA:**
  - 0 real issues across 39 files. The one QA flag is the home canonical without a trailing slash, which matches live.
  - The mobile header check passed.

## Design (premium)

- **Research (screenshotted 20 Oct 2026):** Holcim, The Concrete Collective, Hilti (shot today for Poly-Lift). CEMEX was behind a security check.
- **Chosen three:**
  - **Holcim** (holcim.com): a photo-tiled grid on dark navy.
  - **The Concrete Collective** (concretecollective.com.au): a photo hero and a dark services band.
  - **Hilti** (hilti.com): industrial tiles with one hard accent colour.
- **Concept, "From red dirt to finished slab":**
  - **Hero:** a full-bleed pour-crew hero ("Concrete coatings and concrete work in St. George, poured right from the dirt up") with a "20+ years" stamp, and an orange stencil marquee.
  - **The signature, the exploded slab:** an isometric slab with five layers (native red dirt, compacted base, steel, the pour, finish and seal). The layers separate as you scroll, each with the client's own job photo and their own words about it ("We don't cut corners underground…").
  - **The rest:** a services photo grid, a work mosaic, a reviews band, the FAQ plus estimate form, and blog cards.
- **Brand guide:**
  - charcoal #1F2326
  - the client's logo orange #F08C1E
  - red dirt #B4552D
  - concrete greys
- **Fonts:** Anton (stencil-like display), Work Sans (text), IBM Plex Mono (labels).
- **Logo:** the client's M3 square mark.

## New blog post (1,058 words)

`/post/concrete-silica-dust-diy`, "Cutting or Grinding Concrete Yourself? Read This About Silica Dust First".

- **No cannibalizing.** None of their 12 posts covers silica. It links to repairs, coatings and driveways.
- **Sources (linked), all OSHA:**
  - "Silica, Crystalline": what it is, the tasks that create it, 2.3 million workers exposed, and the diseases linked to it
  - "Health Effects": scar tissue, no cure for silicosis
  - "Construction": Table 1, the exposure control plan, a competent person, housekeeping limits, and "applying water to a saw blade … substantially reduces the amount of dust"
- **It's clear the OSHA rules cover employers, not homeowners.**
- **Topics tried first and dropped:** Utah problem soils and St. George retaining-wall permits. Those official sources (Utah Geological Survey, the St. George municipal code) were unreachable from here, so they weren't used.

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists every page.
- **Schema:**
  - Business node (the client's real address and phone; areas).
  - Breadcrumbs; Service on service pages.
  - FAQPage; BlogPosting.

## Before go-live

- Fix the contact details on Google and anywhere the template shows.
- Confirm years of experience and the reviews.
- Connect the estimate form.
- Re-test mobile speed.
- Set up a Google Business Profile.
