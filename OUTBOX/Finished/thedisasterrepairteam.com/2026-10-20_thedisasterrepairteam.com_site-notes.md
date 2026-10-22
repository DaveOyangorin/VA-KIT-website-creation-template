# thedisasterrepairteam.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **Disaster Repair Team**, Lehi, UT.

**"Check first" is on the outreach list for this business.** Read the warning on the email page before anything is sent.

## Folders and files

- `site/`: the files to put live.
  - All 127 live URLs, with the same canonicals (trailing slash).
  - One new blog post.
  - **Google Analytics 4 G-ZQJHV4JHEF** is kept.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_v3.py`, `p_blog.py`
  - the kit files
  - the styles: `theme.css`, `premium.css`, `concept.css`, `concept.js`
- `2026-10-19_thedisasterrepairteam.com_report.html`: the website plan report.

## Please check first

- **Phone and address don't match Google.**
  - On the site: Northern Utah 385-287-6344 and St. George 435-619-9594; office 45 South 2920 West, Lehi, UT 84043.
  - On Google (report): +1801-515-2257; 441 W Main St Ste E, Lehi, UT 84043.
  - The draft keeps the site's details. Google and the site should match.
- **Kept as the client states them:**
  - Licensed & insured (B-100 General Contractor) and IICRC certified
  - the target 60-minute on-site response
  - over 20 years of experience
  - "4.9 · 120+ Google reviews" (Google currently shows 168)
  - free emergency response planning and free moisture inspections for property teams
- **The report's cost, topic and FAQ data come from foundation searches,** not water damage (reviewer note), so they were not applied. No new foundation pages were made. Ask Angelo for water damage keyword data.

## Photos (important)

- **Most images on the live site are AI-generated.** Several file names end in "-ai", and the rest include the smoke-damage family scene, the man inspecting a ceiling, the commercial crew card, the insulation hero, the foundation inspector, and the blog images. **None are used.**
- **Used:** the client's real job photos: a fire-damaged ceiling above a tub, mold behind removed baseboard, a water-bulged ceiling, wet carpet pulled back, and a mold corner.
- **Not used, flagged:** the truck image, which may be a wrap mockup.
- **Pages without a matching real photo** (foundation, insulation, some commercial pages) use a coloured, photo-free hero.
- **Ask the client for real photos** of jobs, crew and vehicles.

## What was done

- **Text:** the client's own, cleaned: repeated call widgets, star rows and the call bands removed.
- **Report applied:**
  - The home page targets "water damage restoration lehi".
  - Every service page names Lehi in the title, H1 and opening paragraph. Previously no page named Lehi.
  - Every landing page keeps its own city.
- **Meta descriptions:** every page has a unique one. The report said they were missing.
- **QA:**
  - 0 issues across 129 files.
  - No broken images, and no sideways scroll at phone width.
  - The mobile header check passed.

## Design (premium)

- **Research (screenshotted 20 Oct 2026):** SERVPRO, Paul Davis, Linear.
- **Chosen three:**
  - **SERVPRO** (servpro.com): the category's urgency, with water, fire and mold tiles.
  - **Paul Davis** (pauldavis.com): a dark hero with an emergency help panel.
  - **Linear** (linear.app): a dark interface where each state re-colours the page.
- **Concept, "Four kinds of bad day":**
  - Water, fire, smoke and mold each get their own colour: water blue, fire ember, smoke ash and mold green.
  - Every service and city page is themed by its damage type.
- **The signature, the damage-type switcher:** the home hero asks "What happened?". Pick water, fire, smoke or mold and the hero re-colours, cross-fades to that damage's real job photo, and lists the client's own four steps for it.
- **The one-team line:** "separate companies" (dashed, with handoffs) against "Disaster Repair Team" (one solid line that draws in) across the client's four stages: triage, stabilization, insurance and scope, repair and rebuild. It illustrates the client's own "fewer handoffs" point.
- **The rest:** a services bento, a mold-wall parallax band ("Extraction alone is not the finish line"), the two-number areas block, and the FAQ plus request form.
- **Brand guide:**
  - near-black #0E1116
  - call orange #E8542A
  - water #3B9BE0
  - fire #F2682E
  - smoke #9AA0A8
  - mold #6AA84F
- **Fonts:** Archivo Black (display), Instrument Sans (text), JetBrains Mono (labels).
- **Logo:** the client's SVG logo, rendered as an image.

## New blog post (1,128 words)

`/blog/frozen-pipes-utah-winter/`, "Frozen Pipes in a Utah Winter: Prevent Them, Thaw Them, and What to Do When One Bursts".

- **No cannibalizing.** Their six posts don't cover freezing. The new post links to the water damage page, the insurance post and the "what to do immediately" post.
- **Sources (linked):**
  - American Red Cross, "Preventing & Thawing Frozen Pipes": which pipes freeze, prevention, the 55°F setting when away, safe thawing and no open flame.
  - EPA mold guide: dry within 24–48 hours.
- **No coverage promises, no prices.**

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists every page.
- **Schema:**
  - Business node (Lehi address from the site; 24/7; counties served).
  - Breadcrumbs; Service on service and landing pages.
  - FAQPage; BlogPosting.

## Before go-live

- Settle the phone and address with Google.
- Connect the request form.
- Replace the remaining photo-free heroes with real job photos.
- Re-test mobile speed (68 now).
