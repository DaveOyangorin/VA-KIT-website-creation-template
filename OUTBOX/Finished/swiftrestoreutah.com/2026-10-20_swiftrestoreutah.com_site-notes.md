# swiftrestoreutah.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **Swift Restoration and Remodeling**, Ogden, UT.

## Folders and files

- `site/`: the files to put live.
  - Same URLs as the Duda site (no trailing slash) and the same canonicals.
  - Links and assets are root-absolute, so the host must serve folder URLs without adding a slash.
  - **Google Tag Manager GTM-KKGCS6ND** is kept. The `UA-228094282-1` gtag on the live site is injected by the Duda builder, so it isn't carried over. If they rely on it, add GA4 through GTM.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_v3.py`, `p_blog.py`, `mkjobs.py`
  - the kit: `pagekit.py`, `tidy.py`, `engine.py`
  - the styles: `theme.css`, `base.css`, `premium.css`, `concept.css`, `concept.js`
- `2026-10-17_swiftrestoreutah.com_report.html`: the website plan report.

## Please check first

- **NAP** (contact page): Swift Restoration and Remodeling, 2900 Pennsylvania Ave, Unit C, Ogden, UT 84401.
  - (385) 412-8633, 24/7 emergency services. Google writes it +1385-412-8633.
  - Contractor License Numbers 4853926-5501.
- **Two phone numbers.** The live home page's call button says **(385) 402-8536**; everywhere else says (385) 412-8633. The draft uses 412-8633.
- **Rating:** Google shows 4.6 from 179 reviews. It isn't shown until the client confirms it. The live reviews page loads a widget that isn't in the page itself.
- **Kept as the client states them:**
  - locally owned, serving Ogden since 2009
  - "over 13 years of experience in restoration, and over 30 years of experience in construction"
  - IICRC certified (the site shows their IICRC logo)
  - financing through Hearth
- **Left out until confirmed:**
  - "BBB accredited" (on the city pages)
  - any "best / #1" wording
- **The local-guide pages** (Waterfall Canyon Trail, Mount Ogden, the Dinosaur Park, Layton and Ogden parks...) are kept, since they're live URLs with traffic (Waterfall Canyon Trail is 590 searches a month in the report).
  - Their text has errors. For example, the Waterfall Canyon page said the trailhead is "just outside of Park City"; it's in Ogden. That sentence is removed; the rest is kept as written.
  - Worth a fact check before go-live.
- **The free-gift and consumer-report pages** (free carpet cleaning) are kept as the client wrote them. Confirm the offer is still current.

## URLs

- **267 pages rebuilt** (all 266 live pages plus the new post):
  - 36 service pages and guides
  - 20 service-area and local-guide pages
  - 21 case studies
  - 161 restoration-tips posts
  - the root pages
- **One sitemap URL has a double slash** (`/restoration-tips//what-to-do-if-your-basement-floods`). The page is built at the single-slash path, with the live canonical kept.
- **Internal links fixed.** Links on the live site point to URLs that redirect or are broken; the draft links straight to the final page:
  - `/services/mold-removal` → `/services/ogden-mold-removal`
  - `/services/flood-damage-restoration` → `/services/flooded-basement-cleanup`
  - `/services/smoke-damage-repair` → `/services/fire-damage-restoration`
  - `/service-areas/layton-ut` → `/service-areas/water-damage-layton-ut`
  - `/water-heater-burst` → `/restoration-tips/water-heater-burst`
  - `/contact-us` → `/contact`
  - …and 10 more in `pages.py` (`REMAP`).
  - Two targets are **404 on the live site**:
    - `/restoration-tips/how-to-clean-up-water-after-an-appliance-leak` (now links to the appliance-leak page)
    - `/restoration-tips/how-to-detect-water-damage-in-your-ogden-home-before-it-s-too-late` (now links to the tips index)
- **Images.** The blog's older posts reuse a pool of the client's job photos instead of each post's own image, so the preview fits the preview host's file cap. `site/` uses the same images.

## What was done

- **Text:** the client's own, cleaned:
  - The Duda builder split sentences and headings around links ("What Are Common Causes of Water Dam / ge"); those are re-joined.
  - Builder labels ("Blog Layout", "Updated On:", "Author:") are removed.
  - Dates and authors are kept as bylines.
- **Report applied:**
  - The home page targets "water damage restoration ogden" in the title, H1 and first sentence.
  - Every service page names Ogden in its title, H1 and opening paragraph.
  - City and guide pages keep their own text.
- **QA:** 0 issues across 268 pages.
  - Many titles and descriptions sit outside 50–60 and 150–160 characters, mostly the 161 blog posts, left close to the client's wording.
  - The mobile header check passed.
- **Speed:** the live site scored 52/100 on mobile. The draft is plain HTML with WebP photos at 150 KB or less and lazy-loading; re-test after go-live.

## Design (premium)

- **Research (screenshotted 20 Oct 2026):** Belfor, Paul Davis, ServPro, ServiceMaster Restore (blocked), PuroClean (blocked), Normandy Remodeling, Case Design (blocked), Bluestem Remodeling. Chosen three:
  - **Belfor** (belfor.com): black ground, a red diagonal cut, urgent heavy type.
  - **Paul Davis** (pauldavis.com): dark hero with an emergency phone panel.
  - **Bluestem Remodeling** (bluestemremodeling.com): editorial serif italics over finished interiors.
- **Concept, "From flood to finish".** Swift does both halves: emergency restoration and the rebuild and remodel. The site tells that arc with their own photos:
  - **Hero:** a near-black hero with a flame-red diagonal slash and a water-blue edge (the logo's fire and water), two tilted job prints ("Day 1 · drying" and "Finished"), and a 24/7 phone panel.
  - **Marquee** of services.
  - **The recovery timeline**, the signature. A pinned horizontal scroll: scrolling down moves the job sideways from the call to extract and dry, contain, open up, rebuild, and finish, with a progress bar. On phones it becomes a swipe row.
  - **Split section:** restoration as a dark emergency list, remodeling as an editorial serif grid.
  - **A before/after drag slider** of a bedroom remodel.
  - **A bento of case studies**, an owner split with Darin Jenks, and FAQs and tips.
- **Inner pages:** full-bleed job-photo headers.
- **Brand guide** (from the logo):
  - flame red-orange #F0531C (buttons, white text passes at this size)
  - water blue #2F7FD6 and aqua #5FBED2
  - near-black #0A1220 and bone #F6F3EE
- **Fonts:** Plus Jakarta Sans (display and text), Fraunces italic (editorial accent), DM Mono (labels).
- **Motion:** reveals, the timeline, a marquee and photo hover; all off with reduced motion, where the timeline becomes a plain swipe row.

## New blog post (1,057 words)

`/restoration-tips/home-fire-safety-checklist-northern-utah-winters`, "A Home Fire Safety Checklist for Northern Utah Winters".

- **Main phrase:** "home fire safety checklist" (informational, prevention). None of the 161 posts covers smoke alarms, heating or escape basics.
- **No cannibalizing.** It links to fire damage restoration, board-up, odor removal and reconstruction without competing with them.
- **Sources (linked):** U.S. Fire Administration (FEMA):
  - Smoke alarms: placement, monthly tests, yearly batteries, 10-year replacement.
  - Heating fire safety: 3-ft clearance; heating the second leading cause of home fires in 2021; portable heaters 41% of fatal heating fires, 2017–2019.
- No prices. Byline "Swift Restoration and Remodeling". **[[NEEDS: author, e.g. Darin Jenks]]**

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists every page.
- **Schema:**
  - Business node: founding date 2009, founder Darin Jenks, open 24/7, areas.
  - Breadcrumbs; Service on service and city pages.
  - FAQPage where a page has one.
  - BlogPosting on posts (author and date where the post had them).

## Before go-live

- Connect the quote form.
- Add GA4 through GTM if needed.
- Re-test speed.
- Fact-check the local-guide pages.
