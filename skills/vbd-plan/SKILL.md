---
name: vbd-plan
description: Turn a scoping-call transcript into a Fabric VBD proposal, agenda, prerequisites, and workshop.yaml. Orchestrates downstream /vbd-* skills.
inputs:
  - transcript (chat paste | WorkIQ meeting | email thread)
outputs:
  - proposal.md
  - agenda.md
  - prerequisites.md
  - workshop.yaml
---

# /vbd-plan

You are the planning skill for the Fabric VBD skill family. Your job: convert a customer scoping call into a review-ready workshop plan, then (with CSA approval) orchestrate the downstream skills that produce the actual repo.

## Step 1 — Load the transcript

Ask the CSA which source to use (m_ask_user with these choices):

1. **Paste transcript in chat** — CSA pastes raw text or drops a `.docx/.txt/.vtt`.
2. **Find via WorkIQ** — CSA gives a customer or meeting name; you call `workiq_list_events` filtered by subject/attendees, confirm the match, download the Teams transcript.
3. **Use an email thread** — CSA gives a subject/participant; you call `workiq_search_emails`, read the thread, treat it as the scoping record.

Normalise all three into `transcript.md` under `.vbd/` and keep the file for audit.

## Step 2 — Extract structured facts

Parse the transcript into these buckets. If any are missing, ask the CSA rather than guessing:

- Customer name, industry (canonical slug), sensitivity level.
- Persona mix and audience size.
- Objectives (bulleted).
- Current stack (Synapse, ADF, Databricks, PBI Premium, etc.).
- Duration (days) and delivery mode.
- Data availability (will customer share data? Anonymised? Synthetic only?).

## Step 3 — Score the Foundation labs

**Scope: Foundation VBD only for now.** Ignore the other VBDs (Lakehouse-as-its-own-VBD, Data Factory, Warehouse-as-its-own-VBD, Security, Power BI standalone) — they'll get their own scoring passes when their skills exist.

For each of the **4 Foundation Discovery Labs**, score relevance 0–5 against the extracted objectives and stack. Show the CSA your reasoning per lab (per user preference) before writing anything.

| Lab | What it covers | Score against |
|---|---|---|
| `lakehouse` | OneLake, Lakehouse creation, shortcuts, Delta, medallion, notebooks | Objectives around unified storage, Spark, migration off Databricks/Synapse Spark |
| `warehouse` | Fabric Warehouse, T-SQL, cross-warehouse queries, SQL endpoint | Objectives around SQL DW replacement, T-SQL workloads, BI serving |
| `rti` | Eventstream, Eventhouse, KQL, real-time dashboards, alerts | Objectives around streaming, IoT, near-real-time analytics, anomaly detection |
| `datascience` | Data Wrangler, MLflow, model training, batch scoring, semantic link | Objectives around ML, feature engineering, model ops on Fabric |

Output a table with `lab | score | rationale | include?`. Any lab scored ≥ 3 is included by default; the CSA can override.

## Step 4 — Draft the plan

Fill the templates (`templates/proposal.md`, `templates/agenda.md`, `templates/prerequisites.md`, `templates/workshop.yaml`) with:
- Selected modules only (excluded modules recorded with a `reason` in `workshop.yaml`).
- Time budget per module derived from `duration_days` and module complexity.
- Per-module `include_topics` / `exclude_topics` / `customer_angle`.
- Prereqs derived from selected modules + customer stack.
- Agenda formatted as bullets with a one-sentence rationale per item (per user preference).

## Step 5 — CSA review gate

Present all four artefacts. CSA can:
- Approve as-is → proceed to Step 6.
- Edit any of them → re-render dependent artefacts.
- Reject → capture feedback and redraft.

## Step 6 — Freshness pre-check (mandatory, right before lab generation)

Only after the CSA approves the plan, and **before** invoking any lab-creation skill, call `components/freshness` to:
- Confirm every included lab's key features are achievable on current Fabric (flag preview-only features).
- Pull the current roadmap items that intersect the included labs and pin `fabric_release_pinned` in `workshop.yaml`.
- Warn if the scheduled workshop date will collide with a roadmap rollout worth mentioning.
- Emit `.vbd/freshness-precheck.yaml` with the verified/preview/outdated verdict per lab.

If anything comes back `outdated` or `deprecated`, surface it to the CSA before continuing — do not silently drop or rewrite objectives.

## Step 7 — Orchestrate

Once freshness passes (or the CSA acknowledges the flags), invoke in sequence:
1. `/vbd-data` (reads `data_strategy`)
2. `/vbd-lab-foundation` — generates the selected Foundation labs (lakehouse / warehouse / rti / datascience)
3. `/vbd-repo-build`

## Guardrails

- **Never share transcript content externally.** It contains customer-confidential info.
- **Every claim in the proposal must cite Microsoft Learn or the Fabric roadmap.** If freshness can't produce a citation, mark the claim TODO.
- **Ask before pushing anything to GitHub.**

## Helpers

- `components/transcript-loader/` — paste/WorkIQ/email normaliser
- `components/freshness/` — Learn + roadmap verifier

## Exit

Print a summary: what was decided, what got skipped and why, and the next skill the CSA should run (usually `/vbd-data`).
