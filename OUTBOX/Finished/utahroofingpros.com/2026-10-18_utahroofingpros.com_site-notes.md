# utahroofingpros.com redesign: notes for Angelo

Draft, 18 Oct 2026. Nothing is live. Client: **Utah Roofing Pros**, Cottonwood Heights, UT.

- `site/`: the files to put live. Same URLs and canonicals as today (trailing slash). **Google Tag Manager (GTM-N8SH5R5N) and GA4 (G-R2BHVYTVSQ) kept** in the head. The GTM `<noscript>` iframe after `<body>` is not in the draft; add it back on go-live if they want it.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source (`build.py`, `cfg.py`, `pages.py`, `p_blog.py`, `illus.py`, `engine.py`, `migrate.py`, `clean.py`, `qa.py`; old pages in `_build/src/`).
- `2026-10-17_utahroofingpros.com_report.html`: the website plan report.

## ⚠ Please check first

- **AI images on the current site:** every city page uses AI-generated photos (the 1376×768 `{city}_repair`, `{city}_local`, `{city}_commercial` set), and `commercial.png`, `composite.png`, `finance_pic.png`, `image2.webp` and a Higgsfield file (`hf_20260823_…`) are AI or mock-ups too. **None are used.** The draft uses 28 of the client's own job photos.
- **Claims left out until the client confirms:** "GAF Certified™" (badge and text), "Owens Corning Preferred", "Up to 50-Year Warranty", "Lifetime Materials & Workmanship Warranty" / "Limited Lifetime Warranty", "85+ verified 5-star Google reviews" (Google shows 104), "24/7 Emergency Service", "over a decade of combined experience", "trusted by major commercial clients", "approvals within minutes".
- **Financing:** the site offers "12 months, no payments, no interest" and "no upfront costs on approved credit". The draft keeps the financing page but says "ask about current options" until the terms are confirmed.
- **NAP:** Utah Roofing Pros, 2825 E Cottonwood Pkwy #500, Cottonwood Heights, UT 84121, (801) 688-3853, john@utahroofingpros.com (contact page). The report notes Google shows the phone as +1801-688-3853; the site's format is used.
- **Rating:** 4.9 from 104 Google reviews (report). Not shown as a number until the client says OK.
- **Saint Ann's School:** two of the client's photos carry a camera stamp "John Panos, 06/07/2021, Saint Anns School, 430 East 2100 South, South Salt Lake". The stamp is cropped off; the home page mentions the job by name and month. Confirm the client is happy to name it.
- **Kaysville** is listed on /service-areas/ but has no page (the link is dead on the live site). Left out; add a page if they work there.
- `test-homepagedesign/` is a test page: not rebuilt (tell the host to remove or noindex it). `locations.kml` is untouched.

## What was done

- **79 pages, same URLs:** home, about, contact, services (+ residential 6, commercial 3), service areas (+ 52 cities), get started (+ inspection, instant estimate), roof financing, roof insurance claim, projects, legal (+ 3), a new `/blog` with one post, and a 404 page.
- **Report applied:** home targets "roofing company cottonwood heights" (title, H1, first sentence); every service page names Cottonwood Heights in its title, H1 and opening paragraph; the free inspection page targets "roof inspection cottonwood heights". Roof leak repair is not a separate page (ask the client).
- **City pages keep the client's own local text** (each one is different), cleaned of buttons, emoji and the financing terms, with a small map marking the city and links to the other cities in its region.
- **QA:** 0 issues across 79 pages: one H1 each, canonicals, valid JSON-LD, no broken links, image sizes and alt text, no sideways scrolling at 390 and 1440 px. Fonts checked loading.

## Design (premium, site-specific)

- **Concept, "Sun over the ridge":** the logo is a sun rising behind a roof ridge, and their photos keep putting the Wasatch behind their roofs. So photos sit in half-sun (arched) frames, the logo's three roof chevrons are redrawn as a mark, and a horizon rule runs under the hero with the office coordinates.
- **Their own detail:** all 52 service cities plotted on a map in the five regions the client already uses (Salt Lake Valley, Northern Wasatch Front, Utah County, Wasatch Back, Tooele Area), with region filters and the Cottonwood Heights office marked. Positions are approximate; I-15 is drawn for orientation.
- **References:** National Park Service wayfinding maps (plotted dots, region colours, mono coordinates); Field Notes and Best Made catalogue pages (warm paper, workwear photos); editorial pages built on one repeated shape.
- **Colours:** the logo navy (#102944) and sun yellow on warm paper. **Fonts:** Bricolage Grotesque (display), Public Sans (text), DM Mono (labels).

## New blog post (1,400 words)

`/blog/attic-ventilation-utah-homes/`, "Attic Ventilation for Utah Homes: Intake, Exhaust and Ice Dams".

- **Main phrase:** "attic ventilation" (informational). Search volume: not in our data. No service page targets it, so it doesn't compete; it links to the free inspection, roof replacement and swamp cooler removal pages.
- **Sources (linked):** International Residential Code R806 (1/150 and 1/300 ratios, the 40–50% upper-vent condition); Building America Solution Center (PNNL / U.S. DOE) on ice dams, air sealing and ventilation. The worked example is arithmetic on the code ratios.
- No prices. Byline "Utah Roofing Pros". [[NEEDS: author]]

## robots.txt, sitemap, schema

- robots.txt allows everything and the AI search bots; sitemap (78 URLs).
- Schema: RoofingContractor (name, phone, email, address, geo, founders John and Phil Panos, founding date 2017, 52 cities) on every page; Breadcrumb on every inner page; Service on service and city pages; FAQPage on home and the post; BlogPosting on the post; AboutPage and ContactPage.

## Before go-live

- Connect the forms (inspection, estimate, contact) to the client's handler. The live site's instant-estimate widget (Roofle) is commented out in their code; ask if they want it back.
- Re-test mobile speed (was 75/100; aim for 90+).
