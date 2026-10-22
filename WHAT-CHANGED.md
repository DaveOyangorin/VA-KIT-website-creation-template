# What changed in the kit

Every time Angelo changes the rules, playbooks, or templates, a short note goes here.
Newest first. Read the top entry when you see this file change.

---

## 2026-10-13

- **New: `WEBSITE-PROMPTS.md`** — the prompts to build a website step by step, in order,
  Part A: static site. Part B: 3D site. Part C: extra prompts (pages, city pages, blog, checks).
- **Desktop and mobile rules** and **3D site rules** added to `METHOD\website-build.md` section 2b.

- **Real photos: MAMMATA takes them from the client's own website.** It links each real
  photo in the pages and lists them in the notes file. You do not need to download anything,
  and shell access stays off. If Claude asks you to turn shell access on, say no.

## 2026-10-12

- **MAMMATA now has all of Angelo's MAMMATA knowledge** in `METHOD\mammata-knowledge\`
  (start at `00-INDEX.md`). FRAVATA can read it too.
- **New: site map.** `METHOD\website-build.md` section 4b lists the pages a local service
  site needs and their URLs.
- **MAMMATA now builds to Angelo's MAMMATA standard** (`METHOD\website-build.md` section 2b):
  keyword tiers, word counts per page, answer-first writing, schema on every page,
  `sitemap.xml` + `robots.txt` + `404.html` for a new site. Meta descriptions are now
  150–160 characters.
- **MAMMATA now has the blueprint and the full course library** in
  `METHOD\mammata-knowledge\` (`rank-expand-blueprint.txt`, `rank-expand-academy\`).

## 2026-10-11

- **New: two website helpers, MAMMATA and FRAVATA.** They are copies of Angelo's own SEO
  engineer and writer. MAMMATA builds pages. FRAVATA writes the words.
  - `/build-site INBOX\<brief>` builds or adds website pages. The pages are draft files in
    `OUTBOX\<client>-site\`.
  - `/page-copy INBOX\<brief>` writes the words for one page or blog post.
- **Search phrases come from Angelo.** The helpers need a keyword file in `INBOX\`. If it is
  not there, they write a "data request" file in `OUTBOX\` and stop. Tell Angelo.
- **Preview link.** `/build-site` also gives you a private preview link of the pages. Send that
  link **to Angelo only** — never to the client or anyone else. It is not the live site.
- **Nothing goes live from you.** Angelo reviews the pages and puts them live himself.
- New playbook: `METHOD\website-build.md`. Read it once.

## 2026-09-16

- **You have your own app.** Double-click `app\START-VA.cmd`. It opens at
  `http://localhost:5080` and shows your tasks, your time sheet, and your drafts.
  Log your hours there, or with `/log` in Claude — both write the same sheet.
- **Task statuses.** In the app you can set `in progress` and `submitted`. Only Angelo can
  mark a task `approved`.

## 2026-09-15

- **New: your time sheet.** At the end of every work session, type
  `/log <hours> <what you did>` — for example `/log 2.5 claimed Yelp and the health directories`.
  It adds one row to `WORKLOG.csv` with today's date, your hours, the client, and your own words.
  Log the same day. Angelo reads this file.
- **New command: `/revise`.** When Angelo wants a draft changed, a fix note appears in `INBOX\`
  (the name has `_fix_` in it). Type `/revise INBOX\<that file>` and the draft gets fixed.
- **New file: this one.** Check the top of it when Angelo says the kit changed.
