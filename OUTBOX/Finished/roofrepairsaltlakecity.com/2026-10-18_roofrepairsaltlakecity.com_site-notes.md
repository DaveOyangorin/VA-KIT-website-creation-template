# roofrepairsaltlakecity.com redesign: notes for Angelo

Draft, 18 Oct 2026. Nothing is live. Client: **Roof Repair Salt Lake City**, Salt Lake City, UT.

- `site/`: the files to put live. Same URLs and canonicals as today (`https://www.roofrepairsaltlakecity.com/.../`, www and trailing slash).
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source (`build.py`, `cfg.py`, `pages.py`, `p_blog.py`, `illus.py`, `engine.py`, `qa.py`; the old pages are in `_build/src/`). Rebuild with `python -I build.py ../site ../preview`.
- `2026-10-17_roofrepairsaltlakecity.com_report.html`: the website plan report.

## ⚠ Please check first

- **The report marks this business "Check first" on the outreach list.** Read the warning on the report's email page before anything is sent.
- **Phone:** the site shows **(385) 355-4849**; the Google profile shows **+1385-213-7368**. The draft uses the site's number everywhere (one place: `S` in `_build/cfg.py`). Ask which is right.
- **Address:** the site shows "1760 w 2100 s Salt Lake City Utah 84119"; the Google profile shows "1760 2100 S". Copied exactly as the site has it. Ask the client to confirm.
- **Email:** `steveadambdc@gmail.com`, from the contact page.
- **Rating:** 4 stars from 1 Google review. Not shown (the report says not to make it a headline).

## What was done

- **22 pages, same URLs:** home, 15 service pages, about, manufacturers, contact, `/articles/` (empty today: "Nothing Found") with a new article, and a 404 page.
- **Not rebuilt (301 to the home page recommended):** the theme's demo pages `/clients/wpml/`, `/clients/jquery/`, `/clients/microlancer/`, `/clients/envato/` and `/testimonials/john-doe/`.
- **Report applied:** the home page targets "roof repair salt lake city" (title, H1, first sentence). Every service page has Salt Lake City in its title, H1 and opening paragraph, and every page has its own meta description.
- **Service pages keep the client's own text**, cleaned out of the old theme, with a new title, H1 and opening paragraph. Paragraphs with unsupported claims are left out: "best", "leader in", "top roofing company", "most respected", "impeccable", "stellar", "100 percent satisfaction", "hundreds of households", the Wall Street Journal and "62%" statistics, "certified installers", "licensed as residential, commercial...", "24/7 emergency service", guarantees, the Oak Ridge white-roof savings figures, and the theme's sample testimonial ("This company is the best!").
- **Kept from the client's site:** roofing since 2005; residential and commercial; the services and roof systems listed on the home and about pages; custom sheet metal fabrication and ballasted roofing; free evaluation and quote that "stays on record for insurance"; hours (Mon–Sun 9–5); the service area list; the manufacturer list (as text, with a note that it is not a certification claim).
- **Near-duplicate pages to merge (Angelo):** commercial-roofing vs commercial-roofing-systems; tpo-roofing-membrane vs commercial-tpo-roofing-systems; utah-roof-repair vs the home page (the home page owns "roof repair salt lake city", so utah-roof-repair is framed as residential repair).
- **QA:** 0 issues. JSON-LD valid, no broken links, no sideways scrolling at 390 or 1440 px, all fonts load.

## Images

- The current site has **no job photos**: only three stock theme banners, four badge graphics and manufacturer logos. None are used. No stock and no AI images.
- The design is built from type and **original drawings** (`_build/illus.py`): Fig. 1, a house roof with the six places leaks start, which the symptom finder lights up; material swatches drawn as patterns; and a section through a ballasted roof for the article.
- **Ask the client for real job photos.** They can drop straight into the hero and service pages.

## Design (premium, site-specific)

- **Concept, "the repair manual":** a repair-first contractor, so the site reads like a well-made service manual: section codes (RR-01 to RR-15), a numbered figure, an interactive **symptom finder** (pick "water stain on a ceiling", "ice at the eaves" and so on; it explains the likely causes, lights them up on Fig. 1 and links to the fix), material swatches, and a carbon-copy work ticket for the call to action.
- **References:** Haynes and Chilton repair manuals (section codes, figures, step lists), Teenage Engineering product manuals (technical type, one accent color), carbon-copy service tickets.
- **Colors:** manual cream paper, ink, a red-orange service tag, carbon-copy blue. **Fonts:** Anybody (variable-width headings), IBM Plex Sans, IBM Plex Mono. Verified loading.
- No logo exists on the current site; the "RR" mark in the header is a typographic placeholder. Replace it if the client has a logo.

## New article (1,040 words)

`/articles/what-is-a-ballasted-roof/`, "What Is a Ballasted Roof? How Stone-Ballasted Single-Ply Roofs Work".

- **Main phrase:** "ballasted roof" (informational). Search volume: not in our data.
- **Why:** the client lists ballasted roofing on the home page but has no page for it. It doesn't compete with a money page; it links to flat roof repair, commercial roof repair and TPO.
- **Sources (linked in the post):** SPRI 2023 standards presentation (IBC 1507.12 / 1507.13, ANSI/SPRI RP-4, ASTM D448 / D7655 stone); ANSI/SPRI RP-4 (design data to 150 ft); Buildings, "Ballast Can Do It All" (10 psf or more, #4 stone); IIBEC, "A New Look at Ballasted Roof Performance" (corner and perimeter scour).
- No prices. Byline "Roof Repair Salt Lake City". [[NEEDS: author]]

## robots.txt, sitemap, schema

- robots.txt allows everything and the AI search bots; sitemap at `/sitemap.xml` (21 URLs).
- Schema: RoofingContractor (name, phone, email, address, hours, founding date 2005) on every page; Service + Breadcrumb on service pages; FAQPage on the home page and the article; BlogPosting on the article.

## Before go-live

- Connect the contact form (name, email, phone, message) to a form handler.
- 301 the theme demo pages.
- The footer's social links on the current site point at the bare facebook.com / twitter.com home pages, so they were dropped. Add real profiles if the client has them.
- No analytics tag on the current site.
- Re-test mobile speed (report: 61/100).
