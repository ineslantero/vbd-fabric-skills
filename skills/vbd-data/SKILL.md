---
name: vbd-data
description: Generate a small, coherent set of sample CSV files in the customer's industry for the Fabric VBD workshop.
inputs:
  - workshop.yaml
outputs:
  - data/*.csv          (fact + dims, industry-retargeted)
  - data/fetch-data.ps1 (only if a lab needs a large public dataset, e.g. Lakehouse WWI)
  - data/fetch-data.sh
  - data/README.md      (schema per file, row counts, seed used, provenance)
---

# /vbd-data

Produce a small star-schema-shaped set of **CSV files** that fit the customer's industry and the labs selected in `workshop.yaml`. CSVs only — no Parquet, no Delta, no medallion pre-baking. The labs themselves do the transformations.

Reference for style: [ineslantero/fabric-training-cmi — `data/`](https://github.com/ineslantero/fabric-training-cmi/tree/master/data). Reference for shape: the SP CSVs in `skills/vbd-data/references/<lab>/`.

## What the sample CSVs should look like

Every workshop dataset follows the **same star-schema pattern** as the SharePoint Discovery Labs: one fact table + a handful of dimensions with clean foreign keys. The retargeting keeps the shape and swaps the domain.

### Lakehouse lab

The WWI reference uses a retail fact + 4 dims. You mirror the same shape for the customer's industry.

| Reference file | Role | Rows | Customer example (healthcare) |
|---|---|---|---|
| `fact_sale` (in the WWI zip, ~50M rows) | Fact | 5–10k after downsample | `fact_claim.csv` — one row per claim line |
| `dimension_customer.csv` (committed, ~65 KB) | Dim | ~400 | `dimension_member.csv` — one row per patient |
| `dimension_city` | Dim | ~100 | `dimension_facility.csv` — one row per hospital/clinic |
| `dimension_date` | Dim | ~2000 | `dimension_date.csv` — one row per day (keep as-is) |
| `dimension_stock_item` | Dim | ~200 | `dimension_procedure.csv` — one row per CPT code |
| `dimension_employee` | Dim | ~200 | `dimension_provider.csv` — one row per doctor |

**Fact columns** (Lakehouse): keep the same *roles* — surrogate keys to every dim, at least 3 measure columns (e.g. `TotalExcludingTax` → `AllowedAmount`, `TaxAmount` → `PatientResponsibility`, `Profit` → `PaidAmount`), an event date.

### Data Science lab

The NY Taxi reference is a fact (trips) + one small lookup (locations).

| Reference file | Role | Customer example (insurance) |
|---|---|---|
| `yellow_tripdata_YYYY-MM.parquet` (fetched from Azure Open Datasets) | Fact | `fact_policy_quote.csv` — one row per quote, target = `PremiumPaid` |
| `ny-yellow-taxi-location-info.csv` (committed, ~4 KB) | Lookup | `dimension_region.csv` — one row per postcode/region |

**Fact must contain a regression or classification target** the notebook can predict. If the customer transcript doesn't name one, propose one to the CSA (e.g. "predict `PremiumPaid`" for insurance, "predict `LengthOfStay`" for hospital admissions).

### Warehouse and RTI

Do not generate redundant CSVs. Warehouse normally reuses the Lakehouse output; document a complete standalone ingestion route if Warehouse is selected without Lakehouse or replayed independently. RTI can use a verified built-in sample; a bounded optional synthetic event generator must match the documented target schema.

## How to run

1. **Read `workshop.yaml`** — pull `customer.industry`, `customer.name`, and the included labs.
2. **Draft the file list** — one output CSV per reference CSV that's needed, using the mapping above. Include the fact + all dims the lab notebooks reference (peek into `references/<lab>/<lab>-tutorial.md` to see which dims each notebook loads).
3. **Draft the schemas** — for each file, list columns with type + example value + which reference column it maps from.
4. **Show the CSA the mapping table + first 3 rows of each file (dry run)** and ask for approval before writing. Adjust based on feedback.
5. **On approval, generate** with Faker or `random` under a fixed seed. Enforce referential integrity — every FK in the fact must resolve to a row in the matching dim.
6. **Emit `data/README.md`** — one section per file with columns, row count, sample rows, and the seed used.
7. **Make the data usable without the trainer.** Include repo-relative file paths, encoding/delimiter/header/date/null conventions, column types and primary/foreign keys, plus the exact target table names the labs will create. Provide a concrete upload/load procedure or link to the numbered lab steps that do it — "load the CSVs" alone is not a procedure.
8. **Supply deterministic validation evidence.** Record actual generated row counts, key uniqueness, null expectations, foreign-key integrity and one known aggregate/join result the labs rely on. Document the generation date range, seed and Faker/library versions — **a fixed seed alone does not make today's date or a changing dependency deterministic**. Never invent expected results without calculating them from the generated data.
9. **Reconcile all consumers.** Notebook, SQL and KQL snippets, learner challenges and the course walkthrough must use these exact column and table names and types. If a row is intentionally dirty for a cleaning exercise, label it and define the expected before/after check; do not silently violate the clean baseline.

## Guardrails

- **CSV only.** No Parquet, no Delta, no bronze/silver/gold subfolders — labs create those.
- **No PII.** Faker or made-up identifiers, always. Never use real names, emails, or IDs even if the transcript mentioned them.
- **Deterministic.** Fix the seed. Record it in `data/README.md` so the CSA can regenerate byte-identical output.
- **Referential integrity.** Every FK in the fact table must exist in the dim files.
- **Small.** Each file < 5 MB (git-committable). If the customer wants realistic volumes, emit a `scale-up.py` script instead of committing a 500 MB fact.
- **Reference-shaped, not reference-copied.** Never emit rows from the SP CSVs verbatim.
