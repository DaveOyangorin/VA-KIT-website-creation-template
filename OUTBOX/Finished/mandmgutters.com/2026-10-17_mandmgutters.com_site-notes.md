# mandmgutters.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live.

**Client:** M&M Gutters & Exteriors
- 290 S Redwood Rd Suite B, Salt Lake City, UT 84104
- 801.280.2222, shown as the site shows it
- info@mandmgutters.com
- Mon–Fri 8am–5pm
- Owner: Nate Nuttall

**Folders:**
- `site/`: the files to put live.
  - All **183 URLs** of the current WordPress (Divi) site are rebuilt on the same addresses and canonicals, with trailing slashes as today.
  - **All the client's tracking is kept:**
    - GA4 `G-CF0E9ETG68`
    - Google Tag Manager `GTM-57KVKWJJ` and `GTM-KBLHRZ3`. These load the Google Ads tag `AW-1000898368`, the second GA4 property and CallRail.
    - the Podium chat widget
    - two Universal Analytics IDs (see below)
- `preview/`: the private review copy. Forms are off, there's no tracking, and there's a draft strip on top. It opens on the review page, and the site is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `overrides.py`, `p_blog.py`, `extract.py`, `imgprep.py`, `qa.py`, `style.css`, `site.js`, `robots.txt`, `extract.json`).
- `2026-10-17_mandmgutters.com_report.html`: the website plan report.

## ⚠ The site is much bigger than the report says

The report's audit found 36 pages. The site has **183**: 160 blog posts, 12 service pages and the company pages.
- The server blocks plain crawlers (curl gets no answer), which is probably why the audit missed most of it.
- We crawled it in a real browser, one page at a time with a pause between requests, and rebuilt everything.

## Please decide (Angelo)

1. **Five posts target a competitor's brand, "Leaf Guard":**
   - `is-leaf-guard-a-scam-or-a-solution/`, which mentions a class action settlement
   - `getting-a-hold-of-leaf-guard-support-fast/`
   - `why-the-leaf-guard-warranty-is-a-homeowners-best-friend/`
   - `the-best-leaf-guard-utah-reviews-and-services/`
   - `from-yelp-to-reddit-unbiased-reviews-of-gutter-leaf-guards/`

   They're kept as written on their URLs, but brand-targeting content like this carries trademark and defamation risk. Worth a review.
2. **Universal Analytics:** two UA IDs (`UA-53892206-6`, `UA-131026571-1`) are still in the code. Google stopped UA data collection in 2024, so they do nothing. They're kept as found and can be removed.

## What was done

- **185 pages:** the 183 existing URLs, a new blog post and a 404 page.
- **Report applied: Salt Lake City.**
  - The home page title, H1 and first sentence target "gutter installation Salt Lake City".
  - Every service page has Salt Lake City in the title, H1 and an opening answer paragraph (`_build/overrides.py`).
- **Meta descriptions:**
  - 18 pages had none.
  - The home, service and company pages now have hand-written ones.
  - Posts keep their own description, or use their first paragraph if they had none.
- **Service pages:**
  - The client's own copy is kept, cleaned of page-builder leftovers (button labels, empty blocks, an all-caps title repeat).
  - Each has a new hero, an opening answer, side panels, FAQs where facts allow, and the "path of the water" service line.
- **Blog:** all 160 posts are rebuilt with their own text, dates and author ("Nathan Nuttall" or the company). The blog index is grouped by topic, with counts.
- **Old internal links fixed:**
  - 55 old or mistyped link targets in all: links to `/roofing-2/`, `/siding/`, `/windows-2/`, `/soffit-fascia/`, `/rain-gutters/` and `/about-us/`, 33 posts linked without their `/blog/` prefix, 8 service pages linked without `/services/`, and three mistyped post URLs.
  - These redirect or break today. All now point straight at the real page.
- **Images:**
  - 108 WebP files, all M&M's own job photos: finished homes, copper and seamless gutters, heat cable, soffit and fascia, siding, windows.
  - **Not used:** Unsplash stock (hotlinked), Pixabay-style stock, Shutterstock files, 145 Bannerbear auto-generated banners, icons, partner logos and badges, and a HOVER 3D render.
  - 6 images were already broken (404) on the live site.
- **Reviews:** the site shows a Google review widget, not written reviews. The site says 413 reviews and the report says 427, so no count or stars are shown until the client confirms. Two quotes from staff on the about page are used.
- **QA:**
  - 0 issues on both builds: valid JSON-LD, one H1 per page, canonicals, no broken links, and every image has width, height and alt text.
  - 12 pages screenshotted at 390 px and 1440 px, with no sideways scrolling and 0 broken images.
  - Many post titles are the client's own and are longer than 60 characters; they're kept as is.

## Design direction

- **References** (screenshots in the working files):
  - RHEINZINK (rheinzink.com): roof, façade and drainage presented as one system, with wide tracked uppercase type.
  - Marvin (marvin.com): hairline-ruled collection lists.
  - James Hardie (jameshardie.com): material swatch cards.
- **Idea, "the path of the water":** M&M started with gutters and now does the whole exterior.
  - Water runs off the roof, past the heat cable, into the gutters, behind the fascia and down the siding. Every one of those is an M&M service.
  - So the services are drawn as one vertical water line, from roof to ground, on the home page, the service pages and the menu.
  - This backs up the client's own pitch: one company instead of juggling several contractors.
- **Redesign (v2, 17 Oct 2026):** the first draft looked too plain, so it was rebuilt around the photos and the idea:
  - The home page opens full-width on their bay-window job photo, with a spec sheet (K-style 5″ & 6″, copper · aluminum · steel, formed on site, small homes in 2–6 hours).
  - **"The path of the water" is now a drawing:** a section through a house's eave, with rain running down the roof, past the heat cable, into the gutter and down the downspout. The eight numbered points are the eight services and light up with the list beside them.
  - Material cards (copper, 5″ or 6″, heat cable), a large project gallery, a full-width winter band on ice dams, a 1990 → 2005 → 2010 → today timeline, and big staff quotes.
  - The service pages show where each service sits on the path ("03 of 08", with previous and next). The blog posts have a contents list, reading time and an editorial layout.
  - **36 of the client's photos had page-builder frames baked into the file** (black borders, orange and blue corner blocks). The frames are trimmed off so only the photo shows.
- **Colors:** taken from the logo: orange `#f5a83b` and sky blue `#00a6e5`, on deep navy, with warm paper neutrals and copper as a material accent.
- **Fonts:** Archivo (expanded widths for headings), Instrument Serif italic for accent lines, and IBM Plex Mono for spec labels.

## Claims used from the client's own pages: please confirm

- Started in 1990.
- Nate Nuttall joined in 2005 and bought the business in 2010.
- Family-owned; residential and commercial.
- Copper, aluminum and steel gutters; seamless gutters made on site; 5-inch and 6-inch K-style.
- Most small homes done in 2–6 hours; gutter cleaning from $150.
- HOVER 3D models.
- **Financing on approved credit:** 0% for 12 months, 2.99% for 12 years, 7.99% for 10 years, "15 financing options". **Are these current?**
- **The gutter page's own figures** ("basement flooding damage of up to $6,241", "foundation repairs of up to $7,921") are kept as the client wrote them, but no source is given. Consider removing them or citing one.
- **Badges** on the old site (BBB A+, GAF Certified, Owens Corning Preferred Contractor, HomeAdvisor Elite and Top Rated) aren't shown in the draft. Confirm which are current before adding them back.
- **Small inconsistency:** the about page says Nate started "over 16 years ago", but its history section says 2005.

## New blog post (1,109 words)

"5-Inch vs. 6-Inch Gutters: Which Size Does Your Home Need?", at `/blog/5-inch-vs-6-inch-gutters/`.

- **Why this topic:**
  - None of the 160 existing posts covers gutter sizing.
  - M&M's own gutter page says 5-inch is their standard and 6-inch is available.
  - It shows the sizing method with Salt Lake City's real rainfall data.
- **Main keyword:** "5 inch vs 6 inch gutters".
- **Not targeted, to avoid cannibalization:**
  - "gutter installation salt lake city" (home).
  - The rain gutter service page.
  - The existing gutter cost posts.
- **Sources (opened and read):**
  - NOAA Atlas 14 Precipitation Frequency Data Server, queried for downtown Salt Lake City (40.761, −111.891). The 5-minute intensity is 1.90 in/hr for a 2-year storm, 3.23 for 10-year, 4.28 for 25-year and 6.46 for 100-year.
  - This Old House, "How To Size Gutters and Downspouts" (Thomas Baker, updated 20 Apr 2026): pitch factors; capacities of 5,520 / 7,960 adjusted sq ft for 5" / 6" K-style and 2,500 / 3,840 for half-round; downspout rules; two outlets on runs of 60 ft or more.
- **Worked examples:** two of them, with arithmetic that's been checked.
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:** everything open, including AI search bots; `/wp-admin/` and `/wp-login.php` blocked; points to the sitemap.
- **sitemap.xml:** 184 URLs (everything except the 404), with each post's modified date.
- **Schema:**
  - HomeAndConstructionBusiness / RoofingContractor with address, phone, email, hours, founding year 1990, the owner and the six counties.
  - Service, FAQPage (visible questions only), BlogPosting (with author), Blog and BreadcrumbList.

## Before go-live (developer)

- The quote and contact forms keep the same fields (name, email, phone), and need a form handler.
- Check that GTM still fires the Google Ads and CallRail tags on the new pages. They're loaded through the two GTM containers.
- Keep `/wp-content/uploads/` reachable for a while if other sites link to old images, or redirect them.

## Questions for the client (via Angelo)

1. Is it OK to show 4.8 stars from 427 Google reviews? The site says 413.
2. Do you do roof repair and metal roofing? They're the biggest keywords in the report, and there's no page for them yet.
3. Are the financing rates current?
4. Which badges are current: BBB A+, GAF Certified, Owens Corning Preferred, HomeAdvisor Elite?
5. Can we remove the two retired Universal Analytics tags?
6. Should the five "Leaf Guard" brand posts be kept? (Angelo decides.)
7. Is there a source for the $6,241 and $7,921 figures on the gutter page?
