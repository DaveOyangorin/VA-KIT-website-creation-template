# customroofs.biz redesign: notes for Angelo

Draft, 17 Oct 2026. Nothing is live. Client: **Custom Roofing LLC**, located in Lehi, UT.

- `site/`: the files to put live. Same URLs and canonicals as today (`https://customroofs.biz/...`, no www).
- `preview/`: the private review copy. Forms are off and there's a draft strip on top. It opens on the review page (report, fixes, before/after), and the website itself is at `home/`.
- `_build/`: the source (`build.py`, `pages.py`, `p_home.py`, `p_blog.py`, `imgprep.py`, `qa.py`).
- `2026-10-16_customroofs.biz_report.html`: the website plan report.

## ⚠ Please decide first: the address

The Google profile uses **the same address as Aluminum Lock Roofing Inc**: 1950 S 900 W Ste S2, Salt Lake City, UT 84104.

The client's own site shows **no street address**. It only says "Located in Lehi, UT serving all throughout Utah". The draft does the same:
- Footer and schema say "Lehi, UT" only.
- Pages say "located in Lehi, serving Salt Lake City and the Wasatch Front". That's the client's own wording, from the home page and the contact block.

Note that the Google profile says Salt Lake City while the site says Lehi. Once you decide, the address goes in one place (`S` in `_build/build.py`).

- Redesign (v2, 18 Oct 2026): "Cu 29, a coppersmith's sample book". Bodoni Moda + Geist + Geist Mono; verdigris-black, copper, bone. Transparent header over the photo hero; a periodic-table copper tile (29, Cu, 63.546) that weathers through the five patina stages as you scroll; services as copper sample chips on a ring; a sticky section where a standing-seam sheet ages stage by stage; arched photo frame; specimen-labelled gallery; big serif review. The top bar was removed (phone is in the header).

## What was done

- **9 pages, same URLs as today:**
  - Home.
  - `copper-roofing-utah/`.
  - `custom-roofing-maintenance-utah/`.
  - `lehi-custom-siding-home-value/`.
  - `home/roofing-services-lehi-quality-guaranteed/`.
  - `copper-roofing-lehi/` (the client's contact / request-a-quote page).
  - New pages: `blog/` and `blog/why-does-copper-turn-green/`.
  - A 404 page.
- **Report applied:**
  - The home page targets "roofing company salt lake city" in the title, H1 and first sentence. It's worded truthfully: located in Lehi, serving Salt Lake City.
  - Salt Lake City also appears in the copy and the schema `areaServed`.
- **One H1 per page:**
  - The current home page has none.
  - The other current H1s don't use the page keyword. Each new H1 starts with it.
- **No new service pages invented.** The report marks 8 of 10 services as "ask client" (roof repair, metal roofing and the rest).
- **Images:**
  - 18 local WebP photos plus the logo, all from customroofs.biz, all under 150 KB.
  - Every image has width, height and alt text.
  - Left out: the stock photo of a roofer (`image1219.jpg`), the stock "5 stars" photo, and the blue icon graphics. No AI images.
  - The silver logo was cut out of its white background so it sits on the navy header.
- **Reviews:** 4 of the 5 home-page reviews are kept word for word (Scott Summers, Gama Garcia, Shane Reeves, Lacey Reeves). "Sega Nintendo" is left out because it looks like a placeholder name. Confirm with the client.
- **Spanish pages:** the live site has `/es/` versions. They stay as they are. The new pages link to them with `hreflang` tags, and the footer links "Español" (all checked: 200 on 17 Oct).
- **QA:**
  - 0 issues.
  - Titles are 50–60 characters and metas 150–160, except the 404 page.
  - JSON-LD is valid and there are no broken links.
  - No sideways scrolling at 390 px or 1440 px, and 0 broken images.

## Claims left out until the client confirms

| Claim on the current site | Where | Why it's out |
|---|---|---|
| "Over 75 years" | Home page title and intro | Contradicts "15+ years" (home, services) and "over 20 years" (copper page) |
| "700+ projects", "1000+ satisfied clients" | Services page | Shown beside "15+ years"; confirm the numbers |
| "24/7 emergency repairs" | Maintenance page | Confirm before promising it |
| "Certified professionals", "licensed" | Home page | Which license or certification? |
| Copper siding saves energy as "an extra insulation layer" | Siding page | Not supported; left out |

**Kept, because the client states it clearly, but please confirm:**
- The **5-year workmanship warranty on all services** (services page and its meta description).
- The **free consultation** (home, maintenance and siding pages).
- "Contact within 24 hours" was dropped.

## Design direction

- **References** (screenshots in the working files):
  - Copper Development Association (copper.org): offset frames and an editorial feel.
  - Coppercraft (coppercraft.com): copper photography up close.
  - Revere Copper (reverecopper.com): a confident navy and copper pairing.
- **Idea, "the patina scale":** copper weathers from salmon pink through russet, chocolate and slate to blue-green (the stages as Construction Canada describes them). That five-color strip runs under every hero, the footer and the labels. The home page shows the full scale and links to the blog post.
- **Colors:**
  - Brand navy (`#0b1d33`, close to the logo's `#001D3F`).
  - Copper as the action color (`#d0844f`).
  - Verdigris (`#6fb3a3`) as the quiet second accent.
  - Warm paper background.
- **Fonts:** Bricolage Grotesque for headings, Figtree for text.
- **Photos:** in offset copper frames and white-bordered "snaps" with captions.

## New blog post (1,418 words)

"Why Does Copper Turn Green? (And Why It's Slow in Utah)", at `blog/why-does-copper-turn-green/`.

- **Main keyword:** why does copper turn green.
- **Supporting:** how long does it take copper to turn green, copper roof patina, copper patina stages.
- **Not targeted, to avoid cannibalization:**
  - "roofing company salt lake city" (home).
  - "copper roofing utah" and "copper roofing lehi" (service pages).
  - "custom roofing maintenance utah".
  - "lehi custom siding".
  - These are linked to only. The hard head terms ("copper roofing", "copper roof cost") were skipped because there are no client prices.
- **Sources (all opened and checked):**
  - Metal Roofing Manufacturers NZ, https://www.metalroofing.org.nz/node/3860: patina compounds, and 5 / 10 / 18 / 30+ years by climate.
  - Construction Canada, 10 Nov 2017, https://constructioncanada.net/architects-turn-green-reliable-long-lasting-roofing/2: the color stages, 7–10 and 15–25 years, and the arid-climate note.
  - KUER, 5 Feb 2024, https://www.kuer.org/health-science-environment/2024-02-05/what-if-utah-isnt-the-2nd-driest-state-we-all-thought-it-was: Utah is the third-driest state, 34.3 cm a year (1991–2020). Analysis by BYU assistant professor Rob Sowby, using NOAA data.
- **No Utah timeline is given,** because no source has one. The post says so.
- **Author** is shown as "Custom Roofing". `[[NEEDS: author name and role, if the client wants one]]`
- **Schema:** BlogPosting with citations, FAQPage (4 visible questions), BreadcrumbList.

## robots.txt, sitemap, schema

- **robots.txt:**
  - Everything is open, including AI search bots.
  - `/elementor-hf/` (the builder's header and footer templates, now in the live sitemap) and `/wp-admin/` are blocked.
  - Points to `sitemap.xml`.
- **sitemap.xml:** the 8 indexable pages. The 404 page and the builder templates are left out.
- **Schema:**
  - Every page: RoofingContractor and WebSite, with both phones as contact points and the Facebook page in `sameAs`.
  - Services: Service. The services page uses OfferCatalog.
  - Contact: ContactPage.
  - FAQPage only where the questions are visible (home, copper roofing, blog).
  - BreadcrumbList on all pages.

## Problems found on the current site

- **Broken link:** "Gutter" on the services page goes to `/gutters-a-crucial-component-of-home-and-roof-maintenance/`. It redirects twice, then ends on a **404**. The new site lists gutters without a link.
- **Redirecting links:** the home page links to `/lehi-custom-roofing/roofing-services-lehi-quality-guaranteed/` and `/home/contact`. Both redirect. The new site links straight to the final pages.
- **Builder templates in the sitemap:** `elementor-hf-sitemap.xml` lists the header and footer as pages.
- **No tracking code** (no Google Analytics or Tag Manager) was found on the current site, so nothing was carried over. `[[NEEDS: GA4 ID if the client has one]]`

## Questions for the client (via Angelo)

1. How should the shared address with Aluminum Lock Roofing be handled? Should the site keep saying Lehi? (Angelo first.)
2. How many years in business: 75, 15+ or 20+?
3. Are "700+ projects", "1000+ clients", the 5-year workmanship warranty and the free consultation correct?
4. Do you offer 24/7 emergency repairs? Which license or certification should the site name?
5. Which other services do you offer: roof repair, metal roofing, roof replacement, gutter installation, inspections, commercial, flat roofs?
6. Is "Sega Nintendo" a real reviewer?
7. Is 801-889-4220 the right format, and should the secondary line (385-371-7423) stay on the site?
8. Should the Spanish `/es/` pages get the new design too?
9. Do you have a GA4 property? Who should the blog author be?
