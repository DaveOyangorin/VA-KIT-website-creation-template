# Semantic Site Audit & Tools

> Source: AI SEO: Rank Expand Academy (Skool) — `classroom/b74a800f`  
> 11 lessons · 8 videos (~46 min) · 16 KB of written material  
> Internal reference for MAMMATA. Not for redistribution.

---

## Semantic Drift Analysis

### What Semantic Drift Is & Why It Matters

🎥 [Loom](https://www.loom.com/share/c57e8681f78348d3ad5d2c6720d758bd) · 4:04

> **Semantic drift** is when a page slowly moves away from the original topic of the cluster — either because the content changed, the SERP changed, or the site structure shifted.

In this lesson you’ll learn how to use the open-source *Semantic Drift Analyzer* together with Screaming Frog and Google Search Console. You’ll be able to spot pages that have drifted away from their original topic, lost relevance, or no longer fit your content cluster—and turn that into a focused optimization plan.

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/229eef8f8b6847e09b45b9b0620f0ce8eaa162cfa6d5423c9fca0f74426912f0.png)

**Why this matters:**

- It weakens topical authority.
- It creates “weird” pages in clusters that confuse Google.
- It can drag down internal link equity.
- Google may treat these pages as “outliers”, causing traffic decay.

**What this tool solves:**

- It shows **which pages are drifting** based on **semantic distance**
- It combines **content vectors + internal links + GSC performance**
- It gives you a **radial map** of your cluster health

**Signs a site needs this:**

- Large sites / old blogs
- E-commerce product catalogs
- Any site with migrating content
- Teams that publish without cluster guardrails

### Quick Start Guide

🎥 [Loom](https://www.loom.com/share/9e39b8fca24846819ce7d876693bcc0d) · 1:37

## Find Pages That Drift From Their Topic

In this lesson you’ll learn how to use the open-source *Semantic Drift Analyzer* together with Screaming Frog and Google Search Console. You’ll be able to spot pages that have drifted away from their original topic, lost relevance, or no longer fit your content cluster—and turn that into a focused optimization plan.

---

# **Quickstart (experts):**

1. Run Screaming Frog with OpenAI embeddings enabled. Export all URLs as CSV so you have columns: Address, OpenAI Embeddings 1 (or similar), Inlinks.
2. Export a GSC “Search results” CSV with Page + Clicks (optionally Impr/CTR/Pos).
3. Run locally (one by one):

```
git clone https://github.com/lukegravity/semantic-drift-analyzer.git

cd semantic-drift-analyzer

python3 -m venv .venv && source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```

---

# **What you'll need (Requirements slide / section)**

## **Tools:**

- Screaming Frog (licensed, with OpenAI/AI embeddings enabled)
- Google Search Console access for the site
- A Mac/PC with:

- Python 3 installed
- Git (or download ZIP from GitHub)

## **Skill level:**

- Comfortable installing apps / running a few terminal commands
- Basic understanding of:

- URLs, internal links
- Clicks & impressions in GSC
- What “content clusters” are

### 1 - Install & Start Semantic Drift Analyzer

🎥 [Loom](https://www.loom.com/share/bc49eb6dd9f84c78944b21df7a7dd8c4) · 2:29

# Step by step process to install the software

1. **Open your terminal.**
2. **Download the app:**

```
git clone https://github.com/lukegravity/semantic-drift-analyzer.git
cd semantic-drift-analyzer
```

1. **Create and activate a virtual environment (recommended):**

```
python3 -m venv .venv
```

- **For Mac / Linux:**

```
source .venv/bin/activate
```

- **For Windows PowerShell:**

```
.venv\Scripts\activate
```

1. **Install dependencies:**

```
pip install -r requirements.txt
```

1. **Run the app:**

```
streamlit run app.py
```

1. **Open your browser** at the address Streamlit shows (usually [http://localhost:8501](http://localhost:8501)).

### **If you close the terminal**:

1. Open a new one
2. `cd semantic-drift-analyzer`
3. `source .venv/bin/activate`
4. `streamlit run app.py`

### 2 - Export Screaming Frog CSV

🎥 [Loom](https://www.loom.com/share/8ff8f073e62046d089ee99ee618ad819) · 3:25

> **Important:** Your Screaming Frog crawl must include an embeddings column.

If you see long vectors like 0.034, 0.012, -0.028, ... → you’re good.

1. **Configure embeddings once (only first time):**

- In Screaming Frog:

Configuration → API Access → AI/OpenAI

- Add your OpenAI key
- Choose an embedding model like text-embedding-3-small.
- Then go to:

Configuration → Content → Embeddings

- Enable embedding functionality
- Select a prompt that embeds the page content (e.g. using {{content}}).
2. **Crawl the site:**

- Enter the domain, click **Start**.
- Wait until the crawl finishes.
3. **Export the CSV:**

- Go to: Bulk Export → All URLs → CSV (or similar export that includes all internal HTML).
- Make sure this file contains at least:

- Address – the URL
- Your embeddings column (e.g. OpenAI Embeddings 1)
- Inlinks – number of internal links
4. **Quick check:**

- Open the CSV in a spreadsheet.
- Confirm the embeddings column has long numeric vectors like what you pasted:

0.0379,0.0138,-0.0280,....

That’s your **site structure + vectors** file.

### 3 - Export the GSC CSV

1. Open **Google Search Console** → choose your property.
2. Go to **Performance → Search results**.
3. Set a date range (e.g. “Last 3 months”).
4. Make sure **Page** is one of the dimensions (it usually is by default).
5. Click **Export** → **Download CSV**.
6. Verify the CSV has at least:

- Page (URL)
- Clicks
- (Optionally) Impressions, CTR, Position.

This is your **performance** file.

### 4 - Use the Semantic Drift Analyzer

🎥 [Loom](https://www.loom.com/share/12a0ae99bbc640f0a066e1fb70f4fa2c) · 3:53

Inside the Streamlit app:

1. **Upload the Screaming Frog CSV** (embeddings file).
2. **Upload the GSC CSV**.
3. The app will:

- Normalise/clean URLs
- Merge performance onto the crawl file
- Build a semantic “center”
- Measure **distance** of each page from that center
4. You’ll see a **radial / orbit-style visualization**, plus a table.

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/fe0c05adf86a4b3da1a79b02a03ccbbdf04efb09d5064dafbbfcad23c6b7d804-md.png)

### 5 - Interpret The Results

🎥 [Loom](https://www.loom.com/share/2868bb58c801471e827a2947e1b09132) · 6:04

# **🎯 What this visualization shows you**

The Semantic Drift Analyzer creates a **semantic map** of your entire site or content cluster:\\

- The **center** is the cluster’s “semantic core”
- Each **dot = a page**
- Its **distance** shows how far it has drifted from the core topic
- Its **angle** shows which sub-topic or theme it’s most similar to
- Its **size/color** reflects performance (usually clicks from GSC)

This gives you a fast, visual way to see:

- Which pages “belong”
- Which pages drifted
- Which pages are hidden opportunities
- How healthy your clusters are

---

# **⚡ Quick Interpretation Checklist**

> **If a dot is:**

✔ Far out + low clicks → Fix / prune

✔ Far out + high clicks → New cluster opportunity

✔ Close in + low clicks → Improve quality / CTR / links

✔ Grouped at same angle but different distances → Uneven content quality

This alone lets most people take action immediately.

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/dec30734d14f400cbefdf17d109648b84c250f5c8d4b4a70a8a9a0bbd278875d-md.png)

---

# **💡 Key Concepts (simple definitions)**

## **Distance from center**

How “off-topic” or “outlier-ish” the page is compared to the cluster’s semantic core.

## **Angle / neighbourhood**

Which semantic subtheme the page belongs to.

Pages with similar angles share similar topics.

## **Point size / color**

Performance signals, usually **Clicks from GSC**.

Big bright dot = strong performer.

---

# **🔍 Patterns to Look For (and What to DO)**

## **1️⃣ Far from center + LOW clicks**

**→ Drifted or off-topic pages. These drag down topical authority.**

**Actions:**

- Rewrite to realign with the cluster intent
- Move it to another cluster
- Redirect or prune if irrelevant or redundant

## **2️⃣ Far from center + HIGH clicks**

**→ Breakout topic. Don’t “fix” it — expand around it.**

This is a **new cluster trying to form**.

**Actions:**

- Create a new hub / sub-silo for that content area
- Add supporting articles to strengthen the emerging silo
- Improve internal links to spread authority around the new theme

## **3️⃣ Close to center + LOW clicks**

**→ On-topic but underperforming.**

These are your **highest leverage easy wins**.

**Actions:**

- Improve titles, meta descriptions → boost CTR
- Add internal links from the cluster’s strongest pages
- Add FAQs, schema, visuals, enrich content
- Strengthen E-E-A-T signals

## **4️⃣ Group of pages at same angle but different distances**

**→ Subtopic with uneven content quality.**

Some pages are well aligned → others are drifting.

**Actions:**

- Identify “best examples” (close to center + decent clicks)
- Use these as templates for weaker articles
- Rewrite, consolidate, or merge pages where relevant

---

# **🧠 Expert Mode (optional advanced insights)**

## **Angle = semantic direction**

Pages with the same angle share **topic DNA**.

If your cluster has multiple angles far apart → the cluster is too broad.

## **Distance = semantic purity**

Pages far from the core aren’t “bad” — they are just less aligned.

Distance helps choose between:

- Rewrite
- Redirect
- Expand into a new cluster

## **Density = topic consistency**

A dense cluster near the center = a healthy silo.

Sparse, noisy points = messy information architecture or unfocused authors.

## **High drift + high internal links**

If a drifted page still gets many inlinks →

Internal linking is likely pointing at the wrong content.

## **Sudden drift**

When a previously aligned page jumps outwards:

- Content rewrite changed the topic
- Google now sees it differently (SERP intent shift)
- Site structure changed during a migration

## **Cluster splitting**

If a cluster visually “breaks in two”, it’s usually a sign you have **two themes mixed together**.

**Solution:**

Split them into **two hubs** and rebuild internal links accordingly.

### 6 - Advanced Interpretation

# **🧠 Why this matters**

Lesson 5 gives you the **what** and the **basic actions**.

This lesson gives you the **advanced patterns**, the subtle signals and edge cases the best SEOs use to make stronger strategic calls.

---

# **🔭 Advanced Concepts**

## **Semantic Angle = Topic Direction**

Pages with the same angle share deeper semantic DNA.

Use this to:

- Detect natural subtopics
- Spot cluster splits forming
- Identify content that’s thematically misfiled

## **Semantic Distance = Topic Purity**

Distance isn’t “good or bad”, it’s a *signal*:

- Large distance + value → **new cluster**
- Large distance + no value → **drift or misalignment**
- Small distance + no performance → **quality/CTR issue**

## **Semantic Density = Content Consistency**

Dense clusters = strong, coherent topic silos.

Sparse or noisy clusters = diluted topical authority.

---

# **🔍 Advanced Patterns**

## **1️⃣ High drift + high internal links**

This often means:

- Internal links are pointing to the *wrong* page
- Cluster hubs are misaligned
- Navigation is favouring outdated content

> **Fix:** rebuild internal linking with corrected cluster structure.

---

## **2️⃣ High clicks + few neighboring pages**

This is a **“lonely winner”**.

It means:

- You rank for something underserved
- You have an opportunity for a new silo
- Competitors may be weak in this subtopic

> **Action:** build 3–7 supporting pages around it.

---

## **3️⃣ Cluster “splitting” into two angles**

This indicates:

- One cluster contains two different intents
- Google sees them separately
- Your current hub is too broad

> **Action:** split into 2 hubs → reorganize links.

---

## **4️⃣ Sudden drift on previously stable pages**

This happens when:

- Content was rewritten
- A migration changed structure
- SERP intent evolved
- Google reclassified the page

> **Action:** compare old vs new content → realign or split.

---

## **5️⃣ Drifted pages with high impressions but low clicks**

Means the page *appears* often but doesn’t meet intent.

> **Action:** rewrite titles/meta + tighten intent match.

---

## **6️⃣ Pages clustered together but different performance**

Same topic, different outcomes.

> **Action:** analyze top-performing content → turn into templates.

---

# **🎯 Summary**

Expert mode helps you:

- See how topics evolve
- Detect emerging opportunities early
- Spot structural problems (navigation, hubs, internal links)
- Strengthen topical authority with precision

# Next Steps

Now that you know how to interpret the map, let’s look at the 5 types of actions you can take.

### 7 - Determine What Actions To Take

🎥 [Loom](https://www.loom.com/share/3d9ae026734647949d6a40ecff3add89) · 8:28

## **🎯 Purpose**

This lesson helps you **decide exactly what to do** with each page, based on its semantic behavior and performance.

> By the end of this lesson, you’ll know the 5 action types and when to apply them:

**Realign, Expand, Optimize, Consolidate, Prune.**

![](https://assets.skool.com/f/e0c04038afe74a28a97dccc4b03256df/e107cabff8894e11b2eaeee30159cc78e09ba6b9bc62410293b192e754ef1438-md.png)

---

## **🧭 Action Types (Simple Framework)**

### **1️⃣ Realign**

For drifted but valuable pages.

**When:**

- Far from center
- Low–medium clicks
- Still relevant to your business

**Actions:**

- Rewrite content to match the cluster intent
- Add missing subtopics
- Improve readability & clarity
- Tighten internal linking from the cluster hub

---

### **2️⃣ Expand**

For breakout-topic pages.

**When:**

- Far from center
- High clicks
- Obvious new sub-theme or intent

**Actions:**

- Create a new hub/silo for the emerging topic
- Build supporting content around this theme
- Strengthen internal links inside the new silo

---

### **3️⃣ Optimize**

For on-topic but underperforming pages.

**When:**

- Close to center
- Low clicks
- Good content but weak performance

**Actions:**

- Improve title & meta description
- Add schema (FAQ, HowTo, Product)
- Add internal links from the strongest pages
- Add better visuals or E-E-A-T elements

---

### **4️⃣ Consolidate**

For clusters with uneven content quality.

**When:**

- Pages share the same angle
- Some are far from center, some close
- Redundant or overlapping topics

**Actions:**

- Merge weaker pages into stronger ones
- Remove duplicate content
- Use the strongest version as the template

---

### **5️⃣ Prune / Redirect**

For pages that no longer fit your cluster or site strategy.

**When:**

- Far from center
- Low clicks
- Low inlinks
- No strategic value

**Actions:**

- Redirect to strongest relevant page
- Or 410 if irrelevant & no value
- Clean up orphaned URLs on your site

---

## **🧘 Keep it simple**

→ Identify the page type

→ Choose **one** action: realign, expand, optimize, consolidate, prune

→ Add it to your backlog (next lesson)

Once you’ve chosen the right action for each page, the next step is turning that into a backlog you can actually execute.

**➡ Turn these decisions into a backlog you can act on in the next module.**

### 8 - Turn Action Items Into Backlog

🎥 [Loom](https://www.loom.com/share/bc258af936004328bd4f9298962c6c87) · 16:14

# **🎯 Purpose**

This lesson helps you **turn insights into an actionable, prioritized SEO backlog**—so you can execute and measure results.

---

# **📋 Backlog Framework Overview**

Each page receives:

- **Page Type** (Realign / Expand / Optimize / Consolidate / Prune)
- **Recommended Action**
- **Effort** (S / M / L)
- **Impact** (Low / Medium / High)
- **Owner** (optional)
- **Due Date / Sprint** (optional)

---

## **🔥 Step 1 - Export your “Problem Pages”**

Use the table at the bottom of the Semantic Drift Analyzer to:

- Sort by distance
- Filter by low clicks
- Or highlight breakout pages
- Or sort by angle to find sub-clusters

This gives you a shortlist of pages needing attention.

---

## **🔥 Step 2 - Assign the Page Type**

Use the categories from the previous lesson:

- Realign
- Expand
- Optimize
- Consolidate
- Prune/Redirect

This makes prioritization straightforward.

---

## **🔥 Step 3 - Write the Action**

Examples:

- “Rewrite to better match {keyword/topic intent}.”
- “Move this to the {cluster name} silo.”
- “Add 5 internal links + improve CTR.”
- “Combine with URL X and redirect.”
- “Create hub around {breakout topic}.”

Short, clear, actionable.

---

## **🔥 Step 4 - Estimate Effort**

Use a simple scale:

- **S (Small):** CTR update, add links, minor enhancements
- **M (Medium):** Rewrite or consolidation
- **L (Large):** New cluster creation, hub restructuring

Let consultants pick what’s realistic per sprint.

---

## **🔥 Step 5 - Score for Impact**

Impact is based on:

- Clicks
- Impressions
- Importance of the cluster
- Business goals

Use a quick scoring:

- **High impact:** Breakout topics or drifted pages in money clusters
- **Medium:** Underperformers
- **Low:** Old blog posts, low-value areas

---

## **🔥 Step 6 - Sort & Prioritize**

Sort backlog by:

```
Impact DESC
Effort ASC
```

This surfaces:

- Easy wins
- Highest ROI pages
- Deprioritizes heavy tasks with low impact

---

# **Your backlog becomes your roadmap:**

- Fix what’s drifted
- Grow what’s breaking out
- Boost what’s underperforming
- Prune what harms cluster quality

→ This guarantees steady SEO improvement without guesswork.
