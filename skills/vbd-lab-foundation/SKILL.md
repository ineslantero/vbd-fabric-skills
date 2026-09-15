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

## Style rules for the generated labs

- **Talk to the learner.** Second person, active voice ("Create a Lakehouse", not "A Lakehouse should be created").
- **Bullet-first.** Every step is one action, one line, one verb.
- **Show, don't tell.** Every conceptual claim gets a code block, a screenshot placeholder, or a Learn link — never both a claim and a hedge.
- **No filler.** Cut every "In this section, we will…" and "As we discussed above…" — the tutorial does that; your labs shouldn't.
- **Check yourself.** Every lab ends with a *"You should now see…"* checkpoint the learner can verify.

## Exit

Print: labs authored, freshness report location, and any TODOs the CSA must resolve manually before shipping.
