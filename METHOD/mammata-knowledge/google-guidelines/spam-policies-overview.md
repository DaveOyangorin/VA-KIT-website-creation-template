> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# Spam Policies for Google Web Search

- **Source:** https://developers.google.com/search/docs/essentials/spam-policies
- **Type:** Official Google documentation / Spam policy
- **Published / Last updated:** 2026-05-15 UTC; **changelog clarification 2026-06-05** (spam policies apply to generative AI responses)
- **Scraped by FRAVATA:** 2026-06-01; re-verified 2026-06-03

## 2026-06-05 clarification — applies to generative AI responses
Google updated its documentation changelog to clarify: **"Clarified that our spam policies also apply to generative AI responses in Google Search."** The full named-policy list below now explicitly governs AI Overviews and AI Mode, not just classic results. Practical effect: a page that violates any spam policy (cloaking, scaled content abuse, site reputation abuse, link spam, thin affiliation, etc.) is **disqualified from being cited in AI answers** as well as demoted/omitted from the ten blue links. There is no separate "GEO/AEO" exemption — clean, people-first content is the only path to AI visibility. (Source: https://developers.google.com/search/updates)

## What it says
Named spam policies (a violation can cause lower ranking or full omission from Search):

- **Cloaking** — presenting different content to users vs. search engines to manipulate rankings and mislead users.
- **Doorway abuse** — sites/pages created to rank for specific queries that funnel users to a less useful intermediate destination.
- **Expired domain abuse** — buying expired domains and repurposing low-value content primarily to manipulate rankings.
- **Hacked content** — unauthorized content placed via security vulnerabilities (code/page/content injection, malicious redirects).
- **Hidden text and link abuse** — content placed solely to manipulate engines (white-on-white text, off-screen CSS positioning).
- **Keyword stuffing** — filling a page with keywords or numbers to manipulate rankings.
- **Link spam** — creating links to/from a site primarily to manipulate rankings.
- **Machine-generated traffic** — automated queries to Google, including unpermitted scraping for rank checking.
- **Malicious practices** — malware, unwanted software, AND **back button hijacking** (explicit violation; enforcement June 15, 2026). Creates a mismatch between user expectation and outcome, or compromises security/privacy.
- **Misleading functionality** — sites that trick users into thinking they'll get content/services they can't actually receive.
- **Scaled content abuse** — generating many pages without adding value (via generative AI, scraping, or stitching content), to manipulate rankings.
- **Scraping** — taking content from other sites (often automated) and hosting it without original value or proper attribution.
- **Site reputation abuse** — publishing third-party content on an established site primarily to leverage its ranking signals ("parasite SEO").
- **Sneaky redirects** — redirecting users maliciously / showing different content than search engines see or unexpected content.
- **Thin affiliation** — affiliate content with merchant-copied product descriptions and no original content or added value.
- **User-generated spam** — spammy content added through user channels (comments, forum/profile posts), often without the owner's knowledge.

Other practices leading to demotion/removal: legal removals (copyright, defamation, counterfeit, CSAM); personal information removals (exploitative removal, doxxing, non-consensual imagery); policy circumvention (using subdomains/other sites to bypass a policy); scam and fraud (impersonation, false business information).

## What MAMMATA must do
- Run every client site against the full named-policy list above as a checklist; treat any match as a critical finding.
- Check for cloaking by comparing rendered content for Googlebot vs. a normal user agent.
- Verify no hidden text/links (white-on-white, display:none stuffed keywords, off-screen text).
- Audit any AI-assisted or templated content for scaled content abuse — value per page, not page count.
- For the auto repair client auto, scrutinize affiliate/manufacturer-copied descriptions (thin affiliation) and ensure original local value is added.
- Confirm no third-party/guest content is hosted purely to ride the domain's authority (site reputation abuse).
- Lock down user-generated areas (comments/forms) against injected spam links.
- Tie back-button hijacking remediation here (see dedicated file) — it lives under malicious practices.

## Audit checks (scorable yes/no)
- [ ] Rendered content is identical for users and Googlebot (no cloaking).
- [ ] No hidden text or hidden links present.
- [ ] No keyword stuffing in body, titles, alt text, or meta.
- [ ] No purchased/manipulative inbound or outbound link schemes.
- [ ] No mass-generated low-value pages (scaled content abuse).
- [ ] No scraped or unattributed third-party content.
- [ ] No thin-affiliate pages with merchant-copied descriptions and no added value.
- [ ] No third-party "parasite" content leveraging the domain's reputation.
- [ ] No sneaky redirects or misleading functionality.
- [ ] User-generated areas are protected from spam.
- [ ] No back button hijacking (malicious practices) — remediate before 2026-06-15.
