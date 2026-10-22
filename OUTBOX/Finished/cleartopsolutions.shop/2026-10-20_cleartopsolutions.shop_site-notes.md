# cleartopsolutions.shop redesign: notes for Angelo

Draft, 20 Oct 2026. Nothing is live. Client: **ClearTop Solutions**, water damage restoration in St. George, UT.

## Folders and files

- `site/`: the files to put live.
  - Same URLs and canonicals (trailing slash), plus a new `/blog/`.
  - The live site has no tracking tag, so none was added.
- `preview/`: the private review copy. It opens on the review page; the website is at `home/`. Forms are off.
- `_build/`: the source:
  - `build.py`, `cfg.py`, `pages.py`, `home_v3.py`, `p_blog.py`, `illus.py`
  - the kit files
  - the styles: `theme.css`, `premium.css`, `concept.css`, `concept.js`
- `2026-10-17_cleartopsolutions.shop_report.html`: the website plan report.

## Please check first

- **Phones.** The site uses **(435) 288-1334** everywhere. The Google profile (report) lists **+1435-220-4296**. The draft keeps the site's number.
- **Address.** The site shows "2505 S River Road, Ste 2". Google shows 2505 S River Rd, St. George, UT 84790. The ZIP comes from Google.
- **The home page canonical.**
  - On the live site, the home page's canonical points to `/st-george/`, and the two pages carry the same text.
  - The draft keeps it (same canonicals rule) and leaves the home page out of the sitemap.
  - **Recommendation:** once approved, give the home page its own canonical, so the new home page (which targets "water damage restoration st george") can rank.
- **Left out until the client confirms them** (template text with no evidence on the site or Google):
  - "98% Client Satisfaction"
  - "100+ Projects Supported"
  - the five-star row (Google shows no reviews)
  - "certified professionals" and "years of experience"
- **This may be a lead-generation site.** The site looks templated: the same paragraphs on every city page, titles that said "Near You Nationwide", and a different phone from Google. Worth confirming who answers the phone.
- **Kept as the client states it:** licensed & insured, the 24/7 emergency line, and help with insurance claims.

## Photos (important)

- **The site has one photo** (a crew drying a kitchen). **It looks AI-generated**, so it is not used.
- **Services are shown with an original drawing:** a blueprint cutaway of a house. Each service page lights up its own room.
- **Atmosphere photos** are openly licensed, used for backgrounds only and never presented as the client's work. Credits appear on every page that shows them:
  - a desert summer storm and night lightning by A Guy Named Nyal (CC BY-SA 2.0)
  - Zion by Bernard Spragg (public domain)
  - the Virgin River in St. George by Lindsey Winkel, USDA Forest Service (public domain)
  - rain on glass by rawpixel (CC0)
- **Ask the client for real photos** of their jobs, crew and vehicles.

## What was done

- **Text:** the client's own, cleaned.
  - Removed: the counter widgets, the repeated callback forms, the "Prompt response / Clear communication" filler lists, and the services list repeated on every city page.
  - The FAQs became real FAQs.
  - The city "neighborhood" blurbs were cut to a list of place names.
- **Report applied:**
  - Home title, H1 and first sentence target "water damage restoration st george".
  - All 20 service pages name St. George in the title, H1 and opening paragraph.
- **Fixes:** broken email links (Cloudflare-scrambled) on the legal pages.
- **QA:**
  - 0 issues across 33 files.
  - No broken images, and no sideways scroll at phone width.
  - The mobile header check passed.

## Design (premium)

- **Research (screenshotted 20 Oct 2026):**
  - FirstOnsite, Hippo, Flo
  - PuroClean and Rainbow Restores were blocked by bot checks
  - the earlier restoration set: Belfor, Paul Davis
- **Chosen three:**
  - **FirstOnsite** (firstonsite.com): navy with a safety-orange urgent call bar.
  - **Hippo** (hippo.com): a calm, home-centred insurance site with plain words.
  - **Flo** (getflo.com): a sky gradient with floating cards.
- **Concept, "Where's the water?":**
  - **The hero is the signature:** a blueprint cutaway of a two-storey St. George house with six pulsing hotspots (attic, bathroom, ceiling, kitchen, basement, crawl space). Tap one and the client's own one-line explanation and the matching service links appear.
  - **A safety-orange "standing water right now?" bar** with first steps and the phone.
  - **The 48-hour dial:** it fills as you scroll and lights the four job steps, anchored on the EPA's 24–48 hour drying guidance.
  - **Six cropped blueprint room tiles** for the services.
  - **A rain-on-glass quote band** with the EPA line.
  - **Floating "when you call" cards** on a sky gradient.
  - **City photo cards**, plus the FAQ and callback form.
  - **Inner pages:** the same house with the page's room lit. The services hub is grouped by room.
- **Brand guide:**
  - night navy #0C1A2B
  - water cyan #3FB6D9 / #8FD8EE
  - safety orange #E0612B
  - sandstone #F5F2EC
- **Fonts:** Sora (display), IBM Plex Sans (text), IBM Plex Mono (blueprint labels).
- **Logo:** the client's logo, with the white background removed.
- **Reduced motion:** respected. There are no drips, pulses or float, and the dial shows complete.

## New blog post (1,292 words)

`/blog/monsoon-season-st-george-home-prep/`, "Summer Storm Season in St. George: How to Get Your Home Ready for Monsoon Water".

- **No cannibalizing.** No service page covers preparation or insurance timing. The post links to water extraction, basement flood cleanup, ceiling repair and mold remediation.
- **Sources (all linked):**
  - Ready.gov "Floods": homeowner's insurance doesn't cover flooding; a flood policy typically takes up to 30 days to start; the prep checklist; cleanup safety.
  - NWS "Turn Around Don't Drown": 6 in / 12 in / 2 ft of moving water.
  - EPA mold guide: dry within 24–48 hours; the 10 sq ft rule.
- **No monsoon dates** (no official source reached). **No prices.** **[[NEEDS: author]]**

## robots.txt, sitemap, schema

- **robots.txt** allows everything and the AI search bots.
- **sitemap.xml** lists every page except the home page, which canonicalises to /st-george/.
- **Schema:**
  - Business node (St. George address; 24/7; areas).
  - Breadcrumbs; Service on service and city pages.
  - FAQPage; BlogPosting.

## Before go-live

- Confirm the phone, the claims and the home canonical.
- Connect the callback form.
- Swap in real job photos when available.
