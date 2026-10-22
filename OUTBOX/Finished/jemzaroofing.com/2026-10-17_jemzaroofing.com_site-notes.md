# jemzaroofing.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live. Client: **Jemza Roofing**, 2212 S West Temple Ste. #38, Salt Lake City, Utah 84115 · (385) 261-2942 · Jemza@jemzaroofing.com. Reviews name the owner/contact as Omar.

- `site/`: the files to put live.
  - The pages keep their **current file names** (`index.php`, `metal-roofing.php`, `ChimneyCap-Shroud.php` and so on), so every URL stays the same. They're plain HTML saved as `.php`, so no PHP is needed to run them.
  - Canonicals are added (the home page canonical is `https://jemzaroofing.com/`).
  - The current site has no tracking code, so there's nothing to carry over.
- `preview/`: the private review copy. Forms are off, there's a draft strip on top, and the job videos show as links. It opens on the review page, and the site itself is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `p_blog.py`, `imgprep.py`, `qa.py`, `style.css`, `site.js`, `robots.txt`).
- `2026-10-17_jemzaroofing.com_report.html`: the website plan report.

## ⚠ Please check first: the reviews on the Testimonials page look fake

The live `testimonials.php` shows reviews that look like **template text from another business**:

- The intro says "Lake City, Utah, with reliable tire service and 24/7 mobile support".
- The rating reads "4.5 · 2 reviews".
- The reviewers are "David Clark" and "Sarah Bell", writing about "Jemza Roofing Corp.". The company isn't called that anywhere else on the site.

**What the draft does:**
- Those reviews are **not used**.
- The page shows the **4 reviews from the client's own home page**, word for word: Leila Dethlefsen, Paul Stempniak, R P and Aspen Landgren.
- It has a "Leave a review on Google" button that points to the client's Google Maps link.
- The open review form, which posts to `insert.php`, was dropped.
- **Please confirm with the client** that the four home-page reviews are real (they read like Google reviews), and ask where the other two came from.

## Before go-live (developer)

- **Job videos stay on the server.** The 20 videos (about 170 MB) are linked from their current paths under `/img/gallery/.../videos/` and `/img/video/`. **Don't delete the old `img/` folder.** The new images live in `assets/img/`.
- **Contact form.** It keeps the old action (`process.php`) and field names (`name`, `last_name`, `email`, `phone`, `project`, `message`). The live form also sends a `token` and `captcha` field that its PHP generates. Re-add that snippet, or test the handler, before going live.
- **Old pages to remove or keep:** `insert.php`, the review submission script. It's blocked in robots.txt.

## What was done

- **15 pages on the same URLs, plus a 404 page:**
  - Home, about and services.
  - All 8 service pages: metal roofing, asphalt shingles, chimney, chimney cap and shroud, gutter-soffit-fascia, wall panels, snow bars, pavers and ballasted.
  - Portfolio, testimonials and contact.
  - The new blog post.
- **Report applied: Salt Lake City.**
  - The home page title, H1 and first sentence target "roofing company Salt Lake City".
  - Every service page has Salt Lake City in its title, H1 and opening answer paragraph.
  - Before, no page named the city in its title, and 8 of 14 pages had an empty `<title>`.
- **Meta descriptions:** a unique, hand-written one on every page. Before, all 14 pages shared one description.
- **Service pages now have text.**
  - The live service pages are only photos and videos.
  - Each now opens with an answer-first paragraph, then the service description from the client's services page, then captioned photos.
  - General explanations are kept factual, for example what snow bars do and what a ballasted roof is. Utah code facts on the chimney pages are cited in the blog post.
  - Nothing was added about prices, warranties, timelines or years beyond what the site says.
- **Images:**
  - 82 WebP images, all from jemzaroofing.com. They're all real drone and crew photos of Jemza jobs: standing-seam metal, custom chimney shrouds, copper gutters.
  - Low-resolution duplicates were skipped.
  - No stock or AI images.
- **QA:**
  - 0 issues: valid JSON-LD, one H1 per page, a canonical on every page, no broken links, and every image has width, height and alt text.
  - No sideways scrolling at 390 px or 1440 px, and 0 broken images in the screenshots.
  - 1 title and 2 metas are a little outside the ideal length (404 page, home meta).

## Design direction

- **References** (screenshots in the working files):
  - Olson Kundig (olsonkundig.com): a full-bleed photo with one plain sentence over it.
  - Snøhetta (snohetta.com): disciplines as a hairline-ruled index.
  - Dwell (dwell.com): editorial photo captions.
- **Idea, "the roofline portfolio":**
  - Jemza's own photos are its strongest asset. They're aerial shots of mountain-modern homes, standing-seam roofs and custom chimney shrouds, so the site reads like an architecture practice's portfolio.
  - It has a big statement hero, a numbered service index with thumbnails and a captioned project mosaic.
  - A dark band spotlights the chimney shroud work.
  - Bilingual attention ("Hablamos español") sits in the top bar, the hero and the FAQ.
- **Colors:** the logo's navy `#1f3c88` and sky blue `#4a8fd6`, near-black `#16191d`, warm stone backgrounds, and copper `#b0643a` taken from the client's copper caps and gutters.
- **Fonts:** Fraunces for headings, Hanken Grotesk for text, and IBM Plex Mono for labels and captions.
- **Redesign (v2, 18 Oct 2026):** the first draft looked too plain, so it's now a full portfolio:
  - The home page opens full-screen on their own standing-seam photo, with large serif type and a slowly turning "Hablamos español · English" badge.
  - A film strip of eight real projects moves sideways as you scroll down. On phones it's a swipeable row.
  - In the services index, the service's own photo follows your pointer.
  - Also: a copper numbers band (18 years, 50 miles, 2 languages, 8 services), large serif reviews, full-bleed photo heroes on every page and a photo closing band.
  - Seven of the hero photos are now exported at 2,000 px from the client's originals.
- **Tagline used:** "Quality over quantity, always", from the logo.

## Claims used from the client's own pages: please confirm

- Licensed & insured; 18 years of experience; founded in Millcreek, Utah; residential & commercial; satisfaction guarantee.
- Bilingual English/Spanish; "We Cover 50 Miles Around Salt Lake City, Utah 84115"; cash, card, Square and check.
- **Services listed on the site but without their own page:** roof replacement, cedar shingles, presidential shake roof, roofing repair, roof inspections. They're covered on the services page only.
- **Not used:** the 4.9 stars from 29 Google reviews in the report. Show it only once the client confirms.
- **Phone:** shown as on the site, (385) 261-2942. The report asks to confirm the format with the client.

## New blog post (1,560 words)

"Chimney Cap vs. Chimney Shroud: What's the Difference?", at `chimney-cap-vs-chimney-shroud.php`. It's a root-level `.php` page, like the rest of the site, because the site has no blog.

- **Why this topic:** chimney shrouds are Jemza's most distinctive work, with 17 photos on its own page. The question has real search intent, and there's a code rule homeowners don't know about.
- **Main keyword:** "chimney cap vs chimney shroud".
- **Not targeted, to avoid cannibalization:**
  - "roofing company salt lake city" (home).
  - "metal roofing salt lake city".
  - The chimney services page.
  - Earlier kit blog topics (copper patina, Utah timing, 25% rule, metal valleys, drip edge).
- **Sources (all opened and read):**
  - Utah Residential Code 2021, Chapter 10 (UpCodes):
    - R1003.9: termination height.
    - R1003.9.1: masonry chimney cap.
    - R1003.9.2: spark arrestor (4× net free area, 19-ga galvanized or 24-ga stainless, 3/8"–1/2" openings, removable).
    - R1003.20: cricket over 30".
    - R1005.2: decorative shrouds must be listed for the specific factory-built chimney system.
  - International Code Council: Utah adopted the 2021 IRC, effective 1 July 2023.
  - IMC 805.6, the same shroud rule, via Buckley Rumford.
  - InspectApedia, "Chimney Shrouds": the Baird (1991) California shroud fires, and the model-code reason statements.
  - The CSIA's site had no page on caps, so it isn't cited.
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:**
  - Everything is open, including AI search bots.
  - `process.php` and `insert.php` are blocked.
  - Points to `sitemap.xml`. Before, there was no robots.txt and no sitemap (both returned 404).
- **sitemap.xml:** 15 URLs (all pages except the 404).
- **Schema:**
  - RoofingContractor with the exact address, phone, email, Google Maps link, `knowsLanguage` en/es, `paymentAccepted`, and a 50-mile GeoCircle service area.
  - Service on service pages.
  - Review (the 4 home-page reviews; no aggregate rating), FAQPage only where the questions are visible, AboutPage, ContactPage, CollectionPage, BlogPosting and BreadcrumbList.

## Problems found on the current site

- **Template or fake reviews** on testimonials.php (see the top of these notes).
- **8 of 14 pages have an empty `<title>`.** All 14 share one meta description, and there are no canonicals, no sitemap and no robots.txt.
- **The service pages have no text**, only photos and videos, so Google has nothing to rank them for.
- **Heavy pages:** full-size JPGs (up to 4032 px) and the same 16 MB video on every page. Mobile speed was 77/100.
- **An empty Instagram link** in the header ("Follow us").
- **A spelling mistake in a URL:** `pavers_and_ballested.php` should be "ballasted". The URL is kept (same-URL rule); the page now displays "ballasted". A 301 to a corrected URL could come later.
- **The report notes** Jemza shares a building with Advanced Roofing and Moisture Control (roofamc.com), in a different suite. The suite number is kept exactly as written: Ste. #38.

## Questions for the client (via Angelo)

1. Are the reviews on the testimonials page (David Clark, Sarah Bell, "Jemza Roofing Corp.") real? We assumed not.
2. Is it OK to show 4.9 stars from 29 Google reviews?
3. Do you do roof repair, roof inspections and leak repair? Roof repair is the biggest keyword in the report (320 searches a month), and it has no page yet.
4. Should we build pages for roof installation on new builds, and for commercial roofing?
5. Should the phone number be shown as (385) 261-2942, as it is on the site now?
6. Which cities do most of your jobs come from (South Jordan, Sandy, Draper, Park City)? Can you send a few recent jobs for each?
7. Can you share real prices for a cost page?
8. Do you have an Instagram account to link? The current link is empty.
