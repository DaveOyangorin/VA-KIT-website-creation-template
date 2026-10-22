# Course Resources — what's downloaded and what isn't

The Academy attaches **233 resources** across its lessons (a "Resources" box under the video).
These were missed in the original extraction — the `resources` field was run through the
ProseMirror serializer built for lesson bodies, so it silently returned empty for all 572 lessons.
Re-scraped 2026-08-09.

| | Count | Status |
|---|---:|---|
| Google Drive / Sheets resources | 36 | **✅ downloaded** → `files/` (35 files, 13 MB; 1 was a duplicate) |
| Skool-hosted file attachments | 37 | ❌ **not downloaded** — see below |
| Other external links (tools, docs, signups) | 160 | Links only, in the lesson markdown |

---

## ✅ Downloaded — `files/` (35 files, 13 MB)

**n8n workflow JSON (6)** — SEO Reporting · Service Page Blueprint Builder · Reddit SEO Analysis ·
Entity-Based SEO Page Optimization Engine · Wikipedia Citation Opportunity Engine ·
SERP Keyword Visibility Discovery

**Google Sheet templates, as .xlsx (23)** — the companion sheet for nearly every AI Tools &
Workflows automation (Keyword Research, SEO Content Plan, Landing Page Audit, Content Briefing,
Competitor Change Tracker, Internal Linking, Website SEO Data Collector, Marketing Copy
Intelligence, YouTube-to-Blog, Upwork Job Intelligence, Website SEO Health Monitoring, Business
Lead Discovery via Google Maps, SERP Keyword Visibility, Reddit SEO Analysis, Entity-Based SEO,
Wikipedia Citations, SEO Reporting) plus the PAA Scraper sheet, N8N Snippet Generator sheet,
Semantic Branching Resource Pack, LearningSEO.io resource sheet, and the Measure-What-Matters
reporting sheet.

**Documents (6)** — `Our Proprietary Microsite Prompts.pdf` (verified byte-identical to the copy
already in `MAMMATA/`) · Shopify Buy Button guide (PDF) · Microsites Systems Design
(`.drawio` diagram, opens at app.diagrams.net) · Structured Data Expert prompt (`.txt`) ·
Google structured-data type reference (`.txt`) · Google general guidelines (`.html`)

---

## ❌ Not downloaded — 37 Skool-hosted attachments

Skool serves these from `files.skool.com` behind a **signed URL minted only when you click the
resource in the UI**. Every automated route was tried and failed: the `file_id` is not a usable CDN
path (403), the signed URL is not in page data, in-page `fetch` of it is blocked by CORS, and the
browser extension refuses to return any URL containing signature query strings. Chrome has also
begun blocking automatic downloads on this site, which is what broke the blob-download route.

**These need a human to click them.** Open each lesson below and download from its Resources box
into this `files/` folder.

| Lesson | Files | Open |
|---|---|---|
| The Microsite Playbook → One-Click Microsite Builder | `Microsite Builder - Rank Expand Academy.html` | [link](https://www.skool.com/rank-expand-academy/classroom/e93b5251?md=5a29765678244b85b7bb4ec051e3badb) |
| The Microsite Playbook → Add Your AI Receptionist | `vapi_prompt_condensed.txt` | [link](https://www.skool.com/rank-expand-academy/classroom/e93b5251?md=b296665f5fdf49579db95c28cb776609) |
| Offer Library → Quick SEO Audit | `SEO Audit for Seth June 2026.pdf`, `Example email of SEO Audit.png` | [link](https://www.skool.com/rank-expand-academy/classroom/8135b167?md=47b3c10991754c1face99ec9fc9727b2) |
| Offer Library → Local SEO Services | `Example email of Local SEO Services.png` | [link](https://www.skool.com/rank-expand-academy/classroom/8135b167?md=3b5b74432c5b4b44bf56130ec106ddc8) |
| Offer Library → Schema Audit | `Structured Data Opportunities June 2026.pdf`, `Example of email for structured data audit.png` | [link](https://www.skool.com/rank-expand-academy/classroom/8135b167?md=4d2fec943b95464788616d2bd43645ed) |
| Microsite Empire → Website Structure | `Microsites Structure Blueprint.pdf` *(already have)*, `sitemap.txt` | [link](https://www.skool.com/rank-expand-academy/classroom/a0ea58c0?md=513772fc33a74029bd244f9fd2a7689e) |
| Microsite Empire → Upload Your Kirby Install | **`Kirby Base Install - Jan 8 2026.zip`** | [link](https://www.skool.com/rank-expand-academy/classroom/a0ea58c0?md=a974b9c7ccb04603b2caf23ef29c3578) |
| Microsite Empire → Create locations.csv | `locations.csv` | [link](https://www.skool.com/rank-expand-academy/classroom/a0ea58c0?md=a7388df7a8414104b6779635f2433f26) |
| Microsite Empire → Microsite Blueprint for Claude Code | **`Microsite Blueprint.zip`** | [link](https://www.skool.com/rank-expand-academy/classroom/a0ea58c0?md=ccf644bbd5354214b75998db87b3e6bc) |
| Microsite Empire → Setup AI Voice Agent | `vapi_prompt_condensed.txt` | [link](https://www.skool.com/rank-expand-academy/classroom/a0ea58c0?md=670be776cef048df963c5f8973007eb9) |
| AI Tools → SEO Content Plan Workflow | `SEO Content Plan Workfow.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=3893e4c110324c19b6207a4e41556313) |
| AI Tools → Keyword Research Workflow | `Keyword Research Data.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=f3b53e4fde434317821d9b6c82a651b4) |
| AI Tools → Landing Page Audit Workflow | `Landing Page Audit.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=06485544e8484c9eb73e2b958227581c) |
| AI Tools → SEO Content Briefing Workflow | `SEO Content Briefing Workflow.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=d7a689169a2b4f10bcec3fe8d9355267) |
| AI Tools → Automated Competitor SEO Change Tracker | `Automated Competitor SEO Change Tracker.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=9f2c91ea731c43ebaad3146641e26d12) |
| AI Tools → Internal Linking Optimization Workflow | `Internal Linking Optimization Workflow.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=202261815fbc4b39af6dbb426a80b124) |
| AI Tools → SEO Strategy Director | `SEO Strategy Director.json` *(no Drive copy — unique)* | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=aa080326b0bb4ef88aa9f17d61ebae21) |
| AI Tools → Website SEO Data Collector | `Website SEO Data Collector.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=90d43a6fe36f479499a18f90dbbba189) |
| AI Tools → Marketing Copy Intelligence Workflow | `Marketing Copy Intelligence Workflow.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=548cabd1ae9a4dceb4fe606d9d58d9df) |
| AI Tools → YouTube-to-Blog Automation Pipeline | `YouTube-to-Blog Automation Pipeline.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=95e0ece534ed4e9bac4ccc6698b9be2e) |
| AI Tools → Upwork Job Intelligence Digest | `Upwork Job Intelligence Digest v2.0.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=571cff68c83a4da2a52158197370cf06) |
| AI Tools → Website SEO Health Monitoring | `Website SEO Health Monitoring.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=06bebdb1ec7146a59fabc63f1969bfcc) |
| AI Tools → Business Lead Discovery via Google Maps | `Business Lead Discovery Google Maps.json` | [link](https://www.skool.com/rank-expand-academy/classroom/cf75b5d7?md=cc72a89ba10341879715cd89f952bee5) |
| Automation Accelerator → (Claude setup) | **`CLAUDE.md`** | [link](https://www.skool.com/rank-expand-academy/classroom/52339bb6?md=1d1c1602a3ce42b58f75348ca48bb79e) |
| Claude Code Building → SEO Master Class | **`SEO Master Class.pdf`** | [link](https://www.skool.com/rank-expand-academy/classroom/8f8387cf?md=c79c8a728c74422492cc246823b93732) |
| Claude Code Building → LLM Wiki Slidedeck | `LLM-Wiki-Deck.html` | [link](https://www.skool.com/rank-expand-academy/classroom/8f8387cf?md=1bbbe5c55d594133a8325c22b5b55182) |
| Claude Code Building → SFTP Microsite Build | `Microsite-Live-Build-Deck.html` | [link](https://www.skool.com/rank-expand-academy/classroom/8f8387cf?md=512d5cd842cc4ceeb7d6189cd58e92d3) |
| Ranking in AI Overviews → Snippet Generator | `Semantic_Optimizations.json`, `HTTP Tool.json`, `DataforSEO SERP.json` | [link](https://www.skool.com/rank-expand-academy/classroom/a86cc66d?md=7b209a84a5ab4550bf895415535e66e6) |
| Ranking in AI Overviews → PAA Scraper | `PAA_scraper_Apps_Script.gs` | [link](https://www.skool.com/rank-expand-academy/classroom/a86cc66d?md=3d62a7a9a21a4966bd4d8e61d3e90845) |
| How To Dominate AI Search | `2509.08919v1.pdf` *(research paper)* | [link](https://www.skool.com/rank-expand-academy/classroom/90a2d1d1?md=b0018ba4a30d4ed39c4acce1866bb2b4) |
| On-Page SEO Content Frameworks | `On-Page SEO Content Structure.png` | [link](https://www.skool.com/rank-expand-academy/classroom/f78e44ad?md=b174362286e344de8f8866ee9b8ac2e0) |
| Technical SEO Mastery → Indexation | `Crawling vs. Indexing.png` | [link](https://www.skool.com/rank-expand-academy/classroom/ee5f7442?md=95c52f5ed261493db1b1816f159b7371) |

### Priority if you only do some
1. `Kirby Base Install - Jan 8 2026.zip` and `Microsite Blueprint.zip` — the actual build artifacts
2. `SEO Master Class.pdf` and `CLAUDE.md`
3. `SEO Strategy Director.json` — the one n8n workflow with no Google Drive duplicate
4. `sitemap.txt`, `locations.csv`, `vapi_prompt_condensed.txt`, `PAA_scraper_Apps_Script.gs`

Most other Skool-hosted `.json` workflows already have a Drive copy in `files/`, so they're the
lowest priority.

---

*Also worth knowing: 90 inline lesson images are referenced as remote `assets.skool.com` URLs in
the course markdown rather than downloaded. They render only while those URLs stay live.*
