> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

<!-- MAMMATA reference module — extracted verbatim from the agent definition 2026-06-11. The agent def mandates reading this file before the matching task. -->

## GOOGLE 2026 CORE UPDATE KNOWLEDGE BASE

### May 2026 Core Update (MOST RECENT — May 21, 2026)

**Official status:** Rolling out now. Completes ~June 4, 2026.
**Volatility:** Extremely high — 55%+ of monitored sites saw ranking shifts in the first 48 hours.
**Context:** Released 2 days after Google I/O 2026, where Google announced Search now runs on Gemini 3.5 Flash, AI Overviews reach 2.5B monthly users, and AI Mode surpasses 1B monthly users.

**The 5 Primary Ranking Signals in the May 2026 Update:**

**Signal 1 — Search Intent Matching (CRITICAL)**
Google's NLP now reads the real need behind a query with much higher precision. Content must satisfy the user's actual underlying goal — not just match keyword strings. Keyword stuffing effectiveness is near zero. Pages that answer questions completely and clearly win. H1 tags stuffed with comma-separated keyword lists are penalized.

**Signal 2 — E-E-A-T: Experience Amplified Above All (CRITICAL)**
The "Experience" element of E-E-A-T is now the most heavily weighted sub-signal of all four. 73% of top-ranking YMYL pages display detailed author credentials. Bylines must say "Written by [Name], [Credentials]" not "Reviewed by." Author bio pages must contain verifiable professional credentials, license numbers (for regulated fields), institution attended, graduation year, and relevant experience. Generic "staff writer" bylines are a negative signal.

**Signal 3 — Content Quality: Information Gain (CRITICAL)**
Google now measures how much genuinely new knowledge a page contributes compared to what already ranks for the same query. Derivative content — even well-written summaries of existing top-10 results — loses ground. Pages must contain at least one of:
- Original data, surveys, or research
- Firsthand clinical/professional experience with specific outcomes
- Unique perspectives not found elsewhere
- Quotes or access from primary sources
- Specific case studies with real-world results

**Signal 4 — AI Content Detection & Editorial Oversight (HIGH)**
Google's Gemini-powered semantic filter now actively evaluates AI content authenticity. The evaluation is NOT human vs. AI — it is "editorially supervised vs. automatically published." AI-assisted content with meaningful human expert review ranks well. Bulk-published AI output without named human accountability does not. Pattern repetition, structural uniformity, and absence of specific firsthand detail are negative signals.

**Signal 5 — Holistic UX Scoring (HIGH)**
Speed, mobile performance, Core Web Vitals, and accessibility are evaluated as one combined score — not individual checkboxes. One failure pulls down the others. Thresholds:
- LCP: Must be under 2.5 seconds (sites above 3s saw 23% more traffic loss)
- INP: Must be under 200ms (above 300ms caused 31% drops on mobile)
- CLS: Must be under 0.1
- Render-blocking resources: Flag and fix on all pages

### AI Overviews & AI Mode (2026 Reality)
- AI Overviews appear on 48% of all Google queries as of May 2026
- Sites cited INSIDE an AI Overview receive 35% more clicks than a standard position-1 result
- Brands cited in AI Overviews earn 91% more paid clicks than non-cited competitors
- AI Mode has 1B+ monthly users — it is now a primary search surface
- Schema markup is the primary signal feeding AI Overview citations
- Being cited in AI answers is now more commercially valuable than rank #1 below it

### Schema's New Role in 2026
Schema markup's primary purpose has shifted:
- **Old purpose:** Trigger rich result displays (star ratings, FAQ dropdowns, etc.)
- **New primary purpose:** AI entity verification for Google's AI Mode and AI Overviews

Google's Gemini uses schema to verify claims, establish entity relationships, and assess source credibility during answer synthesis. Accurate schema = higher probability of AI Overview citation even when no rich result displays.

**Schema types deprecated for rich results (June 2025):**
Book Actions, Course Info, Claim Review — implement for entity signaling only, not rich results.

**Schema types reduced for abuse (March 2026):**
FAQ, Review, HowTo rich results reduced on pages where schema doesn't reflect genuine primary content. Only implement where content is actually present on page.

**Schema that performs strongest in 2026:**
- MedicalBusiness / Physician (for healthcare — YMYL critical)
- Organization with @id and sameAs (entity identity)
- WebSite with SearchAction
- Person with hasCredential (E-E-A-T signal for authors)
- Article / MedicalWebPage (use MedicalWebPage for health content, not generic BlogPosting)
- Service with areaServed
- BreadcrumbList
- FAQPage (only where FAQ content is visible on page)
- AggregateRating with real review data

### What Gets Penalized in 2026
- H1 tags stuffed with comma-separated keyword lists
- Bylines that say "Reviewed by" without "Written by" a named credentialed author
- Medical/legal/financial content without named authors and verifiable credentials
- AI-generated content published without editorial oversight or named accountability
- Content that restates existing top-10 results without adding original information
- Thin affiliate pages with no original editorial value
- Parasite SEO — third-party content sections exploiting host domain authority
- Expired domain abuse
- Reciprocal link schemes and link networks
- Scaled content abuse (bulk-published template pages)
- Render-blocking resources that delay LCP above 3 seconds
- Schema deployed where the described content isn't visible on the page

### What Gets Rewarded in 2026
- Named authors with verifiable credentials and linked bio pages
- Original data, firsthand experience, and unique perspectives
- Topical authority depth — pillar + cluster content architecture
- Sites with defined, narrow topic coverage (specialists over generalists)
- Fast-loading, mobile-optimized, CWV-passing sites
- Complete, accurate schema markup aligned to visible page content
- External links to primary authoritative sources (PubMed, NIH, .gov, .edu)
- Community-driven platforms with active editorial moderation
- E-commerce brands with strong product pages and real reviews
- Primary sources: brand-owned domains, government institutions, official documentation

## AI OVERVIEW OPTIMIZATION (2026)

When auditing or building pages, always check and optimize for AI Overview citation eligibility:

**Content structure for AI citation:**
- First 100 words must directly answer the primary query — no preamble
- Use H2/H3 headers in natural language question format ("What is X?", "How does X work?")
- Include a concise answer or summary at the top of long-form content
- Structure key definitions as "X is..." format (frequently extracted by AI)
- Include specific numbers, dates, named entities, and verifiable facts — these anchor AI citations
- Avoid vague language ("some studies suggest") — cite specific studies by name and year

**What does NOT help AI Overview citation:**
- llms.txt files (not read by Google in any special way)
- Breaking content into micro-paragraphs to "make citation easier"
- Ideal page length targeting — AI extracts relevant passages from any length

