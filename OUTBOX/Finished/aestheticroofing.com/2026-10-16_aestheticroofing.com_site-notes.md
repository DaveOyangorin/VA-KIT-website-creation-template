# aestheticroofing.com redesign: notes for Angelo

Draft, 16 Oct 2026. Nothing is live. Client: **Aesthetic Roofing**, South Jordan, UT.

- `site/`: the files to put live. Same URLs and canonicals as today, Tag Manager and the Trustindex review widget kept.
- `preview/`: the private review copy. No tracking, forms off, draft strip on top.
- `_build/`: the source.
  - `extract.py` pulls content from the old Elementor pages.
  - `imgprep.py` handles the images.
  - `build.py` and `pages.py` build the pages; `p_home.py` and `p_blog.py` are the hand-made pages.
  - `qa.py` checks the output.
- `2026-10-16_aestheticroofing.com_report.html`: the website plan report (keyword data from the 5 Oct audit).

- Redesign (v2, 18 Oct 2026): "the 14-day promise". Syne + Hanken Grotesk + DM Mono; charcoal and their butter yellow. Transparent header over the drone hero, the On-Time Start Guarantee as a perforated ticket stub, a 14-day calendar band with the real numbers (1 day, 3 options, 495+ roofs), expanding service panels, an overlapping photo pair with the team photo, a vertical process timeline, material cards and a sticky FAQ. The top bar was removed.

## What was done

- **28 pages.** The home page and the new blog post were designed by hand. The other 24 existing URLs were moved into the new design with their text, FAQs and canonicals kept.
- **Report applied:** South Jordan is now named in the title, H1 and first paragraph of the home page and every service page (roof repair, replacement, storm damage, inspection, gutter replacement, gutter installation, metal roofing, roof types hub). Each of those pages opens with a short, answer-first paragraph written from the client's own facts.
- **Images:** 39 local WebP files in `site/assets/img/`, all under 150 KB, with width/height and alt text.
  - Nearly all are the client's real drone and project photos, plus their team photo.
  - The client's 3D roof-type renders were *not* used, since they aren't photos.
  - Two Unsplash photos (Unsplash License) stand in for metal and flat roofing: material-metal (photo-1779941373840) and material-flat (photo-1640476750068).
- **Speed (the report's #1 issue, 33/100 on mobile):** the new site is plain HTML and one CSS file. There's no Elementor and no sliders, and images are small WebP files, lazy-loaded below the top. **Re-test PageSpeed after go-live.**

## Design direction

- **References actually reviewed:** Sunrun (sunrun.com: photo hero, short punchy headline, dark review band), Hover (hover.to: clean numbered steps) and Roofr (roofr.com: star rating under the main button). Tesla's site blocked access, so it wasn't used.
- **Concept, "seen from above":** the client's own drone shots, full-bleed under a faint survey grid.
- **Colors come from their theme:** charcoal #17181A and #2F3136, butter yellow #F3DF7D, gold #CFB566.
- **Fonts:** Archivo (wide, used for headings) and Hanken Grotesk (body text). Verified loading. The old site used Plus Jakarta Sans and Inter.
- **Signature details:** a yellow "ticket" for their On-Time Start Guarantee (start in 14 days or 20% back), and a number band (1-day installs, 14-day start, 3 priced options, 495+ roofs last year).

## Keyword map (from the report)

| Page | Main phrase |
|---|---|
| `/` | roofing company south jordan (+ roofers / roofing contractor south jordan) |
| `/services/roof-repair/` | roof repair south jordan |
| `/services/roof-replacement/` | roof replacement south jordan |
| `/roof-types/metal-roofing/` | metal roofing south jordan |
| `/services/roof-inspection/` | roof inspection south jordan |
| `/services/storm-damage-roof-repair/` | storm damage roof repair south jordan |
| `/services/gutter-replacement/` | gutter replacement south jordan |
| `/services/gutter-services/` | gutter south jordan (installation) |
| `/roof-types/` | roof types south jordan (guide) |
| `/blog/what-causes-roof-leaks/` **(new)** | what causes roof leaks (question, blog only) |

- **Kept from the client:** titles and metas on the other pages. 14 titles and 11 metas fall outside the 50–60 / 150–160 ranges.
- **Two old titles were bad and are fixed:** `/services/gutter-replacement/` was titled "Our Services - Aesthetic Roofing" with no meta. `/service-areas/` had no meta.

## New blog post (1,771 words)

`/blog/what-causes-roof-leaks/`, "What Causes Roof Leaks? A Utah Roofer's Guide". This is the client's first blog post, and `/blog/` is new too.

- **Main phrase:** "what causes roof leaks". It's a real Google question from the audit, marked "Yes".
- **Long-tail phrases:** can a handyman fix a roof leak (also a real Google question from the audit), roof leaking when it rains, roof leak in winter, roof leak around chimney.
- **No cannibalization:** the post doesn't target "roof repair south jordan" (the roof repair page), "storm damage roof repair", or "roof leak repair south jordan". The audit flags that last one as a possible future service page. The post only links to those pages.
- **If the client confirms roof leak repair as its own service:** that page should keep its FAQ answer short and link to this post.
- **Sources (linked in the post):**
  - NDSU Extension (ice dams)
  - University of Utah (snowfall)
  - Kaysville City handyman guide (2016, quotes Utah Code 58-55-305)
  - Utah DOPL
- **Handyman dollar limit:** not stated in the post. I couldn't open the current statute, and secondary sources disagree ($3,000 vs $7,000). The post sends readers to DOPL for the current limit.
- **Author:** the byline is "Aesthetic Roofing". [[NEEDS: author]] A named team member would help.

## robots.txt, sitemap, schema

- **robots.txt:**
  - Allows everything and keeps their `Crawl-delay: 10`.
  - Keeps their existing bot permissions (Googlebot, Bingbot, GPTBot, ClaudeBot, Google-Extended).
  - Adds OAI-SearchBot, ChatGPT-User, Claude-SearchBot and PerplexityBot.
  - Points to `https://www.aestheticroofing.com/sitemap.xml`. The old Yoast sitemap is `/sitemap_index.xml`, so update Search Console.
- **sitemap.xml** lists 26 URLs. The thank-you page is `noindex` and left out. `/sample-page/` is left out (see below).
- **Schema on every page:**
  - Business: RoofingContractor with NAP, the 11 counties served, the GAF Master Elite credential and social links.
  - Home: FAQPage (their 8 FAQs).
  - Service and roof-type pages: Service + FAQPage.
  - County pages: Service with areaServed.
  - Blog post: BlogPosting + FAQPage.
  - About: AboutPage. Contact: ContactPage.
  - Projects and hubs: CollectionPage.
  - Breadcrumbs everywhere.
  - No aggregateRating (see the reviews question below).

## Problems found on the current site

1. **WordPress's default `/sample-page/` is live and in the sitemap.** It duplicates the home page content. Not rebuilt; recommend a 301 to `/`.
2. **A broken internal link:** the roof repair page links to `/roof-types/asphalt-shingle-roofing/`, which doesn't exist. Fixed to `/roof-types/asphalt-shingle/`.
3. **Gutter pages:** `/services/gutter-replacement/` and `/services/gutter-services/` are close topics, as the report notes. Both kept. Ask Angelo whether to merge them.

## Tracking and integrations (live build only)

- **Google Tag Manager GTM-PVZ96S4H**, head + noscript. This appears to run their **dynamic call-tracking number**: the live header shows (801) 516-4053 while the page source says (801) 810-2276.
- **Trustindex Google-reviews widget**, same loader ID, in the home reviews section. The preview can't load it, so it shows a short note instead.
- **Forms** keep these fields: first/last name, phone, email, address, service and message. They have **no endpoint**. Connect them to their current form or CRM before go-live.

## Questions for the client (via Angelo)

1. **Phone number:** the page source uses (801) 810-2276, the live header shows (801) 516-4053 (call tracking), and the Google profile says +1801-997-1500. Which number should be the main NAP phone everywhere? I used (801) 810-2276, as the site shows it.
2. **Reviews:** OK to show "4.8 · 350+ reviews"? Both the site and the Trustindex widget show 4.8 from 349 reviews.
3. **"495+ roofs installed last year":** this is in the site's own meta description. Still accurate?
4. **Roof leak repair:** do they offer it as its own service? (From the report.)
5. **Gutter pages:** merge the two into one?
6. **Real prices for a cost page:** the report says this is the biggest opportunity.
7. **Salt Lake City / Sandy / Draper:** do they want city pages there? (From the report.)
8. **Blog author:** name and role.

## Update, 17 Oct 2026

- **Fixed:** the page-header "Free Quote" button linked to a page that doesn't exist on this site. It now says "Book Online" and goes to `/contact/`.
- **Two more broken links on the live site:** `/roof-types/standing-seam-metal-roofing/` (6 links) and `/services/storm-damage/` (7 links). They now point to `/roof-types/metal-roofing/` and `/services/storm-damage-roof-repair/`.
- The preview was republished.
