# utahoneroofing.com redesign: notes for Angelo

Draft, 18 Oct 2026. Nothing is live. Client: **Utah One Roofing** (legal name **One Roofing LLC**), Salt Lake City, UT.

- `site/`: the files to put live. Same URLs and canonicals as today (`https://utahoneroofing.com/.../`, trailing slash), plus a new `/blog/`.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source (`build.py`, `cfg.py`, `pages.py`, `p_blog.py`, `engine.py`, `migrate.py`, `clean.py`, `imgprep.py`, `qa.py`; old pages in `_build/src/`).
- `2026-10-17_utahoneroofing.com_report.html`: the website plan report.

## ⚠ Please check first

- **The report marks this business "Check first" on the outreach list.** Read the warning on the report's email page before anything is sent.
- **Address:** the site says **5546 W Heathrow Cir**, Salt Lake City, UT 84118; the Google profile says **5536 W Heathrow Cir**. The draft uses the site's (one place: `S` in `_build/cfg.py`). Ask which is right.
- **Phones:** (801) 928-9570 (matches Google) and a second line, (385) 223-9811, both from the contact page.
- **Emails:** info@utahoneroofing.com and oneroofingut@gmail.com, from the contact page.
- **Rating:** 5 stars from 14 Google reviews, not shown until the client OKs it.

## What was done

- **12 pages:** home, the 5 service pages (residential, commercial, roof repair, insurance restoration, skylight installation), services, about, contact, a new `/blog/` with one post, and a 404 page. Same URLs and canonicals.
- **Not rebuilt (301 to the home page or 410 recommended):** 9 theme demo posts at the site root (titles like "Twin Cities commercial Roofing Services", "Rated Hail and Storm Damage Repair in Colorado", "Free photo cute family a roof above their head"), the category, tag and author archives, and `/elementor-hf/footer/`.
- **Report applied:** home targets "roofing company salt lake city" (title, H1, first sentence); every service page names Salt Lake City in its title, H1 and opening paragraph; every page has its own meta description.
- **Service pages keep the client's own text**, cleaned out of Elementor, with a new title, H1 and opening. Dropped: "top-rated", "best", "more than 10 years of experience", "24/7" and "24-hour response", "tile roofs can last up to 100 years", price ranges ("$5,000 to $15,000"), the financing terms, "possible tax incentives", and "100% disabled veteran-owned" (kept as "veteran-owned" until the client confirms the wording).
- **Removed theme demo content:** lorem ipsum, the fake team (Robert C. Simmons "CEO Roof Inc.", Christopher Jhon, Karikoka Ahli, Dickerson MH), placeholder testimonials, the "32k partners" and "Project Completed / Awards Win" counters.
- **Kept from the client's site:** veteran-owned; the services (repair, replacement, insurance restoration, flat and metal roofing, gutters, Velux skylights, green roofing); GAF, Owens Corning and CertainTeed materials (as products used, not certifications); the four-step process; the FAQ answers, including "We're fully licensed and insured" (their own claim; confirm the license number); hours and the seven counties.
- **Broken link fixed:** the services page linked to `/green-roofing/`, which returns 404 on the live site. It now points to the new green roofs post.
- **QA:** 0 issues. JSON-LD valid, no broken links, no sideways scrolling at 390 or 1440 px, 0 broken images, fonts load.

## Images

- **18 of the client's own job photos** (tear-offs, shingle, cedar shake, standing seam metal, a TPO commercial crew with the Wasatch behind, drone shots), all local WebP, plus the client's logo (black and white versions).
- **Not used:** the theme's stock photos (workers in hard hats, "engineer" and "team" headshots, blog stock, testimonial avatars) and a stray "ausport.gov.au" logo. No AI images.

## Design (premium, site-specific)

- **Concept, "the ops board":** the client is veteran-owned, so the site takes the order and plainness of an operations board, kept quiet rather than costume: stencil numerals, field photos pinned as numbered cards in the hero, the client's own four steps as "the One standard", an area-of-operations grid of the seven counties, and a field-photo wall.
- **References:** ops and field boards (pinned cards, grid, stencil numbers), Filson and Patagonia workwear pages (earthy tones, real people at work), Swiss poster grids.
- **Colors:** near-black (from the logo), field olive, sand, signal amber. **Fonts:** Saira Condensed, Saira, Saira Stencil One. Verified loading.

## New blog post (1,067 words)

`/blog/green-roofs-in-utah/`, "Green Roofs in Utah: How They Work, What They Weigh, and Whether They Fit Our Climate".

- **Main phrase:** "green roof utah" (informational). Search volume: not in our data. The client lists green roofing as a service, but no page targets it, so it competes with nothing.
- **Kept off it:** "roofing company salt lake city", "roof repair salt lake city", "commercial roofing salt lake city"; it links to those pages.
- **Sources (linked in the post):** EPA, Using Green Roofs to Reduce Heat Islands; University of Delaware Extension (2–6 in extensive media); Iowa Stormwater Manual (4 in ≈ 28 psf, 12 in ≈ 84 psf saturated); University of Utah lysimeter study on a Salt Lake City green roof, Water 2018 (bare 2.0, sedum 2.5, grass 2.7 mm/day; sedum no lower than natives under irrigation).
- Byline "Utah One Roofing". [[NEEDS: author]]

## robots.txt, sitemap, schema

- robots.txt allows everything and the AI search bots; sitemap (11 URLs).
- Schema: RoofingContractor (name, legal name, phones, email, address, hours, Instagram and Facebook) on every page; Service + Breadcrumb on service pages; FAQPage on home and the post; BlogPosting on the post.

## Before go-live

- Connect the form (name, phone, email, service, message); the old site used reCAPTCHA, so add it back to the new handler.
- Set up the 301s / 410s above.
- No analytics tag on the current site.
