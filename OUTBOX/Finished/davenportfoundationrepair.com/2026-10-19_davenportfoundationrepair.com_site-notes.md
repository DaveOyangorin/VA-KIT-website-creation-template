# davenportfoundationrepair.com redesign: notes for Angelo

Draft, 19 Oct 2026. Nothing is live. Client: **Davenport Foundation Repair**, West Jordan, UT.

- `site/`: the files to put live. Same URLs as today, each page a `.html` file (`/sump-pump/system.html`), with the same canonicals. **Google Tag Manager (GTM-KTXCTXQ) kept** in the head. The GTM `<noscript>` iframe after `<body>` is not in the draft; add it back on go-live if they want it. The manufacturer spec PDFs are copied to the same path (`/core/pdf/`).
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off. The preview leaves out the 60 individual team-bio pages because the preview host caps one preview at 511 files. In the preview, their links go to the team page. `site/` has them all.
- `_build/`: the source (`build.py`, `cfg.py`, `pages.py`, `p_blog.py`, `illus.py`, `engine.py`, `migrate.py`, `clean.py`, `qa.py`); old pages are in `_build/src/raw/`.
- `2026-10-19_davenportfoundationrepair.com_redirects.csv`: the redirect list (see below).
- `2026-10-17_davenportfoundationrepair.com_report.html`: the website plan report.

## ⚠ Please check first

- **Two phone numbers.** The site's header and call buttons use **1-801-569-2302** (probably a tracking line). The location block uses **1-801-429-9989**, the number on the Google profile. The draft keeps the same split: 569-2302 for calls to action, 429-9989 in the address and schema. Ask the client which should be the main number.
- **NAP:** Davenport Foundation Repair, 9427 S 6400 W, West Jordan, UT 84081 (copied exactly).
- **Rating:** Google shows 4.8 from 1,473 reviews; the site's review widget shows 4.9 from 617. Neither number is shown until the client confirms one.
- **Claims left out until confirmed:**
  - "100% Customer Satisfaction"
  - "Best place to work for over 600 employees" (mission statement)
  - "the best cast-iron sump pumps and longest-lasting battery backup pumps"
  - "the largest waterproofing network in the world"
  - "Lifetime Sealant"
  - any "best" wording
- **Kept as the client states them:**
  - 30 years in business, locally owned and operated, led by owner Ron Davenport.
  - Certified Foundation Supportworks dealer and Basement Systems dealer.
  - Written warranties and free inspections.
  - The team list and the 2017 awards page (A Rated, HomeAdvisor Elite Service, BBB A rating; dated, so confirm they're current).
  - Note: the team page mentions a "Regional Controller" and "West Region" staff, so check whether the company now belongs to a larger group.
- **Photos.** Most of the big product photos on the current site come from the Basement Systems / Supportworks network library, not from Davenport's jobs. The draft uses none of them. It uses **36 of the client's own job photos** from their gallery uploads, captioned with the town and job as the client captioned them (Grantsville, Morgan, Lehi, Vernal, Ogden, Draper and more), plus their truck and team photo. More own photos would help, especially at higher resolution.

## Redirects (important for go-live)

The live site is a CMS with far more URLs than its sitemap lists. The draft rebuilds **514 pages**:
- all 115 sitemap pages;
- all 100 blog posts and the 5 blog index pages;
- 294 more pages the site links to: case studies, team bios, 65 city pages, technical papers, galleries, review and testimonial listings.

**Not rebuilt:** the deeper single-item pages the CMS generates: individual reviews (about 600, per the review count), single photos, before/after items, testimonials and videos.
- **In the draft,** links to them point to their listing page.
- **The CSV** lists the 146 item URLs our pages link to, with where each should go. There are more item URLs that nothing in the draft links to. Angelo should either keep the CMS serving those item pages or 301 them to the matching listing page (for example `/about-us/reviews/*` → `/about-us/reviews.html`).
- **42 rebuilt pages** had a live canonical pointing at a duplicate copy under another section that isn't rebuilt (for example a case study filed under both `/about-us/case-studies/` and `/foundation-repair/case-studies/`). They are now self-canonical; the CSV lists those too.

## What was done

- **Pages that keep the client's own text:** all 514, cleaned of menus, gallery widgets and repeated "Get a FREE Quote!" lines.
- **Pages with the same canonical as live:** all except the 42 above, including the 3 pages that canonical to another page, which also stay out of the sitemap.
- **Report applied:**
  - The home page targets "foundation repair west jordan" in the title, H1 and first sentence.
  - Every service page names West Jordan in its title, H1 and opening paragraph; on detail pages the opening paragraph is the page's own description plus "based in West Jordan".
  - Every page has a description.
  - **Speed:** the live site scored 40/100 on mobile. The draft is plain HTML with WebP photos at 160 KB or less and lazy-loading, so re-test after go-live.
- **Mobile:** the live home page scrolls sideways on phones (421 px wide on a 390 px screen). The draft has no sideways scrolling, and the phone header and menu passed the mobile check.
- **QA:** 0 issues across 514 pages: one H1 each, canonicals, valid JSON-LD, no broken links, image sizes and alt text.
  - About 127 titles fall a few characters under 50, and 135 descriptions sit outside 150–160 characters. These are mostly single blog, review, team and gallery item pages, left close to the client's own wording.

## Design (premium, site-specific)

- **Concept, "Below grade":** foundation repair happens where nobody looks, so the site draws it. Every section has an original engineer's cross-section: grade line, soil layers, depth in feet, the house wall and footing, and the repair (push piers, wall anchors, interior drainage and sump, crawl space jacks and liner, slab lifting, helical piles).
- **Home hero:** a whole-house section with five numbered problem spots (settling, bowing wall, wet basement, sinking concrete, wall crack). Each spot links to the matching page.
- **Their own detail:** a "job file" grid of their phone photos captioned with real Utah towns.
- **References:** geotechnical boring logs and section sheets (depth ticks, soil layers, mono labels); Caterpillar and Hilti product pages (industrial yellow on black, condensed type); field notebooks.
- **Colours:** Davenport's logo yellow and near-black, drafting paper, soil ochres.
- **Fonts:** Big Shoulders Display (display), Manrope (text), Spline Sans Mono (labels).

## New blog post (1,063 words)

`/about-us/our-blog/collapsible-soils-in-utah-why-homes-settle.html`, "Collapsible Soils in Utah: Why Some Homes Settle When the Ground Gets Wet". The client's own posts use numbered URLs from their CMS; this one uses a plain slug.

- **Main phrase:** "collapsible soils utah" (informational). Search volume: not in our data. None of their 100 posts covers it and it targets no service keyword. It links to the settlement, push pier, downspout extension and concrete leveling pages.
- **Sources (linked):** all from the Utah Geological Survey:
  - the Problem Soils page;
  - the Survey Notes article "Protecting Utah Homes From Geologic Hazards";
  - Special Study 127 (up to 10% settlement on first wetting, St. George–Hurricane area).
- No prices. Byline "Davenport Foundation Repair". [[NEEDS: author]]

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists 504 URLs (the pages that canonical elsewhere are left out). A rebuilt HTML `/sitemap.html` lists every page.
- **Schema:**
  - Business node (name, address, phone 1-801-429-9989, owner, cities, social profiles) on every page.
  - Breadcrumb on inner pages; Service on service pages.
  - BlogPosting on posts, with author and date where the post had them.
  - FAQPage on the home page and the new post.

## Before go-live

- Connect the estimate and schedule forms to the client's handler.
- Set up the redirects above.
- Re-test mobile speed (aim for 90+).
