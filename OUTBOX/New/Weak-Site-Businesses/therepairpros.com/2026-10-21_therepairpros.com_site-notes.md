# therepairpros.com: redesign notes (21 Oct 2026)

**Not a client yet. Do not contact this business.** Draft only; nothing is live.

## Folders
- `site/`: the files to put live. Same 3 URLs and canonicals (`http://`, as on the live site), plus one new blog post, robots.txt and sitemap.xml.
- `preview/`: the private review copy. `preview/index.html` is the review page; the site is at `preview/home/`.
- `_build/`: the build scripts. Build with `python -I build.py ../site ../preview`, then check with `python -I qa.py ../site`.

## The HTTPS problem
The live site only works over plain http. `therepairpros.com` serves a certificate for the wrong name, and `www` serves an expired one, so browsers show a security warning on https. The site's own canonicals are http, so the draft keeps them. Once the certificate is fixed, change `U` in `_build/cfg.py` to https and rebuild.

## Concept: "The service manual"
- **Layout:** numbered sections (01 Diagnose … 08 Book) and figure captions under their own job photos.
- **Spec readouts:** the real prices ($125 service call, $150–$400 average job, 90-day warranty).
- **Brand band:** the factory-authorized brands.
- **Signature, Diagnose:** pick the product and the symptom (both from their own copy). A work order "prints" with the real visit cost, typical job cost, parts and warranty. "Book this repair" pre-fills the form with the product and symptom.
- **Dropdown links:** the header's Repairs menu deep-links to each product (`#fix-washer`, and so on).
- **References** (screenshotted 21 Oct 2026):
  - iFixit (repair culture)
  - Teenage Engineering (technical type, spec readouts)
  - Fairphone (repairability, plain talk)
- **Brand:** the italic plug wordmark (cut out of their logo JPG as black and white PNGs) and the lettered white van, with signal yellow as the accent.

## Facts used (all from their own site)
- **Contact:** phone (801) 268-6868 and dispatch@therepairpros.com.
- **Service area:** Salt Lake, Utah, Davis and Weber counties, with 61 named cities. The county grouping is plain geography.
- **Products and symptoms:** nine products, with the symptoms their site lists.
- **Process:** their four-step process.
- **Prices and warranty:** the $125 service call, the virtual repairman visit, the $150–$400 average job, and the 90-day parts and labor warranty on factory original parts.
- **Technicians:** licensed, insured, background and drug screened, factory certified and trained.
- **Brands:** Samsung branded engineer, Sharp master service center, "only authorized service center for Philips TV in Utah", Dacor authorized service center, plus the out-of-warranty brands list.
- **Testimonials:** seven, quoted word for word with the names as shown.

## Left out
- "Hundreds of 5-star reviews" and "won several awards". The Google rating (4.8 from 942) is not shown or marked up.
- Any address (the business has none on Google).
- Stock photos (Unsplash stars and electronics bench) and the brand logo image files. Brand names are set in type instead.
- Separate service pages. The report shows 10 services with no page; ask the client which to build first (dryer, washer, refrigerator).

## New blog post
- **URL:** `blog/repair-or-replace-appliance-lifespan`
- **Topic:** "Repair or replace? How long appliances actually last".
- **Sources:**
  - The NAHB/Bank of America *Study of Life Expectancy of Home Components* (Table 1, Appliances, read from the original PDF).
  - ENERGY STAR's refrigerator figures.
  - The Repair Pros' own prices.

## QA
- 5 pages, 0 issues.
- Every image has alt text and dimensions.
- No horizontal scroll at 390px.
- Mobile header fix applied; the menu was checked at the top of the page and scrolled.
