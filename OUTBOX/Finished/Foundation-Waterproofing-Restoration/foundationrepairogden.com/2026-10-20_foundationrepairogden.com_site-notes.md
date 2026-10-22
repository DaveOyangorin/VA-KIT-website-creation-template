# foundationrepairogden.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Business as named on the site: **Fortified Foundations**, Ogden, UT.

## Read this first

- **The report marks this "check first":**
  - There's no Google profile, and the domain is the keyword itself.
  - The site runs on a **lead-generation template**: a quote form on quotes.foundationrepairogden.com, an /opt-out page, star badges with "vote" counts, and initial-only testimonials. It's the same template as roofingsaltlakecityut.com.
  - **Confirm who actually owns the site and answers (385) 213-2324 before any outreach.**
- **Source:**
  - The live site sits behind a Cloudflare block that stops every crawler.
  - The home page was rebuilt from its **December 2024** Internet Archive capture.
  - The other 11 linked pages were rebuilt from **September 2020** captures. The 2024 home page links to exactly the same pages.
  - The report counts **23 pages** now, so some newer pages (probably individual service pages) are missing.
- **The town pages are thin:** about 300 words each. The originals are spun template copy, and nothing was invented to pad them.

## Folders and files

- `site/`: the files to put live.
  - 15 pages at the same URLs and canonicals (no trailing slash, `www.`).
  - A new blog post at `/blog/earthquake-ready-home-ogden`.
  - No tracking tag was found on the live site.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_o.py`, `p_blog.py`
  - the kit files
  - `theme.css`, `concept.css`, `concept.js`
  - the archived pages in `src/`
- `2026-10-19_foundationrepairogden.com_report.html`: the website plan report.

## Facts used (from the site itself)

- **Name and phone:** "Fortified Foundations", (385) 213-2324.
- **Hours:** every day, 07:00 am to 11:00 pm.
- **Towns:** Roy, Hill AFB, Clearfield, Layton, Hooper, Syracuse, Eden, Kaysville.
- **Services** (from its services page): foundation repair, foundation cracks, basement waterproofing, emergency water removal, wall cracks, uneven floors, concrete, block foundations, flooded basements, foundation inspection, foundation forms.
- **Not shown:** the footer says "Ogden, UT 84405" with no street address, and "Free Estimates & Fully Insured". Neither is shown until confirmed.
- **Logo:** the template's logo isn't used. The "Fortified Foundations" wordmark here is purely typographic (a light version for the dark header), made for the draft. **Replace it with the real logo if one exists.**

## Left out (unverifiable or template)

- "licensed, insured, and bonded" and "structural and geotechnical engineers"
- "certified experts", "latest equipment", "master of the craft"
- "national and local standards", "permanent solution"
- the badge ratings and vote counts
- the three initial-only testimonials
- the $5,000–$15,000 price range and the "monthly special"
- "available 24/7" (the hours shown are 7 a.m. to 11 p.m.)
- the FAQ answer on disclosure laws and mortgages

## Design (premium, v2: redone 21 Oct 2026 after review)

Version 1 was all drawings on a light ground and read as a template. Version 2 rebuilds the look around real photographs of Ogden.

- **Research (screenshotted 20 Oct 2026):** Filson, Heath Ceramics, Red Wing Heritage.
- **Chosen three:**
  - **Filson** (filson.com): heritage serif and condensed caps on warm canvas.
  - **Heath Ceramics** (heathceramics.com): editorial serif, earthy clay palette.
  - **Red Wing Heritage** (redwingheritage.com): plain-spoken craft.
- **Concept, "The same ground":** the mountains and canyon W.H. Jackson photographed in the 1870s are the ground Ogden houses stand on today.
  - The site uses those photographs in an ink duotone, with museum-style plate captions.
- **Photos (atmosphere only, credited on every page that uses them):**
  - "Observatory, Ogden, Utah" (the hero) and three Ogden Canyon views, including W.H. Jackson, 1871.
  - All are U.S. National Archives, public domain, via Wikimedia Commons.
  - **They are never presented as Fortified Foundations' work.** The business has no photos of its own.
- **Home page:**
  - **Hero:** full-bleed 1870s Wasatch-over-Ogden photograph with slow parallax and film grain. The headline rises in line by line.
  - **Ticket:** a glass panel with the phone and the estimate button.
  - **Marquee:** a rust strip of the towns served.
  - **"The ground" statement:** set beside the engraving-style plate drawing.
  - **The services ledger.**
  - **Signature, "Heave or settle?":** wet the clay and the floor heaves; switch to settlement and one side drops. Built from the client's own clay explanation.
  - **"How it goes":** a card floating over a full-height Ogden Canyon photograph.
  - **Towns as stone courses**, the FAQ and the form.
- **Inner pages:** archive canyon photos as hero backgrounds.
- **Header:** granite, site-wide, with a light version of the typographic wordmark.
- **Motion:** stops for visitors who choose reduced motion.
- **Brand guide:** limestone #EFE9DF, granite #23201C, iron oxide #B4532A (#D9773F on dark), clay #A8643F, stone #CFC4B2, moisture blue #4F86A6, ink duotone #161310 to #ECE4D6.
- **Fonts:** Fraunces (display), Hanken Grotesk (text), IBM Plex Mono (readouts and plate captions).

## New blog post (1,084 words)

`/blog/earthquake-ready-home-ogden`, "Is Your Home Ready for an Earthquake? A Foundation-First Checklist for Ogden Homeowners".

- **No cannibalizing.** No page covers earthquakes; the client's About page mentions being prepared for them. The post links to services and contact.
- **Sources (linked):**
  - **Ready.gov, "Earthquakes":** secure heavy items; fix structural issues; homeowner policies don't cover quakes; Drop, Cover, Hold On; avoid doorways; post-quake hazards.
  - **American Red Cross, "Earthquake Safety":** get your building evaluated; insurance; learn your utility shut-offs; a 3-day go-kit and a 2-week stay-at-home kit; sturdy shoes; how injuries happen.
- **No fault statistics** (USGS couldn't be reached to check). **No prices.**

## QA

- 0 issues across 15 pages.
- No broken images, and no sideways scroll at phone width.
- The mobile header and menu check passed.
- No JavaScript errors.

## Before go-live

- Confirm ownership.
- Get the current page list, the real logo and a street address.
- Connect the forms.
