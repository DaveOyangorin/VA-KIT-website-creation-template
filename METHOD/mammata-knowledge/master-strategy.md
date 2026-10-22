> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# MAMMATA Master Strategy
Last updated: 2026-06-16 | Maintained by MAMMATA -- updates require user approval

---

## 1. Website Build Principles

Every website in this system must be built to:
- Load in under 2.5s LCP (Core Web Vitals pass threshold)
- Have schema markup on every page (LocalBusiness, Service, FAQPage, BreadcrumbList minimum)
- Be structured as a microsite -- one domain, one city, one niche
- Have no thin pages: minimum 800 words on service pages, 300 on supporting pages
- Canonical tags on every page, www redirect enforced, sitemap + robots.txt present
- Mobile-first HTML, no render-blocking CSS, images in WebP format under 150KB

## 2. Keyword Universe Framework

### Target Tier 1 -- Primary (Service + City)
Pattern: [service] [city] -- e.g., "chiropractor draper utah"
- High commercial intent, direct conversion
- One page per Tier 1 keyword, never shared

### Target Tier 2 -- Qualifier (Service + Modifier + City)
Pattern: [service] near me, best [service] [city], affordable [service] [city]
- Same page as parent Tier 1 via semantic inclusion

### Target Tier 3 -- Informational (Blog / AEO)
Pattern: how to [problem], what is [service], [symptom] [solution]
- Blog posts by FRAVATA -- these feed AI Overviews
- Never target on service pages (cannibalization prevention)

### Cannibalization Rule
Each keyword maps to exactly one URL. If two pages target the same keyword, consolidate.

## 3. Content Strategy -- FRAVATA Voice Rules

All blog and long-form content follows FRAVATA voice:
- Open with a counterintuitive fact, specific number, or scene-setting moment
- NO FORBIDDEN OPENERS: "In today's digital landscape", "SEO is important", "Dive deep"
- Write like a practitioner talking to a peer, not a marketer writing for Google
- Every post must include: one real case study with specific numbers, 3+ cited sources, CTA
- Minimum 2,000 words for blog posts, 1,200 for service pages
- Author: a real, named person from the client's business -- always credited, always with @id schema

## 4. SEO Framework

### Technical (must-pass before any content work)
- HTTPS on all pages
- HTTP to HTTPS + www to non-www redirects working
- Sitemap.xml submitted to GSC
- robots.txt allowing all service pages
- No broken links, no 404s on indexed pages
- LCP < 2.5s on all pages (measured via DataForSEO)
- No render-blocking resources above the fold

### On-Page (per page checklist)
- Title tag 50-60 chars, includes primary keyword + location
- Meta description 150-160 chars, includes CTA
- H1 = one per page, matches title intent
- H2/H3 structure covers semantic variations
- Images: alt text, WebP format, under 150KB
- Internal links: minimum 3 per page
- Primary keyword in: title, H1, first 100 words, at least one H2

### Schema (JSON-LD, injected in head)
Every page gets:
- LocalBusiness (homepage) -- name, address, phone, geo, openingHours
- Service pages -- Service schema + FAQPage (5 Q&As minimum per service page)
- Blog posts -- BlogPosting + FAQPage + BreadcrumbList
- Contact page -- ContactPage + LocalBusiness

## 5. GEO Framework (Geographic SEO)

### Google Business Profile
- Complete all 100% of profile fields
- Minimum 10 photos (interior, exterior, team, work samples)
- Post weekly (use FRAVATA content pipeline for post copy)
- Respond to all reviews within 24h
- Primary category + 5 secondary categories

### Local Citations
Target 50+ consistent NAP citations:
Priority directories: Google, Yelp, Bing Places, Apple Maps, Facebook, BBB,
Angi, HomeAdvisor, Houzz (home services), Healthgrades/ZocDoc (medical)

### Local Content Signals
- City name in title, H1, and first paragraph of every service page
- Separate service pages per city if targeting multiple cities
- Embed Google Map on contact page

## 6. AEO Framework (Answer Engine Optimization)

### AI Overview Eligibility Checklist
- FAQPage schema with 5+ Q&As on every service page
- Q&As match actual conversational search queries (use GSC query data)
- Answers are 40-60 words -- concise enough for AI to extract
- Cite authoritative sources in blog posts (Google, .gov, .edu, major publications)
- Author schema with verified @id pointing to an about page
- E-E-A-T signals: credentials, case studies, real results with numbers

### Featured Snippet Targets
- Definition questions: "What is [service]?" -- 40-60 word paragraph answer
- How-to questions: numbered list format (3-7 steps)
- Comparison questions: table format

### AI Citation Strategy (post-May 2026 Core Update)
- Write content that is original, not a summary of other pages
- Include data, case studies, and firsthand experience Google cannot find elsewhere
- Every blog post must have one original insight not available on competing pages

---

