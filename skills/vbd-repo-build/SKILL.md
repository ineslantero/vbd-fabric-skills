---
name: vbd-repo-build
description: Assemble the final shareable customer repo from workshop.yaml + generated labs + data. Optional GitHub push on explicit CSA approval.
inputs:
  - workshop.yaml
  - proposal.md, agenda.md, prerequisites.md
  - labs/*, data/, .vbd/freshness-*.yaml
outputs:
  - <deliverable.repo_name>/ folder ready to zip or push
  - FRESHNESS.md (rollup)
---

# /vbd-repo-build

Final assembler. Consumes everything produced by upstream skills and stages a clean repo the CSA can hand to the customer.

## Layout

```
<repo_name>/
├── README.md           ← generated from templates/repo-readme.md
├── agenda.md
├── prerequisites.md
├── FRESHNESS.md        ← aggregated from .vbd/freshness-*.yaml
├── data/
├── labs/
│   ├── 01-lakehouse/
│   ├── 02-warehouse/
│   ├── 03-rti/
│   └── 04-datascience/
├── notebooks/          ← copies (or symlinks) from labs for easy top-level browsing
├── scripts/
│   └── setup/          ← workspace bootstrap (optional; only if CSA opts in)
└── solutions/          ← only if deliverable.include_solutions=true
```

## Steps

1. Verify all upstream artefacts exist. Fail loudly if any lab freshness report is missing.
2. Render `README.md` from `templates/repo-readme.md`.
3. Roll up per-lab freshness reports into `FRESHNESS.md` (one section per module, summary badge at top).
4. Copy artefacts into the staged folder, respecting `deliverable.include_solutions`.
5. Redact any `transcript.md` under `.vbd/` — that stays with the CSA, never ships to customer.
6. Print a manifest (files, sizes, per-file freshness status) for CSA review.
7. **Ask before pushing** (per user preference). Only push to GitHub after explicit approval:
   - `gh repo create <repo_name> --private --push` if `deliverable.repo_host = github-private`.
   - Else zip and hand back the path.

## Guardrails

- Never push if any lab's freshness status is `outdated` and unresolved.
- Never include `.vbd/transcript.md` in the pushed repo.
- If the workshop sensitivity is `confidential` or higher, warn the CSA before any external push.
