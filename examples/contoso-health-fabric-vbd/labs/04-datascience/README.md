# Lab 04: Data Science — 30-day readmission risk

> **Module:** Data Science · **Duration:** ~4h · **Personas:** data scientist, data engineer
>
> _Content verified against Microsoft Learn on 2026-09-15. Fabric release pinned: 2026-09._

## Learning objectives

- Run the ingest → explore → train → predict flow on customer-domain data.
- Log experiments to **MLflow** and register a model in the Fabric model registry.
- Batch score against the gold layer and write predictions back to the Lakehouse.

## Customer context

Same de-identified synthetic dataset as the Lakehouse lab. Target: predict 30-day readmission risk from prior claims + demographics. Model output feeds a care-management workflow.

## Prerequisites

- Lab 01 complete.
- Notebooks attached to the workshop workspace.

## Notebooks (run in order)

| # | Notebook | Purpose |
|---|---|---|
| 1 | [`notebooks/1-ingest-data.ipynb`](notebooks/1-ingest-data.ipynb) | Load features from gold layer, join with admissions table |
| 2 | [`notebooks/2-explore-cleanse-data.ipynb`](notebooks/2-explore-cleanse-data.ipynb) | EDA + feature engineering |
| 3 | [`notebooks/3-train-evaluate.ipynb`](notebooks/3-train-evaluate.ipynb) | Train + MLflow autologging + register model |
| 4 | [`notebooks/4-predict.ipynb`](notebooks/4-predict.ipynb) | Batch score → write predictions to Lakehouse |

_Refs:_
- [Data Science overview](https://learn.microsoft.com/fabric/data-science/data-science-overview)
- [MLflow autologging](https://learn.microsoft.com/fabric/data-science/mlflow-autologging)
- [Model registry](https://learn.microsoft.com/fabric/data-science/machine-learning-model)

## Checkpoints

- After nb 3: model version 1 visible in the model registry.
- After nb 4: `Tables/predictions_readmission` exists with one row per member for the scoring window.

## Troubleshooting

- **MLflow UI empty** — you didn't set `mlflow.set_experiment(...)`; autologging still writes runs but they land in `default`.
- **Model registry access denied** — user needs Contributor role on the workspace.

## What's next

Day 3 wraps with a governance lightning talk — the model above will need row-level security and PHI-safe explanations before productionisation. That's scoped as a follow-on VBD.

---

<sub>Freshness report: [`../../.vbd/freshness-foundation.yaml`](../../.vbd/freshness-foundation.yaml)</sub>
