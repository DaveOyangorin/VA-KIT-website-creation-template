# rasmussenlandscapes.com: redesign notes (21 Oct 2026)

**Not a client yet. Do not contact this business.** Draft only; nothing is live.

## Folders
- `site/` holds the files to put live: all 94 URLs and canonicals kept (no trailing slash, mixed case kept: `/Services`, `/Contact`, `/DesignBuild`, `/aerate6eed311a`), plus one new post, robots.txt and sitemap.xml.
  - The 6 email landing pages and the invoice page are noindex and left out of the sitemap.
- `preview/` is the private review copy. `preview/index.html` is the review page; the site is at `preview/home/`.
- `_build/`: run `python -I build.py ../site ../preview`, then `python -I qa.py ../site`.

## Concept: "Your yard. Our work." (their own line)
- **Look:** a garden journal. Their job photography runs large, set in Fraunces serif, with spruce and sod greens taken from the badge logo.
- **Signature, the Yard year dial:** pick a month to see what Rasmussen does in your yard then. Each of the 13 items is quoted from the page that describes it:
  - sprinkler turn-on, April–May
  - summer tune-up, July–September
  - shut-off, from October
  - aeration, March–April and again late August–September
  - three hedge trims
  - spring and fall cleanups
  - weeding
  - snow removal
- Where a page names a season rather than months, the item shows across that season.
- **Home page:** also has three service spreads, a portfolio mosaic, quotes over the phone (satellite imaging), the 18 city pages, an FAQ and their reviews word for word.
- **Inner pages:** every page keeps its own copy, with headings cleaned up and related links added. Portfolio and Projects now show their job photos.
- **References** (screenshotted 21 Oct 2026):
  - Gardenista
  - Chanticleer
  - Longwood Gardens
  - Terrain and Monrovia blocked the screenshot.

## Facts and flags
- **Address:** the Google NAP is shown, copied exactly: 3446 S W Temple St, South Salt Lake, UT 84115, +1801-466-0303.
  - The site itself says "3446 S West Temple, Salt Lake City, UT 84115". **Confirm which to show.**
- **Claims left out of their copy until confirmed:** "Utah's premier/premiere", "best in the business", "50 years". Customer reviews are kept word for word, and the History page keeps the owner's own story (it mentions 1971).
- **Template filler:** several pages carried leftover filler ("Write a tagline…", "Project Name", "555 555-5555"). It was removed, but those pages (the values subpages, Projects, Media) are thin. Ask whether to rewrite or retire them.
- **Tracking:** kept as on the live site (Universal Analytics UA-162917173-1). UA stopped collecting in 2023, so a GA4 ID is needed.
- **Photos:** only their own (the P10… camera series, the rock steps, crew photos). Stock and template images are removed.
- **Not shown:** the Google rating (4.5 from 629).

## New blog post
`blog/when-to-water-your-lawn-utah`, 1,335 words.
- **Sources:**
  - Utah Division of Water Resources / Slow the Flow (Weekly Lawn Watering Guide, USU cycle chart)
  - KSL, April 22, 2025, quoting the state water director and USU's Kelly Kopp
  - their own sprinkler pages
- **Keyword check:** it doesn't target "sprinkler repair" or "lawn care".

## QA
- 96 files, 0 issues.
- Every image has alt text and dimensions.
- No horizontal scroll at 390px.
- Mobile header fix applied; menu checked.
