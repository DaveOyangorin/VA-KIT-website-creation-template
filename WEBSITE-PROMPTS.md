# Website prompts — copy, paste, run in order

Type these in the Claude Code tab, with the `VA-KIT` folder open.
Change the parts in `<...>`. Do one step, read the answer, then do the next.

## Before you start: what to install

1. **Claude desktop app** from `claude.ai/download`, signed in with **your own** paid Claude
   plan (Pro or Max) that includes Claude Code.
2. **Google Chrome**, for the desktop and mobile check (A7).
3. **Node.js LTS** from `nodejs.org`, only for your task and hours app (`app\START-VA.cmd`).
   Websites work without it.
4. **The VA-KIT folder**, opened in the Claude app: **Code** tab → choose folder → `VA-KIT`.

**Skills, plugins and connectors: none.** MAMMATA, FRAVATA, ALLIEVA and every `/command` are
already inside the VA-KIT folder. The private preview link is part of your Claude account.

**Do not install** other skills, plugins or connectors (DataForSEO, Netlify, Wix, WordPress,
Google, browser control). If Claude asks you to install something or turn on shell access,
say no and ask Angelo.

**Test:** type `/build-site` and press Enter. If Claude lists the INBOX files or asks which
file to use, you are ready.

---

- **Part A — static site:** a normal, fast website (plain HTML + CSS). Use this by default.
- **Part B — 3D site:** a static site with a 3D effect on top. Only when Angelo's brief says 3D.
- **Part C — extra prompts:** add pages, city pages, blog posts, fixes.

---

# PART A — STATIC SITE

## A1. Start

```
Read WHAT-CHANGED.md. Then list what is in INBOX for <client>.
```

## A2. Check you have everything

```
Check INBOX for <client>: is there a site brief and a keyword file? If the keyword file is missing, write the data request for Angelo and stop.
```

If you get a data request: send it to Angelo and wait.

## A3. Read the client's current site and brand

```
Use MAMMATA: read <client website address>. Write down in the notes file the real business name, address, phone, hours, services, cities served, the logo URL, the brand colors and fonts, and the real photos. Only facts you saw on the site or in INBOX.
```

## A4. Plan the site (no building yet)

```
Use MAMMATA to plan the <client> website from INBOX\<brief file>. Follow METHOD\website-build.md sections 2b and 4b and the blueprint in METHOD\mammata-knowledge. Give me only the page table: page, main search phrase, tier, word target, schema type. Do not build yet.
```

Read the table. Ask Claude to change it if a page looks wrong.

## A5. Build the site

```
/build-site INBOX\<brief file>
```

## A6. Real photos from the client's website

```
Use MAMMATA: take the real photos from <client website address> and put them in the pages in OUTBOX\<client>-site\. Real alt text. List every photo in the notes file.
```

That is all. The pages show the client's real photos. You do not download anything.

## A7. Desktop and mobile check

```
Use MAMMATA: check every page in OUTBOX\<client>-site\ against METHOD\website-build.md "Desktop and mobile" and "Speed and mobile". Check a 360px phone, a 768px tablet and a 1280px desktop. Fix every problem in the files and list what you fixed.
```

Then check with your own eyes:
1. Open a page from `OUTBOX\<client>-site\` in Chrome (double-click it).
2. Press **F12**, then **Ctrl + Shift + M**. Now you see the phone view.
3. Choose a phone at the top (for example iPhone SE). Scroll the whole page.
4. Look for: text too small, things cut off, sideways scrolling, buttons too close together.
5. Press **Ctrl + Shift + M** again for the desktop view. Make the window wide and narrow.
6. Tell Claude what you saw: `On the phone view of <page>, <what is wrong>. Fix it.`

## A8. Speed check

```
Use MAMMATA: check every page in OUTBOX\<client>-site\ for speed: image sizes and width/height, lazy loading below the top, the top image with fetchpriority="high", scripts with defer, no big frameworks, one small style.css. Fix what fails and list it.
```

## A9. SEO check

```
Use MAMMATA: run "Check before you finish" in METHOD\website-build.md on every page in OUTBOX\<client>-site\. Count the characters and the words, do not guess. Check every JSON-LD block and every link. Fix what fails and give me the list.
```

## A10. AI-answer check

```
Use MAMMATA: check every page against METHOD\website-build.md "Answers that search engines and AI tools can quote" and METHOD\mammata-knowledge\google-guidelines\ai-citation-and-ask-maps-playbook.md part C3. Is the answer first, in 40-60 words, before any byline? Fix what fails.
```

## A11. Preview link for Angelo

```
Rebuild OUTBOX\<client>-site\_preview.html and publish the private preview. Give me the link.
```

Send the link **to Angelo only**.

## A12. Angelo's changes

```
/revise INBOX\<fix note file>
```

## A13. Log your time

```
/log <hours> built the <client> website pages
```

---

# PART B — 3D SITE

Only when Angelo's brief says 3D. Do **A1 to A6 first**: the static site is the base.
The 3D is added on top. Google reads the normal page, not the 3D.

## B1. Plan the 3D

```
Use MAMMATA: read METHOD\website-build.md "3D sites". Suggest 2 ideas for one 3D scene on the <client> home page that fit the business (for example <a slowly turning product, a floating house, moving shapes in the brand colors>). For each idea: what it shows, how it works on phones, how it looks with reduced motion. Do not build yet.
```

Pick one idea, or ask Angelo.

## B2. Build the 3D scene

```
Use MAMMATA: add idea <1 or 2> as a 3D scene to the top section of OUTBOX\<client>-site\index.html. Follow METHOD\website-build.md "3D sites" exactly: Three.js 0.160.0 from cdn.jsdelivr.net, a still image first, 3D starts after load, lower quality on phones, pause when off screen, still image only with reduced motion. All text stays normal HTML. Do not change any words, links or schema.
```

## B3. 3D on phones

```
Use MAMMATA: check the 3D scene in OUTBOX\<client>-site\index.html for phones: does it cover text or the Call button, does it block scrolling, is the quality lowered, does it stop when off screen? Fix every problem.
```

Then check with your own eyes in Chrome phone view (A7 steps 1–4). The page must scroll smoothly.

## B4. 3D check-up

```
Use MAMMATA: check that the 3D page still passes A7, A8 and A9: the same words, headings, links, NAP and schema as the static page, the still image has real alt text, the scene has aria-hidden="true". List anything that changed and fix it.
```

## B5. More 3D (only if Angelo asks)

```
Use MAMMATA: add a small 3D effect to <page> in the same style as the home page, following METHOD\website-build.md "3D sites". One scene per page at most.
```

Then do **A11** (preview link) and send the link to Angelo only.

---

# PART C — EXTRA PROMPTS

## Add one page to an existing site

```
Use MAMMATA: add a page for <service> to OUTBOX\<client>-site\. Main phrase: <phrase from the keyword file>. Copy the header, menu, footer and CSS of the existing pages exactly. Link it from the Services page and 2-4 related pages.
```

## City pages

```
Use MAMMATA: build city pages for <service> in <city 1>, <city 2>, <city 3> — only cities in the brief. Each page needs real local content, never the same page with the town name swapped. Link them from the Service areas page.
```

## A blog post

```
/page-copy INBOX\<brief file> — blog post, main phrase: <question phrase from the keyword file>
```

Then:

```
Use MAMMATA: turn OUTBOX\<copy file> into a blog page in OUTBOX\<client>-site\blog\ with BlogPosting and BreadcrumbList schema. Link it from 2-3 related service pages.
```

## Better words for one page (when a page is thin)

```
/page-copy INBOX\<brief file> — page: <page name>, main phrase: <phrase from the keyword file>
```

Then:

```
Use MAMMATA: put the copy from OUTBOX\<copy file> into OUTBOX\<client>-site\<page>.html exactly as written.
```

## Internal links check

```
Use MAMMATA: map all links between the pages in OUTBOX\<client>-site\. Find pages with fewer than 3 links in or out, and pages no other page links to. Add the missing links with clear anchor text.
```

## Schema check

```
Use MAMMATA: check the JSON-LD on every page in OUTBOX\<client>-site\: does it parse, does it match the page type table in METHOD\website-build.md 2b, is the business the same on every page, is every fact real? Fix what fails.
```

## What is still missing

```
List every [[NEEDS ...]] in OUTBOX\<client>-site\ and the notes file, grouped: for the client, for Angelo.
```

Send that list to Angelo.

---

**Never** type keys, passwords or logins into Claude. **Never** turn on shell access.
**Never** put the site live — Angelo does that.
