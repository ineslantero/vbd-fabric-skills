---
name: vbd-repo-build
description: Assemble the final shareable customer repo from workshop.yaml + generated labs + data. Optional GitHub push on explicit CSA approval.
inputs:
  - workshop.yaml
  - workshop-plan.md
  - labs/*, data/, .vbd/freshness-*.yaml
outputs:
  - ./out/<deliverable.repo_name>/ folder ready for CSA review and push
  - FRESHNESS.md (rollup)
---

# /vbd-repo-build

Final assembler. Consumes everything produced by upstream skills and stages a clean repo the CSA can hand to the customer.

## Layout

Staged locally at `./out/<deliverable.repo_name>/` relative to the directory where the skill was invoked. The `./out/` parent is created if missing and is in `.gitignore`. `.vbd/` stays at the invocation root — **outside** `./out/` — so the transcript audit survives but is never included in the staged folder.

```
./out/<repo_name>/
├── README.md           ← generated from templates/repo-readme.md
├── workshop-plan.md    ← proposal + agenda + prereqs in one file
├── FRESHNESS.md        ← aggregated from .vbd/freshness-*.yaml
├── data/
├── labs/
│   ├── 01-lakehouse/
│   ├── 02-warehouse/
│   ├── 03-rti/
│   ├── 04-datascience/
│   └── 05-security-and-governance/   ← present when /vbd-lab-security ran
├── notebooks/          ← copies (or symlinks) from labs for easy top-level browsing
├── scripts/
│   └── setup/          ← workspace bootstrap (optional; only if CSA opts in)
└── solutions/          ← only if deliverable.include_solutions=true
```

Only the labs that were actually generated appear under `labs/`. Numbering is fixed (01 lakehouse, 02 warehouse, 03 rti, 04 datascience, 05 security-and-governance) regardless of which subset the plan selected — gaps are expected and keep the lab identity stable across engagements.

## Steps

1. Verify all upstream artefacts exist (`workshop.yaml`, `workshop-plan.md`, every `labs/<nn>-*/` for included labs, `data/`, every `.vbd/freshness-*.yaml`). Fail loudly if any lab freshness report is missing.
2. Render `README.md` from `templates/repo-readme.md`.
3. Roll up per-lab freshness reports into `FRESHNESS.md` (one section per module, summary table at top).
4. Copy artefacts into `./out/<repo_name>/`, respecting `deliverable.include_solutions`.
5. Redact — never copy `.vbd/transcript.md`, `.vbd/transcript.raw/` or any other `.vbd/*` evidence into `./out/`. These stay with the CSA.
6. **Local approval gate.** Print the staged manifest for CSA review and stop. Do not touch GitHub yet. The manifest must show:
   - Local staging path (`./out/<repo_name>/`) and total size.
   - File tree with sizes.
   - Per-lab freshness status (verified / preview / outdated / unresolved).
   - Target publication destination (`gh repo create ineslantero/<repo_name> --private`) and visibility.
   - Any sensitivity-label warnings (confidential or higher workshops get a prominent banner).
   - Explicit prompt: *"Reply 'approve' to publish, 'edit' to describe changes, or 'cancel' to stop."*
7. **Publish on explicit approval only.** Create a new private GitHub repo under the CSA's account and push `./out/<repo_name>/` to it:
   ```
   gh repo create <repo_name> --private --source ./out/<repo_name> --push
   ```
   Only new private repos are supported — never push to a pre-existing repo and never create a public one. If the repo name already exists under the CSA account, stop and ask for a new name rather than overwriting. On `edit`, re-run from Step 2 after capturing the change. On `cancel`, leave the staged folder in place and exit cleanly.

## Guardrails

- Never push if any lab's freshness status is `outdated` and unresolved.
- Never include `.vbd/transcript.md` in the pushed repo.
- Never push without passing the local approval gate (Step 6) first.
- Never create a public repo. Never push to a pre-existing repo.
- If the workshop sensitivity is `confidential` or higher, warn the CSA before any external push.

## Publication guardrails

- **Public reusable skills and templates must not contain customer-specific scoping, names, tenant IDs, private links or private source extracts.** Those live only in the generated customer deliverable, never in this skill repo.
- **Confidential source access does not confer permission to publish.** Respect sensitivity labels and usage rights on anything read from SharePoint, OneDrive, or Teams; do not strip protection.
- **Show the exact destination and publication content, and obtain confirmation before any update visible to others.** Keep local commits separate from outbound pushes — committing is not publishing.
- **Use a private destination for customer deliverables unless the customer explicitly approved public distribution.** Do not silently change repository visibility.
