# ezroofingnow.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live. Client: **EZ Roofing**, with locations in Salt Lake City, UT and Cabot, AR. The legal name is EZ Contracting LLC.

- `site/`: the files to put live. It has the same URLs and canonicals as today (`https://ezroofingnow.com/...`, no www), and keeps all the tracking (see below).
- `preview/`: the private review copy. It has no tracking, forms are off, and there's a draft strip on top. It opens on the review page, and the site itself is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `p_home.py`, `p_blog.py`, `extract.py`, `imgprep.py`, `qa.py`).
- `2026-10-17_ezroofingnow.com_report.html`: the website plan report.

## What was done

- **All 251 live URLs rebuilt in the new design, plus 2 new pages:** the new blog post and a 404 page. That's 253 in total. Every canonical points to itself, as it does today. The live pages are:
  - Home.
  - 30 Utah pages (12 Salt Lake City service pages, 17 city pages, and the Utah hub).
  - 89 Arkansas pages.
  - 79 blog posts.
  - 10 projects.
  - The team pages.
  - The about, process, financing and legal pages.
- **Report applied:**
  - The home page title, H1 and first sentence target "roofing company Salt Lake City" (title: "Roofing Company Salt Lake City | EZ Roofing Utah & Arkansas").
  - The 12 Salt Lake City service pages already have Salt Lake City in their titles and H1s. Those were kept.
- **Name fix:** 6 Salt Lake City pages call the company **"EZ Roofing Arkansas"** in their titles and copy. They are the roof repair, roof replacement, residential, commercial and free inspection pages, plus the Salt Lake City city page. All now say "EZ Roofing".
- **Meta descriptions:** 35 pages had none.
  - The home page, the new post and the index pages got hand-written ones.
  - The rest (mostly blog posts) use a description taken from the page's own first paragraph.
- **Images:**
  - 222 local WebP files, all under 150 KB, all from ezroofingnow.com.
  - **15 stock photos of models were removed** (workers in hard hats, door and window installers, a gutter cleaner) so nothing poses as EZ's crew.
  - Heroes on Utah pages only use Utah projects (King and Salkordeh in Sandy, Mackerel in Draper, Shotorbani in Holladay, Waldron in Woods Cross). Arkansas pages only use Arkansas projects.
  - No AI images.
- **Noindex (kept on their URLs, left out of the sitemap):**
  - `home-test/` and `schedule-a-inspection-test/`: test copies of live pages.
  - The 8 team-member pages under `team/`, which on the live site show only a name. The real bios are on "Meet Our Team".
  - **Please confirm**, since this changes how they're indexed today.
- **QA:**
  - 0 issues: valid JSON-LD, one H1 per page, no broken links.
  - Every image has width, height and alt text.
  - No sideways scrolling at 390 px or 1440 px, and 0 broken images.
  - 173 titles and 193 metas are outside the ideal length. They're the client's own text, kept as is to avoid changing 200+ rankings at once. The home page, the new post and the index pages are within range.

## Tracking (live build only)

Everything below was copied from the live site and is in `_build/tracking_head.html`:
- Google tag GT-WR9QTC5.
- GA4 G-5157FJ55BP.
- Google Ads AW-11175312295.
- Meta Pixel 196172105641169.
- **CallRail** (company 330669320).

CallRail swaps the phone numbers on the live site. That's why visitors see extra 501 numbers, such as (501) 462-5661 in the header and (501) 462-2976. The pages print the base numbers from the footer: Utah (888) 575-3025 and Arkansas (501) 691-4283. CallRail keeps swapping them on the live build. The preview has no tracking, so it shows the base numbers.

## Design direction

- **References** (screenshots in the working files):
  - Owens Corning roofing (owenscorning.com): the layered "Total Protection Roofing System". EZ is an Owens Corning Preferred Contractor.
  - Malarkey Roofing Products (malarkeyroofing.com): the split-photo hero and a spec row of real numbers.
  - CertainTeed roofing (certainteed.com/roofing): a bold photo hero with a dark overlay.
- **Idea, "the property evaluation":** EZ leads with a free, in-person evaluation of the roof, soffit, fascia, gutters, windows and siding. It's a 26-point inspection, per their process page. The hero shows that checklist as an evaluation sheet. The **EZ Shield Roofing System** gets the same checklist treatment, with its seven components exactly as the about page lists them:
  - synthetic felt
  - ice & water barrier
  - full perimeter drip edge
  - real starter strip
  - 6-nail pattern rated for 130 MPH
  - hail-resistant ridge cap
  - flashing at walls and penetrations
- **Spec row (all from their site):**
  - Founded in 2017.
  - 5-year workmanship warranty and extended 25-year warranties.
  - $2M insurance policy.
  - BBB A+.
- **Colors:** brand maroon `#681214` (from the current site), warm charcoal, and amber as the action color.
- **Fonts:** Archivo (condensed) for headings, Source Sans 3 for text.
- Redesign (v2, 18 Oct 2026): "the property evaluation". Archivo condensed + Source Sans 3; maroon/charcoal/amber. Transparent header over a drone hero, clipboard evaluation sheet that ticks in, spec band (2017, 5–25 yr, $2M policy, A+), sticky stacking EZ Shield cards, scanning drone photo, state photo cards, crew band, single review as a pull quote. The logo is white, so it sits on dark with no chip.

## New blog post (1,423 words)

"The Best Time of Year to Replace a Roof in Utah", at `best-time-of-year-to-replace-a-roof-in-utah/`. Like their other posts, it sits at the site root.

- **Main keyword:** best time of year to replace a roof. It also answers a real Google question from the report: "What time of year is the cheapest to replace a roof?"
- **Not targeted, to avoid cannibalization:**
  - "roofing company salt lake city" (home).
  - "roof replacement salt lake city" (its service page, which is linked).
  - "free roof inspection" (`our-free-inspection/`).
  - None of their 79 existing posts covers roof timing. The winter care and replacement-signs posts are linked, not repeated.
- **Sources (both opened and checked):**
  - NOAA NCEI 1991–2020 monthly climate normals for Salt Lake City International Airport, station USW00024127. This is the official data file (https://www.ncei.noaa.gov/data/normals-monthly/1991-2020/access/USW00024127.csv). The month-by-month table uses its highs, lows, snowfall and number of days at 40°F or warmer.
  - Owens Corning Technical Bulletin TB-10022497-A, "Cold Weather Shingle Installation", April 2026 (https://www.owenscorning.com/dms/10022497). It covers the 40°F threshold, sun-activated sealant, hand sealing with ASTM D4586 cement, and the 1/16-inch end-joint gap.
- **No seasonal price claim.** No reliable Utah data was found, and the post says so.
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.
- **Author** is "EZ Roofing". `[[NEEDS: author name, e.g. Brian Stephens, if the client wants one]]`

## robots.txt, sitemap, schema

- **robots.txt:**
  - Everything is open, including AI search bots.
  - `/wp-admin/` and internal search are blocked.
  - Test and team pages use noindex instead of a block, so Google can read the tag.
- **sitemap.xml:** 242 indexable URLs. The noindex pages and the 404 page are left out.
- **Schema:**
  - An Organization (EZ Roofing, legal name EZ Contracting LLC, founded 2017) with two RoofingContractor locations: Utah and Arkansas, each with its full address, phone and daily 9:00–5:00 hours.
  - Utah pages point their Service schema at the Utah location, and Arkansas pages at the Arkansas location.
  - BlogPosting on every post.
  - CollectionPage on the index pages.
  - FAQPage only where the questions are visible.
  - BreadcrumbList on all pages.

## Problems found on the current site

- **Wrong company name on Utah pages.** "EZ Roofing Arkansas" appears on 6 Salt Lake City pages (see above).
- **Home page vs Salt Lake City city page.** `utah-city/salt-lake-city/` has the H1 "Roofing Company in Salt Lake City, Utah" and repeats the home page's content. Both now compete for "roofing company salt lake city". Option: merge it into the home page with a redirect, or rewrite it as a Salt Lake City hub. **Angelo decides.**
- **Templated city pages.** All 17 Utah city pages have the same 474 words, and the 20 Arkansas city pages share 404 words. Google may treat them as duplicates. They need real local jobs and photos from the client.
- **Two commercial pages compete:** `commercial-roofing-services/` and `commercial-roof/` (the report says merge). Both are kept until Angelo approves a redirect.
- **Two blog index pages:** `blog/` (the WordPress posts page) and `ez-roofing-blog/`. Both are kept. Consider redirecting one to the other.
- **Rating claim.** The home page says "5 star Google rating", but the Google profile shows 4.7 from 51 reviews. The claim is left off.
- **Old address.** The $25 gift-card promo page (`25free/`) shows an old Cabot address, 2225 Bill Foster Memorial Hwy W, #B. The footer and contact page say 13 Nalley Road, #C. The page is kept, flagged.
- **Broken items:**
  - A link to `/arkansas-city/conway/` redirects (fixed to the real Conway page).
  - 3 blog screenshots return 404 (dropped).
- **Contact page wording.** It calls Cabot "Headquarters". The new contact page keeps that.

## Questions for the client (via Angelo)

1. Which business name should the site show: "EZ Roofing", "EZ Roofing Utah" for Utah pages, or "EZ Contracting LLC"?
2. Should Utah keep the toll-free (888) 575-3025, or is there a local 801 number? (The report suggests a local number.)
3. Is it OK to show 4.7 stars from 51 reviews instead of "5 star Google rating"?
4. Should "commercial roofing" and "commercial roof" be merged, and should the Salt Lake City city page be merged into the home page? (Angelo first.)
5. What is the pre-cast concrete page for? Is it a service you offer?
6. Which state is license #0428111225 for?
7. Can the $25 promo page with the old address be retired?
8. Can you send real local jobs and photos for the city pages?
9. Who should be named as the blog author?
