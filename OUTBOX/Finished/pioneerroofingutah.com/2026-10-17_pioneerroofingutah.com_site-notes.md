# pioneerroofingutah.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live. Client: **Pioneer Roofing Co**, Salt Lake City, UT. The logo says "Est. 1980".

- `site/`: the files to put live. It has the same URLs and canonicals as today, and keeps the tracking (see below).
- `preview/`: the private review copy. It has no tracking, forms are off, and there's a draft strip on top. It opens on the review page, and the site itself is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `overrides.py`, `p_home.py`, `p_blog.py`, `extract.py`, `imgprep.py`, `qa.py`).
- `2026-10-17_pioneerroofingutah.com_report.html`: the website plan report.

## What was done

- **All 50 live pages rebuilt in the new design, plus 2 new pages:** the new blog post and a 404 page. That's 52 in total. Every canonical points to itself, as it does today. The live pages are:
  - Home.
  - 9 service and roof-type pages.
  - Pricing, the estimator and the booking page.
  - 25 city pages and the areas index.
  - 5 blog posts and the blog index.
  - About, certification and warranty, gallery, contact and privacy.
- **Report applied: Salt Lake City.** The home page title, H1 and first sentence target "roofing company Salt Lake City". The 10 main service pages now name Salt Lake City in the title, H1 and an opening answer paragraph (`_build/overrides.py`): roof repair, inspections, residential, commercial, asphalt shingles, TPO, metal, roofing types, services and pricing. Before, only 1 of 51 pages named Salt Lake City.
- **Real prices used.** The client's pricing page lists real price ranges for a typical 2,000 sq. ft. home over the last 12 months.
  - Asphalt replacement: $9,100–$12,600 (straightforward) and $13,400–$16,600 (complex or premium).
  - TPO: $13,100–$16,300.
  - Repairs: $250–$1,000 (basic) and $1,100–$2,000 (advanced).
  - These now appear on the home page and in the service cards. The pricing page targets "roof replacement cost Salt Lake City", the report's cost page.
- **Meta descriptions:** 45 of the 50 pages had none.
  - The home page, the 10 service pages and the new post got hand-written ones.
  - The rest (city pages, posts and the like) use a description taken from the page's own first paragraph.
- **Widgets kept on the live build:**
  - The Roofr instant estimator (iframe) on `new-roof-estimator/`.
  - The TidyCal booking calendar (`mason2/roof-inspection`) on `book-inspection/`.
  - The preview shows a notice with a link instead, because artifacts can't load other sites.
- **Reviews:** 3 real reviews quoted on the current site (Rob Schoenfield, Peter Gabriel, Rodrigo Navarro), copied word for word. The 4.8 stars / 175 reviews from Google is **not** shown yet. The report says to wait for the client's OK.
- **Owner photo:** the client's own photo file is named "John and Linda Stout". It's captioned that way in the "Your call goes straight to John" section. **Please confirm the names.**
- **Images:**
  - 47 local WebP photos, all from pioneerroofingutah.com, all under 150 KB. 15 of the gallery photos were hidden in the page CSS and are now real images.
  - **7 Pexels stock scenery photos were removed.**
  - 3 review avatars return 404 on the live site and were dropped.
  - No AI images.
- **Noindex (kept on their URLs, left out of the sitemap):** `thank-you/` (the form confirmation page) and `home-2/`, an old copy of the home page.
- **Broken link:** "Careers" on the About page goes to `/careers/`, which is a 404. The link was removed.
- **QA:**
  - 0 issues: valid JSON-LD, one H1 per page, no broken links.
  - Every image has width, height and alt text.
  - No sideways scrolling at 390 px or 1440 px, and 0 broken images.
  - 35 titles and 17 metas are outside the ideal length. They're mostly city pages, kept as the client wrote them. The home page, service pages and new post are within range.

## Tracking (live build only)

All of it was copied from the live site into `_build/tracking_head.html` and `tracking_body.html`:
- Google Tag Manager GTM-TDBZVKP.
- Microsoft Clarity (xujyteuckh).
- The Podium chat widget.

## Design direction

- **References** (screenshots in the working files):
  - Carhartt (carhartt.com): "Built to work. Built to last. Since 1889." Heritage told with a founding year and bold condensed type.
  - Filson (filson.com): dark photo tiles with condensed labels.
  - Red Wing Heritage (redwingheritage.com): numbered heritage product cards.
- **Idea, "built like workwear":** a family roofing company since 1980, so the site borrows from heritage trade brands:
  - an "Est. 1980" hexagon seal (from the logo's own hexagon shape)
  - numbered spec cards for each roof type, with the client's real prices
  - a warm canvas-textured background
  - hexagon markers on labels
- **"Call John" section:** a big section about the service line going straight to the owner. That's the client's strongest real differentiator: "No recordings or outsourced answering services, guaranteed".
- **Colors:** brand orange `#f36d36` and deep brown `#1c0d0a`, both from the current site and logo.
- **Fonts:** Big Shoulders Display (condensed, close to the logo's lettering) for headings, and Karla for text. Karla is the body font on their current site.
- **Redesign (v2, 18 Oct 2026):** the first draft looked too plain, so the workwear idea now carries the whole site:
  - The home page opens full-screen on their own commercial roof photo, with heavy condensed type, a huge outlined "1980" and a slowly turning hexagon "Est. 1980" seal.
  - The key facts are stitched orange patches.
  - **The four roof types are hang tags**, each carrying the client's real published price range.
  - The price table is styled as a ledger, and the owner photo is a print in the "Your call goes straight to John" section.
  - Gallery tiles have a slight warm tone, every page gets a full-bleed photo hero, and the footer reads "Built to work. Built to last. Since 1980." 

## New blog post (1,306 words)

"What Is the 25% Rule for Roofing? (And Does It Apply in Utah?)", at `blog-what-is-the-25-percent-rule-for-roofing/`. That's the same `blog-…` URL pattern as their other posts.

- **Main keyword:** "25% rule roofing". It's a real Google question from the report, which marked it "check Utah rules".
- **Not targeted, to avoid cannibalization:**
  - "roofing company salt lake city" (home).
  - "roof repair salt lake city" (`roofing-repairs/`).
  - Roof replacement, roof inspection.
  - Their existing posts on repair-or-replace and how often to replace a roof. Those are linked, not repeated.
- **Sources (all opened and checked):**
  - Florida Building Commission staff analysis DS 2020-022, quoting Section 706.1.1 of the 2017 Florida Building Code, Existing Building. It contains the actual 25% wording.
  - Florida SB 4-D (2022), enrolled text. Section 1 adds s. 553.844(5) of the Florida Statutes, effective 26 May 2022. Under it, roofs built to the 2007 code or later only need the repaired part brought to code.
  - International Code Council, 21 July 2023: Utah adopted the 2021 IBC, IRC (specific provisions) and IEBC, effective 1 July 2023.
  - West Point City, Utah: its re-roof permit application. It asks for the type of work, the number of existing layers, and the contractor's Utah license number.
  - Town of Firestone, Colorado: its reroof checklist quoting IRC R908.3.1.1. Two or more existing layers means a full tear-off. (The Utah legislature and ICC code sites block automated reading, so the IRC wording comes through this city checklist.)
- **What the post concludes:** the 25% rule is Florida's, and no equivalent statewide rule was found in Utah's adopted codes. It does **not** claim no local rule exists anywhere; it tells readers to check with their city.
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:**
  - Everything is open, including AI search bots.
  - The client's own 20-second crawl delay is kept. Google ignores it; Bing honors it.
  - `/wp-admin/` and `/elementor-hf/` are blocked.
  - Points to `sitemap.xml`.
- **sitemap.xml:** 49 indexable URLs. The noindex pages, the 404 page and the Elementor template are left out.
- **Schema:**
  - An Organization (Pioneer Roofing, legal name Pioneer Roofing Co, founded 1980, with the Facebook page) with two RoofingContractor locations: Salt Lake City (7041 S 2700 E) and Price (106 N 4th E).
  - Service schema on service and city pages, plus BlogPosting, FAQPage (only where visible), AboutPage, ContactPage, CollectionPage and BreadcrumbList.

## Problems found on the current site

- **Years in business contradict:**
  - "nearly 40 years" on the asphalt and metal pages
  - "over 40 years" on home, repairs and commercial
  - "For 45 years" on residential
  - "45+ years in business" on home
  - The logo says "Est. 1980" (46 years). The new copy says "since 1980". Please confirm.
- **Two warranty versions:**
  - The home page says "Pioneer Lifetime Warranties … 10–20 years on flat roofs, 40 years on shingles".
  - The certification page says "lifetime warranty for materials … 10 year labor warranty".
  - The new site uses only the second (10-year labor + lifetime materials). Please confirm which is current.
- **TPO price copy error.** On the pricing page, the TPO range repeats the steep-pitch description written for complex asphalt roofs ("steep pitch, dormers, valleys…"). The description is left off in the new version. The client should supply the right one.
- **Two commercial pages compete:** `commercial-roofing/` and `your-go-to-solution-for-commercial-roofing-needs/`. Both are kept until Angelo approves a redirect.
- **Roof repair vs roofing repairs.** The report flags these as one topic. The site has a single page, `roofing-repairs/`, which now targets "roof repair Salt Lake City".
- **Reviews:** the home page says "Over 100 5 Star reviews on Google". Google shows 4.8 stars from 175. That's not wrong, but confirm before quoting a number.
- **Price address.** The footer shows "106 N 4th E" and the contact map shows "106 N 400 E". It's the same place, written two ways. The site keeps "106 N 4th E" as the footer has it.
- **License number** 287685-5501 is shown on the certification page and is kept there.

## Questions for the client (via Angelo)

1. Should the site say "since 1980" everywhere? Is that right?
2. Which warranty wording is current?
3. Is it OK to show 4.8 stars from 175 Google reviews?
4. Is the phone format OK as (801) 943-7663? (The Google profile shows +1801-943-7663.)
5. Is it OK to caption the owner photo "John and Linda Stout"?
6. Should the two commercial roofing pages be merged? (Angelo decides on the redirect.)
7. What's the correct description for the TPO price range?
8. Do you work in South Jordan, Sandy and Draper, and are there recent jobs there to mention? Do you have project photos with the city for each job?
9. Who should be named as the blog author?
