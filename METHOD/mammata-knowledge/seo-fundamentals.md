> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

<!-- MAMMATA reference module — extracted verbatim from the agent definition 2026-06-11. The agent def mandates reading this file before the matching task. -->

## SEO KNOWLEDGE BASE (Core Fundamentals)

### Core SEO Fundamentals (from Google Search Central)
- **Crawlability**: Ensure Googlebot can access all important pages. Use sitemaps, clean robots.txt, no crawl blocks on key content.
- **Indexability**: Pages must return 200, have canonical tags, no noindex on important pages.
- **E-E-A-T**: Experience (most weighted in 2026), Expertise, Authoritativeness, Trustworthiness — essential for all competitive searches, not just YMYL.
- **Core Web Vitals**: LCP < 2.5s, CLS < 0.1, INP < 200ms — evaluated as a combined holistic score in 2026.
- **Mobile-First**: Google indexes mobile version first. Always audit mobile experience independently.
- **HTTPS**: Required. HTTP pages treated as untrustworthy.
- **URL Structure**: Short, descriptive, keyword-inclusive, hyphen-separated URLs.
- **Title Tags**: 50-60 chars, primary keyword near the start — never the brand name first.
- **Meta Descriptions**: 150-160 chars (never over 160), compelling, includes keyword.
- **H1**: One per page, single intent only — never a comma-separated keyword list.
- **H2-H6**: Logical hierarchy matching natural language question formats.
- **Internal Linking**: Connect related pages with descriptive anchor text. Minimum 3 per page.
- **External Links**: 2-3 outbound links per page to authoritative primary sources (not other aggregators).
- **Image Optimization**: WebP format, compressed, alt text, descriptive filenames, explicit width/height attributes.
- **Page Speed**: Defer non-critical JS, use CDN, preload LCP image, minimize render-blocking resources.

### Keyword Research Methodology (2026)
1. Start with Google Search Console — find existing rankings positions 5-20 (quick wins)
2. Identify user intent: Informational / Navigational / Commercial / Transactional
3. Apply Information Gain test: what does this page say that top 10 results do not?
4. Target long-tail keywords (3+ words) — lower competition, higher intent
5. Conduct competitor gap analysis — find keywords they rank for that the site doesn't
6. Map keywords to funnel stages: Awareness → Consideration → Decision
7. Research AI Overview appearance on target queries — optimize for citation eligibility

### Structured Data / Schema Markup (2026 Standards)

**Always use JSON-LD in `<script type="application/ld+json">` in `<head>`.**

**Use @id and @graph to link schema entities together across pages.**

Schema types for 2026:
- **MedicalBusiness** — for healthcare businesses (replaces LocalBusiness for medical)
- **Physician** — for licensed medical professionals (replaces generic Person for doctors)
- **MedicalWebPage** — for health content pages (replaces BlogPosting for YMYL health content)
- **MedicalTherapy / MedicalCondition** — for treatment and condition pages
- **LocalBusiness** — for non-medical local businesses
- **Organization** — for companies (always include @id and sameAs)
- **WebSite** — enables sitelinks search box
- **Article** — for content (non-medical)
- **Person with hasCredential** — for author profiles with certifications
- **Product with AggregateRating** — for ecommerce
- **FAQPage** — ONLY where FAQ content is visibly on the page
- **HowTo** — ONLY where step-by-step instructions are visibly on the page
- **BreadcrumbList** — on all non-homepage pages
- **Service with areaServed** — for service businesses
- **VideoObject** — for video content

**Google's Rules (strictly enforced in 2026):**
- Structured data must reflect visible page content exactly
- No misleading, spammy, or promotional markup
- No hidden content in markup that isn't on page
- AggregateRating must use real review data, not fabricated numbers
- Test with Google Rich Results Test before deploying

### On-Page SEO Checklist (2026)
- [ ] Title tag: unique, primary keyword first, 50-60 chars, no brand name first — MUST include at least 2 CTR signals (power modifier, social proof, urgency, exact query match, or differentiator)
- [ ] Meta description: 150-160 chars, written as a 160-char AD not a service list — must include trust signal, benefit, and phone number (local businesses) — NEVER a generic list of services
- [ ] H1: one per page, single intent only, never comma-separated keywords
- [ ] H2-H6: natural language question formats, secondary keywords
- [ ] URL: short, descriptive, hyphen-separated
- [ ] Images: WebP compressed, alt text, explicit width/height, descriptive filenames
- [ ] Internal links: minimum 3 per page, descriptive anchors
- [ ] External links: 2-3 per page to PubMed, NIH, .gov, .edu, or industry primary sources
- [ ] Schema markup: appropriate type for page + FAQPage where applicable
- [ ] Canonical tag: self-referencing on all pages
- [ ] Mobile responsive: passes Google Mobile-Friendly Test
- [ ] Page speed: LCP < 2.5s, INP < 200ms, CLS < 0.1 on mobile
- [ ] HTTPS: SSL certificate valid and not expiring within 60 days
- [ ] No broken links (404s)
- [ ] No duplicate content, titles, or descriptions
- [ ] No render-blocking resources
- [ ] Named author with credentials on all content pages
- [ ] Author bio page linked from all content bylines
- [ ] First paragraph directly answers the primary query (AI Overview eligibility)
- [ ] Information Gain: page contains original data or firsthand experience not in top 10

### Technical SEO
- **Sitemap**: XML sitemap submitted to Google Search Console
- **Robots.txt**: Properly configured, not blocking key content
- **Redirects**: 301 for permanent, 302 for temporary — no redirect chains (single-hop only)
- **Canonical Tags**: `<link rel="canonical" href="...">` on all pages
- **Hreflang**: For multilingual sites
- **JavaScript SEO**: Ensure content is rendered/indexable by Googlebot
- **www vs non-www**: 301 redirect enforced consistently
- **SSL expiry**: Check and flag any certificate expiring within 60 days
