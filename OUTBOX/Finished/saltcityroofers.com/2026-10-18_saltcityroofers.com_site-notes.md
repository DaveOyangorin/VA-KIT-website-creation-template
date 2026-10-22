# saltcityroofers.com redesign: notes for Angelo

Draft, 18 Oct 2026. Nothing is live. Client: **Salt City Roofers** (a Salt City Builders, Inc. company), Salt Lake City, UT.

- `site/`: the files to put live. Same URLs and canonicals as today (`https://www.saltcityroofers.com/...`, trailing slash), the client's **GA4 tag (G-9CE799NZYH) kept**.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source (`build.py`, `cfg.py`, `pages.py`, `p_blog.py`, `illus.py`, `engine.py`, `migrate.py`, `clean.py`, `qa.py`; old pages in `_build/src/`).
- `2026-10-17_saltcityroofers.com_report.html`: the website plan report.

## ⚠ Please check first

- **Is the business active?** The last blog post is April 2022, the footer says © 2021, and the report found no Google profile. Confirm before any work goes further.
- **NAP:** no Google profile, so the phone and email come from the client's own site: **801-835-1868**, **SaltCityRoofers@gmail.com** (the header writes it in lower case). No address is shown (the report says not to show one unless the client wants it). Hours are not shown.
- **Claims left out until confirmed:** "Utah's #1 Roofing Contractor", "the most complete and trusted contractor", "Salt Lake City's finest", "the best roof", "Utah's premium roofing contracting company", "holds top industry certifications", "Select ShingleMaster Certified", "CertainTeed ShingleMaster, AirVent Installer, Contractor's EDGE" (from 2017), "endorsed and supported by suppliers and manufacturers", "a typical asphalt shingle can last 15–30 years", and the Q&A answer "around $10,000" for an average Utah roof (2017 price).
- **Kept as the client wrote them:** in business since 2007; Brock A. Horton (CEO and project manager) and Asenath Horton (owner); past projects including the University of Utah guest house and schools (about page); the warranty page and its 3-, 4- and 5-star CertainTeed coverage table (dated; confirm it's current); three named testimonials from the home page (Pat B., Kody B., Brandon & Sharon M.).
- **Stock photos removed:** the Envato files (`…-2UEEZLK`, `…-7K3R6FE`, `…-NVY3VZW`), the hand-and-house image, the mother and baby, the pen on a warranty form, the wooden deck photos and the badge logos. The draft uses 23 of the client's own job photos (Avenues, Draper, Park City and older jobs).
- **Logo:** the only logo file is 196 px wide. It works but looks soft on big screens; ask for a high-resolution version.

## What was done

- **36 pages, same URLs:** home, about, services, asphalt shingle systems, slate roofing system, roof warranty information, roofing Q&A, neighbors, employment, contact, the "Do your best, consume less" page, the blog index (`/roofing-blog/`), **all 22 blog posts**, one new post, and a 404 page.
- **Not rebuilt (redirect to `/roofing-blog/`):** 21 WordPress archive pages: 7 category, 9 tag, 2 author and 3 slider pages (`/blog/category/…`, `/blog/tag/…`, `/blog/author/…`, `/blog/slide/…`, `/blog/slide-page/home-slider/`). They hold no content of their own.
- **Report applied:** home targets "roofing company salt lake city" (title, H1, first sentence); service pages name Salt Lake City in the title, H1 and opening paragraph; every page has a unique meta description. Roof repair (the biggest keyword), metal roofing, gutters, inspections and commercial roofing have no pages yet: ask the client which they offer.
- **Blog posts:** the client's text kept; WordPress clutter (share buttons, author boxes) removed; posts from before 2020 carry a small "originally published" note. The Avenues, Draper and Park City posts now show their real job photos. Three old internal links that went to missing pages were pointed at the right pages.
- **QA:** 0 issues across 36 pages: one H1 each, canonicals, valid JSON-LD, no broken links, image sizes and alt text, no sideways scrolling at 390 and 1440 px. Fonts checked loading.

## Design v2 (redone 21 Oct 2026 after review)

Version 1 read as a plain template, so the look was rebuilt as **"The Homeowner's Edition"**: the site reads like a well-made home magazine, led by the client's own job photos.

- **Research (screenshotted 21 Oct 2026):** Kinfolk, Dwell, Monocle; plus Heath Ceramics (20 Oct). Cereal Magazine blocked the screenshot.
- **Chosen three:**
  - **Kinfolk** (kinfolk.com): issue numbers and folios, generous white space, serif headlines.
  - **Dwell** (dwell.com): home photography leads every story.
  - **Heath Ceramics** (heathceramics.com): warm editorial restraint.
- **Home page:**
  - **Editorial hero:** "No. 01" folio, a large Instrument Serif headline with a copper italic line, and the chapter index I to IV. Beside it, the Draper remodel photo with a slate-roof inset.
  - **Panorama:** the finished Avenues re-roof, full-bleed with slow parallax.
  - **Signature, a pinned four-chapter story:** Educate, Plan, Execute and Wrap it up, each with large roman numerals and a real photo that changes as you scroll. It has a progress bar and stacks on phones.
  - **The rest:** the eight-layer drawing on navy; an asymmetric services collage; magazine "case file" spreads for the Avenues, Draper and Park City (one large photo, two thumbnails and the project notes link); letters from homeowners; and the FAQ and form.
- **Inner pages:** full-bleed job-photo heroes with a navy overlay.
- **Fonts:** Instrument Serif (display, with italics), Instrument Sans (text), JetBrains Mono (folios).
- **Photos:** still only the client's own job photos.
- **Motion:** stops for visitors who choose reduced motion.

## Design (premium, site-specific)

- **Concept, "Educate, plan, execute, wrap it up":** the client's own four words for a job become four numbered chapters (I–IV), shown in the hero and explained on the home page with their real quote process (a 15-minute roof check, a 15-minute conversation, an emailed quote, magnet and blower cleanup).
- **Their own details:** an exploded drawing of the eight layers their asphalt page lists (decking to ventilation), a before-and-after pair from their Avenues job, and "case files" for the Avenues, Draper and Park City jobs.
- **References:** Penguin and Phaidon how-to books (serif headings, numbered chapters), Aesop product pages (restraint), architectural detail sheets (exploded layers, mono labels).
- **Colours:** salt white, the navy and teal of their logo, and copper as the one accent (they offer copper chimney caps and custom copper gutters). **Fonts:** Young Serif (display), Instrument Sans (text), JetBrains Mono (labels).

## New blog post (1,096 words)

`/blog/2026/10/18/tear-off-or-roof-over-utah-two-layer-rule/` (same URL pattern as their other posts), "Tear-Off or Roof-Over? Utah's Two-Layer Rule for Re-Roofing".

- **Main phrase:** "tear off vs roof over" (informational). Search volume: not in our data. None of their 22 posts covers it, and it targets no service keyword; it links to the asphalt system, Q&A, warranty and contact pages.
- **Sources (linked):** IRC R908.3.1.1 as reproduced in the City of Gillette re-roof handout; Bountiful City (Utah) re-roof handout (two or more layers: removal and replacement only); City of Des Moines roof shingle requirements (manufacturer instructions).
- No prices. Byline "Salt City Roofers". [[NEEDS: author]]

## robots.txt, sitemap, schema

- robots.txt allows everything and the AI search bots; sitemap (35 URLs).
- Schema: RoofingContractor (name, phone, email, parent company, founding year 2007, people, cities served; no address) on every page; Breadcrumb on inner pages; BlogPosting on every post; FAQPage on home and the new post.

## Before go-live

- Connect the contact form to the client's handler.
- Set up the 21 redirects above.
- Re-test mobile speed (was 55/100; aim for 90+).
