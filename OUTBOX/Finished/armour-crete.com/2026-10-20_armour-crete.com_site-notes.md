# armour-crete.com redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **Armour Crete** (Google: "Armored Concrete Systems"), St. George, UT.

## Folders and files

- `site/`: the files to put live.
  - Same URLs and canonicals (trailing slash), plus a new `/blog/`.
  - **Google Analytics 4 G-MYHF4YMJ3Y** is kept, as on the live site.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_v3.py`, `p_blog.py`, `illus.py`
  - the kit files
  - the styles: `theme.css`, `premium.css`, `concept.css`
- `2026-10-17_armour-crete.com_report.html`: the website plan report.

## Please check first

- **Name.** The site says "Armour Crete"; the Google profile says "Armored Concrete Systems". The draft uses the site's name. The Google profile and the site should match.
- **Phones.**
  - The site header lists **Dylan 435-994-5235** (also the live schema number) and **Zac 435-224-6987**. The draft keeps both, with names.
  - The Google profile lists **+1435-938-9271**, a third number.
- **Email:** evans@armour-crete.com.
- **Address:** none on the site or Google (service-area business), so none is shown.
- **Rating:** Google shows 5.0 from 3 reviews. It isn't shown until the client confirms it.
- **Kept as the client states them:**
  - licensed and insured; certified Deco applicator
  - 24-hour cure; the two-year maintenance cycle
  - the product list
  - "Deco Products has manufactured in Denver since 1991"
  - the concrete movement figures (5.5 millionths of an inch per inch per °F; about 1/3 in. on a 50 ft slab with a 100°F swing)

## Photos (important)

The live site has **no photos at all**, only the logo. So:

- **Services** are shown with **original drawings**:
  - six finish textures (broom finish, exposed aggregate, wet-look, pool deck, expansion joint, blacktop)
  - a four-state slab cross-section (moves, drinks, breaks, sealed) drawn from the client's own explanation
- **Atmosphere photos** are openly licensed landscapes, used for backgrounds only and never presented as the client's work:
  - Snow Canyon State Park by pkinney62 (Flickr, CC BY 2.0)
  - Color Country (BLM Utah) and Pine Valley Mountains (U.S. Forest Service), both public domain
  - Credits appear on every page that shows them.
- **Ask the client for photos of their own finished jobs.** They would replace the drawings in the service headers.

## What was done

- **Text:** the client's own, cleaned (counters like "24h / 2yr" removed; FAQs turned into real FAQs).
- **Report applied:**
  - The home page targets "concrete sealing st george" in the title, H1 and first sentence.
  - Every service page names St. George in its title, H1 and opening paragraph.
- **Biggest gap from the report:** concrete lifting isn't on the site. No page was invented; ask the client.
- **QA:** 0 issues across 18 pages. The mobile header check passed.

## Design (premium)

- **Research (screenshotted 20 Oct 2026):** Deco Products (their manufacturer), Concrete Craft (closed), Euclid/Increte, SUNDEK, plus the earlier construction set (Layton, Big-D, Mortenson). Chosen three:
  - **SUNDEK** (sundek.com): a dark full-bleed dusk hero over decorative concrete.
  - **Euclid's Increte line** (increte.com): a catalog of finishes and colours.
  - **Layton Construction** (laytonconstruction.com): an editorial serif headline and stat row.
- **Concept, "Sealed for the desert":**
  - **Hero:** a full-bleed Snow Canyon slickrock hero under a transparent header, with the "24 hours" honest-answer card.
  - **A marquee** of the six Deco products.
  - **The sticky slab story**, the signature. The drawing changes as you scroll: it moves, drinks, breaks, then sealed water beads on top.
  - **Dark finish tiles** with drawn textures for each service.
  - **The four-step process** with a big 24.
  - **A parallax band** for the two-year cycle.
  - **Product cards**, a homes-and-builders split, and the FAQ and assessment form.
- **Brand guide:**
  - red-rock terracotta #C25A32
  - sandstone #F5EFE6 / #EBE0CF
  - desert-dusk ink #1B1512
  - water blue #3F8FB0 (drops only)
- **Fonts:** Gloock (serif display), Geist (text), Geist Mono (labels). The logo was converted from white-on-black to transparent ink and white versions.

## New blog post (1,035 words)

`/blog/efflorescence-white-stains-concrete-st-george/`, "White Stains on Concrete in St. George: What Efflorescence Is and How to Stop It".

- **Main phrase:** "efflorescence on concrete" (informational).
- **No cannibalizing.** No page targets it; it links to driveway, pool deck, expansion joint and product pages.
- **Source (linked):** T. Ritchie, "Efflorescence", Canadian Building Digest CBD-2, National Research Council Canada:
  - salts plus water plus evaporation
  - the salt sources
  - fix the wetting first, then scrub or use a dilute acid
  - the water-repellent caution
- Local details (pool salt, softeners, hard water) come from the client's own text.
- No prices. **[[NEEDS: author]]**

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists every page.
- **Schema:**
  - Business node (no street address; St. George; phone; email; areas).
  - Breadcrumbs; Service on service and city pages.
  - FAQPage; BlogPosting.

## Before go-live

- Connect the assessment form.
- Confirm the name and phone.
- Swap in the client's own job photos when available.
