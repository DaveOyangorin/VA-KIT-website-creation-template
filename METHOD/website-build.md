# Novarte AI — How We Build a Website Page

For MAMMATA and FRAVATA. Read it before every website job.

---

## 1. One page = one search phrase

- Each page answers **one main search phrase** (from Angelo's keyword file in `INBOX\`).
- Two pages never target the same phrase. If two pages fight for one phrase, flag it to Angelo.
- The main phrase goes in: the URL slug, the title tag, the H1, and the first sentence.
- 2–4 related phrases go in the H2s and the lines under them.
- No keyword data for a page = no page yet. Write a data request (`TEMPLATES\data-request.md`).

## 2. What every page has

| Part | Rule |
|---|---|
| File name / slug | lowercase, words joined with `-`, carries the main phrase: `drain-cleaning-sandy-ut.html` |
| Title tag | 50–60 characters, main phrase first, business name last if it fits |
| Meta description | 150–160 characters, a real reason to click, ends with an action |
| Canonical | `<link rel="canonical">` with the page's own full URL |
| H1 | exactly one, carries the main phrase |
| First paragraph | answers the main question in 40–60 words. No warm-up. The main phrase is in the first 100 words |
| H2s | specific ("What a Drain Camera Shows You"), never "Our Process" or "Introduction". At least one H2 carries the main phrase |
| Call to action | the client's real phone / booking link, copied exactly |
| Contact block | Name, Address, Phone copied character for character from the source |
| Internal links | 3–5 links to related pages on the same site, with descriptive anchor text |
| Outbound links | content pages: 2–3 links to real primary sources you opened (Google, .gov, .edu, a trade body) |
| Author | content and blog pages: a real, named person from the client's business, with real credentials from the brief. None in the brief = `[[NEEDS: author]]` |
| Schema | on every page — see 2b |
| Images | WebP, under 150 KB, real alt text that says what is in the picture, `width` and `height` set, `loading="lazy"` below the top of the page (never on the top image) |

## 2b. MAMMATA's build standard

This is Angelo's MAMMATA standard. The full sources are in `METHOD\mammata-knowledge\`:
`website-build-standards.md` (schema templates), `master-strategy.md`, and the files that
`00-INDEX.md` names for each task.

**Which phrase goes where (keyword tiers)**
- Tier 1, service + city ("drain cleaning sandy ut"): one page each. Never shared.
- Tier 2, the same with a word added ("best", "near me", "affordable"): on the Tier 1 page.
  Never its own page.
- Tier 3, questions ("how to", "what is", a problem): blog posts only. Never on service pages.

**How long (real words, no filler)**

| Page | Words |
|---|---|
| Home | 800+ |
| Service page | 1,200 target, never under 800 |
| City / area page | 300+ of content that is only about that place |
| About, FAQ, team | 300+ |
| Blog post | 1,200–2,000. A pillar post on a broad topic: 3,000+ |
| Contact, estimate, thank you, legal | no minimum |

Never pad a page to reach the number. If the real facts are not enough, write
`[[NEEDS: more facts about <what>]]` and list it in the notes.

**Answers that search engines and AI tools can quote**
- Put the answer first. The byline, credentials and "about us" go after the answer, never above it.
- Write sentences that make sense alone. AI tools quote one sentence, not a paragraph.
- A "what is" question: a 40–60 word paragraph. A "how to": a numbered list of 3–7 steps.
  A comparison: a table.
- Service pages: an FAQ with 5+ real questions (People-also-ask or the client's own customers),
  each answer 40–60 words.
- Give something that other pages do not have: real details, numbers and experience from the
  brief. Formatting alone does not get a page cited.

**Schema (JSON-LD in the `<head>`) — on every page, real facts only**

| Page | Schema |
|---|---|
| Home | `LocalBusiness` (or the right type: `Plumber`, `Dentist`, `MedicalBusiness`…) + `WebSite`: name, address, phone, geo, opening hours, area served, `sameAs` |
| Service page | `Service` + `FAQPage` + `BreadcrumbList` |
| City page | `Service` with `areaServed` = that city + `FAQPage` + `BreadcrumbList` |
| Blog post | `BlogPosting` (health topics: `MedicalWebPage`) + `BreadcrumbList`, author linked by `@id` to the About page |
| About | `Person` (doctors: `Physician`) with `hasCredential` — only credentials in the brief |
| Contact | `ContactPage` + `LocalBusiness` |

- The business has the same `@id` and the same name, address and phone on every page.
- `aggregateRating`: only when the brief gives the real rating, the real count and where they
  come from. Otherwise leave it out.
- No `FAQPage` without the questions visible on the page. No empty answer.
- Templates: `mammata-knowledge\website-build-standards.md` and `fravata-web-copy-system.txt` 8.3.

**Speed and mobile**
- Mobile first. One small `style.css`. No big frameworks, no sliders, no web fonts beyond 2.
- Scripts at the end with `defer`. Nothing blocks the top of the page from showing.
- The goal is the top of the page on screen in under 2.5 seconds on a phone.

**Desktop and mobile — every page must work on both**
- `<meta name="viewport" content="width=device-width, initial-scale=1">` on every page.
- Write the CSS for phones first, then add `@media (min-width: 768px)` for tablets and
  `@media (min-width: 1024px)` for desktop. Content no wider than 1200px on desktop.
- No sideways scrolling on a 360px phone. Images: `max-width: 100%; height: auto`. Wide
  tables sit in a box that scrolls.
- Text at least 16px, line height 1.5 or more. Buttons and links at least 48px tall, with space
  between them.
- Phone number as a tap-to-call `tel:` link. On phones, a "Call" bar fixed at the bottom of
  the screen. On desktop, the phone number shows in the header.
- Phone menu: a simple menu button made with `<details>` or plain CSS, no big script.
- Top image: no `loading="lazy"`, add `fetchpriority="high"`. No autoplay video on phones.
- Service cards: one column on phones, 2–3 columns on desktop.

**3D sites (only when the brief asks for 3D)**
The 3D part is decoration on top of a normal static page. Google and AI tools read the HTML
text, not the 3D scene. So:
- All the words, headings, links, NAP and schema are normal HTML, exactly like a static page.
  Never put text, menus or the phone number only inside the 3D scene.
- One 3D scene per page at most, usually in the top section. The rest of the page is static.
- Use Three.js from `https://cdn.jsdelivr.net/npm/three@0.160.0/` (exact version). No other
  script hosts. Small models only (`.glb` under 2 MB), or shapes made in code.
- A still image behind the scene shows first (`fetchpriority="high"`). The 3D starts after
  the page has loaded, and the page works fine if it never starts.
- Phones: lower quality (`renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5))`), fewer
  objects, or the still image only. Pause the scene when it is off screen or the tab is hidden.
- `prefers-reduced-motion: reduce` = no movement, still image only.
- The 3D never covers the text or the Call button, and never blocks scrolling on a phone.
- The scene has `aria-hidden="true"`; the still image has real alt text.
- Webcam, microphone or motion-sensor tricks: never, unless Angelo's brief asks for them.

**Site files for a new site (drafts — Angelo puts them live)**
- `sitemap.xml` with every page that should be in Google (not the thank-you page).
- `robots.txt`: allow everything, add the `Sitemap:` line. Never block the AI search bots
  (`OAI-SearchBot`, `ChatGPT-User`, `Claude-SearchBot`, `PerplexityBot`).
- `404.html` with links back to the main pages.
- The thank-you page gets `<meta name="robots" content="noindex">`.
- **Never make an `llms.txt` file.** Angelo does not use it.

**Existing sites**
- Make an existing page better before you add a new page for the same phrase. Updating wins
  over publishing new.
- Change `dateModified` only when the content really changed.

**Microsites** (only when the brief says "microsite")
- One domain, one city, one service.
- It gets its own name and look. Never copy the client's brand onto it, unless the brief says so.

## 3. Match the site

- A new page on an existing site copies the existing page's `<head>` tags, header, menu,
  footer and CSS classes exactly. Read 2 existing pages before you build.
- A new site: one shared `style.css`, the same header, menu and footer on every page.
- Add the new page to the menu or to a related page's links, so it is not an orphan.
- Mobile first: the page must read well on a phone. No text in images.

## 4. Local pages

- Name the real city or area from the brief. Never make a page for a town the client does not
  serve.
- City pages need real local content (the service in that place, real details from the
  brief). Never copy one city page and swap the town name.

## 4b. Site map for a local service site

Use this list for a new site. For an existing site, add only the pages that are missing and
that Angelo's brief asks for. Build a page only when the brief has real facts for it.

**Main pages**
- Home `/`
- Services `/services` — links to every service page
- One page per service `/<service-name>` — one main search phrase each
- Service areas `/service-areas` — links to every city page
- One page per real city or area served `/<service>-<city>-<state>` — real local content only

**Pages that turn visitors into calls**
- Contact `/contact`
- Get an estimate `/estimate`
- Thank you `/thank-you` (after a form; `noindex`)
- A "Call now" button with the real phone link `tel:` on every page

**Trust and footer pages**
- About `/about`, Meet the team `/meet-the-team`, FAQ `/faq`, Careers `/careers` (only if hiring)
- Privacy policy `/privacy-policy`, Terms `/terms-conditions`, Disclaimer `/disclaimer`,
  Accessibility `/accessibility`

Every page links up to its parent (service → Services, city → Service areas) and across to
2–5 related pages. The menu holds the main pages. The footer holds the rest.

## 5. What is NOT the VA's job

MAMMATA builds the schema, `sitemap.xml` and `robots.txt` as draft files. Angelo checks them.
These go in the notes file under **"For Angelo / developer"** — never do them:
redirects, DNS, server and hosting settings, tracking codes, forms that send data,
Google Business Profile changes, putting the site live.

### Real photos — MAMMATA takes them from the client's own website

Claude in this kit cannot download files (no shell, on purpose). **Never ask the VA to turn
shell access on.** It does not need to:

1. MAMMATA reads the client's own website with WebFetch and finds the real photos (the `src`
   of each `<img>`, and `og:image`). Only photos on the client's own domain.
2. In the page it uses the photo's **full URL**:
   `<img src="https://client-site.com/path/photo.jpg" alt="..." data-local="images/drain-camera-inspection-sandy.webp">`.
   `data-local` is the file name the photo gets when Angelo puts the site live.
3. It writes real alt text. It opens the photo URL with WebFetch when it can, to see what is
   in it. If it cannot see it, it uses the old page's alt text or caption, and adds
   "check alt text" to the notes.
4. The notes file lists every photo: the URL, the `data-local` file name, and the page.
5. **The VA does nothing more.** Angelo saves the photos as local files before go-live,
   because the old site's photo links stop working when the new site replaces it.

Photos already in `OUTBOX\<client>-site\images\` (saved by the VA or Angelo) win: use
`images/<file>` for those. No real photo anywhere = `[[NEEDS IMAGE: what it shows]]` in the
page and in the notes. Never use stock photos of fake staff or fake customers. Never use a
photo from another business's website.

## 6. The preview page (for Angelo's review)

After the pages are built, MAMMATA makes one extra file:
`OUTBOX\<client>-site\_preview.html`. It is a review copy, not the website.

- **A strip at the very top:** "DRAFT PREVIEW for <client> - made by Novarte AI for review - not
  the live site". Under each page's name, show its URL slug, title tag and meta description.
- **All pages in one file,** stacked one under the other. A sticky bar at the top has plain
  `#anchor` jump links to each page. No tabs and no JavaScript menus — they do not work inside
  the preview.
- **No `<html>`, `<head>` or `<body>` tags.** Put the site's CSS inside one `<style>` block at
  the top, so the design looks the same.
- **Images:** keep local links relative (`images/photo.jpg`), never starting with `/`. Photos
  from the client's own site keep their full `https://` URL. If they do not show in the
  preview, that is OK: say so in one line. The HTML files in `OUTBOX\` still show them.
- **Remove** every tracking code (Google Analytics, Tag Manager, Meta Pixel, chat widgets).
- **Turn off every form:** no `action`, and the button says "Form is off in this preview".
- **Scripts:** only from `cdn.jsdelivr.net/npm/` or `cdnjs.cloudflare.com`, with an exact
  version. Nothing else.
- Keep the client's design exactly as built. Do not restyle it.

Then Claude publishes it as a **private Artifact** on the VA's own Claude account and gives
her the link. She sends the link **only to Angelo**. She never shares it with the client or
anyone else. If publishing is refused or not available, the files in `OUTBOX\` are enough.

## 7. Check before you finish

- [ ] Every page has one main phrase from Angelo's keyword file, written in the notes file.
- [ ] No two pages chase one phrase. Tier 3 questions are only on blog posts.
- [ ] Title 50–60, meta 150–160 — count the characters.
- [ ] One H1 per page. Main phrase in the first 100 words and in one H2.
- [ ] First paragraph answers the question in 40–60 words, before any byline.
- [ ] Word count meets 2b for each page (count it), with no filler.
- [ ] Every page has a canonical and schema for its page type. Every JSON-LD block parses.
- [ ] 3–5 internal links on every page. No orphan page.
- [ ] New site: `sitemap.xml`, `robots.txt`, `404.html` made. No `llms.txt`.
- [ ] Name, address, phone match the source exactly, on every page.
- [ ] Every number and claim is in an INBOX file. No invented fact.
- [ ] No banned phrase from `writing-voice.md`.
- [ ] Every link points to a real page in the site folder, or a real URL from the brief.
- [ ] No "Claude", "AI", "Novarte" or agent name in the client's pages.
- [ ] Every `[[NEEDS: ...]]` is listed in the notes file.
