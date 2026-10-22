---
description: Build or add website pages (HTML drafts in OUTBOX) + a private preview link for Angelo
argument-hint: <site brief in INBOX>
---

Hand this job to the **MAMMATA** agent (`subagent_type: MAMMATA`) with the brief `$ARGUMENTS`.

If `$ARGUMENTS` is empty, list the files in `INBOX\` and ask the VA which file to use.

If MAMMATA wrote a data request instead of pages, tell the VA: "Angelo needs to send
keyword data first." Stop there.

When MAMMATA finishes and `OUTBOX\<client>-site\_preview.html` exists:
1. Read the whole file. Check that it has the "DRAFT PREVIEW" strip at the top, no tracking
   code, and no form that sends data. Fix it first if not.
2. Publish it with the **Artifact** tool as a **private** artifact (`file_path` = that file,
   title `<Client> site preview`, `icon` = `globe`). Pass the images it uses through `files`.
   It is a review copy of a draft for this client's agency, not the live site. Keep the
   client's design exactly; do not redesign it.
3. Open the link once and look. If the page is broken, fix the file and publish again to the
   same file.
4. Never pin it, never make it public, never send it anywhere yourself.
5. If publishing is refused or not available, say so in one line. The files in `OUTBOX\` are
   enough.

Tell the VA: which pages were made, the OUTBOX paths, the preview link, and any questions.
Tell her: "Send this link to Angelo only. Do not share it with the client."
