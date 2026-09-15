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

Ground-truth references live in `skills/vbd-data/references/<lab>/` — one folder per Foundation Discovery Lab, populated with the original CSVs shipped by the SharePoint IP release ([`02 - Discovery Labs`](https://microsoft.sharepoint.com/teams/ASDIPRelease/IP%20Release/Data%20and%20AI/Fabric/1%20-%20Upskilling/1%20-%20Foundation)). The skill uses these to fix the schema, file count, and volume; the actual generated files are always retargeted to the customer's industry. See also [ineslantero/fabric-training-cmi — `data/`](https://github.com/ineslantero/fabric-training-cmi/tree/master/data) for a customer-relevant example of the same pattern.

## What to generate

1. Read `workshop.yaml` — pull `customer.industry`, `customer.name`, and the included labs.
2. **Look at `references/<lab>/` for the shape.** Each included lab has a `references/<lab>/` folder holding the original CSVs shipped with the SharePoint Discovery Lab (WWI retail data for Lakehouse, NY Taxi for Data Science, etc.). Use those as the ground-truth **schema, row-count, and file-count** target — one output CSV per reference CSV, same column count and role, retargeted to the customer's industry.
3. Propose a **small star-schema-shaped set of CSVs** for that industry that mirrors the reference file list:
   - Same number of files as the reference lab
   - Same fact/dim split
   - Same approximate row count (± an order of magnitude)
4. Show the CSA the proposed file list + column list per file (side-by-side with the reference file it maps to), and ask for approval before writing.
5. On approval, generate the CSVs using Faker or plain Python `random` with a fixed seed.

## References folder — deterministic contract

```
skills/vbd-data/references/
├── README.md                    ← how to use / where the sources came from
├── lakehouse/                   ← CSVs from SP: 02 - Discovery Labs/01 - Lakehouse Lab/Data
│   ├── dimension_customer.csv
│   └── fetch-wwi-data.ps1/.sh   ← downloads the 1.9 GB WWI zip on demand (gitignored)
└── datascience/                 ← CSVs from SP: 02 - Discovery Labs/04 - Data Science Lab/Data
```

Only labs that ship with seed data have a reference folder. Labs without seed data are **not** represented here:
- `warehouse` — the DW lab loads data via T-SQL `CREATE TABLE ... AS SELECT` / `COPY INTO` from the Lakehouse output, no external CSV needed.
- `rti` — the RTI lab consumes Fabric built-in sample streams (Bicycles / Stocks / YellowTaxi) or a custom event producer, no CSV seed.

The skill **must not** copy the reference CSVs verbatim — they're for shape only. Always regenerate against the customer domain.

## Instructing the customer to fetch large data

For any reference folder that contains a `fetch-*.ps1` / `fetch-*.sh` script (e.g. `lakehouse/fetch-wwi-data.ps1` for the WWI zip), the generated lab README **must** include an explicit "Download the sample data" step near the top telling the customer to run the equivalent fetch script from the generated repo. See `/vbd-lab-foundation` for the exact wording.

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
