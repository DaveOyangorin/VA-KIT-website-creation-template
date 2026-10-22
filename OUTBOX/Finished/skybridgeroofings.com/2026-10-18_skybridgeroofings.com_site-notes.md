# skybridgeroofings.com redesign: notes for Angelo

Draft, 18 Oct 2026. Nothing is live. Client: **Sky Bridge Roofing**, South Salt Lake, UT.

- `site/`: the files to put live. Same URLs and canonicals as today (`https://skybridgeroofings.com/pages/...`, no trailing slash). The host must serve `/pages/roof-repair` without a trailing slash (each page is a folder with an `index.html`).
- `preview/`: the private review copy. Forms are off and there's a draft strip on top. It opens on the review page (report, fixes, before/after), and the website itself is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `details.py`, `p_blog.py`, `imgprep.py`, `qa.py`). Rebuild with `python -I build.py ../site ../preview`.
- `2026-10-17_skybridgeroofings.com_report.html`: the website plan report.

## ⚠ Please check first

- **The report flags this business as "Check first" on the outreach list.** Read the warning on the report's email page before anything is sent.
- **Address:** `3007 S W Temple St, South Salt Lake, UT 84115` comes from the Google profile; the client's site shows no address. It is in the footer, contact page and schema. Confirm with the client, or remove it in one place (`S` in `_build/build.py`).
- **Phone:** shown as `(435) 659-4915`, the way the client's own contact page shows it. The Google profile lists `+1435-659-4915`.
- **Email:** `cesar@skybridgeroofing.com` is copied exactly from the site. Note the domain: the email says skybridgeroofing**.com**, the website is skybridgeroofing**s**.com. Ask which is right.
- **Rating:** 5 stars from 25 reviews (Google) is not shown until the client confirms it.

## What was done

- **16 pages, same URLs as today:**
  - Home.
  - 10 service pages: `/pages/roof-repair`, `/pages/roof-raplecement` (the client's URL, typo kept so links and rankings carry over), `/pages/metal-roofing`, `/pages/roof-inspection`, `/pages/shingles`, `/pages/tpo`, `/pages/epdm`, `/pages/roof-coatings`, `/pages/gutters`, `/pages/wall-panels`.
  - `/pages/about-us` and `/pages/contact`.
  - `/blogs/noticias` (the client's empty Shopify blog) and a new post on it.
  - A 404 page.
- **Not rebuilt (301s recommended):** `/pages/plantilla-servicios` (a Spanish template page with placeholder text, "Dato 1", "Dato 2") → `/pages/shingles`; `/collections/frontpage` (empty Shopify collection) → `/`.
- **Report applied:** the home page targets "roofing company south salt lake" in the title, H1 and first sentence. Every service page names South Salt Lake in its title, H1 and first paragraph. Every page has its own meta description. Every image has alt text.
- **Services:** the client's own site has pages for 10 services, so the report's "ask client" list is partly answered: they do gutters. Still to ask: roof installation on new builds, storm damage repair, emergency repair as its own service, insurance claims. No new service pages were invented.
- **Images and video:**
  - The client's own: team photo, crew with the trucks, a wall-panel job, a ballasted low-slope roof (from their Facebook), soffit and gutter.
  - Their three videos on the current site: drone footage of a new build with dark standing-seam metal roofs (hero, wide and tall versions), and an office film of the team working on roof drawings. Compressed to 3.6 MB total; stills from them are used as photos.
  - Not used: banner graphics with text baked in, Pinterest-size stock photos (hash file names), a stock hard hat, a stock EPDM sunset, and TPO/coating photos whose source can't be confirmed. No AI images.
- **Original drawings:** one construction detail per system (shingles, standing seam, TPO, EPDM, coating, gutter, wall panel, flashing repair, tear-off, inspection plan), drawn for this site in `_build/details.py`. Generic build-ups, no product claims.
- **QA:** 0 issues. JSON-LD valid, no broken links, no sideways scrolling at 390 px or 1440 px (the live site is 476 px wide on a phone), 0 broken images, all fonts load. Titles 50–60 and metas 150–160 except the 404 page.
- Service pages run about 400–650 words, shorter than the report's 1,200+ target. The client's own content is thin and a lot of it is unverified claims; once the client answers the questions below (warranty, prices, years, jobs and cities), each page can grow with real detail.

## Design (premium, site-specific)

- **Concept, "drawing board to rooftop":** the client's own office film shows the team working out roof details on screens and a whiteboard, and their drone film shows the standing-seam roof that came out of it. The site reads like a set of construction documents laid over real footage: a blueprint grid, title blocks, and one original detail drawing per roofing system.
- **References:** architectural drawing sets (title blocks, detail callouts), Snøhetta and BIG project pages (full-bleed film, restrained type), Carlisle and Firestone detail libraries (one detail per system).
- **Colors:** night navy, drafting-film blue lines, sky blue accent (the "sky" in Sky Bridge), concrete white. The client's logo is black and white, so it sits cleanly in the dark header.
- **Fonts:** Red Hat Display (headings), Red Hat Text (body), Red Hat Mono (labels and sheet numbers). Verified loading.
- **Signature pieces:** live drone film in the hero with a title block, the ten-system detail index, the office film band ("Every roof starts at a desk"), a drone photo wall, the three project types on the estimate form, and the team photo with their mission statement.

## Claims left out until the client confirms

| Claim on the current site | Where | Why it's out |
|---|---|---|
| Reviews from "Alex M.", "Priya K.", "Diego R." | Home | Read like theme placeholders; use real Google reviews instead |
| "2-hour emergency response" | Roof repair | Not confirmed (report: only claim speed if the client confirms) |
| "1-Year Workmanship Guarantee", "Extended Performance Warranty", "Lifetime Non-Prorated", "Triple-seal guarantee" | Service pages, About | Warranty terms need the client's real documents |
| "Decade+ of expertise", "1M+ sq ft protected", "Zero recurrence rate" | About | No source |
| Lifespans (30–70+ years), "130 MPH", "Class A fire rating", "hurricane-force" | Replacement, Metal | Product-specific; depend on the exact product |
| "Cooling costs down up to 30%" / "up to 40%" | Coatings, Metal | No source |
| "Insurance Documentation Support" | Roof repair | Ask whether they help with insurance claims |
| "5-Star Rated" | Banners | Shown once the client confirms the rating |

## New blog post (1,183 words)

`/blogs/noticias/do-you-need-a-permit-to-replace-a-roof-in-south-salt-lake`, "Do You Need a Permit to Replace a Roof in South Salt Lake?"

- **Main phrase:** "permit to replace a roof south salt lake" (informational, long tail, local). Search volume: not in our data.
- **Why this topic:** local, useful before a replacement, and it doesn't compete with any money page. Kept off it on purpose: "roofing company south salt lake" (home), "roof replacement south salt lake" (replacement page) and "roof repair south salt lake" (repair page). The post only links to them.
- **Sources (linked in the post, checked 18 Oct 2026):**
  - South Salt Lake building FAQ: "Any reroof of a structure requires a building permit"; inspections at 801-483-6032; 15 business days; 180-day expiry; double fee for work started without a permit.
  - South Salt Lake Building Permits page (City Hall, 220 E Morris Avenue).
  - ICC: Utah adopted the 2021 International Codes, effective July 1, 2023.
  - Bountiful City reroof policy: no recover over two or more existing layers.
- **No fees or prices** (none published). Author byline: "Sky Bridge Roofing". [[NEEDS: author]]

## robots.txt, sitemap, schema

- **robots.txt:** allows everything and the AI search bots. Sitemap: `https://skybridgeroofings.com/sitemap.xml`. (The live Shopify robots.txt is mostly shopping-agent text; it goes away with the new site.)
- **sitemap.xml:** 15 URLs (all pages except the 404).
- **Schema:** RoofingContractor (name, phone, email, address, hours) on every page; Service + FAQPage + Breadcrumb on service pages; AboutPage, ContactPage, Blog and BlogPosting (+ FAQPage) where they belong. All valid.

## Before go-live

- Connect the estimate form (name, phone, email, project type, message) to a form handler.
- Set up the 301s above.
- No analytics tag on the current site; add one if the client wants it.
- Re-test mobile speed (report: 76/100, target 90+).
