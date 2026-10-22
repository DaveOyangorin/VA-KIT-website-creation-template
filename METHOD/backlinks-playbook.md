# Novarte AI — Backlink Playbook (for the VA)

A **backlink** is a link from another website to the client's website. Google treats good
backlinks like recommendations. A few real ones beat hundreds of junk ones.

A strong local link profile is built on real things: real partners, real awards, real
certifications, real directories.

---

## The one test for every link

> **Would this link still make sense if Google didn't exist?**

If a real customer could find the client through that page, or the link comes from a real
relationship, it passes. If it only exists "for SEO", skip it.

**Relevance beats authority.** A local partner in the same trade beats a big random site.

---

## The 7 pillars (where good local links come from)

1. **Industry partners & certifications** — associations, brands the client is certified by,
   insurer or vendor "find a provider" pages. Only certifications the client really holds.
2. **Awards & recognition** — award pages and the press about them.
3. **Press & editorial** — local news, trade magazines, journalist requests.
4. **Social profiles** — Facebook, LinkedIn, Instagram, YouTube, X — each with the website URL.
5. **Directories & citations** — Google, Apple, Bing, Yelp, BBB, Yellow Pages, Nextdoor,
   industry directories, the local Chamber.
6. **Community & sponsorships** — teams, schools, charities, events the client supports.
7. **B2B platforms** — LinkedIn company page, business networks.

## The 4 phases (always in this order)

1. **Foundation** — claim/complete the free core listings and social profiles. NAP identical.
2. **Niche authority** — industry directories, associations, certifications.
3. **Awards & press** — pitches and applications.
4. **Community** — sponsors, partners, local groups. Ongoing.

Finish most of Phase 1 before starting Phase 2. Foundation mistakes spread everywhere.

---

## The rules

1. **NAP is sacred.** Name, Address, Phone must be **character-for-character** the same on
   every listing: same "Suite" vs "#", same abbreviations, same phone format. Copy it from the
   plan. Never type it from memory.
2. **Claim, never duplicate.** Before creating a listing, search the site for the business
   name, the phone number, and the address. If a listing exists, **claim** it. Two listings for
   one business hurt rankings and are hard to delete.
3. **Skip anything the brief says not to pursue.** Those are standing decisions from Angelo.
4. **Nothing paid without Angelo's OK.** Many paid listings use `nofollow` links, which pass
   no SEO value. A $300 nofollow listing is worth $0 in links.
5. **Never buy links.** No link packages, no "guest post" sellers, no PBNs (fake blog
   networks), no link swaps with random sites, no fake reviews. These can get the client
   penalized.
6. **Natural anchor text.** The clickable text should be the business name or the plain web
   address. Never stuff keywords ("best plumber Sandy Utah") into links.
7. **Every outreach target needs a reason.** A real relationship, a real story, or a real
   resource. No template blasts. 3–5 personal emails at a time.
8. **Never guess a contact.** Find the real contact page yourself. Confirm it before sending.
9. **Healthcare, legal, and money clients (YMYL)** — only real credentials, real licenses,
   real people. Accuracy matters more than speed.
10. **Logins go in the password manager Angelo chooses.** Never in the tracker, a doc, or
    a chat. Use the client email Angelo gives you for sign-ups.

---

## How to check if a link is "dofollow" (after it goes live)

1. Open the page with the client's link in Chrome.
2. Right-click the link → **Inspect**.
3. Look at the highlighted `<a ...>` code.
   - Contains `rel="nofollow"`, `rel="sponsored"` or `rel="ugc"` → write `no` in the tracker.
   - None of those → write `yes`.

---

## Tracker statuses

| Status | Meaning |
|---|---|
| `todo` | not started |
| `approved` | Angelo said go |
| `submitted` | you claimed / created / sent it |
| `pending` | waiting for the site to verify or reply |
| `live` | the link is up — paste its URL in `live_link_url` |
| `rejected` | the site said no |
| `skip` | decided not to do it — write why in `notes` |

Follow up on anything `submitted` or `pending` for more than 14 days.

---

## Your weekly loop

1. Run `/backlinks INBOX\<plan>` → get the next batch.
2. Angelo approves (he moves the files to `OUTBOX\_approved\` or marks rows `approved`).
3. Do the batch by hand. Update the tracker after each one.
4. Friday: check `live` links for dofollow, and follow up on old `pending` rows.
