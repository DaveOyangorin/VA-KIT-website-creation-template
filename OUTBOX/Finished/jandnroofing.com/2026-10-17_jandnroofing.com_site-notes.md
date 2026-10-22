# jandnroofing.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live. Client: **J & N Roofing Maintenance, LLC**, West Valley City, UT. Testimonials name the owner as Norm.

- `site/`: the files to put live. It has the same URLs and canonicals as today for every page J & N wrote. The current site has no tracking code, so there's nothing to carry over.
- `preview/`: the private review copy. Forms are off and there's a draft strip on top. It opens on the review page, and the site itself is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `overrides.py`, `p_home.py`, `p_blog.py`, `extract.py`, `imgprep.py`, `qa.py`, `post_classes.json`).
- `2026-10-17_jandnroofing.com_copied-posts.txt`: **the 411 copied posts** (see below).
- `2026-10-17_jandnroofing.com_report.html`: the website plan report.

## ⚠ Please decide first: 411 copied blog posts

The report counted 488 pages. **411 of the 452 blog posts were not written by J & N.** They're articles copied from goodshomedesign.com in 2015–2016: crochet patterns, Easter crafts, log cabins, dog houses, aquariums and the like. That's also where the report's odd "solar powered e bike" keyword came from.

How we know:
- Their images are hotlinked from `cdn.goodshomedesign.com`.
- Their Amazon links carry **another site's affiliate tag** (`goodshcom-20`), so any affiliate money from them goes to that site, not to J & N.
- Their text matches the original articles.

Why this matters:
- Republishing someone else's articles risks copyright complaints.
- Hundreds of off-topic pages dilute what Google thinks the site is about (roofing in West Valley City).

**What the draft does:** those 411 posts are **not rebuilt**. Everything J & N actually wrote is rebuilt on the same URLs:
- 41 roofing posts
- 29 pages
- 5 testimonials
- 2 category archives

The full list of copied URLs is in `2026-10-17_jandnroofing.com_copied-posts.txt`.

**Angelo's decision:** when the new site goes live, the copied URLs should return **410 Gone** (recommended: it tells Google they were removed on purpose), or be kept as they are with noindex. Either way, nothing is redirected to roofing pages, because that would look manipulative. They can be added back to the build if the client insists.

Separately, the report flags that the domain doesn't obviously match "J & N Roofing Maintenance LLC". Everything on the site (name, phone, logo) is J & N's, so it's the right site.

## What was done

- **79 pages:**
  - All of J & N's own pages and posts, on their current URLs and canonicals.
  - The new blog post and a 404 page.
- **Report applied: West Valley City.**
  - The home page title, H1 and first sentence target "roofing company West Valley City".
  - All 11 service pages, plus services and about, now have West Valley City in the title, H1 and an opening answer paragraph (`_build/overrides.py`).
  - Before, the services only mentioned the Salt Lake City metro.
- **Meta descriptions:** hand-written for the home page, service pages, the new post and the main pages. The remaining posts use a description taken from each page's own first paragraph.
- **References page privacy.** The live References page lists private homeowners by name **with their personal phone numbers**. The draft keeps the names and business references but holds back every phone number, with "available on request". **Please confirm with the client** whether those people agreed to be listed with their numbers.
- **Testimonial privacy.** One testimonial's title and URL include the customer's street address ("1216 Tierney Cir. Sandy"). The URL is kept (same-URL rule), but the page now shows "Benn Hayden – Sandy, UT". Consider a redirect to a cleaner URL later.
- **Broken and redirecting links fixed:**
  - `/services-2/...`, `/roofing-repairs/`, `/roof-ventilation/`, `/new-construction/` and `/gutter-cleaning/` now point straight at the `/services/...` pages.
  - The 404 links to `/financing/` and `/services-2/` were removed or repointed.
  - Links from J & N posts into copied posts were unlinked.
- **Noindex (kept on their URLs, left out of the sitemap):** `thank-you/` and `search-archives-template/`, a WordPress template that listed every post, including the copied ones.
- **Images:**
  - 101 WebP images, all under 150 KB, all from jandnroofing.com.
  - Most of J & N's photos (the gallery, sliders and posts) look like **stock photography**: perfect suburban roofs, posed roofers, a "happy family". They're kept where the client placed them, but **heroes only use house and roof shots, never people who could pass for the crew**.
  - **Please ask the client for real job photos.**
- **QA:**
  - 0 issues: valid JSON-LD, one H1 per page, no broken links.
  - Every image has width, height and alt text.
  - No sideways scrolling at 390 px or 1440 px, and 0 broken images.
  - 31 titles and 36 metas are outside the ideal length. They're mostly the client's own post titles, kept as is.

## Design direction

- **References** (screenshots in the working files):
  - This Old House (thisoldhouse.com): an editorial serif voice for home maintenance.
  - iFixit (ifixit.com): guides as clear cards, "Never take broken for an answer".
  - Basecamp (basecamp.com): a plain-spoken letter from the company.
  - Patagonia Worn Wear blocked the screenshot and wasn't used.
- **Idea, "the roof maintenance handbook":** "Roofing Maintenance" is in the company's name, so the site reads like a well-made home-maintenance publication:
  - services presented as "chapters"
  - a "roof maintenance handbook" block linking the new post, the glossary, the FAQ and the warranty page
  - a **note from the J & N team**, written only from statements on the client's own pages (pride in the work, explaining roof pitch and ventilation, often recommending a repair instead of a new roof). It's signed with the logo, not a personal name.
- **Colors:** the logo's brush-script red `#d6212b`, near-black `#0f1114` and the site's teal `#148ba9`, on warm paper.
- **Fonts:** Newsreader (serif) for headings, Work Sans for text, and Courier Prime for typewritten labels.
- **Redesign (v2, 18 Oct 2026):** the first draft looked too plain, so the handbook idea now runs the whole site:
  - The home page opens like a magazine cover. Next to the H1 is **Fig. 1, an original line drawing of the parts of a roof**: ridge vent, shingles, underlayment, deck, flashing, drip edge, gutter and soffit vents, each numbered and explained.
  - Since J & N's photos look like stock, the home page leads with type and the drawing rather than a stock hero.
  - Services are a numbered table of contents. The guides sit on a bookshelf, and the letter from the team is a taped paper note.
  - The client's real discounts ($70 / $130 / $200 with a GAF system) are dashed tear-off coupons, and the reviews are big serif pull quotes.
  - Inner pages open with an editorial header and the photo as a captioned "plate".

## Claims used from the client's own pages: please confirm

- **GAF certified roofing contractor; GAF System Plus Warranty.** The warranty page also names a GAF representative with a phone number. It's kept on that page as the client wrote it; confirm it's current.
- **Special offers:**
  - $70 off a complete re-shingle over an existing roof
  - $130 off a tear-off and re-shingle
  - $200 off a tear-off, re-sheath and re-shingle
  - All of these apply with a GAF system and warranty. Are they still current?
- **Hours and support line:** 7am–5pm Monday–Friday, and a 24-hour support line at (801) 949-7845.
- **Training:** "technicians, managers and foremen all go through regular yearly training".
- **Years in business are not used anywhere.** The site says "20 years", "over twenty years", "27 years", "over 27 years" and "over 30 years" on different pages.
- **Address:** 3842 S 2200 W, West Valley City, UT 84119, from the Google profile. The current site doesn't show a street address. It's now in the footer and schema. **Please confirm it should be public.**

## New blog post (1,164 words)

"How Far Should Shingles Overhang the Drip Edge?", at `how-far-should-shingles-overhang-the-drip-edge/`. That's the same root-level URL pattern as their other posts.

- **Why this topic:** it ties to J & N's own warranty page, which gives the shingle manufacturer's 1/4-inch overhang guidance and warns that water rolls back under shingles without it.
- **Main keyword:** "how far should shingles overhang the drip edge".
- **Not targeted, to avoid cannibalization:**
  - "roofing company west valley city" (home).
  - Roof repair and replacement (service pages).
  - The many "roofing salt lake city" posts.
- **Sources (all opened and read):**
  - ARMA (Asphalt Roofing Manufacturers Association), "Installation of Drip Edge at Eaves and Rakes", 6 May 2025. It gives the 1/4"–3/4" overhang for L-shaped drip edge, trimmed flush for T/D-shaped edges, 3/8"–1" with no drip edge, the underlayment order, and nails every 8–10".
  - City of Pacific, Missouri, "2018 IRC Section R905 Requirements" (Ordinance 3181, 7 April 2020). It quotes IRC R905.2.8.5 word for word: drip edge required at eaves and rakes, 2" laps, at least 1/4" below the sheathing and 2" onto the deck, fasteners at most 12" apart, underlayment over the drip edge at eaves and under it at rakes.
  - International Code Council, 21 July 2023: Utah adopted the 2021 IRC, effective 1 July 2023.
  - J & N's own warranty support page.
- **First choice dropped:** a post on "What does the GAF System Plus warranty cover?". GAF's site blocks automated access to its warranty documents, and the topic wasn't written on third-party copies.
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:**
  - Everything is open, including AI search bots.
  - `/wp-admin/` and internal search are blocked.
  - Points to `sitemap.xml`.
  - The copied posts are not blocked in robots.txt. A 410 is the cleaner way to remove them (see above).
- **sitemap.xml:** 76 indexable URLs. The noindex pages, the 404 page and all copied posts are left out.
- **Schema:**
  - RoofingContractor with address, phone, email, the Facebook and Yelp profiles, and an emergency contact point for the 24-hour line.
  - Service on service pages, plus BlogPosting, FAQPage (only where the questions are visible), AboutPage, ContactPage, CollectionPage, BreadcrumbList, and DefinedTermSet on the glossary.

## Problems found on the current site

- **The 411 copied posts** (see the top of these notes).
- **Keyword cannibalization in J & N's own posts.** 36 of the 41 roofing posts are near-duplicate "roofing salt lake city" pages competing with each other. Some even have "-2" versions (`roofing-company-salt-lake-city/` and `-2/`, `roofing-salt-lake-city-ut/` and `-2/`, `salt-lake-city-roofing-contractors/` and `-2/`). Suggest merging them into a few strong pages with redirects. **Angelo decides.**
- **Private phone numbers** on the References page (see above).
- **Contradicting years in business** (see above).
- **Outdated wording:** the home page says the team trains to "2020 roofing standards". That wasn't carried over.
- **Broken links** to `/financing/` and `/services-2/` (fixed in the draft).

## Questions for the client (via Angelo)

1. Should the 411 copied posts get a 410 (recommended) or be noindexed? (Angelo first.)
2. How many years has J & N been in business?
3. Did the people on the References page agree to having their phone numbers published?
4. Should the street address (3842 S 2200 W) be shown on the site?
5. Are the $70 / $130 / $200 special offers still current? Is the GAF representative listed on the warranty page still correct?
6. Can you send real job photos, ideally with the city for each?
7. Is it OK to show 5 stars from 9 Google reviews?
8. Should the near-duplicate "roofing salt lake city" posts be merged? (Angelo decides.)
9. Do you work in Salt Lake City, South Jordan, Sandy and Draper, with recent jobs there to mention? Can you share real prices?
