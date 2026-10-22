# Claude Code Building

> Source: AI SEO: Rank Expand Academy (Skool) — `classroom/8f8387cf`  
> 10 lessons · 5 videos (~78 min) · 33 KB of written material  
> Internal reference for MAMMATA. Not for redistribution.

---

## Building Websites with AI Coding Tools

🎥 [Loom](https://www.loom.com/share/c0b3be606ed1412ba78c580a8d8e9160) · 11:09

## Pre-Work Understanding & Expectations

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/7008385072a94d57b42258b8e0cad35f10fafc3ac8a849cbacdcba0c06747bfa-md.png)

# How to run this build yourself...a quick guide

## **1. Get the right tool: Claude Code (not just chat)**

This build works because Claude can **run commands** on your machine — `git`, the GitHub CLI, SFTP, and WordPress's WP-CLI. A normal chat window can only give advice.

- Install **Claude Code** (the desktop app or the CLI). On Windows it runs in a Git Bash / PowerShell environment; on Mac/Linux it uses your terminal.
- Open it **in a dedicated project folder** (e.g. `Documents/my-site`). Everything Claude creates lands there.
- Why it matters: the agent executes and verifies each step, so you get a working site, not just instructions.

## **2. Accounts & things to have ready *****before***** you start**

- **A Kinsta site with a staging environment.** Staging = a safe copy you can break without touching a live site. You can use another host but you must specific this to Claude Code.
- **A GitHub account** (free). This is your code backup + version history.
- **A Pexels account** (free, optional) if you want stock photos — you'll get an API key at [pexels.com/api](http://pexels.com/api).
- 20–30 minutes and a willingness to answer Claude's questions about your niche.

## **3. Where to find each credential (exact clicks)**

- **Kinsta SFTP/SSH** → MyKinsta → your site → **Environment (Staging)** → **SFTP/SSH info**. You'll see **Host, Port, Username, Password**. These same details give Claude **WP-CLI over SSH**, which is how it controls WordPress.
- **WordPress Application Password** (this is *not* your login password) → WP Admin → **Users → Profile** → scroll to **Application Passwords** → type a name like "claude" → **Add New** → copy the generated code. It's used for the WordPress REST API.
- **GitHub** → don't make a token at all if you can avoid it. Instead run `gh auth login` (see #4).

Note: ask Claude Code to explain if you get lost along the way. Since the publishing of this guide, things may have changed and Claude Code has the updates readily available but you must ask it. Utilize Claude Code as your tech support. 

## **4. The secret-handling workflow....learn this, it's the important part**

Anything you type in the chat can end up in a transcript you might share. So **never paste secrets into the chat.** Instead:

- Claude creates a file called `.env` in your project and adds it to `.gitignore` (a list of files Git ignores). `.env` stays on your computer and is *never* uploaded to GitHub.
- **You** open `.env` in a text editor and paste your Kinsta SFTP password, WP application password, etc. Claude reads them from the file without printing them back.
- For GitHub, run this in your own terminal:

```
gh auth login
```

Choose [**GitHub.com**](http://GitHub.com)** → HTTPS → Login with a web browser**, approve in the browser. Now your computer holds the credential and Claude uses it — no token ever touches the chat.
- Mental model: **the **`.env` file (and `gh auth login`) is the secure side door; the chat is the public front window.

Note: sometimes I (Jesse) paste secrets into chat because I'm lazy. But best practice is above.

## **5. Understand what Claude is doing under the hood (so you can follow along)**

- **Permalinks first.** It sets URLs to `/%postname%/` (e.g. `/best-running-shoes/`). Clean URLs help SEO. Bonus: WordPress's REST API behaves oddly on "Plain" permalinks, so fixing this early avoids errors.
- **Two ways it talks to the site:** the **REST API** (over HTTPS, using your app password) for content, and **WP-CLI over SSH** for installing themes, setting options, etc. WP-CLI is the powerful one.
- **The SSH password trick (Windows):** Windows Git Bash often lacks `sshpass`, so passwords can't normally be passed automatically. Claude uses OpenSSH's `SSH_ASKPASS` feature to feed the password from `.env` — wrapped in a small reusable script so no password is ever typed into a command.
- **Child theme = your code.** Blocksy is the engine; the **child theme** holds your custom templates, CSS, and (optionally) SEO code. It's deployed via SFTP and committed to GitHub, so your work is reproducible and backed up.

## **6. The caching gotcha (this will confuse you if you don't know it)**

Kinsta + its CDN serve **cached** pages. After a change you might refresh and see… nothing different. That's the cache, not a bug.

- Fix: Claude runs `wp kinsta cache purge --all`, or adds `?cb=123` to the URL to bypass the cache when checking.
- Same idea bites password protection: **server-level passwords don't work with full-page caching.** So on **staging**, turn the CDN/cache **off** if you want a password (staging doesn't need speed). **Production** keeps the cache and stays public.

## **7. Images (what we learned)**

- **Public domain** (free, no credit needed): NASA, SpaceX's own photos, anything marked CC0.
- **Wikimedia Commons** (real subjects, usually needs a one-line credit): great for specific people/products. Claude can store the credit in the image caption automatically.
- **Pexels / Unsplash** (free for commercial use, no credit): best for generic/topical shots.
- **Off-limits:** company press photos, brand logos, news-agency images — copyrighted.
- Tiny technical lesson: WordPress rejects image URLs that lack a real file extension. A URL ending in `/png` fails; `.jpg`/`.png` works.

## **8. Common errors you'll likely hit (and the fix)**

- **"It looks unchanged after I edited it"** → cache. Purge it (#6).
- **Category names showing **`&amp;` → avoid `&` in category names; write "and" instead.
- **An image shows as a blank box** → it loaded over `http` on an `https` page ("mixed content"). Force https.
- `gh auth login` rejects your token → use the **browser login** flow instead of pasting a token.
- **Theme/plugin installs fail over the API** → WordPress can't install *themes* via REST; use WP-CLI over SSH (`wp theme install …`).

## **9. Security must-dos when you're done**

- **Rotate** any password that ever appeared in plaintext (Kinsta SFTP, WP app password) and **revoke** any GitHub token you created.
- Keep the **repo private**.
- On the live site: strong admin password + **2FA**, and remember to set `blog_public` back to `1` and remove staging-only protections when you launch.

## **10. Set expectations**

- This uses your own Claude/Anthropic account, so longer builds consume usage. Work in stages (foundation → pages → posts) and review as you go.
- Claude will ask a lot of questions up front — answer them well and the rest goes faster. Garbage in, garbage out.

## Claude Code Prompting

**Copy and paste this into Claude Code (read the prompt first and iterate to your needs, such as specific hosting, parent theme etc):**

You are my web-development partner. We're going to build a WordPress website together

and I want you to GUIDE ME STEP BY STEP, asking questions before big decisions and

explaining what you're doing. Assume I may be non-technical. Don't dump everything at

once — work in clear stages and check in with me.

# The goal & stack

- Host: Kinsta (I have a staging site).

- Theme: Blocksy with a CUSTOM CHILD THEME. All custom design and code lives in the

  child theme so it's versioned and reproducible.

- Version control: a PRIVATE GitHub repo. Commit and push everything we make (the child

  theme, docs, helper scripts) after each meaningful step.

- SEO: follow modern best practices — clean URLs (/%postname%/), exactly one H1 per page,

  strong title tags + meta descriptions, dense internal linking between related posts,

  schema/JSON-LD, an XML sitemap, fast loading. Ask me whether I want this built bespoke

  in the child theme (no plugins) or via a plugin like RankMath.

- My niche/topic: I'll tell you — ASK ME about it before assuming anything.

# How we work (please follow this order)

1. INTERVIEW ME FIRST. Ask specific questions about: my niche/topic and purpose; my target

   audience; how the site makes money (display ads / affiliate / leads / product sales);

   brand name, colors, fonts, logo; reference sites whose look I like; and which pages I want.

2. Propose a site architecture (pages + categories/hubs) and a design direction, and get my

   approval before building.

3. Build the FOUNDATION: set permalinks to /%postname%/, install Blocksy, create + activate

   the child theme, create categories and navigation.

4. Build PAGES FIRST, then blog posts later.

5. Show me screenshots or live links as you go so I can give feedback before moving on.

6. Commit and push to GitHub after each stage.

# Access I'll give you — HANDLE AS SECRETS

I'll provide three sets of credentials. Treat them carefully:

- NEVER print, echo, log, or repeat any secret back into this chat — I may share this

  conversation publicly.

- Create the project folder and a gitignored `.env` file. I'll put the secrets in `.env`;

  you read them from there WITHOUT displaying them. Make sure `.env` is in `.gitignore`.

- For GitHub, instead of me pasting a token into chat, have me run `gh auth login` in my own

  terminal so the credential is stored by my OS and you just use it. (Install `gh` if needed.)

- If we ever need credentials in automation/CI, store them as ENCRYPTED GitHub Actions

  secrets — never commit plaintext.

The credentials are:

- Kinsta SFTP/SSH: host, port, username, password (Kinsta provides WP-CLI over SSH).

- A WordPress Application Password (WP Admin → Users → Profile → Application Passwords) for

  the REST API.

- My GitHub account (via `gh auth login`).

# Technical notes to make this smooth

- You can drive the entire build from the command line: the WordPress REST API (use the

  `?rest_route=/...` form if permalinks are still "Plain"), plus WP-CLI over SSH.

- If my machine has no `sshpass`, use OpenSSH's `SSH_ASKPASS` with `SSH_ASKPASS_REQUIRE=force`

  to pass the SSH password non-interactively. Wrap SSH/WP-CLI/SFTP in a small helper script

  that reads `.env`, so commands are clean and no secret is hard-coded.

- Deploy the child theme to `wp-content/themes/` via SFTP/scp; install Blocksy with

  `wp theme install blocksy`, then activate the child theme.

- Kinsta has full-page edge caching: after changes, purge with `wp kinsta cache purge --all`,

  or append `?cb=123` to a URL to bypass the cache when you check your work.

- Set the staging site to noindex (`wp option update blog_public 0`) so it isn't indexed.

- For placeholder images, prefer legally-clean sources: public-domain (NASA/SpaceX/Wikimedia

  CC0), Wikimedia Commons (store the credit in the image caption), or free stock (Pexels/

  Unsplash). Don't use copyrighted press photos.

# Security reminders to give me

- Remind me to ROTATE any credential that ever appeared in plaintext once setup is done.

- Remind me to password-protect the staging site — and note the catch: server-level password

  protection conflicts with edge caching, so I should turn the CDN/cache OFF on staging if I

  enable a password (production stays cached + public).

Start by confirming you understand, then begin Step 1 and interview me.

## The SEO Book for Download

You can now use my book,[ "The SEO BOOK"](https://www.amazon.com/SEO-Book-Optimization-Strategies-Traffic/dp/B0DJ5HTGDY/ref=sr_1_1?crid=LYRQUL61VVCY&dib=eyJ2IjoiMSJ9.GV-yV36z0Z9_84oNy4CY1ddTUrMU3Sj9U6UR-2irj5pVMu_eIlZl6Somk_lgFATgCNN8I_pONsMHMIkvVO4HgHrs5dy_rO6L3RNKsgUXtmp-rMmmeUNA-0d3SfZ-06f4s-YnAQd4Tm8oOBaxQd-hNVHYJfbus5yHOozeD9gOvpbyAWYCI4YUhvgR4VMiqcK87fujp_VXKIZZLm3TpnM9gdFlF4J81CJRmICAr_9l5cY.Ye2uzBiUK7NQtJYC2UFJL2Qx5gJiWfUxD6lt99BOZio&dib_tag=se&keywords=the+seo+book&qid=1781713627&sprefix=the+seo+boo%2Caps%2C170&sr=8-1) to copy + paste into Claude Code so it knows the preferences/rules of SEO, interlinking, and more.

## Claude Code Website Build #1

🎥 [Loom](https://youtu.be/aeImsK3u7Ac) · 12:41

## Claude Code Local Business Prompt

**Paste this into your claude code conversation to begin a local business website:**

I want you to help me plan and design a local business website structure using my preferred SEO and conversion framework.

My structural preference is a local lead generation style website built around clear commercial intent, strong service pages, strong location pages, simple internal linking, and repeated calls to action.

The website should not be built primarily like a blog. It should be built like a local business asset designed to rank for service plus city searches and convert visitors into phone calls, form fills, or quote requests.

Here is the structure I prefer:

Homepage

The homepage should act as the main local authority hub. It should clearly explain what the business does, who it serves, the main city or market, the top services, why the company is trustworthy, and how to contact them. It should link clearly to the main service pages and the main service area pages.

Services Hub

There should be a main services page that lists and summarizes every core service. This page should link to each individual service page.

Individual Service Pages

Each main service should have its own dedicated page. These pages should target searches like service plus city, service near me, emergency service, and related buying intent terms.

Each service page should usually include:

A strong headline with the core service and main location

A short explanation of the problem the customer is facing

A clear explanation of the service

Trust signals

The process

Common causes or situations

Signs the customer needs help

Why choose this company

Service area links

FAQs

Strong calls to action throughout the page

Service Areas Hub

There should be a main service areas page that lists the primary city, nearby cities, towns, counties, neighborhoods, and surrounding areas served.

Location Pages

Important cities or towns should have their own dedicated location pages. These should target searches like service in city, business type in city, and city specific service intent.

Each location page should usually include:

A headline focused on the city or town

A short local intro

A summary of the main services available in that location

Links back to the individual service pages

Nearby areas served

Local trust elements if available

FAQs

A strong call to action

Internal Linking

The site should use a simple internal linking system.

The homepage links to the service hub, top service pages, service areas hub, and top location pages.

The services hub links to all service pages.

Each service page links to relevant location pages.

The service areas hub links to all location pages.

Each location page links back to the most important service pages.

Footer links should include the main services, main locations, contact page, about page, and quote or estimate page.

Conversion Flow

The website should be designed for leads, not just information.

Every major page should include repeated calls to action such as call now, request a quote, schedule service, get an estimate, or contact us.

Emergency or urgent service businesses should have phone calls emphasized heavily.

Non emergency businesses can emphasize forms, consultations, appointments, or quotes.

Trust Layer

The structure should include room for proof and credibility, such as:

Reviews

Before and after photos

Project examples

Certifications

Licenses

Insurance information

Team photos

Local experience

Guarantees

Case studies

Brands or products used

Financing if relevant

Insurance claim help if relevant

Content Style

The content should be clear, direct, locally relevant, and commercially useful.

Avoid generic filler.

Avoid making every location page identical.

Make each service page specific to the actual customer problem, the service process, and the buying decision.

The goal is to create a clean SEO structure that helps Google understand what the business does, where it operates, and which pages should rank for which local searches.

Before creating the website structure, please confirm that you understand my preferred local SEO framework.

Then ask me the most important questions needed to guide the next step, including questions about:

The business niche

The main services

The most profitable services

The main city

The service radius

The cities or towns to target

Whether the business is emergency based or appointment based

The preferred call to action

The level of proof available

Whether there are photos, reviews, licenses, or certifications

Whether the goal is SEO only, paid traffic conversion, or both

Whether we need a small site, medium site, or large local SEO build

After I answer, create a recommended sitemap and explain the purpose of each page.

## Local SEO Playbook: Combo of SEO Book, Schema, etc

Thank you to [Bryan Collins](https://www.skool.com/@bryan-collins-6765) for putting this combo of his tactics + Jesse's "The SEO BOOK" into a nice format, allowing the community to copy + paste into Claude to help guide structure of the website. 

*This is base camp. Our entire SEO doctrine in one place: the strategy engine (Jesse Cunningham's Maverick Method, from the SEO Master Class) fused with everything we've built on top of it — local SEO, authority mapping, content production, the build pipeline, technical/schema standards, and AI-search optimization. Jesse gave us the framework; the rest is how we actually run it.*

## How to use this

Read it once end-to-end so the system is in your head. After that, treat it like a config file, not an article — open the section you need, and for any build, hand the relevant sections (plus the master checklist at the end) to your AI build assistant so it produces work to *our* standard instead of the model's defaults.

The order of the playbook follows the order of a job: **strategy → local → authority → content → technical → AI search → build → distribution → measurement.**

---

## 1. The non-negotiables (read first, every time)

These are the rules that override convenience. Most "mystery" ranking losses trace back to breaking one of them.

- **LocalBusiness schema on the homepage only. Never AggregateRating on LocalBusiness — under any circumstances.**
- **Single-hop 301 redirects only.** No chains, no loops, no catch-all redirects. Map redirects *before* any DNS flip — a 404 on a ranking URL is lost revenue.
- **FAQPage schema rendered expanded in static HTML.** Collapsed FAQs deprioritize the keyword-rich content and force JS execution AI crawlers may skip.
- **No service × location pages** without enough genuinely unique content to justify separate indexing.
- **GBP primary category is the #1 local ranking lever.** Treat it as a deliberate, seasonal decision.
- **Factual, non-promotional tone earns AI citations; promotional tone gets penalized.** Spokes inform; money pages sell.

---

## 2. The Maverick Method — the strategy & content engine

Jesse's five-phase backbone. This is *how we do SEO content*, regardless of tool. Motivation → Action → Validation → Expansion → Repeat, on a loop.

### Phase 1 — MOTIVATION (research & intent)

Start with *why someone searches*, not what they typed.

**Classify intent with DEEPR** before committing a keyword: **D**ecision-making, **E**ntertainment, **E**ducation, **P**roblem-solving, **R**esearch. Strong pages serve two or three at once. Open the current #1 result, score it against DEEPR, and build for where it's thin. Avoid pure purchasing-intent keywords tied to a competitor's brand — you can't out-rank a brand on its own name with a new site.

**Find the gaps** competitors missed: People Also Ask (expand until you have 8–12 relevant questions — these become headings and FAQs), forums/Reddit/Quora, product reviews, and DataForSEO for searched terms with weak content behind them.

**Pick the tier you can win.** Keywords ladder from broad/competitive to specific/winnable; new sites win on the specific end first. Keep the difficulty ladder relative to *our* DataForSEO metrics, not fixed DA bands.

**Choose your production gear:**

- **Blanket** — templated, scalable, topically-relevant content at volume. ~80% of a build. Easy to hand to AI/VA.
- **Sniper** — one-off, data-driven articles on specific low-competition keywords, each with a tailored outline. Use it to build hubs around pages that start winning.

**Structure into tiers/hubs** in a spreadsheet (the single source of truth):

- **Tier 1** — broadest article; the spine. Job is structure and authority, not necessarily ranking.
- **Tier 2** — sub-category articles under T1.
- **Tier 3** — specific long-tail articles under T2.
- Tiers are **fluid** — the same article can be T1 in one hub and T3 in another.

**Two content types that won't rank but earn their place:**

- **Gap content** — relevant, essential content too competitive to rank, but without it there's a hole in the knowledge graph.
- **Bridge content** — connective articles linking two loosely-related hubs; keeps authority flowing.

### Phase 2 — ACTION (build & optimize)

**Page template** (set before generating): slug (short, base keyword, *patterned* across a hub), title tag (<55 char, keyword + modifier), meta description (<155 char, keyword + related terms). One **H1**; everything else H2/H3/H4, broad-to-specific, phrased the way a user searches, capitalized properly (Google pulls headings as written for snippets).

**First paragraph is a snippet play** — give the most essential answer immediately in ≤300 characters, plainly. Then a short **reassurance** (often a question showing you get the user's why) and a **teaser** (preview with keywords)

**Body:** bite-sized chunks (2–3 sentences), tables/lists where clearer than prose, most important info closest to each H2. Natural keyword density (swap vague pronouns for keywords), entity/semantic terms throughout. Lead with **data from credible non-competitor sources** (.gov, official, primary) and link to the highlighted passage, not just the page.

**Interlinking:**

- Anchor text carries the keyword (highest-volume natural variation).
- **Upline/downline pattern:** every spoke links the one above and below it in the spreadsheet, top wraps to bottom — so every article links to ≥2 others and the hub is fully connected. Formulaic and VA/AI-executable.
- Every T2 links up to its T1; every T3 links up to its T2.
- Add **natural links** on top of the structured ones wherever they serve the reader.
- The goal is a Wikipedia-style **knowledge graph**, all flowing back toward the homepage.

**FAQ section:** source from PAA, 7+ per page. Answer immediately in ~300 chars, **never with "yes"/"no"** (Google rephrases questions and breaks the answer), include keywords naturally, plant internal links inside answers. Render expanded, FAQPage schema.

### Phase 3 — VALIDATION (measure, then act)

Do more of what works, stop what doesn't. (Full metric detail in §10.) Core read: organic vs branded traffic, keyword rankings/average position (fluctuation = Google undecided = strengthen the page), CTR, GA4 engagement. Measure **hubs** via patterned-slug filters, and recover earned CTR with the **n-gram check** (pull query variations from GSC, confirm the exact phrasing exists in the article, add what's missing).

### Phase 4 — EXPANSION (build the moat)

Fortify winners. Identify the top performer, check you're not cannibalizing existing content, pull related keywords, screen out branded terms and ones that don't link naturally, check competitor domain strength, then promote the winner to a T1 and build T2s around it linking back. That ring is the moat.

### Phase 5 — REPEAT

Run all phases forever, across every client. Every quality page and on-point keyword is a deposit into Google's trust account. Consistency is the game.

---

## 3. Local SEO layer

Where our local work goes beyond the book.

**Ranking-factor hierarchy** (Whitespark-aligned, practitioner-confirmed): **#1 primary category**, **#2 proximity**, **#3 keywords in the business title**. Review *recency* has climbed significantly (≈#11 and rising) — the biggest recent shift.

**Tactical doctrine:**

- **Seasonal category switching** — primary category follows demand (HVAC: furnace repair in fall, AC repair in spring). Plan the rotation per vertical so the VA isn't deciding case-by-case.
- **Products section has higher visibility than Services** — use it even for service businesses.
- **Physical address beats SAB for rankings.** Use SAB only when the client genuinely can't show an address (home-based, privacy).
- **Driving-directions signal** still works — staff should use Maps to the location regularly.
- **Citation descriptions** optimized with semantic triples across 100+ directories.

**NAP & brand mentions:** establish one canonical NAP format and never deviate (St. vs Street, Suite vs Ste). Audit the top 20–30 citation sources first — that's most of the value. Unlinked brand mentions count as implied links; include the full business name naturally in all published content.

---

## 4. Authority & links — "claim before you beg"

~80% of valuable local/niche backlinks already exist as unclaimed listings in regulators, associations, supplier directories, and partner ecosystems. Mine those *first*; cold outreach is last. Every business belongs to a real-world ecosystem — map where it legitimately belongs and connect it to every legitimate node.

**The tiers:**

- **Tier 0 — Entity Validation** (the glue, not a link tier): identical NAP/logo/description everywhere — GBP, Bing Places, Apple Business Connect, Facebook, LinkedIn, YouTube — *and* wire every profile into the site's Organization/Person schema via sameAs. This turns a pile of citations into an entity graph. Do it first.
- **Tier 1 — Claim (.gov + association):** highest authority, near-zero outreach (e.g. regulator credential listings, "find a [pro]" association directories).
- **Tier 2 — Relationship / vendor:** suppliers, buyers, equipment dealers, the referral web (the USPS-link pattern from CRST). Light outreach: "Do you have a vendor / preferred-contractor page?"
- **Tier 3 — Local:** chambers, county directories, regional business orgs.
- **Tier 4 — Editorial / earned (do last):** magazine profiles, regional press (hook to a news peg), HARO-style sourcing, HASO swaps.

**KPI reframe:** don't count raw backlinks — track **new qualified entities connected per month**, gated by a **DataForSEO DA/relevance check before anything counts** (kills junk-padding). Example month: 3 directories + 2 associations + 1 vendor + 1 podcast + 1 press mention.

**Phasing:** Phase 1 (0–30 days) site + schema + GBP + cluster + Tier 0 + Tier 1–3 *claims* (goal 20–30 citations — works *only* because they're claims, not earned links). Phase 2 (30–90) content distribution for topical authority. Phase 3 (ongoing) 2–5 *qualified* earned links/month, activity-tracked.

**The system:** the EFP_Authority_Map workbook is the template — Start Here / Tier 0 / Authority Map / Monthly KPI tabs, dropdown-controlled so VAs don't freestyle. Strip the client-specific rows and it carries to any client. **The defensible asset is the authority-mapping judgment** (where a business belongs online) — that's productized here, and it's why a content-volume tool isn't the bottleneck.

**White-hat outreach (VA-executable):** offer a free PDF companion guide of the Amazon ebook (*Make Your Website Ring*), paperback link inside (preserves TOS), with a contextual backlink to the relevant service page embedded in the PDF. Earns links via real expertise, no payment, no grey-hat.

**YMYL exception (insurance):** association/relationship lanes only — no standard Tier 4 grey-hat tactics. Highest E-E-A-T bar.

---

## 5. Content production

**R&E article workflow — Part 1 (structure):** define audience + intent in Claude first → generate 10 clickbaity titles, filter for SEO term + mystery → keyword + related questions via DataForSEO Keyword Explorer → hook = stat or stat+promise (avoid fictional-story hooks, accuracy risk) → **Johnson Box** up top (benefits + service CTA, skimmable list, interesting fact + visual idea per item) → **KeyTakeaway** callout before the body → FAQ section always expanded. Grade on the content-tool checklist; aim 100%.

**R&E article workflow — Part 2 (CTA & publish):** inject the **service-page CTA at items ~5 and ~10**, rendered as an image to reduce SEO text weight → AI image prompts per section (use GPT-4 for images; 4.1 may not generate them) → Grammarly pass (proofread + fact-check + plagiarism + AI detection) → 1,200–1,300 words → post → monitor GSC → tweak on impressions/CTR.

**Mandatory E-E-A-T elements:** named bylines (e.g. Sean Griffin for CRST, Henry Kowalec for EFP), "CRST Insider Tip" callouts with first-hand observations, "in our experience…" language, KeyTakeaway before the body, 7+ FAQs, local geographic specificity, Article + FAQPage JSON-LD.

**Blueprint system:** each cluster is built from a blueprint (the EFP 32-spoke model across 5 clusters) including entity maps, emotional architecture, and interlinking targets, built on the Rank & Expand Page Recipe + Semantic Authority Framework.

---

## 6. Technical & schema doctrine

**Schema (centralized, validated — never per-page LLM guesses):**

- LocalBusiness homepage only; **never** AggregateRating on it.
- Article: headline, author, datePublished, dateModified, description.
- FAQPage: every FAQ expanded, never collapsed.
- Person: named expert on every YMYL page.
- Output one clean JSON-LD block per page from validated code.
- **Original-publish-date schema** for genuine pre-HCU articles: datePublished = original year, dateModified = today. Signals you were the original authority, not a newcomer. Never fabricate dates.

**Architecture:** trailingSlash: never; centralized canonicals; single-hop 301s (redirect map before DNS flip; catch-alls destroy rankings); no thin service × location pages; Core Web Vitals as a ranking and UX factor; subdomain vs root-blog decision (root /blog/ preferred for new builds; subdomain consolidates an existing one).

---

## 7. AI search / GEO-AEO (our differentiator)

AI engines (Google AI Mode, the chat engines) decompose one query into 10–20+ sub-queries and retrieve at the **passage level**, synthesizing an answer from the best individual passages across the web. Implications:

- A single great article rarely gets pulled; a **cluster with deep coverage + tight internal linking** gets pulled repeatedly, because the engine finds a relevant passage for many sub-queries on your site. This is *why* the tier/hub structure and interlinking matter more now, not less.
- **Factual, non-promotional passages in spokes get cited before commercial pages** — by design. Blog/comparison content at a factual tone earns 40%+ of AI citations; promotional tone is penalized.
- The **sameAs entity graph** (Tier 0) is what lets AI engines resolve the business as a confident entity

## 8. Master build checklist (hand this to the AI)

**Research**

- Keyword classified with DEEPR; branded/pure-purchasing terms screened out
- 8–12 PAA questions collected; tier (1/2/3) assigned in the sitemap spreadsheet
- Blanket vs. sniper decided; DataForSEO data pulled into rows

**Build**

- Slug (patterned), title (<55), meta (<155); one H1, H2/H3 as real searches
- First paragraph answers in <300 chars (snippet); reassurance + teaser
- Body in 2–3 sentence chunks; data from credible non-competitor sources
- Media compressed (<100kB), descriptive filenames + alt text
- Upline/downline + up-tier + natural interlinks
- 7+ FAQs: immediate answers, no yes/no, internal links, expanded, FAQPage schema
- E-E-A-T: named byline, KeyTakeaway, Insider Tip, "in our experience"

**Local**

- GBP primary category set (seasonal plan noted); Products section used
- NAP canonical format consistent across site + top citations
- Tier 0 entity profiles live and wired via sameAs
- Local Falcon baseline scanned

**Technical**

- LocalBusiness homepage-only, no AggregateRating
- Article + FAQPage (+ Person on YMYL) JSON-LD, centralized
- trailingSlash never; centralized canonicals; single-hop 301s mapped pre-flip
- No thin service × location pages; Core Web Vitals checked
- Submitted to IndexNow / Omega

**Authority & measure**

- Authority map built; claims mined before outreach; KPI gated on DataForSEO
- GSC + GA4 connected; branded vs organic separated
- Hub measured via patterned-slug filter; n-gram CTR check on winners
- Syndicated via M.A.R.C.; expansion hub planned around top performers

## 🆕 Microsite Blueprint for Claude Code

🎥 [Loom](https://www.loom.com/share/0e7ac66c2f244361a4ad01aec9c58646) · 9:14

A complete microsite-building system you plug into Claude Code, so it builds sites from a proven blueprint instead of guessing.

This is the microsite method packaged as a knowledge base Claude Code reads while it works. Drop it into your project, and Claude builds to spec.

**This tool will help you:**

- Connect the Microsite Blueprint to Claude Code in a few minutes.
- Have Claude build microsites that follow the method, page by page.
- Skip the blank-page problem: the structure, the rules, the framework are already in place.

**🔒 Unlocks with Microsite Empire on day 30 or with **[**Premium**](https://skool.com/rank-expand-academy/plans)

## 🆕 SFTP Claude Code Microsite Build (w/ Prompts)

🎥 [Loom](https://youtu.be/XvCvKawtJAk) · 35:08

## 🆕LLM Wiki Slidedeck + Prompts

🎥 [Loom](https://youtu.be/1lDT4g_z3L0) · 9:35
