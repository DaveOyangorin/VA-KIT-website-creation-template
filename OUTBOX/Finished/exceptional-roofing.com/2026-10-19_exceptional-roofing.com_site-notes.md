# exceptional-roofing.com redesign: notes for Angelo

Draft, 19 Oct 2026. Nothing is live. Client: **Exceptional Roofing**, Salt Lake Valley (service-area business).

## Folders and files

- `site/`: the files to put live.
  - Same URLs and canonicals as the WordPress site (trailing slash).
  - No tracking code was found on the live site, so none is added.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `p_blog.py`, `illus.py`
  - the shared kit: `pagekit.py`, `tidy.py`, `engine.py`
  - the styles: `theme.css`, `base.css`, `concept.css`
- `2026-10-16_exceptional-roofing.com_report.html`: the website plan report.

## Please check first

- **No address** on the Google profile or the site, so none is shown. The site lists the areas they work in, in words.
- **Phones** (contact page):
  - Estimator 801-680-6499. This is also the Google number (+1801-680-6499) and the site's call-or-text line; it's the main number in the draft.
  - Production 801-809-8535.
- **Email:** ExceptionalroofingUT@gmail.com.
- **Best hours:** Mon–Fri 6:30 AM–7:00 PM, Sat 9:00 AM–5:00 PM, Sun closed.
- **Rating:** Google shows 4.8 from 16 reviews. It isn't shown until the client confirms it. The live reviews page has no reviews on it.
- **Left out:** "For over 30 years our Salt Lake Valley has been the base of multiple family run operations". It's vague and doesn't say how long this company has operated.
- **Kept as the client states it:** "downtown Salt Lake's Leonardo Museum" as a past project. It appears only in their own text on the about page. Confirm before using it more prominently.
- **Financing:** through Acorn Finance, using the client's own pre-qualify link and disclaimer.

## Fixes

- **Broken links.** Every internal link on the live site points to `https://exceptional-roofing.com/wb_exceptional-roofing.com/...`, a WordPress install path. The draft links to the real URLs.
- **WordPress leftovers aren't rebuilt.** 301 them as follows:
  - `/hello-world/` → `/blog/`
  - `/sample-page/` → `/`
  - `/category/uncategorized/` and `/author/exceptionalroofingoz/` → `/blog/`
- **Duplicate pages.** `/commercial/` and `/commercial-roofing/` are identical. `/commercial/` is kept but canonicals to `/commercial-roofing/` and stays out of the sitemap.
- **Report applied:**
  - The home page targets "roofing company salt lake city" in the title, H1 and first sentence.
  - Every service page names Salt Lake City in its title, H1 and opening paragraph.
  - City pages keep their own text.
- **Gap from the report:** "roof installation" is named on the home page but has no page. None was invented; ask the client whether they want one.
- **QA:** 0 issues across 45 pages.
  - Some titles and descriptions fall a little outside 50–60 and 150–160 characters (mostly city pages).
  - The mobile header check passed.
- **Speed:** the live site scored 97/100 on mobile. The draft is plain HTML with WebP photos at 150 KB or less; re-test after go-live.

## Design (premium, v3 redesign, 19 Oct 2026)

- **Research (screenshotted and reviewed 19 Oct 2026):** 12 industry sites: Big-D, Layton, Jacobsen, Mortenson, Groundworks (blocked by a bot check), Ram Jack, Copper X, Baker Roofing, Strike Group, Power Design, Tremco Roofing; Okland timed out. Chosen three:
  - **Copper X** (copperx.ca): full-bleed hero shot of the roof itself, the craft is the image.
  - **Baker Roofing** (bakerroofing.com): heritage voice, tilted photo prints, condensed display type.
  - **Strike Group** (strikegroup.ca): condensed uppercase headlines and a photo cut on a diagonal.
- **Concept, "Every material":** a full-bleed hero on their own mountain-home roof under a transparent header; a product marquee (the exact brands they install); a big editorial intro with counted stats; the **material selector** as the signature (pick a material: its drawn swatch lights up and the big photo cross-fades to one of their roofs, framed on a diagonal cut); a bento photo mosaic of services; a parallax band with their slogan; tilted job-file prints; a draggable before/after slider (chimney cap); a split full-height photo for the service area.
- **Inner pages:** full-bleed photo headers with heavy condensed titles; city pages each get one of their photos.
- **Brand guide:** copper #C8783F (accent, from their copper work), slate #15191B / #22282B (from the logo grey), warm stone #F4F1EB, logo green kept on the logo only. Buttons copper with dark text (contrast passes). Fonts: Antonio (condensed uppercase display), Schibsted Grotesk (text), Azeret Mono (labels), all Google Fonts, verified loading.
- **Motion:** scroll reveals, hero and band parallax, marquee, counters, photo zoom on hover, material cross-fades; all off with reduced motion.

## New blog post (1,010 words)

`/ice-dams-utah-roofs/`, "Ice Dams on Utah Roofs: Why They Form and How to Stop Them". It sits at the root, like their WordPress posts.

- **Main phrase:** "ice dams utah" (informational). No page covers it.
- **No cannibalizing.** It links to roof repair, inspections, emergency roofing, maintenance and metal roofing without targeting their keywords.
- **Sources (linked):**
  - University of Minnesota Extension, "Dealing with and preventing ice dams".
  - Utah Residential Code 2021, R905.1.2 Ice barriers (24 in. inside the wall line; 36 in. up the slope on 8:12 and steeper).
- No prices. Byline "Exceptional Roofing". **[[NEEDS: author]]**

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists the indexable pages.
- **Schema:**
  - RoofingContractor node (no street address; city only; hours; phone; email).
  - Breadcrumbs; Service on service and city pages.
  - FAQPage where a page has one.
  - BlogPosting on the post.

## Before go-live

- Connect the estimate form.
- Set up the redirects above.
- Re-test speed.
