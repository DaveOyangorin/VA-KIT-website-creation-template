# oakleyroofingslc.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live.

**Client:** Oakley Roofing
- 49 West Burton Ave., Salt Lake City, UT 84115, as the contact page shows it. The footer says "South Salt Lake".
- (801) 651-1000, shown as the site shows it
- M–F 8am–6pm, Sat–Sun 10am–4pm
- Founder and owner: Bryce Oakley, 1993

**Folders:**
- `site/`: the files to put live.
  - All 16 real pages are rebuilt on the same URLs and canonicals, with trailing slashes as today. A blog and a 404 page are added.
  - The client's GA4 tag `G-MHKPHZ5LRT` is kept. No other tracking was found.
- `preview/`: the private review copy. Forms are off, there's no tracking, and there's a draft strip on top. It opens on the review page, and the site is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `p_blog.py`, `imgprep.py`, `qa.py`, `style.css`, `site.js`, `robots.txt`).
- `2026-10-17_oakleyroofingslc.com_report.html`: the website plan report.

## Please decide (Angelo)

1. **WordPress leftovers.** Three junk URLs are in the live sitemap: `hello-world/` (the default post), `category/uncategorized/` and `author/supportthemesupport-net/`.
   - They're kept as noindex pages that point to the new blog, so nothing breaks.
   - Better: 301 all three to `/blog/` when it goes live.
2. **Near-duplicate hub pages.** `residential/` and `residential-roofing-services/` overlap, and so do `commercial/` and `commercial-services/`.
   - In the draft, the first of each pair is the full service page ("residential roofing salt lake city", "commercial roofing salt lake city"), and the second is a short hub that links to installation and repairs.
   - They could be merged with a 301 later.

## Problems on the current site

- **Other phone numbers on the solar pages.** The solar pages show **(801) 949-0929** and **(801) 683-6085**, and the email **sales@oakleysolarlroofing.com**. That email has a typo in the domain: "solarl".
  - The draft uses the main office number everywhere.
  - Ask which number and email solar enquiries should go to.
- **Service area contradicts itself.** Some pages say "Northern Utah", and others say "Utah, Nevada, Colorado & Wyoming". The draft says Salt Lake City and Utah until the client confirms.
- **Wrong hail rating.** The Tesla Solar Roof page says the tiles are "Class 3 ANSI FM 4473 (Best Hail Rating)". Class 4 is the top class in FM 4473, so that line isn't reused.
- **Claims not used:**
  - "#1 roofer in Utah", "the best roofing company Salt Lake has to offer", "premier".
  - "We can guarantee your roof will be able to withstand any type of weather."
  - "Average savings after 20 years: $20,000" (no source given).
- **Partner logos.** The site shows GAF Master Select, Owens Corning Preferred Contractor, Johns Manville, TAMKO, Versico and NRCA logos with no detail. They're left off until the client confirms each one.
- **Years.** The site says "over 20 years", "over 25 years" and "since 1993". The draft uses "since 1993".

## Images: only 7 of 37 are real job photos

- **Used:** 7 photos that look like Oakley's own jobs:
  - a white single-ply roof deck
  - a restaurant metal roof from the air
  - an apartment new-build with a white roof
  - a low-slope commercial roof from the air
  - a custom home under construction
  - a home with a solar roof in the snow
  - a white membrane roof at sunset
- **Not used:**
  - 9 Depositphotos stock images, plus other stock roofer and house photos
  - Tesla's own marketing renders and the Powerwall product shot
  - a stock appliance photo
  - the partner logos
- **Please ask the client to confirm all 7 are their jobs, and for more photos.**

## What was done

- **22 pages built:** the 16 real pages, a blog index, the new post, the three leftovers (noindex) and a 404 page.
- **Report applied: Salt Lake City.**
  - The home page title, H1 and first sentence target "roofing company salt lake city".
  - Every service page has Salt Lake City in the title, H1 and an opening answer.
  - "Roof repair salt lake city", the biggest keyword, goes to `residential-roofing-repairs/`.
  - "Roof installation salt lake city" goes to `residential-roofing-installation/`.
- **Copy:**
  - Rewritten only from the client's own facts: 1993; Bryce Oakley; the owner involved start to finish; mostly referrals and repeat customers; a licensed crew trained and certified by the manufacturers, some with them more than a decade.
  - Also from the site: a custom fabrication shop in Salt Lake City; TPO, EPDM, PVC, shingle and metal; roofs from 900 to 45,000 sq ft (commercial) and 900 to 15,000 (homes); the building types; FHA roof inspections; Tesla Certified Solar Roof Installers; and twice-yearly commercial inspections.
- **Reviews:** the three named reviews on the home page, word for word, with no stars. The 4.6-star / 14-review Google rating isn't shown until the client confirms it.
- **Solar specs:** the tile and Powerwall figures are the ones the client's pages list. The Powerwall figures are labeled as Powerwall 2, since Tesla has newer models; please confirm.
- **QA:**
  - 0 issues: valid JSON-LD, one H1 per page, canonicals, no broken links, and width, height and alt text on every image.
  - 12 pages screenshotted at 390 px and 1440 px, with no sideways scrolling and 0 broken images.

## Design direction: "the fifth elevation"

- **References** (screenshots in the working files):
  - BIG (big.dk): an image-led project index.
  - Henning Larsen (henninglarsen.com): full-bleed photo slides with mono captions and progress lines.
  - Holcim Elevate (holcimelevate.com): commercial roofing systems presented by audience.
  - Tesla's Solar Roof page was tried, but it blocked the screenshot.
- **Idea:**
  - Architects call the roof a building's "fifth elevation", and most of Oakley's real photos are taken from above. So the site reads like an architecture practice's drawing set.
  - The photos sit full-bleed inside a drawing frame, and every page hero has a title block (Project / Location / Sheet number).
  - The home page shows a project index of real jobs, with a preview that follows your pointer.
  - **The signature piece is an exploded section of a low-slope roof:** deck, vapor retarder, insulation, cover board and membrane. It opens as you scroll. TPO / EPDM / PVC tabs change the membrane and show how each one is seamed, its usual color and its ASTM standard, all from sourced facts.
- **Colors:** the logo is pure black, so the palette is black and concrete paper, with one signal orange taken from the lift in their own photo.
- **Fonts:** Unbounded, whose wide geometric capitals echo the logo's lettering; Instrument Sans for text; Spline Sans Mono for annotations.

## New blog post (1,252 words)

"TPO vs. EPDM vs. PVC: Which Flat Roof Membrane Fits Your Building?", at `/blog/tpo-vs-epdm-vs-pvc/`.

- **Why this topic:**
  - Oakley installs all three membranes, and commercial is their strongest line.
  - No page on the site explains how the membranes differ.
- **Main keyword:** "tpo vs epdm vs pvc".
- **Not targeted, to avoid cannibalization:**
  - "commercial roofing salt lake city" (`/commercial/`)
  - "commercial roofing installation salt lake city"
  - "roof repair salt lake city"
- **Sources (opened and read):**
  - Andrew A. Hunt, "Understanding Single-Ply Roofing Systems", CE Center / BNP Media, sponsored by Johns Manville, January 2019. Used for composition, seams, colors, EPDM thickness and sheet sizes, seam-tape strength, attachment methods, history, and PVC's grease resistance.
  - Taylor Gingerich, "SpecTopics: Understanding ASTM Standards for Roofing Membranes", Carlisle SynTec, December 2021. Used for the ASTM standards, and PVC's 16 mils minimum over the scrim.
  - The 2021 International Building Code as adopted by Utah (UpCodes):
    - Section 1507.12.1: a minimum design slope of 1/4 in 12
    - Table 1507.12.2: the membrane standards
    - Section 1512.2.1.1: no recover over two or more existing layers
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:** everything open, including AI search bots; `/wp-admin/` and `/wp-login.php` blocked; points to the sitemap.
- **sitemap.xml:** 18 URLs (everything except the noindex leftovers and the 404).
- **Schema:**
  - RoofingContractor with address, phone, hours, founding year 1993 and founder Bryce Oakley.
  - Service, FAQPage (visible questions only), BlogPosting, Blog, AboutPage, ContactPage and BreadcrumbList.

## Before go-live (developer)

- The contact form keeps the same fields (name, phone, email, message) and needs a form handler.
- Add the three 301 redirects above.
- Keep `/wp-content/uploads/` reachable for a while, or redirect old image URLs.

## Questions for the client (via Angelo)

1. Is it OK to show 4.6 stars from 14 Google reviews?
2. Which phone number and email address should solar enquiries go to?
3. Where do you work: Northern Utah, or Utah, Nevada, Colorado and Wyoming?
4. Which certifications are current: GAF Master Select, Owens Corning Preferred, and the others?
5. Should metal roofing, roof replacement and roof inspection get their own pages? They're keywords in the report.
6. Are all 7 photos your jobs? Can you send more?
7. Do you still install the Powerwall, and which model?
8. Is the address "Salt Lake City" or "South Salt Lake"? The site uses both.
