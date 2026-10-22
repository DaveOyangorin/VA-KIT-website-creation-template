> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# Top SEO / AEO GitHub Repos — Master File

**Owner:** FRAVATA (Novarte AI) · standing `/github-hunt` task
**Last verified:** 2026-06-06
**Method:** GitHub REST API (`/search/repositories` sorted by stars + per-repo `/repos/{owner}/{name}` for exact stars, last-push date, license, archived flag), cross-checked against GitHub search result pages. A repo is **[CONF]** only after its API record + README were opened and confirmed real, maintained, and license-checked.

**Ranking logic (per definition):** 1) practical value to Novarte's real work — local service-business SEO + AEO (chiropractic, plumbing, auto repair); 2) maintenance / recency (a maintained small repo beats a flashy abandoned one); 3) stars / community. Commercial-use license is a hard requirement for anything MAMMATA runs against client sites.

**Scope this run:** 60+ repos surfaced across 11 searches (SEO, structured data / JSON-LD, technical-SEO crawler/audit, core web vitals, llms.txt, awesome-seo, answer engine optimization, generative engine optimization, programmatic SEO, sitemap/indexing). **~17 inspected in detail (API + README), 5 listed in Top 5, 6 in runners-up/watching.**

---

## TOP 5

### 1. seo-skills/seo-audit-skill  (SEOmator Audit)
- **URL:** https://github.com/seo-skills/seo-audit-skill
- **What it does:** Open-source SEO audit engine — CLI (`npm i -g @seomator/seo-audit`) + Electron desktop app. Runs 250+ audit rules across ~20 categories: core meta/canonical, Core Web Vitals (LCP/CLS/FCP/TTFB/INP via Playwright), security headers, **JSON-LD / Schema.org validation incl. LocalBusiness + Organization**, accessibility, content quality, JS raw-vs-rendered DOM diff. Detects AI-bot access + `/llms.txt`. Exports console / JSON / HTML / Markdown / LLM-XML.
- **Why it matters for SEO/AEO:** One tool covers the exact MAMMATA audit surface — technical SEO + CWV + **LocalBusiness schema validation** + AEO signals (llms.txt + AI-bot access) — and emits machine-readable output an agent can ingest.
- **Stars / last commit:** 271★ · pushed 2026-05-08 (active) · created 2026-01-23 · 37 forks · not archived
- **License:** MIT (commercial use OK)
- **How Novarte/MAMMATA could use it:** Primary candidate for an automated pre-audit pass on local service clients — pipe the JSON/Markdown output into MAMMATA's audit, lean on the LocalBusiness-schema + llms.txt checks for the local + AEO angle.
- **Confidence:** [CONF] — API record + README verified 2026-06-06
- **Date verified:** 2026-06-06

### 2. addyosmani/web-quality-skills
- **URL:** https://github.com/addyosmani/web-quality-skills
- **What it does:** Agent Skills (Claude Code / Codex / Gemini CLI / claude.ai) for auditing & fixing web quality on Google Lighthouse + Core Web Vitals lines. Six skills: web-quality-audit, performance, core-web-vitals, accessibility, seo, best-practices. Framework-agnostic (React/Vue/Next/Astro/plain HTML). Install: `npx skills add addyosmani/web-quality-skills`.
- **Why it matters for SEO/AEO:** CWV + Lighthouse performance is a confirmed Google signal and a recurring weak spot on small-business sites. Authored by Addy Osmani (Google Chrome) = high trust, and it plugs straight into the Claude Code workflow Novarte already runs.
- **Stars / last commit:** 2,184★ · pushed 2026-05-09 (active) · created 2026-01-18 · 199 forks · not archived
- **License:** MIT (commercial use OK)
- **How Novarte/MAMMATA could use it:** Drop-in CWV/perf/a11y skill for the build side (static rebuilds like client rebuilds). Run `core-web-vitals` + `seo` skills against a rebuild before deploy.
- **Confidence:** [CONF] — API record + README verified 2026-06-06
- **Date verified:** 2026-06-06

### 3. dodopayments/dualmark
- **URL:** https://github.com/dodopayments/dualmark
- **What it does:** Open-source AEO infrastructure. Auto-generates a **markdown "twin"** of every page + an `llms.txt`, and uses HTTP content negotiation (Accept header + 24-bot User-Agent detection) to serve clean markdown to AI crawlers (ChatGPT/Claude/Perplexity) while humans keep the HTML. Framework-agnostic middleware with adapters for Astro, Next.js App Router, SvelteKit; edge support (Cloudflare Workers, Vercel Edge, Deno). CLI conformance score (0–125).
- **Why it matters for SEO/AEO:** This is the purpose-built AEO play — it directly targets *getting cited by answer engines* by feeding them clean, chrome-free content, which aligns with the AI-citation playbook (clean extractable content as a multiplier for non-Google engines).
- **Stars / last commit:** 80★ · pushed 2026-06-04 (very active) · created 2026-05-05 · 25 forks · not archived
- **License:** Apache-2.0 (commercial use OK)
- **How Novarte/MAMMATA could use it:** Pilot AEO layer on a static client rebuild to expose markdown twins + llms.txt to AI crawlers. Young (created May 2026) → pilot/watch before production, but the most on-target AEO repo found.
- **Confidence:** [CONF] — API record + README verified 2026-06-06 (young repo — re-verify maintenance next run)
- **Date verified:** 2026-06-06

### 4. AnswerDotAI/llms-txt
- **URL:** https://github.com/AnswerDotAI/llms-txt
- **What it does:** The canonical `/llms.txt` standard repo (Answer.AI / Jeremy Howard) — spec + Python tooling/CLI for producing and parsing llms.txt and `llms-full.txt`, helping LLMs use a site's content.
- **Why it matters for SEO/AEO:** llms.txt is the emerging convention for telling answer engines what's on your site. Owning the *source-of-truth* spec (not a third-party generator) keeps Novarte's AEO output standards-correct.
- **Stars / last commit:** 2,423★ · pushed 2026-05-20 (active) · created 2024-09-01 · 135 forks · not archived
- **License:** Apache-2.0 (commercial use OK)
- **How Novarte/MAMMATA could use it:** Reference spec for hand-authoring/validating llms.txt on client sites; pair with dualmark (auto-gen) or use standalone for static sites. Treat as the authority MAMMATA cites in AEO recommendations.
- **Confidence:** [CONF] — API record verified 2026-06-06
- **Date verified:** 2026-06-06

### 5. iamvishnusankar/next-sitemap
- **URL:** https://github.com/iamvishnusankar/next-sitemap
- **What it does:** Mature sitemap + robots.txt generator for Next.js — index sitemaps, split sitemaps, per-route config, i18n/alternate refs.
- **Why it matters for SEO/AEO:** Crawlability fundamentals (XML sitemap + robots) are table stakes; this is the best-maintained, highest-star OSS option for the Next.js stack and removes a manual, error-prone step.
- **Stars / last commit:** 3,733★ · pushed 2026-05-13 (active) · created 2020-08-02 · 142 forks · not archived
- **License:** MIT (commercial use OK)
- **How Novarte/MAMMATA could use it:** Standard sitemap/robots generation for any Next.js client build; verify output during the technical-SEO audit. (Stack-specific — only applies to Next.js builds.)
- **Confidence:** [CONF] — API record verified 2026-06-06
- **Date verified:** 2026-06-06

---

## RUNNERS-UP / WATCHING

- **bmpi-dev/awesome-seo** — https://github.com/bmpi-dev/awesome-seo — 2,706★ · pushed 2026-04-02 · MIT. Curated SEO research + monetization list, actively maintained. Good lead-mining reference, not a tool. **[CONF]**
- **amplifying-ai/awesome-generative-engine-optimization** — https://github.com/amplifying-ai/awesome-generative-engine-optimization — 398★ · pushed 2026-04-14 · no license declared. Curated GEO/AEO resource guide — the best AEO-specific reading list found. Reference only; no license = don't redistribute content. **[CONF]**
- **Auriti-Labs/geo-optimizer-skill** — https://github.com/Auriti-Labs/geo-optimizer-skill — 458★ · pushed 2026-06-05 · MIT. GEO audit/optimize Claude skill, very fresh. Promising AEO skill to trial; younger ecosystem — watch. **[CONF — metadata; README not yet deep-read]**
- **RehanSaeed/Schema.NET** — https://github.com/RehanSaeed/Schema.NET — 683★ · pushed 2026-06-02 · MIT. Strongly-typed Schema.org for C#/.NET. Excellent but stack-mismatched (Novarte builds aren't .NET). Watch in case of .NET work. **[CONF]**
- **goenning/google-indexing-script** — https://github.com/goenning/google-indexing-script — 7,651★ · **pushed 2024-10-10 (STALE ~20mo)** · MIT. Bulk Google Indexing API submitter. High stars but unmaintained → demoted from Top 5 per "maintained beats flashy" rule. Usable if it still works, but verify against current Indexing API before trusting. **[CONF — flagged stale]**
- **google/schemarama** — https://github.com/google/schemarama — 150★ · **ARCHIVED** (read-only since 2024) · Apache-2.0. Schema.org validation from Google. Disqualified for active use (archived); kept as a spec/reference artifact only. **[CONF — archived, excluded]**

### Also surfaced, not listed (low value / noise / unverified)
Mostly low-star or single-stack: `garmeeh/next-seo` (Next.js meta mgmt, useful but stack-specific), `aFarkas/lazysizes` (lazy-load lib, tangential), `joshbuchea/HEAD` (HTML head reference, not a tool), assorted <30★ AEO/GEO experiments (ansvisor, aeo-radar, aeo.js, getcito) — too immature to recommend yet but the AEO category is moving fast; re-scan next run.

---

## NOTES FOR NEXT RUN (watch list)
- Re-verify **dualmark** maintenance + adoption (created May 2026 — confirm it didn't stall).
- Deep-read **Auriti-Labs/geo-optimizer-skill** and **onvoyage-ai/gtm-engineer-skills** (1,142★ AEO skill) READMEs — both candidates to displace a Top-5 slot.
- Watch the sub-30★ AEO/GEO experiments as the category matures (ansvisor, aeo-radar, getcito).
- Re-check **google-indexing-script** — if it gets a 2026 commit, it jumps back up.
