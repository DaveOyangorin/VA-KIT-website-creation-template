# Novarte VA — your app

A small app that runs on **your** computer, from this shared folder. It shows the tasks Angelo
sent you, lets you log your hours, and lists your drafts.

## Start it

1. Double-click **`START-VA.cmd`** (in this folder).
2. Your browser opens at **http://localhost:5080**.
3. Leave the small black window open while you work. Close it to stop the app.

First time only: if it says Node.js is missing, install it once from <https://nodejs.org>
(the big "LTS" button), then double-click `START-VA.cmd` again.

## The three tabs

| Tab | What it is |
|---|---|
| **My tasks** | What Angelo sent. Open the brief, then set the status: `in progress` → `submitted`. |
| **My time** | Log date, hours, client, job and a comment saying what you did. |
| **My drafts** | What your Claude wrote into `OUTBOX`, and what Angelo has approved. **Website photos → Save the photos** saves the client's real photos into the site folder as small WebP files. |

## How it stays in step with Angelo

Everything is a file in this folder, and OneDrive syncs it both ways:

- `tasks.json` — the task list (his app writes it too)
- `INBOX\` — his briefs and documents
- `OUTBOX\` — your drafts · `OUTBOX\_approved\` — the ones he approved
- `WORKLOG.csv` — your hours

Changes can take a minute to appear. Press **Refresh** if you are impatient.

## Good to know

- The app only reads and writes **this folder**. Nothing else on your PC.
- It goes online for one thing only: **Save the photos** downloads the photos a site page
  links (https, picture files only).
- It listens on your own machine only (`localhost`), so nobody else can open it.
- It does **not** run Claude. That is the Claude Code side of the kit (`START-HERE.md`).
- Only Angelo can mark a task `approved`. You can set `open`, `in progress`, `submitted`.
- Never put passwords in a file here.

## For the technical helper

`node server.js` (Node 18+, no dependencies). `VA_PORT` changes the port, `VA_KIT` the folder.
Tests: `node test\run-tests.js` — exit 0 means everything passed.
