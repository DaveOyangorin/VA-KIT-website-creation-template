> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# AI Search: Schema, Crawler Access & Freshness — 2026 Reference

Compiled 2026-08-25. Source-verified by direct fetch of primary documentation.
Every claim is tagged. **PROVEN** = primary vendor doc or controlled study.
**PLAUSIBLE** = credible study, sample size stated. **UNVERIFIED** = do not put in a client deck.

---

## PART 1 — SCHEMA: WHAT STILL WORKS IN 2026

### 1.1 The settled facts (already established, do not re-litigate)

- Schema does **not** raise AI citations in aggregate. Ahrefs matched difference-in-differences,
  1,885 pages that added JSON-LD Aug 2025–Mar 2026 vs 4,000 matched controls:
  **Google AI Overviews −4.6%** (statistically significant), AI Mode +2.4% and ChatGPT +2.2%
  (both indistinguishable from zero). Ahrefs pooled all schema types and did not break down by type.
  **PROVEN** — https://ahrefs.com/blog/schema-ai-citations/
- Google's official position, verbatim: *"You don't need to create new machine readable files,
  AI text files, or markup to appear in these features. There's also no special schema.org
  structured data that you need to add."*
  **PROVEN** — https://developers.google.com/search/docs/appearance/ai-features
- Eligibility rule for AI Overviews / AI Mode, verbatim: *"a page must be indexed and eligible to
  be shown in Google Search with a snippet… There are no additional technical requirements."*
  This means **Google's normal canonicalisation and indexing pipeline governs AI Overviews citations.**
  **PROVEN** — same URL.
- Microsoft is the **only** AI vendor on record confirming schema use. Fabrice Canel, Bing principal
  PM, SMX Munich, March 2025: schema markup helps Microsoft's LLMs including Copilot understand content.
  **PROVEN** — https://searchengineland.com/microsoft-bing-copilot-use-schema-for-its-llms-453455
- OpenAI, Anthropic and Perplexity crawler docs contain **zero** mention of schema.org, JSON-LD,
  microdata or RDFa. Verified by direct fetch of all three.
  **PROVEN (absence)** — developers.openai.com/api/docs/bots · support.claude.com/en/articles/8896518 ·
  docs.perplexity.ai/guides/bots

### 1.2 DEAD TYPES — remove from all new builds

| Type | Status | Dates |
|---|---|---|
| **FAQPage** | **DEAD.** Produces nothing. | Aug 8 2023 restricted to authoritative gov/health sites only. **May 7 2026** rich results stopped appearing. June 2026 search-appearance filter, Search Console report and Rich Results Test support removed. Aug 2026 Search Console API support removed. **PROVEN** — developers.google.com/search/updates |
| **HowTo** | **DEAD. Documentation removed entirely.** | Aug 8 2023 restricted to desktop only. Sept 2023 removed from desktop too. Google: the rich result *"is no longer shown in search results on both desktop and mobile devices."* **PROVEN** |
| **Sitelinks searchbox** (`WebSite` + `SearchAction`) | **DEAD** | Announced Oct 21 2024, retired globally **Nov 21 2024**. `WebSite` markup for *site names* still supported. **PROVEN** — developers.google.com/search/blog/2024/10/sitelinks-search-box |
| course info, estimated salary, learning video, special announcement, vehicle listing | **REMOVED** | Retirement banners June 12 2025, documentation removed **Sept 9 2025**. **PROVEN** |
| ClaimReview, book actions | **RETIRED** | Banners added June 12 2025. **PROVEN** |
| practice problem | **REMOVED** | Deprecated Nov 5 2025, docs removed Jan 6 2026. **PROVEN** |
| **Service** | **Never supported.** Absent from the entire Search Gallery. No rich result, ever. **PROVEN** |
| **Dataset** | **Not used by Google Search.** Google changelog Nov 5 2025: *"Dataset structured data is only used by Dataset Search, and not Google Search."* **PROVEN** |
| **Speakable** | **Beta. US-based news publishers only, English only, Google Assistant smart speakers.** No visible result. Dead weight for any local-service or e-commerce client. **PROVEN** |

**Removal guidance:** Google's standing position is that unused structured data does not cause
problems. Do not bill a client to strip dead markup — just stop shipping it. **PLAUSIBLE**
(Google's 2023 wording, not restated on the 2026 FAQ page).

### 1.3 LIVE TYPES — still earn rich results

| Type | Rich result | Notes |
|---|---|---|
| **Product** | Product snippet, merchant listing, variants, loyalty program, return policy, shipping | The only type family with a positive AI-citation signal (see 1.5). Offer floor: `price`, `priceCurrency`, `availability`. **PROVEN** |
| **Organization** | No standalone rich result, but the documented entity path | Google verbatim: helps *"disambiguate your organization in search results"*; properties *"can influence visual elements in Search results (such as which `logo` is shown in Search results and your knowledge panel)."* `iso6523`/`naics` used *"behind the scenes to disambiguate."* **PROVEN** |
| **LocalBusiness** (+ subtypes: `Physician`, `MedicalBusiness`, `CleaningService`, `HomeAndConstructionBusiness`…) | Local knowledge panel | **PROVEN** |
| **Review / AggregateRating** | Review snippet (stars) | ⚠️ See the self-serving trap in 1.4. **PROVEN** |
| **Article / NewsArticle** | Enhanced title/image/date | Verbatim: *"there's no markup requirement to be eligible for Google News features like Top stories."* **PROVEN** |
| **BreadcrumbList** | Breadcrumb trail | Scope line: *"available on **desktop**."* Google: *"provide breadcrumbs that represent a typical user path… instead of mirroring the URL structure."* **PROVEN** |
| **Event** | Event experience | Unique leaf URL per event required. *"Virtual experiences that have no real-world component aren't supported."* Must be publicly bookable. **PROVEN** |
| **JobPosting** | Job experience | No deprecation banner; region list intact as of doc update 2025-12-18. **PROVEN** |
| **Recipe** | Recipe rich result + host carousel via `ItemList` | **PROVEN** |
| **VideoObject** | Video rich result, key moments (`Clip`/`SeekToAction`), LIVE badge (`BroadcastEvent`) | **PROVEN** |
| **ProfilePage** | Powers Discussions and Forums; author identity | **PROVEN** |
| **QAPage / DiscussionForumPosting** | Forum/Q&A features | **New March 24 2026:** `commentCount`, `digitalSourceType` added to QAPage; `sharedContent`, `commentCount`, `digitalSourceType` to DiscussionForumPosting. `digitalSourceType` declares AI vs human origin — `TrainedAlgorithmicMediaDigitalSource` for LLM output. Omitting it = Google assumes human. **PROVEN** |

### 1.4 ⚠️ THE SELF-SERVING REVIEW TRAP — check this on every local client

Google verbatim: *"If the entity that's being reviewed controls the reviews about itself, their
pages that use `LocalBusiness` or any other type of `Organization` structured data are ineligible
for star review feature."* **PROVEN** —
https://developers.google.com/search/docs/appearance/structured-data/review-snippet

**Translation:** a local business putting `AggregateRating` or first-party `Review` markup about
itself on its own site **gets no stars**. This is extremely common on agency-built local sites and
is almost always wasted work. Stars for a local business come from **Google Business Profile**,
not from markup.

Types that ARE eligible for review snippets: Book, Course, Event, LocalBusiness*, Movie, Product,
Recipe, SoftwareApp, plus CreativeWorkSeason/Series, Episode, Game, MediaObject, MusicPlaylist,
MusicRecording, Organization* — (* only when reviews are not self-controlled).

### 1.5 Do AI engines actually parse schema? Per-type evidence

**Fischman (Feb 2026)** — the only per-type controlled dataset. 730 AI citations from ChatGPT
(GPT-4o browsing) and Gemini (1.5 Pro grounding), 75 commercial queries, 1,006 unique pages,
Google top-10 via SerpAPI as control, Ahrefs DR covariate, GEE models.
- Pooled: schema presence OR = 0.546, p < .001 (negative).
- Corrected within-Google: OR = 0.678, **p = .296 — null.**
- **Organic rank dominates: OR = 0.762 per position, p < .001.** Position 1 → 43% citation rate;
  position 7 → 5%.
- **Generic schema (Article, Organization, BreadcrumbList) = zero measurable advantage.**
- **Attribute-rich Product/Review schema: 61.7% vs 41.6% cited, p = .012.** Strongest for DR ≤ 60.
- **PLAUSIBLE** (n=730 citations, preprint) — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=6284518

**SE Ranking** (129,000 domains / 216,524 pages / 20 niches / 100,000 prompts, XGBoost + SHAP):
*"Pages with FAQ schema markup have 3.6 citations, compared to 4.2 without."* Their conclusion:
*"schema markup is icing on the cake."* **PLAUSIBLE** — https://seranking.com/blog/how-to-optimize-for-chatgpt/

**Volpini et al., arXiv:2603.10700** (submitted 11 Mar 2026, 2,439 evaluations / 349 queries,
4 domains, Vertex AI Vector Search + Google ADK): *"while JSON-LD markup alone provides only
modest improvements"* (d = 0.18), a dereferenceable **entity hub page** with agent instructions,
breadcrumbs and interlinking achieved **+29.6% / +29.8% accuracy**. **The win is content
architecture, not markup.** **PLAUSIBLE**

### 1.6 Does JSON-LD survive into the model? Contradictory — do not assert either way

- **SearchVIU, Oct 30 2025.** One test page, 8 price-injection scenarios, 5 engines.
  **JSON-LD-only, JSON-LD-via-JS, hidden microdata and hidden RDFa all scored 0/5 engines.**
  ChatGPT and Gemini picked up *visible* microdata and *visible* RDFa — but the value was in
  rendered text, so that measures reading HTML, not parsing markup. **Claude scored 0/8 on every
  scenario.** Verbatim: *"JSON-LD Schema Markup is NOT extracted by ANY system during direct fetch."*
  **PLAUSIBLE** (n=1 page) — https://www.searchviu.com/en/schema-markup-and-ai-in-2025-what-chatgpt-claude-perplexity-gemini-really-see/
- **Williams-Cook "Duck Test", Feb 2026.** Address placed *only* inside deliberately invalid JSON-LD
  (`@type: MallardEnterprise`). **Both ChatGPT and Perplexity returned it.** His conclusion:
  *"they were not parsing it as schema… reading the visible-ish text of the page, picking out the
  bit that looked like an address."* **PLAUSIBLE** —
  https://markwilliamscook.substack.com/p/schema-llms-and-the-low-bar-for-evidence
- **No primary source exists.** An OpenAI Developer Community thread asking exactly this got **no
  OpenAI staff response**. **UNVERIFIED.**

**Both authors converge on the same mechanism: tokenised as prose, not parsed as a graph.**

**The one operational rule, supported by both studies and by Google's own policy:
NEVER put a fact only in JSON-LD.** Google verbatim: *"Don't mark up content that is not visible
to readers of the page."* Structured data must be *"a true representation of the page content."*
**PROVEN** — https://developers.google.com/search/docs/appearance/structured-data/sd-policies

**Microdata / RDFa: no evidence any AI engine has a parser for either. Stay on JSON-LD.**

---

## PART 2 — CRAWLER ACCESS (the highest-value technical audit)

### 2.1 ⚠️ TIME-CRITICAL: Cloudflare default change, September 15 2026

Announced July 1 2026. **PROVEN** — https://blog.cloudflare.com/content-independence-day-ai-options/ ·
https://developers.cloudflare.com/changelog/post/2026-07-01-ai-traffic-options/

- Verbatim: *"New domains onboarding to Cloudflare receive updated defaults: Bots classified as
  Training or as Agent are blocked on pages that display ads, while Search remains allowed."*
- Verbatim: *"Multi-purpose crawlers that combine Search and Training will be affected by the new
  defaults to block Training."* Cloudflare names them: **Googlebot, Applebot and BingBot.**
- Opt-out before Sept 15 at `dash.cloudflare.com/?to=/:account/:zone/security/settings`.
- The legacy **"Block AI bots"** toggle deprecates Sept 15 2026. The old toggle deliberately spared
  mixed-purpose bots; the new policies **do not**.
- Scope caveat: primary sources say **"new domains onboarding to Cloudflare"** only. Claims that it
  also hits existing free zones are **UNVERIFIED** — check per zone.

**Prior change:** July 1 2025 "Content Independence Day" — *"Every new Cloudflare domain now blocks
all known AI crawlers by default."* **PROVEN** —
https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/

### 2.2 The documented accidental-block case

**August 4 2026, Search Engine Journal (Roger Montti).** Site owner set Cloudflare **AI Training =
Block**; **Googlebot and Bingbot immediately received HTTP 403 on sitemap fetches.** Reversed
instantly on disabling. Cloudflare's AI Crawl Control dashboard showed the bots as *blocked*, not
spoofed — ruling out impersonation. Root cause is Cloudflare's own documented mixed-crawler rule.
**John Mueller asked the reporter to DM him** so Google could investigate. **PROVEN** —
https://www.searchenginejournal.com/report-that-cloudflare-ai-bot-blocking-prevents-googlebot-from-indexing-sites/584673/

**Symptom pattern to look for in Search Console:** Page Indexing → *"Blocked due to access
forbidden (403)"*. URL Inspection → *"Page fetch: Failed"* (network/WAF layer, independent of
robots.txt — this is the firewall tell, as opposed to *"blocked by robots.txt"*).

### 2.3 The black-box probe (no server access needed)

Run a browser UA and each bot UA against the same URL, same IP, same minute, ≥1s apart.

| Chrome UA | Bot UA | Verdict |
|---|---|---|
| 200 | 200 | No block. Crawler reachable. |
| **200** | **403 / 429** | **UA blocklist — actionable finding.** |
| 403 | 403 | Not AI-specific. Your IP/ASN/geo is blocked, or the site denies all non-browser clients. Re-test from another network. |
| 200 | challenge page | Ambiguous by design. Escalate to logs. |

**⚠️ Never write "GPTBot is blocked" from a spoofed-UA 403 alone.** A spoofed UA from an office IP
*is* an impersonator, and any IP-verifying system should block it. Write instead: *"a request
identifying itself as GPTBot from an unverified IP receives 403 while a browser request receives
200. This proves a user-agent-conditional rule exists. Confirming the genuine GPTBot IP range is
also blocked requires access logs."*

**⚠️ Google-Extended and Applebot-Extended have NO user agent.** They are robots.txt opt-out tokens
and make zero requests. Any tool reporting "Google-Extended: 403" is producing a fabricated result.
Test them by reading robots.txt. **PROVEN** —
https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers

### 2.4 Verified bot identity sources (IP lists — there is no rDNS shortcut for AI bots)

- OpenAI: `https://openai.com/gptbot.json`, `searchbot.json`, `chatgpt-user.json` — **PROVEN**
- Anthropic, all three bots in one file: `https://claude.com/crawling/bots.json` — **PROVEN**
- Perplexity: `https://www.perplexity.com/perplexitybot.json`, `perplexity-user.json` — **PROVEN**
- Google: reverse-DNS then forward-DNS; hostname must end `googlebot.com`, `google.com` or
  `googleusercontent.com`. **PROVEN** —
  https://developers.google.com/crawling/docs/crawlers-fetchers/verify-google-requests

**Only pre-AI crawlers (Google, Apple, Common Crawl, Bing) support reverse DNS.
Every AI-native crawler is IP-list-only.**

### 2.5 Host defaults worth knowing

- **Netlify** — does not block AI crawlers. Static host, no WAF in front by default. Novarte's
  client sites are on Netlify, which removes this entire risk category.
- **Cloudflare** — see 2.1. The one to check on every new client.
- Other host defaults (WP Engine, SiteGround, AWS WAF, Akamai, Fastly, Imperva) were researched but
  **NOT verified in this pass** — see the quarantine section at the end.

---

## PART 3 — SITEMAPS, CANONICAL, FRESHNESS

### 3.1 Do AI crawlers read XML sitemaps? Mostly unknown.

- **OpenAI, Anthropic, Perplexity, Meta, Amazon: SILENT.** No mention of sitemaps, lastmod,
  canonical or crawl scheduling anywhere in their crawler docs. Verified by direct fetch.
  **PROVEN (absence)**
- **Bing is the only first-party confirmation** and it explicitly frames sitemaps for AI search.
  Fabrice Canel + Krishna Madhavan, July 31 2025: *"Bing will attempt to fetch it immediately upon
  submission. After that, it will revisit your sitemap on a regular basis, typically at least once
  per day."* **PROVEN** —
  https://blogs.bing.com/webmaster/July-2025/Keeping-Content-Discoverable-with-Sitemaps-in-AI-Powered-Search
- **Google AI Overviews / AI Mode ride the Google Search index**, so normal Googlebot sitemap
  behaviour applies. **PROVEN** (via the ai-features eligibility rule).
- **Log evidence is thin.** WISLR, 48 days of own-domain CDN logs (2026-02-01 to 2026-03-20,
  71,603 total requests, 12,099 AI bot requests, 19 bots): sitemap.xml hits were Bingbot 139,
  Claude-SearchBot 135, Meta-WebIndexer 30, **ClaudeBot 14 (first ever March 18)**, **GPTBot 2
  (first ever March 19)**. Also: **zero AI bots requested /llms.txt across 48 days.**
  **PLAUSIBLE but weak — n=1 domain.** https://www.wislr.com/articles/ai-bot-behavior-log-analysis/

**Verdict: keep sitemaps correct and fetchable — cheap insurance, and the Aug 2026 Cloudflare
incident shows sitemap 403s are a real failure mode. But do not sell "AI sitemap optimisation."**

### 3.2 Does `<lastmod>` drive AI crawler re-fetch? No evidence either way.

- **Google baseline (PROVEN):** *"Google ignores `<priority>` and `<changefreq>` values."* `<lastmod>`
  is used only when *"consistently and verifiably… accurate"* and must reflect *"the last
  significant update to the page — an update to the copyright date is not."*
  https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
  Trust is effectively **binary per site** — wrong lastmods make Google ignore all of them.
- **For OpenAI / Anthropic / Perplexity / Meta: no vendor statement, no published study.
  COULD NOT CONFIRM.** Anyone claiming lastmod drives GPTBot/ClaudeBot re-crawl is asserting
  something with no published basis.

### 3.3 Canonical and syndication

- **Google-only:** normal canonicalisation governs AI Overviews/AI Mode citations. **PROVEN.**
- **Glenn Gabe, 2025-09-16** — nine publishers syndicating to Yahoo/MSN, tested across ChatGPT,
  Perplexity, Claude, Gemini. Verbatim: *"Sometimes the original url ranked in AI search, sometimes
  the syndicated content on third-party sites like Yahoo or MSN ranked, and sometimes they both
  ranked."* **Perplexity consistently cited the syndication partner.** **Claude frequently cited
  both URLs side by side.** Gemini often cited neither. On cross-domain canonical: *"not
  foolproof… both urls are often indexed."* His recommendation: **noindex the syndicated copy.**
  **PLAUSIBLE — qualitative, 4 documented cases, no frequency percentages.** This is the best
  evidence that exists and it is not quantified.
  https://www.gsqi.com/marketing-blog/ai-search-and-syndicated-content/
- **ChatGPT appends `utm_source=chatgpt.com`** to outbound citation links. Practical consequence:
  every AI-referred visitor lands on a unique URL variant, so full-page and CDN caches miss —
  **your best-cited content serves slowest to AI-referred traffic.** **PROVEN by observation.**
- Claims that AI engines cite AMP/print/m-dot URLs instead of the canonical: **COULD NOT CONFIRM.**

### 3.4 FRESHNESS — the benchmark numbers to audit clients against

**Median age of cited content (peer-reviewed, EDBT/ICDT 2026 Workshops, arXiv:2601.16858):**

| Engine | Consumer electronics | Automotive |
|---|---|---|
| Claude 4.5 Sonnet | **62.3 days** | 148.0 days |
| GPT-4o | 79.8 days | 162.2 days |
| Perplexity Sonar Pro | 90.4 days | 216.6 days |
| Google Search | 130.4 days | 492.9 days |

*Answer engines cite newer material than Google on the median.* **PROVEN (peer-reviewed).**

**Mean age (Ahrefs, 16,975,000 cited URLs, 2025-07-28) — Claude not included:**

| Surface | Mean days since publication | % fresher than organic |
|---|---|---|
| ChatGPT | **958** | 32.3% |
| Copilot | 1,056 | 25.4% |
| Gemini | 1,118 | 21.1% |
| Perplexity | 1,166 | 17.6% |
| Google AI Overviews | 1,432 | −1.1% |

All AI surfaces average **1,064 days vs 1,432 organic = 25.7% fresher** on publication date, but
only **13.1% fresher** on last-update date. Ahrefs' own caveat: average cited age is still 2.9
years — **long-lived content dominates AI citations.** **PROVEN.**
https://ahrefs.com/blog/do-ai-assistants-prefer-to-cite-fresh-content/

**Use medians for editorial planning. Do not plan against the mean — it is dragged by an
evergreen long tail.**

**Share of citations from pages updated within one year (Seer Interactive, June 2026 —
7,683 pages, 47,097 citations, Mar–Jun 2026, four verticals):**
**Gemini 78% · ChatGPT 73% · Perplexity 65%.** Perplexity is most forgiving of older content.
**PLAUSIBLE.** — https://www.seerinteractive.com/insights/study-content-recencys-impact-on-ai-visibility-in-2026

### 3.5 ⚠️ TWO CLAIMS TO REJECT AND ONE TO KEEP

- ❌ **"95% of ChatGPT citations are from content under 10 months old" — REFUTED. Do not use.**
  Traced to a **verbal remark by Ethan Smith (Graphite) on a Webflow AEO webinar**. No published
  study, methodology or sample size. Attributions to SE Ranking are **false** — that study contains
  no "95%" and no "10 months", and its own data contradicts it (*"very new content (up to 2 months
  old) averages 3.6 citations"* vs *"1.5–5 years… 3.1"*). Directly refuted by Ahrefs: ChatGPT's mean
  cited-page age is **958 days (~2.6 years)**, median ~500 days. **Not compatible with 95% under 10 months.**
- ❌ Also reject, all with **no traceable original**: *"76.4% of most-cited pages updated within 30
  days"*, *"content under 30 days earns 3.2× more citations"*, *"4.5-week citation half-life"*,
  *"1-year half-life"*.
- ✅ **"Claude is ~3× more likely than ChatGPT to cite 2–4-week-old content" — SURVIVES.**
  First-party Muck Rack, from a **25M+ cited-link** dataset across ChatGPT, Claude and Gemini,
  17 industries. Verbatim: *"Claude has a citation sweet spot in the past 10 weeks, whereas ChatGPT
  shows a sharp citation drop-off after about one week."* Independently corroborated in direction
  by the peer-reviewed median table above (Claude freshest at 62.3 days).
  **PLAUSIBLE** — per-bucket methodology is behind a lead-gen form.
  https://muckrack.com/blog/how-claude-cites-media

### 3.6 UPDATE beats PUBLISH NEW — best-supported freshness finding

- **SE Ranking (n=216,524 pages):** content **updated within the past three months averages 6.0
  citations vs 3.6** for older equivalents (**+67% on the same page**). Brand-new content (≤2
  months old) averages **3.6 — statistically indistinguishable from 1.5–5-year-old content at 3.1.**
  **Publication recency alone buys almost nothing; update recency nearly doubles citations.**
- **Seer Interactive (independent corroboration):** *"The freshness LLMs reward is being
  manufactured by updates, not by new publishing."* 72% of cited pages appeared fresh by
  last-update date but only 42% were first published in the last year. Refreshed older content
  outperformed genuinely new pages **across all four verticals.**
- **Counterweight (PROVEN):** in Ahrefs' 17M dataset the freshness premium on *last-updated* date
  (13.1%) is **half** the premium on *publication* date (25.7%).
- ⚠️ **No true controlled A/B exists.** Nobody has published *update URL A vs publish new URL B,
  matched topics, measured citation*. The strongest defensible statement is that **two independent
  observational datasets agree that update recency correlates with AI citation.**

### 3.7 Publish-to-first-citation lag (the only controlled experiment)

**Semrush, December 2025.** 81 FAQ-style test pages published Sept 2025 on a DR-84 domain, tracked
daily for 30 days across ChatGPT Search and Google AI Mode.

| Day | Google AI Mode | ChatGPT Search |
|---|---|---|
| 1 | 36% | 10% |
| 7 | 56% | 17% |
| 14 | 48% | 35% |
| 30 | 26% | **42%** |
| Peak | 59% | 42% |

**Google AI Mode is fast but volatile** — cites within 24h then decays. **ChatGPT Search is slow
but sticky** — accumulates and retains. **Neither ever cited all 81 pages.**
⚠️ This study was surfaced in research but **NOT independently verified in this pass** — confirm
before client use.

### 3.8 Crawl ≠ citation

High GPTBot volume is OpenAI **building its index**, not evidence of AI visibility. The bots that
correlate with actual answers are **ChatGPT-User, OAI-SearchBot, Claude-SearchBot, Perplexity-User**.
Conflating them is the most common error in this space.

---

## PART 4 — THE REPEATABLE CLIENT AUDIT

Run this on every new client and at every quarterly review.

1. **Host + WAF fingerprint.** `curl -sSI https://site/` → read `server`, `cf-ray`, `x-nf-request-id`,
   `x-vercel-id`. Netlify/Vercel = low risk. **Cloudflare = check §2.1 before Sept 15 2026.**
2. **robots.txt, fetched as a browser.** Look for AI-bot Disallow lines and `Content-Signal:` lines.
   This is the only IP-independent test, and the only way to test Google-Extended / Applebot-Extended.
3. **Crawler probe matrix.** Browser UA + 8–10 bot UAs against the homepage, ≥1s apart.
   Apply the §2.3 table. All 200 = pass.
4. **Snippet controls — DO NOT SKIP.** A page can pass every crawler test and still be ineligible
   for AI citation. Google's ai-features doc names `nosnippet`, `data-nosnippet`, `max-snippet` and
   `noindex` as *the* controls for AI Overviews and AI Mode appearance. **PROVEN** —
   https://developers.google.com/search/docs/appearance/ai-features
   Check all three layers, on **every** page in the sitemap, not a sample:
   - `<meta name="robots">` and `<meta name="googlebot">` — read the `content` attribute only
   - the `X-Robots-Tag` HTTP response header (can be set per-path by a host config or `_headers` file)
   - inline `data-nosnippet` attributes in the body

   ⚠️ **Grep carefully.** Matching the bare word `none` against whole-page HTML produces mass false
   positives from CSS (`display:none`, `border:none`). Scope the match to the `content=` attribute
   of a robots meta tag, or you will report blockers that do not exist.

   **Absence of a directive = no restriction** (Google chooses the limit). `index, follow` is a
   no-op — those are already the defaults. The pro-visibility setting is
   `max-snippet:-1, max-image-preview:large, max-video-preview:-1`, which removes the ceiling.

5. **Schema inventory.** Extract every `"@type"` from the homepage and 2–3 template pages.
   Flag: FAQPage, HowTo, SearchAction, Speakable, Service, Dataset (all dead weight).
   Flag: self-serving AggregateRating/Review on a LocalBusiness or Organization (no stars).
   Confirm: canonical present, `sameAs` populated, `@id` used for entity linking.
6. **Sitemap health.** URL count, `<lastmod>` coverage (should be 100%), newest and oldest dates.
7. **Freshness distribution.** Bucket lastmod into ≤30d / 31–90d / 91–180d / 181–365d / >1yr.
   Benchmark against §3.4: target ≥73% updated within one year to match ChatGPT's cited pool.
8. **Search Console.** Page Indexing → *"Blocked due to access forbidden (403)"*.
   URL Inspection → *"Page fetch: Failed"* = firewall. Crawl Stats → Host status.

**What NOT to sell:** llms.txt (settled — ~zero fetches), "AI sitemap optimisation", schema as an
AI-citation lever, or removal of dead FAQ/HowTo markup.

**What DOES move the needle, in order of evidence strength:**
1. Organic rank (Fischman: OR = 0.762/position — position 1 = 43% citation rate, position 7 = 5%).
2. Referring domains (SE Ranking: strongest single predictor).
3. Content depth (SE Ranking: >20,000 chars = 10.18 citations vs 2.39 for very short pages;
   sections of 120–180 words between headings = 4.6 vs 2.7 for sections under 50 words).
4. **Updating existing URLs** on a ≤3-month cadence (§3.6).
5. Crawler access being unblocked (binary — worth zero if broken, capped if fine).

---

## ⚠️ QUARANTINE — RESEARCHED BUT NOT VERIFIED IN THIS PASS

Re-verify each before putting any of it in a client deliverable:

- Vendor-by-vendor WAF defaults: WP Engine (reported 429s on ClaudeBot UA), SiteGround (reported
  to block training crawlers by default), AWS WAF `CategoryAI`, Fastly NG-WAF signal names,
  Akamai reference-number formats, Imperva blocks returning HTTP 200, Sucuri.
- Cloudflare dashboard menu paths, AI Labyrinth, Pay Per Crawl (402), Content Signals Policy,
  Super Bot Fight Mode behaviour, the verified-bot category taxonomy.
- Web Bot Auth / RFC 9421 adoption status.
- Free external AI-crawler testing tools and their limits.
- Semrush 81-page lag experiment (§3.7), Writesonic 62-element crawler study,
  Vercel/MERJ crawler dataset, the ChatGPT "labrador" index reporting.

**Anything above this line was verified by direct fetch of the cited source on 2026-08-25.**
