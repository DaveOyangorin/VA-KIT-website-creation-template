# jsprofinish.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **JS ProFinish**, a basement finishing contractor in Clearfield, UT.

## Folders and files

- `site/`: the files to put live.
  - Same URLs and canonicals (no trailing slash, as on the live Next.js site), plus a new `/blog`.
  - **The Google Ads tag AW-17847227430 is kept**, as on the live site.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_v3.py`, `p_blog.py`
  - the kit files
  - the styles: `theme.css`, `premium.css`, `concept.css`, `concept.js`
- `2026-10-17_jsprofinish.com_report.html`: the website plan report.

## Please check first (important)

- **The report is about a different business.**
  - The report's Google profile is "Vista Concrete Construction", 2650 Liberty Ave, Ogden, +1385-644-6281, a concrete contractor with 5 stars from 45 reviews. The report itself asks you to confirm the site.
  - Everything on jsprofinish.com says **JS ProFinish**, 1740 S 300 W #8, Clearfield, UT 84015, (385) 626-3514, jsprofinish@gmail.com, owner Pablo J. Padilla, UT Lic. #11152584-5501.
  - **The draft uses only the site's own facts.** Nothing from the Vista profile is used.
- **Report keywords.**
  - Because the keyword set was pulled for the other business, the home page keeps the client's own target, "basement finishing" in Northern Utah, and names Ogden in the first sentence.
  - The report's "bathroom remodeling ogden" home target, and its French drain, foundation repair and water damage gaps, were not built. Ask before building any of them.
- **Safe parts of the report that were applied:** every service page names Ogden in its title, H1 and first paragraph.
- **Rating.** The live site states "4.8 out of 5 from 18 Google reviews, as of September 2026". The draft shows it the same way, with the date. Confirm it is still current.
- **Reviews.** The three quotes are the ones already on the live site, with the reviewers' names: Ash Roberts, Robert Hansen (shortened, as on the site) and Garret Atkin.
- **Kept as the client states them:**
  - the cost ranges and their HomeAdvisor and Angi sources
  - the 6 to 12 week timelines
  - the license classes
  - "flooring by others" on the Clinton job

## Photos

- **All 61 photos are the client's own job photos**, taken from the live site, with the client's own alt text.
- **No stock and no AI images.**

## What was done

- **Text:** the client's own, cleaned:
  - Next.js comment splits fixed ("ZIP code s", stray spaces before commas)
  - author and "Updated September 2026" lines rebuilt
  - gallery and project sections rebuilt from the page structure
- **Links:** the site used relative links, and all of them are kept and resolve.
- **QA:**
  - 28 files: 27 pages plus the 404.
  - 0 broken internal links, 0 broken images, and no sideways scroll at phone width.
  - The mobile header check passed.
  - The one QA flag is the home canonical without a trailing slash, which matches the live site.

## Design (premium)

- **Research (screenshotted 20 Oct 2026):** Hammer & Hand, Normandy Remodeling, The Basement Sanctuary, Sun Design, Wilson Construction, Board & Vellum. Chosen three:
  - **Hammer & Hand** (hammerandhand.com): craft photography with labelled image tiles.
  - **Sun Design** (sundesigninc.com): a warm editorial serif and "a home like yours" room cards.
  - **The Basement Sanctuary** (finishedbasementcompany.com): the basement category's own leader, built on finished-room photography.
- **Concept, "Bare studs to finished":**
  - **Asymmetric hero:** on a drywall-paper ground, the finished family room photo with a taped "where every job starts" print of bare studs overlapping it, a pencil arrow, and the rating card.
  - **A tape-measure marquee** of the trades.
  - **The signature: the "same room" scrubber.** The client photographed the same rooms from the same spot on three visits. Drag the tape measure, or let it play once, to cross-fade drywall hung, then taped and textured, then finished. Only the two rooms the client itself paired are used.
  - **Trades index:** numbered rows with a photo preview that follows the hover.
  - **Tilted room cards** in a snap-scroll row.
  - **A parallax quote band:** the inspector praising the framing.
  - **The rest of the page:** a big 4.8 review block, three steps joined by a chalk line that draws in, the cost guide card, the owner split, both counties, and the FAQ plus estimate form with the client's own fields.
- **Inner pages:**
  - Photo heroes, with each page's own job photos as a strip.
  - A Clinton project card.
  - Cost tiers as cards.
  - A filterable gallery.
  - The Clinton page has the scrubber, a "who did what" block and all 18 stage photos.
- **Brand guide:**
  - drywall white #F4F2EE
  - joint-compound grey #E8E4DC
  - charcoal ink #1D1A17
  - framing-lumber pine #C17A3A
  - tape-measure yellow #E9C547
  - chalk-line blue #2F5D8A
- **Fonts:** Bricolage Grotesque (display and text), Newsreader italic (accents), JetBrains Mono (tape labels).
- **Logo:** the live site's text logo ("JS ProFinish" with an underline) recreated as an image.
- **Reduced motion:** respected. There is no autoplay, no parallax, and the chalk line is drawn statically.

## New blog post (1,150 words)

`/blog/basement-egress-window-requirements-utah`, "Basement Bedroom Egress Windows in Utah: The Code in Plain English".

- **Main phrase:** "basement egress window requirements" (informational).
- **No cannibalizing.** No page targets it. The post links to the cost guide, basement remodeling, Ogden and Layton.
- **Sources:**
  - Murray City "Basement Finish Permit" checklist, updated 9/16/2024 (linked).
  - Utah's adoption of the 2021 IRC (Utah Code Title 15A).
- **Facts used:**
  - the 5.7 sq ft opening, at least 24 in high and 20 in wide, with the sill no more than 44 in above the floor
  - window wells of 9 sq ft and 36 in wide, with a ladder when deeper than 44 in, and a 36 in path under decks
  - bedrooms of 70 sq ft and 7 ft in any direction
  - ceilings of 7 ft, 6 ft 8 in and 6 ft 4 in
  - interconnected smoke and CO alarms
- **The post tells readers to confirm with their own city.** No prices.
- **[[NEEDS: author]]** The post is credited to the business. Ask whether Pablo wants his name on it, as on his other guides.

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists every page.
- **Schema:**
  - Business node (HomeAndConstructionBusiness + GeneralContractor; Clearfield address; hours; founder; areas).
  - Breadcrumbs; Service on service, city and county pages.
  - FAQPage; BlogPosting.

## Before go-live

- Confirm with Angelo that this is the right business and site.
- Connect the estimate form.
- Confirm the rating text.
- Re-test mobile speed. The live site scores 99, so keep it above 90.
