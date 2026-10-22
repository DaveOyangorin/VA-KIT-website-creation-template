# stgeorgehomeservices.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **St. George Home Services**, owner Ryan Nunez, St. George, UT.

## Folders and files

- `site/`: the files to put live.
  - All 197 live URLs, with the same canonicals (no trailing slash).
  - Also kept at their own URLs: the giveaway page `/win` (noindex, as live), the research files (`/research/*.pdf`, `/research/facts.json`) and `/llms.txt`.
  - New: `/blog` and one post.
  - **Google Analytics 4 G-TVT7CYGXX6** is kept.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `sx.py` (the extractor), `home_v3.py`, `p_blog.py`
  - the kit files
  - the styles: `theme.css`, `premium.css`, `concept.css`, `concept.js`
- `2026-10-19_stgeorgehomeservices.com_report.html`: the website plan report.

## Please check first

- **Probably the wrong report group.** The report sits with foundation and waterproofing, but this is a plumber and HVAC company.
  - The report's foundation cost, topic and FAQ sections were **not** used.
  - Home keyword: the report says "ac repair st george", but plumbing has more searches. The draft names both in the home title, H1 and first sentence.
- **Kept as the client states them:**
  - every fact on the site, with its footnote and source list
  - Plain Terms: the quote is the number; the $150 diagnostic fee (+$50 evenings, weekends and holidays), credited if hired; the one-year guarantee
  - hours: 7–5 on weekdays, emergencies any hour
  - the license "on request"
  - "St. George, UT 84770, we come to you" (no street address)
- **Google** shows 5 stars from 1 review. It isn't shown.
- **The giveaway** (`/win`) closes 27 Oct 2026. Check that it's still running at go-live.

## Photos (important)

- **Only the client's own job photos are used**: 153 of them, each captioned with the client's own alt text. The hero image on every page is a real photo.
- **Left out:**
  - the site's "brand" hero images (dusk St. George street scenes, an attic duct scene, a condenser close-up). They look generated.
  - the "illustration-*" lighting renders, which are labelled as illustrations.
- **The real permanent-lighting photos** (orange and purple scallops, porch close-ups) are used.

## What was done

- **A structure-preserving extractor** (`sx.py`) keeps the client's own markup:
  - headings, lists and tables (the manufacturer limit tables, for example)
  - footnote marks, the numbered source lists with working anchors, and the FAQs
- **Removed from the extracted text:** the repeated call bands and the services strip. These are rebuilt as the site's own components.
- **Report applied:** the home page targets plumbing and AC repair in St. George. Service and hub H1s name St. George.
- **Breadcrumbs:** each service sits under its own trade (heating and air, plumbing, accessible living, and so on).
- **QA:**
  - 201 files, with 0 broken links or images.
  - No sideways scroll at phone width.
  - The mobile header check passed.
  - The one QA flag is the home canonical without a trailing slash, which matches live.
  - Titles and metas are the client's own and many run long. They're kept as written.

## Design (premium)

- **Research (screenshotted 20 Oct 2026):** Basecamp, Everlane (About, "Radical Transparency"), Stripe Press. Patagonia "Our Footprint" was blocked.
- **Chosen three:**
  - **Basecamp** (basecamp.com): a plain-spoken letter on paper, signed by the founder.
  - **Everlane** (everlane.com/about): transparency as the brand.
  - **Stripe Press** (stripe.press): editorial serif typography.
- **Concept, "The paper trail":** the client's whole voice is "don't take our word for it", so the site looks like documents. It has a ruled-paper ground, a literary serif, mono footnote marks, and every photo captioned like evidence ("Our photo").
- **Home page:**
  - **Hero:** a taped-on letter from Ryan, quoting his own video transcript word for word, with his photo and signature line.
  - **A four-promise ledger strip.**
  - **Signature 1, the Plain Terms receipt:** it prints line by line as you scroll ($150 / +$50 / credited / no second number), then stamps "Approved by you".
  - **Trades bento** with real photos.
  - **A before/after slider** on a wall they painted.
  - **Signature 2, the eight-town switcher:** each town shows the first documented fact of four sections, with its source link, read straight from the client's town pages.
  - **The rest:** a permanent-lighting parallax band, a guides index and the FAQ.
- **Inner pages:** a documentary hero (title set like a book page, the page's own photo pinned beside it), source tables styled as ledgers, and footnote anchors that highlight their source.
- **Brand guide:**
  - paper #F6F2EA
  - the client's logo ink #171614
  - red-rock rust #A8432A (marks, the stamp)
  - hard-water blue #2C5D7C (links, footnotes)
- **Fonts:** Literata (display), Archivo (text, the client's own face), Spline Sans Mono (footnotes, receipt).
- **Logo:** the client's own SVG lockup, rendered as an image.

## New blog post (1,171 words)

`/blog/water-heater-temperature-setting`, "What Temperature Should Your Water Heater Be? 120, 140, and the Trade-Off".

- **No cannibalizing.** No guide or service page covers temperature settings. The post links to the hard-water guide, water heater flush, tankless descaling, recirculation pump and thermal expansion.
- **Sources (all linked):**
  - CPSC Publication 5098: 120°F; the burn times at 150, 140, 130 and 120°F; how to check and adjust.
  - OSHA Legionella control: 68–122°F growth range; tanks below 140°F with scale and sediment.
  - WHO Legionellosis fact sheet: hot water above 50°C, leaving the heater at 60°C.
- **No prices.**

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots. The client's own `llms.txt` is kept.
- **sitemap.xml** lists every page except `/win` (noindex).
- **Schema:**
  - Business node (HomeAndConstructionBusiness + Plumber; St. George 84770, no street; hours; founder).
  - Breadcrumbs; Service on service pages.
  - FAQPage; BlogPosting.

## Before go-live

- Connect the "three things" form.
- Confirm the home keyword and the generated-image question.
- Re-test mobile speed. The live site scores 96.
