---
name: vbd-lab-foundation
description: Author the 4 Fabric Foundation Discovery Labs (Lakehouse, Warehouse, RTI, Data Science) tailored to the customer in workshop.yaml.
inputs:
  - workshop.yaml
  - data/ (from /vbd-data)
outputs:
  - labs/01-lakehouse/     README + notebooks
  - labs/02-warehouse/     README + T-SQL scripts
  - labs/03-rti/           README + KQL + eventstream config
  - labs/04-datascience/   README + 4 notebooks (ingest, explore, train, predict)
  - .vbd/freshness-foundation.yaml
---

# /vbd-lab-foundation

Regenerate the SharePoint Foundation Discovery Labs against the customer's data and industry angle. **You never invent lab structure** — you re-skin the reference tutorial for each lab.

## The 4 labs

| # | Lab | Reference | Data comes from | Tech taught |
|---|---|---|---|---|
| 01 | **Lakehouse** | `references/lakehouse/lakehouse-tutorial.md` | `data/*.csv` + WWI zip via fetch script | Lakehouse, OneLake, shortcuts, Delta, Spark, SQL endpoint |
| 02 | **Warehouse** | `references/warehouse/warehouse-tutorial.md` | Lakehouse output (Lab 01) | Warehouse, T-SQL, stored procs, semantic model |
| 03 | **RTI** | `references/rti/rti-tutorial.md` | Fabric built-in sample streams | Eventstream, Eventhouse, KQL, real-time dashboard, Activator |
| 04 | **Data Science** | `references/datascience/datascience-tutorial.md` | `data/*.csv` (customer regression/classification target) | Notebooks, MLflow, batch scoring, semantic link |

## Authoring loop — one pass per included lab

1. **Load the reference tutorial** at `references/<lab>/<lab>-tutorial.md` and its `sources.yaml`. Extract objectives, step order, checkpoints, and every code snippet + Learn citation.
2. **Load `templates/lab-readme.md`** and populate the header from `workshop.yaml` + `data/README.md`.
3. **Re-skin each step** — keep the objective, order, and Fabric operation; swap WWI/taxi names for the customer's entity names (e.g. `fact_sale` → `fact_claim`, `dimension_customer` → `dimension_member`). Preserve every Learn URL.
4. **If the lab needs a big download**, prepend a **Step 0 — Download the sample data** block (both PowerShell and Bash), pointing at `data/fetch-data.ps1` / `.sh`. Only Lakehouse needs this today (1.9 GB WWI zip); Warehouse and RTI don't.
5. **Add exercise + solution notebooks** — TODOs in the exercise, mirrored solutions in `solutions/` (only shipped if `deliverable.include_solutions=true`).
6. **Freshness gate — mandatory.** Call `components/freshness.verify(draft)` before writing. Every feature name, UI path, KQL/SQL snippet, and REST endpoint is validated against Microsoft Learn. Preview features get a preview banner; deprecated features are rewritten; anything unresolved after 3 attempts becomes a TODO with a citation.
7. **Emit `.vbd/freshness-foundation.yaml`** — machine-readable verification report.

## Sample "Step 0 — Download the sample data" block

```markdown
## Step 0 — Download the sample data

Grab the ~1.9 GB workshop dataset before you start:

- **PowerShell:** `./data/fetch-data.ps1`
- **Bash:** `./data/fetch-data.sh`

Safe to re-run — the script skips the download if the zip is already there.
```

## Style rules for generated labs

Modelled on [ineslantero/fabric-training-cmi/labs](https://github.com/ineslantero/fabric-training-cmi/tree/master/labs) — concise, engaging, action-first. Every lab follows the same skeleton (see `templates/lab-readme.md`):

1. **Objective** — 4–8 bullets, one capability each ("Create a Fabric Lakehouse", "Query tables through the SQL analytics endpoint").
2. **Why this matters for {customer.name}** — 4–7 bullets connecting each capability to the customer's business ("OneLake gives {customer} a shared data layer for actuarial modelling"). *Never* say "in this lab, we will…".
3. **Microsoft Learn references** — flat bullet list at the top of the lab, not scattered under each step. Pull these straight from `references/<lab>/sources.yaml`.
4. **Prerequisites** — Fabric access, capacity, permissions, and the exact CSV files the lab uses (path: `data/<file>.csv`).
5. **Data setup options** *(from Lab 02 onwards, so labs are replayable)*:
   - Option A — you already have the tables loaded from a prior lab
   - Option B — start fresh: create workspace + Lakehouse + upload CSVs + load to tables
6. **Sample data** — one h3 per CSV file with a one-line description and a flat `Fields:` list.
7. **Lab steps** — `### Step N: <Verb> <Object>`. Each step is bullets, one action per bullet, imperative mood. Code blocks for SQL/Python where useful. Optional short **Explanation:** paragraph at the end of a step (never before). Optional **Checkpoint:** line the learner can verify.
8. **Troubleshooting** — 3–6 `**symptom** → fix` bullets.
9. **What's next** — one sentence pointing at the next lab.

### Voice

- **Second person imperative.** "Open Microsoft Fabric", "Go to Workspaces", "Select New item". Never "we will now open…".
- **One action per bullet.** No compound sentences.
- **No filler.** Cut "In this section", "As you can see", "Let's now", "We're going to". If a sentence can be removed without losing meaning, remove it.
- **Show, don't tell.** Every conceptual claim gets a code block, a link, or a checkpoint — never both a claim and a hedge.
- **Explanations come last.** After the actions, one short paragraph telling the learner *why* what they just did matters. Prefix with `**Explanation:**`.

### Naming convention for items the learner creates

Use `{{customer.slug}}_lab{{N}}_<item>_name` so no two attendees clash — e.g. `contoso_lab01_lh_name` for a Lakehouse. This mirrors the CMI labs and works well in shared training workspaces.

## Exit

Print: labs authored, freshness report location, and any TODOs the CSA must resolve manually before shipping.
