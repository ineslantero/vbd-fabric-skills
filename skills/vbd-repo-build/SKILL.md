---
name: vbd-repo-build
description: Assemble and review a practical Fabric course and lab repository with evidence-backed procedures. Publish to GitHub only after explicit approval.
inputs:
  - workshop.yaml
  - workshop-plan.md
  - labs/*, data/, .vbd/freshness-*.yaml
outputs:
  - <deliverable.repo_name>/ folder ready to zip or push
  - FRESHNESS.md (sanitised rollup)
---

# /vbd-repo-build

Assemble the outputs of the upstream skills into a coherent course and independently reproducible lab repository. Resolve shared `templates/` and `components/` from the source repository root, two levels above this skill's real directory; resolve installation links first.

## Deliverable layout

```text
<repo_name>/
  README.md
  workshop.yaml
  workshop-plan.md
  FRESHNESS.md
  data/
  labs/
    <nn-module>/README.md
    <nn-module>/notebooks/  (when needed)
    <nn-module>/scripts/    (when needed)
  solutions/               (only when explicitly requested)
```

No `templates/repo-readme.md` is supplied in this repository. Compose the course entry point from the approved plan and actual file inventory; do not pretend to render a missing template. Do not duplicate lab code at the top level unless there is a documented single source of truth.

## Assembly and review

1. Read the approved plan and all included lab/data artifacts. Require their source-review records; follow `components/freshness/README.md`, which is a review workflow rather than an implemented verifier.
2. Write the course entry point with an honest delivery route, prerequisites by persona, timed module map, links to concrete worked examples and learner exercises, and the expected completion evidence. Keep historical delivery dates separate from subsequent revision dates.
3. Reconcile `workshop.yaml`, the course plan and labs. All included modules have matching objectives, working relative links, input/output names and realistic timings. `teaching` and `learning` fields are required for new modules; flag legacy omissions rather than treating them as validated.
4. Apply the practical quality gate below to **every** included lab, not just a sample. Fix tightly coupled notebook/script/schema mismatches and remove obsolete contradictory instructions.
5. Roll source records into a customer-safe `FRESHNESS.md`. Distinguish documentation reviewed, static checks and authorised live execution. Link lab footers to this shipped rollup. Preserve unresolved/blocked status rather than creating a success-shaped summary.
6. Stage only the approved artifacts. Exclude raw transcripts, private `.vbd` evidence, private identifiers, credentials, real customer datasets and protected Office content. Respect `deliverable.include_solutions`; keep worked bootstrap code runnable even when challenge solutions are omitted.
7. Use existing relevant checks if present; otherwise inspect notebook JSON, code/schema consistency and links without claiming an automated suite exists. Validate rendered artifacts rather than expecting raw template placeholders to be runnable. Do not run paid Fabric jobs, change tenant settings or send real alerts without separate approval.
8. Present the exact staged manifest, change summary, known limitations, target repository/visibility and outbound publication text for CSA approval. Only after explicit approval push/create the requested repository or pull request. Never overwrite pre-existing edits or commit unrelated files.

## Practical quality gate

| Required evidence | Reject or correct when |
|---|---|
| Course explain -> demonstrate -> practise -> check -> debrief map | Only an agenda or a list of features is provided |
| Explicit executed/observed/offline/blocked route | A worksheet or demonstration is called executed hands-on work |
| Starting state, roles, item prefix and feature-specific prerequisites | Trial, licence or administrator access is assumed for all features |
| Full numbered UI/code procedure with exact values and execution surface | "Configure", "upload" or "create a model" is left unexplained |
| Per-step expected result, check, recovery and current Learn source | A general reading list substitutes for procedural evidence |
| Relevant verified Microsoft blog context, or explicit source limitation | An announcement alone is used as availability or execution proof |
| Concrete independent learner change with acceptance criteria | The learner only repeats a trainer demonstration |
| Actual input schemas and deterministic validation values | Code uses nonexistent fields or fabricated output |
| Standalone replay or precise documented prerequisite route | Lab N silently depends on unprovided results from Lab N-1 |
| Scoped cleanup, bounded cost and safe rerun behaviour | Streams run forever or instructions remove shared/production resources |
| Honest freshness and execution record | HTTP success is claimed as a Fabric execution test |
| Teaching/practice/setup/check/cleanup times fit the course | New practical work silently overflows the advertised day |

A lab with an unresolved required step is not runnable-ready. Optional blocked extensions may remain clearly excluded from the executable route after review.

## Publication guardrails

- Public reusable skills and templates must not contain customer-specific scoping, names, tenant IDs, private links or private source extracts.
- Never include `.vbd/transcript.md` or other raw conversation evidence in the deliverable.
- Confidential source access does not confer permission to publish. Respect labels and usage rights; do not strip protection.
- Show the exact destination and publication content and obtain confirmation before sending any update visible to others. Keep local commits separate from outbound pushes.
- Use a private destination for customer deliverables unless the customer explicitly approved public distribution; do not silently change visibility.
