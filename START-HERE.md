# Welcome to the Novarte AI VA Kit

This folder teaches you how Novarte AI works. It also gives you a helper called **ALLIEVA**.
ALLIEVA writes drafts for you. You check them, Angelo approves them, and then you do the
real-world step (claim the listing, send the email, paste into GHL).

---

## 1. One-time setup (about 15 minutes)

1. **Install the Claude desktop app** from https://claude.ai/download and sign in with
   **your own** Claude account (a paid plan that includes Claude Code).
2. **Accept the OneDrive share.** Open the share link Angelo sent you. Click
   **"Add shortcut to My files"**. Wait until the `VA-KIT` folder shows on your computer in
   File Explorer under OneDrive.
3. **Keep it synced.** In File Explorer, right-click `VA-KIT` → **Always keep on this device**.
4. **Open the kit in Claude.** In the Claude app, open the **Code** tab → choose a folder →
   pick `VA-KIT`.
5. **Test it.** Type `/backlinks` and press Enter. ALLIEVA should list the INBOX files or ask
   which file to use. If it does, you're ready.

---

## 1b. Your app (tasks, hours, drafts)

Open the folder `app\` and double-click **`START-VA.cmd`**. Your browser opens your app at
`http://localhost:5080`. It has three tabs:

- **My tasks** — what Angelo sent. Open the brief, then set `in progress` → `submitted`.
- **My time** — log the date, the hours, the client, and a comment on what you did.
- **My drafts** — what you produced, and what Angelo approved.

Leave the small black window open while you work; close it to stop the app.
The app and Angelo's app share this folder, so both of you see the same tasks and hours.

---

## 2. Your daily flow

1. **Check `INBOX\`** for new files from Angelo. A file with `_fix_` in the name is a fix
   note → run `/revise` on it. Also glance at the top of `WHAT-CHANGED.md` for kit updates.
2. **Run the command** for the job (table below).
3. **Read the draft** in `OUTBOX\`. Answer ALLIEVA's questions if it asks any.
4. **Wait for Angelo's OK.** He moves approved files to `OUTBOX\_approved\`.
5. **Do the real step** by hand, using only the approved file.
6. **Update the tracker** if it's backlink work.
7. **Log your time at the end of every session.** Type
   `/log <hours> <what you did>` — for example `/log 2.5 claimed Yelp and the health directories`.
   It writes the date, the hours and your words into `WORKLOG.csv`. Angelo reads that file.
   Log it the same day. Say what you actually did, and say it plainly if something blocked you.

---

## 3. Your first job: backlinks

```
/backlinks INBOX\<client>_backlink-strategy_<date>.md
```

Start with **Phase 1 (foundation)** rows only. Read `METHOD\backlinks-playbook.md` first —
it takes 10 minutes and explains every rule.

---

## 4. Commands

| Type this | You get |
|---|---|
| `/backlinks INBOX\file` | Link tracker (CSV) + listing text + outreach emails |
| `/audit-review INBOX\file` | A plain to-do list from an SEO audit |
| `/website INBOX\file` | New titles, meta descriptions, headings, page copy, FAQ |
| `/gbp INBOX\file` | Google Business Profile posts (CSV) + profile text |
| `/emails INBOX\file` | A Go High Level email campaign + paste steps |
| `/build-site INBOX\file` | Website pages as draft files in `OUTBOX\<client>-site\` + a private preview link (send it to Angelo only). **For a whole website, follow `WEBSITE-PROMPTS.md` step by step** (static or 3D) |
| `/page-copy INBOX\file` | The words for one page or blog post |
| `/revise INBOX\fix-note` | Fixes your draft using Angelo's fix note |
| `/log 2.5 claimed Yelp and the health directories` | Logs your time: date, hours, and what you did |

Tip: type `/` and a list of all commands pops up, with a short explanation beside each one.

You can also just ask in plain words, like *"write 8 GBP posts from the brief in my INBOX"*.

---

## 5. The rules

- **Nothing goes live without Angelo's OK.**
- **Copy the business name, address, and phone exactly.** Never retype them.
- **Claim listings that already exist.** Never make a second listing.
- **Never pay for anything.** Flag it to Angelo.
- **Never buy links or reviews.**
- **Passwords go in the password manager Angelo gives you.** Never in this folder, never in
  a chat with Claude.
- **If a draft has a fact you think is wrong, don't use it.** Ask Angelo.

---

## 6. What's in the folder

| Folder | What it is |
|---|---|
| `INBOX\` | Files from Angelo |
| `OUTBOX\` | Your drafts. `_approved\` = OK to use |
| `METHOD\` | Novarte's playbooks. Read them to learn the method |
| `TEMPLATES\` | The shape of every draft |
| `CLAUDE.md`, `.claude\` | ALLIEVA's instructions. Don't edit |
