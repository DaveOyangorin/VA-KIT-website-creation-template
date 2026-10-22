# jordanriverroofing.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live.

**Client:** Jordan River Roofing
- 1278 W Kimman Lane, Taylorsville, UT 84123
- 801-857-1417
- phil@jordanriverroofing.com
- Owner: Phil (Philip Jordan, per the site's own schema)

**Folders:**
- `site/`: the files to put live.
  - Every one of the current site's **92 URLs** is rebuilt at the same address: `/about`, `/services/new-roof-replacement/sandy` and so on, with no trailing slash, as today.
  - Each URL is a folder with an `index.html`, and links are root-relative.
  - **The host must serve `/about` from `about/index.html` without forcing a trailing slash.** Netlify, Cloudflare Pages and most static hosts do this.
  - There's no tracking code on the current site to carry over.
- `preview/`: the private review copy. Forms are off, there's a draft strip on top, and it opens on the review page. The site itself is at `home/`.
- `_build/`: the source:
  - `build.py`, `pages.py`, `p_blog.py`, `imgprep.py`, `qa.py`
  - `style.css`, `site.js`, `robots.txt`
  - `client_text.json`: the old site's city paragraphs and legal text
- `2026-10-17_jordanriverroofing.com_report.html`: the website plan report.

## ⚠ The biggest problem: Google sees one page, not 92

The current site is a **single-page React app**, built on GoHighLevel's AI site builder ("vibe"). That explains the report's "the audit found 0 pages".

- Every URL returns the same empty HTML shell.
- All the content is drawn by JavaScript.
- Every page has the same title and the same meta description.
- Every page has **`canonical="/"`**, which tells Google that all 92 pages are copies of the home page.
- `sitemap.xml` also returns the app shell, so there's no real sitemap.

**The new site** is plain HTML. Every page has its own title, description and canonical, and there's a real `sitemap.xml`.

## ⚠ Please decide: the 65 service × city pages

The site has a page for every service in every city: 5 services × 13 cities, for example `/services/roof-repairs-maintenance/sandy`.

- They're **doorway pages**: about 75–77% identical once the city name is swapped.
- They're filled with AI-written local copy ("canyon wind gusts", "valley temperature inversions").
- Some of that copy is **wrong**. The commercial TPO pages say they're backed by the TAMKO DiamondShield warranty, which is a shingle warranty, and some promise "the strongest warranty in Utah".

**What the draft does:**
- All 65 URLs still exist, so nothing breaks.
- Each is now a short, honest page that links to the full service page and the city page.
- Each has a **canonical pointing to its main service page**, and none are in the sitemap.

**Angelo decides:** keep them like this, or 301-redirect them to the main service pages later. The 13 city pages under `/service-areas/` are kept as real, indexable pages.

## Numbers and claims on the old site that contradict each other (not used)

- **Years:**
  - The about page and the schema say **founded in 2019**. Phil had "over a decade" in roofing before that.
  - Other pages say "**Since 2003**", "**20+ years**", "for over two decades" and "**over 15 years**".
  - The draft uses only "founded in 2019".
- **Rating:**
  - The home page says "4.9★ average rating".
  - The report has **4.8 from 48** Google reviews.
  - No rating is shown until the client confirms.
- **Unverifiable stats:** "5,000+ roofs completed", "500+ roofs repaired", "98% satisfaction rate", "thousands of homeowners", "A+ rated", "100% leak-free guarantee", "30% HVAC reduction". None are used.
- **24/7 / same-day emergency service** and "we respond within one business hour" (the contact page says "one business day"). Not used, per the report: claim 24/7 only if the client confirms.
- **BBB accredited:** no BBB listing for Jordan River Roofing came up in a search. Not used.
- **GAF, CertainTeed and Owens Corning "certified partner" logos:** not used. The site's own warranty and about pages only describe **TAMKO**.
- **Hours:** the header and schema say Mon–Fri 8–6, Sat 8–4. The contact page says Mon–Fri 7–6. The header hours are used.
- **Gallery captions** name cities, such as "Commercial Roof System — Salt Lake City", that don't match the photos (that one is a house). The new captions describe what's in each photo, with no cities.

## What was done

- **94 pages:** the 92 existing URLs, a new blog post and a 404 page.
- **Report applied: Taylorsville.**
  - The home page title, H1 and first sentence target "roofing company Taylorsville".
  - All 5 service pages have Taylorsville in the title, H1 and opening paragraph.
- **Service pages rewritten.** The old ones were AI filler with contradicting numbers. The new ones use only facts the site agrees on, plus plain explanations:
  - the service bullet lists
  - free inspections with photo reports
  - itemized estimates
  - the 4-step process
  - adjuster meetings
  - details from customers' own reviews, such as a tear-off done in 1.5 days, and a leak fixed the next day during a home sale
- **The warranty page** was checked against **TAMKO's own Edge contractor program brochure**:
  - DiamondShield gives 25 years of workmanship coverage and a 50-year Full Start period.
  - It needs Titan XT or StormFighter FLEX shingles and 4 TAMKO accessories, and the roof must be a full tear-off or new installation.
  - It's transferable once within 20 years.
  - Note: the old site said "StormFighter"; TAMKO's product name is **StormFighter FLEX**.
- **Reviews:** the 13 reviews from the home page, word for word, with no stars added.
- **Images:**
  - Only the **7 clearly real job photos** are used: the company truck, tear-offs on a Tudor and a Victorian, a finished roof, the truck and trailer, and the yard banner.
  - **⚠ The wide crew-and-truck banner photo is no longer used.** Looking closely at it, the lettering on the truck and trailer is garbled ("sorlcecinsoafrrenring.com") and the phone number on the truck is wrong. Both are typical of an AI-generated or AI-altered image. The truck in it is also a different model from the one in the client's other photos. Please ask the client whether it's a real photo.
  - **23 of the old site's 36 images look AI-generated.** They're the 1376×768 and 1200×896 pictures on the service and city pages, with idealized mountain scenery. **None are used.**
  - The other 5 files are logos.
  - **Please ask the client for more real photos.**
- **QA:**
  - 0 issues on both builds: valid JSON-LD, one H1 per page, a canonical on every page, no broken links, and every image has width, height and alt text.
  - 12 pages screenshotted at 390 px and 1440 px, with no sideways scrolling and 0 broken images.
  - Many service × city titles run past 60 characters. Those pages are canonicalized, so it doesn't matter much.

## Design direction

- **References** (screenshots in the working files):
  - UTA's route list (rideuta.com): colored line chips in ruled rows.
  - National Park Service park pages (nps.gov/zion): a plain sans and dark info bands.
  - The Jordan River Commission (jordanrivercommission.com): the river as a local identity.
  - Field Notes was tried but blocked the screenshot.
- **Idea, "the Valley Line":**
  - The company is named after the river that runs north through the Salt Lake Valley, so the service area is drawn as a **transit line**.
  - It has 13 stops from Draper and Riverton in the south to North Salt Lake in the north, with Taylorsville marked "Home base".
  - The east-bench cities (Sandy, Cottonwood Heights, Holladay, Millcreek) branch off the line.
  - Each service gets a line code (RR, RP, CM, EM, AV).
  - This carries the design without needing photos, which the client doesn't have many of yet.
- **Redesign (v2, 17 Oct 2026):** the first draft looked too plain, so the transit idea now runs the whole site:
  - The home page has big signage type, the real job photos as tilted prints, the five service lines as coloured stripes, and a departure-board strip (Founded 2019 · Free inspections · Itemized · DiamondShield · 13 stops).
  - **The Valley Line is a real route map:** the 13 cities on a line along the river, the east-bench cities on a branch and Taylorsville as home base. Every stop links to its city page. On phones it becomes the vertical list.
  - Services are route rows with large line chips (RR, RP, CM, EM, AV). The process is drawn as a route with four stations, and the 13 home-page reviews move slowly on two rails that pause on hover.
  - The inner pages share the same hero, with the page's line colour and a station marker, and the photo as a print.
- **Colors:** taken from the logo: navy `#1d3a6b` / deep `#0f2140`, roofline lime `#7bd12b` and river blue `#1e9be0`, plus three more line colours for the services.
- **Fonts:** Overpass, which comes from the US highway-sign lettering, at heavy weights, and Overpass Mono.

## New blog post (1,256 words)

"Ridge Vent vs. Turtle Vents: Which Is Better?", at `/blog/ridge-vent-vs-turtle-vents`.

- **Why this topic:**
  - One of their own reviews (Ket Knok) says other bidders "wanted to keep the old inefficient turtle vents".
  - It ties directly to the attic ventilation service.
- **Main keyword:** "ridge vent vs turtle vents".
- **Not targeted, to avoid cannibalization:**
  - "roofing company taylorsville" (home).
  - The service pages.
  - Earlier kit blog topics.
- **Sources (all opened and read):**
  - Air Vent (Gibraltar Building Products) help center: don't mix two types of exhaust vents over a common attic, because they can short-circuit.
  - Penn State's Pennsylvania Housing Research Center, "Attic Ventilation: Understanding the Why" webinar handout, 7 Oct 2022. It quotes 2018 IRC R806.2: 1/150, or 1/300 with 40–50% of the vents high and within 3 ft of the ridge. It also quotes R806.3: a 1-inch air space.
  - International Code Council: Utah adopted the 2021 IRC, effective 1 July 2023.
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:** everything open, including AI search bots, and it points to the sitemap.
- **sitemap.xml:** 28 URLs. That's every page except the 65 canonicalized service × city pages and the 404.
- **Schema:**
  - RoofingContractor with the exact address, phone, email, geo, Google Maps link, founding date 2019, founder, hours (header version) and the 13 cities.
  - Service, FAQPage (visible questions only), AboutPage, ContactPage, CollectionPage, BlogPosting and BreadcrumbList.
  - No rating or review counts until the client confirms them.

## Before go-live (developer)

- **Contact forms:** same fields as now (name, phone, email, subject, message). They need a form handler: GoHighLevel form, Netlify Forms or similar.
- **Trailing slashes:** serve the folders without a trailing-slash redirect, so the URLs match today's.
- **Domain:** the old schema used `www.jordanriverroofing.com`, but the site answers on `jordanriverroofing.com`. The draft uses the non-www version. Redirect www to it.

## Questions for the client (via Angelo)

1. Were you founded in 2019, or have you been in business since 2003? The site says both.
2. Do you really offer 24/7 emergency service, and same-day?
3. Are you BBB accredited? We couldn't find a listing.
4. Are you certified with GAF, CertainTeed or Owens Corning, or only TAMKO? Which TAMKO Edge tier are you? The 25-year DiamondShield workmanship coverage needs TAMKO's top, invite-only tier.
5. Is it OK to show 4.8 stars from 48 Google reviews?
6. Do your office hours start at 8am or 7am?
7. Can you send more real job photos, ideally with the city for each? And is the wide crew-and-truck photo on the old home page a real photo? Its lettering looks AI-generated.
8. Should we keep the 65 service × city pages or redirect them to the main service pages? (Angelo decides.)
9. Do you do roof work in Salt Lake City itself? It has the most searches for roof repair after Taylorsville.
