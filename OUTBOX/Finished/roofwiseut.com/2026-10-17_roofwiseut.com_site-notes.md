# roofwiseut.com redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live.

**Client:** RoofWise. The logo spells it "Roof-Wise".
- (435) 655-1246, as shown on the site
- roofwisesaltlake@gmail.com
- No street address appears on the site.

**Folders:**
- `site/`: the files to put live.
  - The same **10 URLs** as today: `/`, `/about`, `/roof-replacement`, `/roof-repair`, `/commercial-roofing`, `/gutters`, `/insurance-claims`, `/service-area`, `/contact` and `/schedule-inspection`. No trailing slash, as today.
  - Each URL is a folder with an `index.html`, and links are root-relative.
  - The host must serve `/about` from `about/index.html` without forcing a trailing slash.
- `preview/`: the private review copy. Forms are off and there's a draft strip on top. It opens on the review page, and the site is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `p_blog.py`, `imgprep.py`, `qa.py`, `style.css`, `site.js`, `robots.txt`).
- `2026-10-17_roofwiseut.com_report.html`: the website plan report.

## ⚠ Please fix first: the site points Google to a different domain

The current site is built with **Lovable** (an AI site builder). Both its `robots.txt` and its `sitemap.xml` point to **`roofwise-clear-path.lovable.app`**, not roofwiseut.com. Every URL in the sitemap is on the lovable.app domain.

- That app domain is a full duplicate copy of the site.
- The page canonicals are relative (`/about`), so they don't say which domain is the real one.

**The new site:**
- has absolute canonicals on `https://roofwiseut.com/...`
- has a sitemap and robots.txt on the real domain

**Angelo:** when the new site goes live, the lovable.app copy should be unpublished, or redirected to roofwiseut.com.

## Images: 12 of 14 look AI-generated

These all look AI-made, so none are used:
- all six job "photos": a man on a roof with the same idealized Wasatch backdrop, a perfect new home, a crew on a stone house
- the six 3D graphics: a phone, the Utah icon, the magnifying glass

They're in sizes typical of image generators (1200×912, 1408×1008).

**The only real footage is the home page hero video:** a 34-second drone orbit of a real RoofWise re-roof on a hillside home, with the crew working on underlayment.
- **Four frames from that video** are the photos on the new site.
- **The home page hero plays the same footage,** cut to a 14-second, 1.6 MB muted loop (1280 px, no sound) instead of the old 30 MB file. It pauses for visitors who turn off motion.
- **Please ask the client for real job photos.**

## What was done

- **12 pages:** the 10 current URLs, a new blog post and a 404 page.
- **Report applied: Salt Lake City.**
  - The home page title, H1 and first sentence target "roofing company Salt Lake City".
  - Every service page has Salt Lake City in the title, H1 and opening paragraph, and mentions the six Northern Utah counties.
  - Before, no page named the city; everything said "Northern Utah".
- **Service pages:** the old ones had 66–101 words. They're rewritten using only facts from the site:
  - licensed and insured
  - 10-year workmanship warranty on replacements
  - in-house crew with 20+ years of experience
  - itemized proposals
  - the 6-step replacement plan and the 4-step inspection process
  - the services and their lists
  - Each now has FAQs.
- **Insurance page:** kept as a help page, as the report suggests. The client's disclaimer is used word for word. It adds the Utah Insurance Department's own claim steps, with a link to the source.
- **The "next step" list** from the home page ("I just had a storm" → "Schedule an inspection") is now a clear table.
- **Not used:**
  - "Utah's most trusted roofing contractors" and "one of the best workmanship warranties in the industry". These are superlatives we can't back up.
  - Any star rating.
- **Forms:**
  - The contact form keeps the same fields: name, phone, email, property address, message, preferred contact method and photo upload.
  - The live inspection scheduler is an 8-step wizard, and we could only see step 1 ("What type of property is this?"). The new page has one form with the property type, the client's own "what's going on" list, address, contact details and preferred time.
  - Both forms need a handler before go-live.
- **QA:**
  - 0 issues: valid JSON-LD, one H1 per page, absolute canonicals, no broken links, and every image has width, height and alt text.
  - 11 pages screenshotted at 390 px and 1440 px, with no sideways scrolling and 0 broken images. Three pages scrolled sideways on phones at first; that's fixed.

## Design direction

- **References** (screenshots in the working files):
  - The NWS Salt Lake City office page (weather.gov/slc): "Issued / Valid" stamp blocks and plain data layout.
  - Ready.gov severe weather: plain public-information pages and notice boxes.
  - IBHS (ibhs.org): research cards with colored top rules.
  - Consumer Reports and Carfax were tried but blocked the screenshot.
- **Idea, "the inspection report":** the client's own line is "Inspect. Document. Understand.", so the site reads like a clear inspection report:
  - a report stamp block on each page ("Prepared by / Service area / Warranty / Crew")
  - numbered steps and checklists marked "Covered"
  - a situation → next-step table
  - Ready.gov-style notice boxes for the insurance disclaimer
  - the drone frames captioned like report evidence ("Frame 02")
- **Redesign (v2, 17 Oct 2026):** the first draft looked too plain, so the report idea is now shot from the air:
  - The home page opens on their own drone footage, full-width, behind a camera viewfinder (corner marks, a REC light, and a timecode that follows the real video).
  - "A roof explained, point by point": a drone frame with numbered markers. Only what can be seen is labelled: new underlayment, shingle bundles staged, skylights, the ladder and the crew trailer.
  - "Find your situation" is now a picker: choose what's going on and the next step appears.
  - The service list swaps the drone view as you point at each service.
  - A green fact band (10-year warranty, 20+ years crew, 200+ customers, 6 counties), dark process steps, and square corners and hairlines throughout, like a printed report.
- **Colors:** the logo's green (`#5fb80d`) on a green-black night (`#0b0f0d`) and warm report paper.
- **Fonts:** Inter Tight for headings, Public Sans (the US Web Design System typeface) for text, and JetBrains Mono for the report labels.

## New blog post (1,138 words)

"What Does Hail Damage Look Like on a Roof?", at `/blog/what-does-hail-damage-look-like-on-a-roof`.

- **Why this topic:** RoofWise's site is built around storm damage and insurance. This answers the question homeowners ask after a storm, and links to the inspection and insurance pages.
- **Main keyword:** "what does hail damage look like on a roof".
- **Not targeted, to avoid cannibalization:**
  - "roofing company salt lake city" (home).
  - Roof repair and the insurance claims page.
  - Earlier kit blog topics.
- **Sources (all opened and read):**
  - National Weather Service (Melbourne, FL office): the hail size chart. Quarter-size (1 inch) and larger is "severe"; the severe-storm criteria are 1-inch hail or 58 mph winds.
  - Insurance Journal, 2 Oct 2025, on the IBHS study in *Frontiers in Materials*. In a series of tests, cumulative granule loss from hail smaller than an inch exceeded the loss from one 2-inch stone.
  - IBHS Hail Impact-Resistant Shingle Ratings, for the damage types (granule loss, dents, surface cracks).
  - The Utah Insurance Department's home claims page, for the claim steps.
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:** everything open, including AI search bots, and it now points to `https://roofwiseut.com/sitemap.xml`.
- **sitemap.xml:** 11 URLs on roofwiseut.com.
- **Schema:**
  - RoofingContractor with phone, email and the six counties as the service area, with no street address.
  - Service, FAQPage (visible questions only), AboutPage, ContactPage, BlogPosting and BreadcrumbList.
  - The old site had schema on the home page only.

## Before go-live (developer)

- Connect both forms (contact and schedule inspection) to a form handler.
- Unpublish or redirect `roofwise-clear-path.lovable.app` to roofwiseut.com.
- Serve the folders without a trailing-slash redirect.

## Questions for the client (via Angelo)

1. Should the street address from the Google profile (5903 S Clear Vista Dr, Salt Lake City, UT 84118) be shown on the site?
2. Is it OK to show 5 stars from 25 Google reviews?
3. Do you install metal roofs? It's the biggest gap in the report (170 searches), and no page was built for it.
4. Are these still current: 200+ customers, 50+ realtor relationships, 9+ years serving Utah, 20+ years of crew experience?
5. Can you send real job photos, beyond the drone video?
6. Is the brand name "RoofWise" or "Roof-Wise"? The site uses both.
7. Should the phone number be shown as (435) 655-1246?
