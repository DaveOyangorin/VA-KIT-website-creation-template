# gprroofing.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live. Client: **Go Pro Roofing**, West Valley City, UT. The owner named on the site is José.

- `site/`: the files to put live. It has the same URLs and canonicals as today, and keeps the tracking (see below).
- `preview/`: the private review copy. It has no tracking, forms are off, and there's a draft strip on top. It opens on the review page, and the site itself is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `overrides.py`, `p_home.py`, `p_blog.py`, `extract.py`, `imgprep.py`, `qa.py`, `real_photos.txt`).
- `2026-10-17_gprroofing.com_report.html`: the website plan report.

## What was done

- **All 30 live pages rebuilt in the new design, plus 2 new pages:** the new blog post and a 404 page. That's 32 in total. The live pages are:
  - Home.
  - Services and 6 service pages.
  - About, reviews, gallery and contact.
  - The blog index, 4 category archives and 10 posts.
  - Sitemap, privacy and terms.
  - The MetForm form template is left out and blocked in robots.txt.
- **Report applied: West Valley City.** The home page title, H1 and first sentence target "roofing company West Valley City". These 8 pages now have West Valley City in the title, H1 and an opening answer paragraph (`_build/overrides.py`):
  - Roof repair, roof replacement, metal, asphalt, residential installation, services and about.
  - TPO (it keeps "Salt Lake City", which is in its URL, and mentions the West Valley City base).
- **Wrong H1 fixed.** The live roof repair page's H1 reads "Residential & Commercial Roof Replacement Experts in Salt Lake Valley". It's now "Roof Repair in West Valley City".
- **Meta descriptions:** 29 of the 30 pages had none.
  - The home page, the service pages, blog, gallery, reviews and the new post got hand-written ones.
  - The posts and category pages use a description taken from each page's own first paragraph.
- **Images: real only.**
  - The current site mixes the client's real job photos with many stock or AI-looking images (posed workers, a woman catching a leak in a bucket, "happy family" shots, stock workers with the GPR logo added).
  - Only images clearly from Go Pro Roofing were kept: watermarked job photos, WhatsApp job photos, the crew in GPR hoodies, the annotated inspection photo, plus the certification badges and the Owens Corning color chart. That's 34 in the preview. The full allowlist is in `_build/real_photos.txt`.
  - **87 images were left off.**
  - **The client should send more real job photos, ideally with the city for each.**
- **Logo:** the live logo file is **40,974 × 7,261 px (1.7 MB)** and loads on every page. That's a big part of the 26/100 mobile speed. It's now 600 px wide. It keeps its red block, as on the current site, because "GO PRO" is black and "ROOFING" is white.
- **Reviews:** 10 Google reviews quoted on the current site's reviews page (through Trustindex), copied word for word with names. The 5.0 / 60+ rating is **not** shown as a number yet. The report says to wait for the client's OK.
- **Broken links:**
  - `/residential-roof-installation-uta/` is a typo that WordPress redirects; it now points to the right page.
  - A link to `/why-weather-resilient-roofing-is-becoming-essential-for-todays-homeowners/` is a 404 and was removed.
- **Category pages** (`/category/blog/` and the other 3) had no canonical tag. They now point to themselves and list the posts.
- **Noindex (kept on their URLs, left out of the sitemap):** `privacy-policy/` and `terms-of-service/`, which are empty on the live site. Both show a placeholder: `[[NEEDS: text from the client]]`.
- **QA:**
  - 0 issues: valid JSON-LD, one H1 per page, no broken links.
  - Every image has width, height and alt text.
  - No sideways scrolling at 390 px or 1440 px, and 0 broken images.
  - 17 titles and 5 metas are outside the ideal length. They're mostly the client's own post titles, kept as is.

## Tracking (live build only)

All of it was copied from the live site into `_build/tracking_head.html` and `tracking_body.html`:
- Google Tag Manager GTM-T82JSDLV.
- Google tag GT-KT9JQ5QQ.
- GA4 G-9D85GNBBRR.
- Meta Pixel 981501656561958.
- The LeadConnector chat widget.

## Design direction

- **References** (screenshots in the working files):
  - Milwaukee Tool (milwaukeetool.com): red bands, heavy condensed caps, slanted tags.
  - Hilti (hilti.com): "Pick the right product for the job" selector charts.
  - Snap-on (snapon.com): "for professionals performing critical tasks".
- **Idea, "pro-grade":** the name says it, so the site borrows from professional tool brands:
  - slanted red tags and buttons
  - italic condensed headings
  - 8 numbered service tiles
  - a **"Pick the right roof for the job"** chart comparing asphalt, metal and TPO, using figures from the client's own FAQs
  - a "photo-documented" panel quoting a customer about the before/during/after photos
- **Colors:** the client's own deep red `#990000`, near-black `#1C1B1F` and warm off-white `#F4F1EE`, from their Elementor settings.
- **Fonts:** Barlow Condensed (italic) for headings, and Manrope for text. Manrope is the body font on their current site.
- **Redesign (v2, 18 Oct 2026):** the first draft looked too plain, so the tool-brand idea is pushed all the way:
  - The home page opens full-screen on their own crew photo with huge italic condensed type, a red diagonal slash, and a "spec plate" (5-year workmanship, up to 50-year materials, 1–3 days, $0 estimate).
  - The eight services are a catalog lineup (GPR·01 to GPR·08) with a red wipe on hover.
  - "Pick the right roof" is now a selector: choose asphalt, metal or TPO to see its lifespan, Utah cost and best use. The full table is still on the page.
  - Credentials sit next to the photo-documented review and their own annotated inspection photo.
  - **The job-site wall crops the watermarked photos from the bottom**, so the house shows instead of the big GPR logo watermark. The original files are unchanged.

## Claims used from the client's own pages: please confirm

- **Prices** (from their FAQs): roof replacement in Utah typically $8,000–$15,000; repairs $300–$1,500; TPO $5–$12 per sq. ft. installed.
- **Timing:** emergency calls typically handled the same or next day; standard repairs in 1–3 business days; most replacements 1–3 days; residential installs 1–2 days.
- **Lifespans** (their FAQs): asphalt 20–30 years (premium up to 50), metal 40–70, TPO 20–30.
- **"24/7 Emergency Service"** (site header). The report asks to confirm before claiming it.
- **Warranties:** 5-year workmanship and up to 50-year material warranties.
- **Credentials:** Master Roofer Certified; Owens Corning Preferred Contractor; recognized by CertainTeed and GAF. **The badges say "GAF Master Elite", but the text says "GAF Recognized/Authorized".** Which is current?
- **"Latino-owned & locally operated"** and **"over a decade of experience"** (residential page).
- **Address:** 5291 W Ted Wy, West Valley City, UT 84120, from the Google profile. The current site doesn't show a street address, only "Salt Lake County". It's now in the footer, contact page and schema. **Please confirm it should be public.**

## New blog post (1,248 words)

"How Are Valleys Done on a Metal Roof?", at `how-to-do-valleys-on-a-metal-roof/`. That's the same root-level URL pattern as their other posts.

- **Main keyword:** "how do you do valleys with metal roofing". It's a real Google question from the report.
- **Not targeted, to avoid cannibalization:**
  - "roofing company west valley city" (home).
  - "metal roofing west valley city" and "metal roofing contractors west valley city" (the metal page, which is linked).
  - Their existing post on metal roof cost (linked).
- **Sources (both opened and read):**
  - ATAS International, Field-Lok standing seam installation guide, Valley Detail. Self-adhered underlayment about 18" up both sides; a valley pan; a joggle cleat 4–6" from the center, fastened 6" on center through butyl tape; panels turned under into the cleat with clips at 2'-0".
  - HPM, Exposed Fasten Design & Detail Guide, March 2023. Valleys must be the proper width, drain, and be kept free of debris; inside closures set in sealant; valley trim needs a 9" lap (3" for other trims) with two beads of butyl; minimum slope 3:12.
- **Customer quote:** the post quotes a customer review about before/during/after photos (Misty Jensen, Google). It's on the current site.
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:**
  - Everything is open, including AI search bots.
  - The client's 10-second crawl delay is kept. Google ignores it; Bing honors it.
  - `/wp-admin/` and `/metform-form/` are blocked.
  - Points to `sitemap.xml`.
- **sitemap.xml:** 29 indexable URLs. The empty privacy and terms pages and the 404 page are left out.
- **Schema:**
  - RoofingContractor with address, phone, email and the Facebook, Instagram, TikTok and YouTube profiles. `areaServed` covers West Valley City, Salt Lake County and Utah County.
  - Service on service pages, plus BlogPosting, FAQPage (only where the questions are visible), AboutPage, ContactPage, CollectionPage and BreadcrumbList.

## Problems found on the current site

- **The 1.7 MB logo** (see above), and mobile speed of 26/100.
- **Roof repair page H1** says roof replacement (fixed).
- **Two posts answer the same question:** `who-to-call-for-roof-leak/` and `who-to-call-for-leaking-roof/`. Both are kept until Angelo approves a redirect.
- **Possible keyword overlap:** the report flags "roof installation" vs "residential roof installation" and "metal roofing" vs "metal roofing contractors". The site has one page for each pair, so nothing overlaps today.
- **Missing pages:** "Emergency roof repair" and "roof inspection" have no pages of their own (the report lists them as home-page-only). No pages were invented. Waiting on the client.
- **Home page counter:** the "Satisfied customers" counter shows "0%" when it doesn't animate. It was not carried over.

## Questions for the client (via Angelo)

1. Are the price ranges and timing from your FAQs correct to show more prominently?
2. Is "24/7 emergency service" accurate?
3. GAF Master Elite or GAF certified: which is current?
4. Is it OK to show 5.0 stars from 62 Google reviews?
5. Should the street address (5291 W Ted Wy) be shown on the site?
6. Can you send privacy policy and terms of service text?
7. Should the two roof-leak posts be merged? (Angelo decides on the redirect.)
8. Can you send more real job photos, with the city for each?
9. Do you work in Salt Lake City, South Jordan, Sandy and Draper, with jobs there to mention? Do you offer emergency repair and roof inspection as their own services, so we can build those pages?
