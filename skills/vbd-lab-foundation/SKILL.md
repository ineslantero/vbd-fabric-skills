---
name: vbd-lab-foundation
description: Author the Fabric Foundation Discovery Labs (Lakehouse, Data Warehouse, Real-Time Intelligence, Data Science) tailored to the customer in workshop.yaml.
inputs:
  - workshop.yaml
  - data/ (from /vbd-data)
outputs:
  - labs/01-lakehouse/     README + scripts + notebook cells + data slice
  - labs/02-warehouse/     README + T-SQL scripts + notebook cells
  - labs/03-rti/           README + KQL scripts + eventstream config
  - labs/04-datascience/   README + 4 notebooks (ingest, explore, train, predict)
  - .vbd/freshness-foundation.yaml
---

# /vbd-lab-foundation

Replaces the static SharePoint Foundation Discovery Labs bundle (`Data and AI/Fabric/1 - Upskilling/1 - Foundation/Upskilling on MS Fabric Foundation/Assets/02 - Discovery Labs`) with regenerable, customer-relevant, freshness-verified content.

## What it produces

Four labs, each mapped one-to-one against the current SharePoint asset it replaces:

| Lab | Replaces | Data | Tech |
|---|---|---|---|
| 01 Lakehouse | `Lakehouse Tutorial.docx` + `wwi-sample-dataset.zip` | Customer domain (from `/vbd-data`) | Lakehouse, OneLake, Delta, Spark, SQL endpoint |
| 02 Data Warehouse | `Fabric Data Warehouse Tutorial.docx` + T-SQL scripts | Same domain, gold layer | Warehouse, T-SQL, stored procs, semantic model |
| 03 Real-Time Intelligence | `Real-time Intelligence Tutorial.docx` + KQL scripts | Streaming variant of the fact table | Eventstream, Eventhouse (KQL DB), Activator, real-time dashboard |
| 04 Data Science | `Data Science Tutorial.docx` + NY-taxi notebooks (`1-ingest`, `2-explore`, `3-train`, `4-predict`) | Customer-domain regression/classification target | Notebooks, MLflow, model registry, batch scoring |

## Authoring rules

For each lab:

1. **Load the template** `templates/lab-readme.md` and populate from `workshop.yaml` + `data/README.md`.
2. **Draft steps** grounded in the *concepts* (workspace, OneLake, medallion, Delta, KQL, MLflow), not screenshots. Use API/UI paths but describe them narratively so a rename doesn't invalidate the whole step.
3. **Compose exercises + solutions** — TODOs in the exercise notebook, mirrored solutions in `solutions/` (only shipped if `deliverable.include_solutions=true`).
4. **Freshness gate — mandatory.** Before writing files, call `components/freshness.verify(draft)`. Every feature name, UI path, KQL/SQL construct, and REST endpoint must be validated against Microsoft Learn. Roadmap-preview features get a preview banner. Deprecated features are rewritten. Loop caps at 3 attempts; anything unresolved becomes a TODO with citation.
5. **Emit `.vbd/freshness-foundation.yaml`** — machine-readable report embedded at repo root.

## Lab 01 — Lakehouse content outline

_Skill will fill this in; here's the shape_

- **Objectives:** create a workspace, create a Lakehouse, load bronze via shortcut/upload, transform to silver via notebook, build gold aggregate, query via SQL endpoint.
- **Steps:** workspace creation → Lakehouse creation → ingest (Data Factory copy or upload) → notebook to Delta → SQL endpoint query → semantic model.
- **Customer angle:** e.g. "map OneLake to your existing ADLS Gen2 estate via shortcuts".
- **Notebook:** `01 - Create Delta Tables.ipynb` (replaces the SharePoint one), `02 - Business Aggregates.ipynb`.
- **Learn refs to cite:**
  - https://learn.microsoft.com/fabric/onelake/onelake-overview
  - https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview
  - https://learn.microsoft.com/fabric/onelake/onelake-shortcuts

## Lab 02 — Data Warehouse content outline

- **Objectives:** create Warehouse, load from Lakehouse via `INSERT ... SELECT` or COPY INTO, write stored proc for aggregate, expose via semantic model.
- **Scripts:** T-SQL for `Create Tables`, `Load Tables`, `Create Aggregate Procedure`, `Run Aggregate Procedure` (mirrors SharePoint `.txt` scripts, but generated against the customer schema).
- **Learn refs:**
  - https://learn.microsoft.com/fabric/data-warehouse/data-warehousing
  - https://learn.microsoft.com/fabric/data-warehouse/ingest-data
  - https://learn.microsoft.com/fabric/data-warehouse/tutorial-load-data

## Lab 03 — Real-Time Intelligence content outline

- **Objectives:** stand up an Eventstream, ingest into an Eventhouse (KQL DB), query with KQL, build a real-time dashboard, trigger an Activator alert.
- **Data:** streaming variant of the customer fact table (e.g. claims stream, txn stream, telemetry stream).
- **KQL scripts:** replaces `Real-Time Intelligence Tutorial KQL Scripts.txt`.
- **Learn refs:**
  - https://learn.microsoft.com/fabric/real-time-intelligence/overview
  - https://learn.microsoft.com/fabric/real-time-intelligence/event-streams/overview
  - https://learn.microsoft.com/fabric/real-time-intelligence/data-activator/activator-introduction

## Lab 04 — Data Science content outline

- **Objectives:** run the 4-notebook flow on customer data — ingest, explore, train, predict.
- **Notebooks:** `1-ingest-data.ipynb`, `2-explore-cleanse-data.ipynb`, `3-train-evaluate.ipynb`, `4-predict.ipynb` (mirrors SharePoint but re-targeted at customer regression/classification).
- **Learn refs:**
  - https://learn.microsoft.com/fabric/data-science/data-science-overview
  - https://learn.microsoft.com/fabric/data-science/mlflow-autologging

## Exit

Write a summary of what was authored, the freshness report location, and any TODOs the CSA must resolve manually.
