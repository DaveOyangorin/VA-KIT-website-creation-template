> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# Optimizing Your Website for Generative AI Features on Google Search

- **Source:** https://developers.google.com/search/docs/fundamentals/ai-optimization-guide (guide) and https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing (announcement)
- **Type:** Official Google documentation + Search Central blog
- **Published / Last updated:** Guide last updated 2026-06-15 UTC (mythbusting section revised with explicit llms.txt/markdown wording). Original announcement posted Friday, May 15, 2026 by John Mueller, Google Search.
- **Scraped by FRAVATA:** 2026-06-01. Re-verified 2026-06-16.

## What it says
- Core premise: SEO is still foundational for AI search because "our generative AI features on Google Search are rooted in our core Search ranking and quality systems." There is no separate "AEO/GEO" discipline to chase.
- **Indexing eligibility:** To appear in generative AI features, a page must be indexed and eligible to be shown in Google Search with a snippet, meeting the standard Search technical requirements.
- **Content attributes Google wants:**
  - Unique perspective / non-commodity content — don't recycle what's already on the web; provide a viewpoint that stands out.
  - Helpful, reliable, people-first content (not common-knowledge summaries).
  - Audience-first organization — clear paragraphs, sections, and headings written for humans.
  - High-quality, relevant images and videos where appropriate.
  - Local, shopping, image, and video content where relevant (the guide covers these specifically).
  - Do NOT mass-produce "separate content for every possible variation" to manipulate rankings (that is scaled content abuse).
- **Technical structure:** content must be crawlable; use semantic HTML; follow JavaScript SEO best practices if using frameworks; maintain good page experience across devices; reduce duplicate content.
- **Mythbusting — Google explicitly says these are NOT required:**
  - `llms.txt` files or other "special" markup. **(Reinforced 2026-06-15:** Google revised the guide's mythbusting section with explicit wording — `llms.txt` files "won't harm (nor help) your visibility or rankings in Google Search, as Google Search ignores them," and "Google Search itself doesn't use" machine-readable files, AI text files, markup, or Markdown. Restated, not a new rule. Source: AI optimization guide #mythbusting via SEL https://searchengineland.com/google-says-llms-txt-files-wont-harm-or-help-your-search-rankings-480264 2026-06-15. Same position aired in the "Search Off the Record" podcast — Mueller/Splitt, GSC, 2026-06-15.)
  - "Chunking" content into tiny pieces.
  - Rewriting content specifically for AI systems.
  - Seeking inauthentic "mentions" across the web.
  - Over-focusing on structured data (helpful but not required).
- **How the AI features work (context, not action items):**
  - Retrieval-Augmented Generation (RAG) / "grounding" — relies on core Search ranking to retrieve relevant, fresh pages.
  - Query fan-out — Google generates concurrent related queries to fetch additional results.
- **Emerging:** stay informed about AI agents interacting with sites (browser agents, new protocols). Marked as early/evolving guidance.
- **Measurement (added 2026-06-05):** Google launched **Search Generative AI performance reports in Search Console** (Search Central blog, 2026-06-03/06: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports). Gives dedicated impression data for AI Overviews, AI Mode, and generative features in Discover — broken out by pages, countries, devices, and dates (hourly→monthly). **No click data.** Rolling out to a subset of sites. Search Console also exposes controls to limit/block content appearing in AI responses (via existing `nosnippet` / preview controls). This is a measurement + opt-out surface, NOT a new ranking lever — the optimization guidance above is unchanged.

## What MAMMATA must do
- Treat AI-feature optimization as ordinary good SEO — do NOT add `llms.txt`, AI-specific rewrites, or content chunking to any client site; they are confirmed non-factors.
- Confirm every key page is indexable and snippet-eligible (no `noindex`, no `nosnippet`, no robots blocks) — that is the entry ticket to AI features.
- For each client, ensure pages carry a genuine unique angle (e.g., the health client auto-accident pillar's first-hand clinical detail; plumbing / auto repair clients local service specifics) rather than commodity boilerplate.
- Verify crawlability and JS rendering on each site; flag any framework that hides content behind client-side rendering.
- Add relevant high-quality images/video to thin service and location pages.
- Do not create near-duplicate pages per city/variation purely for coverage (ties to scaled content abuse + the existing "city pages low ROI" note for the health client).

## Audit checks (scorable yes/no)
- [ ] Key pages are indexed and snippet-eligible (no noindex/nosnippet/robots block).
- [ ] Site contains NO `llms.txt` or AI-specific markup added in a misguided "GEO" attempt.
- [ ] Primary content is crawlable without requiring JS execution to read main text.
- [ ] Each money page has a unique, non-commodity angle vs. competitors.
- [ ] No mass-produced per-variation/per-city duplicate pages exist solely for rankings.
- [ ] Relevant, high-quality images/video present on core service pages.
- [ ] Page experience (mobile, speed) is acceptable across devices.
