# sandsroofingutah.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **S&S Roofing, Inc.**, West Valley City / Salt Lake City and Park City, UT.

## Folders and files

- `site/`: the files to put live.
  - All 49 live pages at the same URLs and canonicals (trailing slash), plus the new blog post and a 404 page.
  - Tracking is kept exactly as on the live site:
    - Google Ads AW-16973777089, with its lead-form conversion snippet
    - the Amazon pixel
    - Google Tag Manager GTM-MF6VFD8T
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source (`build.py`, `cfg.py`, `pages.py`, `p_blog.py`, `style.css`, `site.js`, the kit files).
- `2026-10-17_sandsroofingutah.com_report.html`: the website plan report.

## Please check first

- **Address conflict (same street and ZIP, different city):**
  - The site's contact page says "2331 South Redwood Road, Salt Lake City, Utah 84119". This is used, copied exactly.
  - The Google profile says "2331 S Redwood Rd, West Valley City, UT 84119".
  - **Ask the client which one to show.**
- **Details used (the site's own contact page):**
  - +1 (801) 272-7000 (Salt Lake)
  - +1 (435) 658-4344 (Park City)
  - admin@sandsroofingutah.com
  - Mon–Fri 8:00am–5:00pm; Sat/Sun closed
- **Reviews:** 4.6 stars from 149 (Google profile, per the report). **Not shown as a number** until the client confirms it.
- **Left out until confirmed:**
  - "35+ years of combined experience"
  - "Customer Satisfaction Guaranteed"
  - "the best materials"
  - the "Happy Clients" counter
  - the roof-calculator link
- **Ad landing pages:**
  - The 16 ad and channel landing pages (Valpak, Value Pages, Yellow Pages, magazines, ABC4, TV and so on) keep their URLs and forms.
  - They are set to noindex and left out of the sitemap so they don't compete with the service pages.
  - Confirm this is fine.
- **Services to ask about (report):**
  - roof installation
  - leak repair
  - emergency repair
  - inspections (named in the service grid only)
  - flat roof repair
  - **No pages were invented.**

## Photos

- **All real**, from the client's own site: crew on roofs, drone shots, flat and TPO work, and the refugee hub job (before, tear-off, crew, vent, after). In total, 31 images, resized to WebP and saved locally.
- **No stock and no AI images.**

## What was done

- **Text:** the client's own, cleaned. Removed: repeated calls to action, form-builder junk and unbacked claims.
- **Report applied:**
  - The home page targets "roofing company west valley city" in the title, H1 and first sentence.
  - Service pages name West Valley City in the title, H1 and first paragraph.
- **QA:**
  - 0 issues across 51 pages.
  - No broken images, and no sideways scroll at phone width.
  - The mobile header and menu check passed.
- **JavaScript fix:** a stray closing bracket in the site script was stopping every interactive feature. It is fixed, and the script passes a syntax check.

## Design (premium, v2: redone 20 Oct 2026 after review)

The first pass kept the old template (boxed cards, a symmetric hero) and added effects on top. Angelo called it basic, so the design was redone from scratch.

- **Research (screenshotted 20 Oct 2026):** Carhartt, Carhartt WIP, Liquid Death, Ableton, Mailchimp, Red Wing. Duluth Trading blocked the screenshot.
- **Chosen three:**
  - **Carhartt** (carhartt.com): yellow on black, condensed caps over real work photography.
  - **Liquid Death** (liquiddeath.com): oversized headlines and full-bleed confidence.
  - **Ableton** (ableton.com): asymmetric, overlapping image tiles.
- **Concept, "Above the valley":**
  - A roofer works where nobody else stands: up top, looking out over the Salt Lake Valley. S&S has the drone photos to show it.
  - The hero is their own full-bleed shot of a metal roof above the valley, with slow parallax.
- **Motif: the 6/12 roof pitch (26.6°).**
  - Diagonal cuts between sections.
  - Gable-topped cards. A 4:1 gable is exactly a 6/12 pitch.
  - Gable-framed photos.
  - Pitch readouts as section markers.
- **Signature, "Layer by layer":**
  - A drawn section through one roof slope. Drag the handle up the slope, or tap a stage, and the roof builds: deck after tear-off, flashing and underlayment, shingles, ridge vent, final inspection.
  - Each stage swaps in a real S&S crew photo of that step, with the client's own words.
  - The drawing is labelled as an illustration.
- **The rest:**
  - an asymmetric sector collage
  - a big-type services index with a photo that follows the cursor
  - a drifting crew film strip ("Every photo here is ours")
  - the refugee hub as a before/after spread
  - a wall of the channels people find them through (TV, magazines, Valpak and so on), linking to those landing pages
  - a review rotator
  - a free-quote form in a gable panel
  - a giant outlined wordmark in the footer
- **Reduced motion:** all motion stops for visitors who choose it.
- **Brand guide:**
  - hard-hat yellow #FFD20A (from the logo)
  - asphalt #111214
  - slate #26282C
  - galvanized paper #F2EFE7
  - wood #C9A06A and steel #9AA1A8 (drawing only)
  - mascot red, kept to a minimum
- **Fonts:** Big Shoulders Display (signage), Instrument Sans (text), IBM Plex Mono (labels and readouts).
- **Testimonials:** shown word for word, without star ratings (not verified).

## New blog post (1,154 words)

`/how-much-snow-can-a-roof-hold-utah/`, "How Much Snow Can Your Roof Hold? A Utah Homeowner's Guide".

- **No cannibalizing:**
  - None of the client's posts covers the topic, and no page targets it. Snow removal and heat cable appear only as lines on /services/.
  - The post links to services, the roof-drain and cricket posts, and contact.
- **Source:** FEMA P-957, Snow Load Safety Guide (warning signs of an overstressed roof, and what to do).
- **No snow weights in pounds are quoted** (they couldn't be checked against the FEMA text). **No prices.**

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists the 34 indexable pages.
- **Schema:**
  - RoofingContractor (the contact-page address, phones and hours)
  - Breadcrumbs, FAQPage, BlogPosting

## Before go-live

- Confirm the address wording, the review numbers, and the five services to ask about.
- Connect the forms.
- Check that the tracking tags still fire on the new pages.
