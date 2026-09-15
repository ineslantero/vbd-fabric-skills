---
name: vbd-data
description: Generate a set of sample CSV files relevant to the customer's use case for a Fabric VBD workshop.
inputs:
  - workshop.yaml
outputs:
  - data/*.csv
  - data/README.md (schema + provenance)
---

# /vbd-data

Produce a small set of **CSV files** with dummy data that fits the customer's industry and the objectives captured in `workshop.yaml`. Keep it simple — CSVs only, no medallion pre-baking, no Parquet, no Delta. The labs themselves will do the transformations.

Reference for shape and volume: [ineslantero/fabric-training-cmi — `data/`](https://github.com/ineslantero/fabric-training-cmi/tree/master/data) — a handful of related CSVs (customers, orders, products, etc.), a few thousand rows each, that tell a coherent story across the Foundation labs.

## What to generate

1. Read `workshop.yaml` — pull `customer.industry`, `customer.name`, and the included labs.
2. Propose a **small star-schema-shaped set of CSVs** for that industry:
   - 1 fact table (e.g. `claims.csv`, `transactions.csv`, `sales.csv`)
   - 3–5 dimension tables (customer/member, product/procedure, date, location, etc.)
3. Show the CSA the proposed file list + column list per file, and ask for approval before writing.
4. On approval, generate the CSVs using Faker or plain Python `random` with a fixed seed. Aim for ~1–10k rows in the fact table, ~100–1000 in each dimension.

## Output shape

```
data/
├── README.md              ← file list, columns per file, row counts, seed used
├── <fact>.csv
├── <dim1>.csv
├── <dim2>.csv
└── ...
```

## Guardrails

- **CSV only.** No Parquet, no Delta, no bronze/silver/gold folders — labs create those.
- **No PII.** Use Faker or made-up identifiers; never use real names/emails/IDs even if the transcript mentioned them.
- **Deterministic.** Fix the seed and record it in `data/README.md`.
- **Coherent across files.** Foreign keys in the fact table must actually exist in the dim files (referential integrity).
- **Small.** Files should be committable to a git repo (< 5 MB each). If the CSA wants larger volumes, add a note in the README and generate a script the customer can run to scale up.
