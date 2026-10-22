> VA COPY of MAMMATA's knowledge file, made 2026-10-12 for the VA kit. Client names, logins and
> internal tools were removed. Where it says DataForSEO, GSC or a script: you do not have
> those - use the keyword file Angelo put in INBOX\. The kit's CLAUDE.md rules win.

# Google Search Essentials (formerly Webmaster Guidelines)

- **Source:** https://developers.google.com/search/docs/essentials
- **Type:** Official Google documentation
- **Published / Last updated:** 2025-12-10 UTC
- **Scraped by FRAVATA:** 2026-06-01

## What it says
Search Essentials has three parts:

1. **Technical requirements** — "the bare minimum that Google Search needs from a web page in order to show it in search results." Google notes there are "actually very few technical things you need to do," and most sites meet them without deliberate effort. Core requirements: Googlebot must be able to access the page (not blocked by robots), the page returns an HTTP 200 status with usable content, and the content is indexable (no noindex).

2. **Spam policies** — behaviors/tactics that can lower a page or whole site's ranking or fully omit it from Search. (See spam-policies-overview.md.) Sites focused on quality content and user experience aligned with Google's principles perform better.

3. **Key best practices** (highest-impact actions):
   - Create helpful, reliable, people-first content.
   - Use words people would search for in prominent places — titles, headings, alt text, and link text.
   - Make links crawlable so Google can discover other pages on the site (use `<a href>` with a real URL).
   - Promote your site within relevant communities to reach the right people.
   - Follow best practices for images, videos, structured data, and JavaScript.
   - Enhance appearance in Search by adopting relevant Search features.
   - Control content visibility properly (correct opt-out / removal methods).

## What MAMMATA must do
- Confirm the technical floor on every client: Googlebot access allowed, pages return 200, no stray noindex on money pages.
- Ensure internal links use crawlable `<a href="real-url">` anchors (not JS-only onclick navigation) so all service/location pages are discoverable.
- Verify search-intent keywords appear in titles, H1/H2 headings, alt text, and internal link anchor text — without stuffing.
- Confirm images have descriptive alt text and structured data is valid where used.
- Check that any pages meant to be excluded use the correct method (noindex/robots), and pages meant to rank are NOT accidentally excluded.

## Audit checks (scorable yes/no)
- [ ] Googlebot can access all key pages (robots.txt + headers verified).
- [ ] All key pages return HTTP 200 with indexable content.
- [ ] No accidental noindex on pages that should rank.
- [ ] Internal links are crawlable `<a href>` anchors.
- [ ] Search-relevant terms present in titles, headings, alt text, and link text.
- [ ] Images have descriptive alt text; structured data validates.
- [ ] Intentional exclusions use the correct opt-out method.
