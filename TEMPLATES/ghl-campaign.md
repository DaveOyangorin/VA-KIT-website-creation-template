> **For Angelo** · Source: INBOX\<file> · Made: <date>
> Done: <one line>
> Needs your OK on: <…>
> Open questions: <…>

# <Campaign Name>

| Field | Value |
|---|---|
| Client | |
| Goal | |
| Audience | |
| Enters when (trigger) | e.g. tag `<tag-name>` is added |
| Sender name | |
| Sender email | (Angelo sets this in GHL) |
| Number of emails | |
| Exit when | e.g. books an appointment / tag `<tag>` added |

Merge field note: `{{contact.first_name}}` — if a contact has no first name, GHL shows blank,
so every greeting must still read fine without it ("Hi {{contact.first_name}}," → "Hi ,"
looks bad; use "Hi there," as the fallback where GHL allows, or start without a name).

---

## Email 1 — Day 0

- **Subject:** <≤ 50 chars>
- **Alternate subjects:** <…> · <…>
- **Preview text:** <≤ 90 chars>
- **CTA button text:** <2–4 words>
- **CTA link:** <URL>
- **Tag to add on click:** <tag or "none">

**Body**

<80–180 words.>

---

## Email 2 — Day <n>

(same fields)

---

## How to paste into GHL

(Menu names in GHL can change a little. Ask Angelo if you can't find one.)

1. **Create each email:** Marketing → Emails → Templates → New → pick a blank/simple
   layout → paste subject, preview text, and body → add the button with the CTA link → Save
   with the name `<Client> – <Campaign> – Email <n>`.
2. **Send yourself a test** of every email. Check the name field, links, and phone view.
3. **Build the workflow:** Automation → Workflows → Create → Start from scratch.
4. **Trigger:** the "Enters when" row above (e.g. Contact Tag → `<tag-name>`).
5. For each email in order: add **Send Email** (pick the template) → add **Wait** for the
   days until the next email.
6. Add the **exit / goal** from the table (e.g. Goal Event → tag added or appointment booked).
7. Add the "Tag to add on click" steps if listed.
8. Save as **Draft**. Do **not** publish. Tell Angelo it's ready — he turns it on.
