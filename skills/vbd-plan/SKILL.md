---
name: vbd-plan
description: Turn a scoping-call transcript into a Fabric VBD workshop plan (single markdown) plus a workshop.yaml. Orchestrates downstream /vbd-* skills.
inputs:
  - transcript (chat paste | WorkIQ meeting | email thread)
outputs:
  - workshop-plan.md   (proposal + agenda + prerequisites in one concise file)
  - workshop.yaml      (machine-readable spec consumed by downstream skills)
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

## Step 3 — Score the candidate labs

**Two modules exist today: Foundation and Security.** Ignore the other VBDs (Lakehouse-as-its-own-VBD, Data Factory, Warehouse-as-its-own-VBD, Power BI standalone) — they'll get their own scoring passes when their skills exist.

Decide **which module** first, then score its labs.

> **Rule of thumb:** Foundation teaches people to *build*; Security reviews what they have *already built*.
> A customer with several use cases already in production will score 0–1 on every Foundation lab — when
> that happens you are looking at the wrong module, not at a customer with no needs.

### 3a — Module selection

| Signal in the transcript | Module |
|---|---|
| Green-field, migrating off Synapse/Databricks, "we need to learn Fabric" | `foundation` |
| Production estate, "is our setup still right", baselines drifted, onboarding partners, catalogue adoption stalled | `security` |
| Audience is data engineers, analysts, data scientists | `foundation` |
| Audience is platform engineering, security, governance, tenant admins | `security` |

### 3b — Foundation Discovery Labs

For each of the **4 Foundation Discovery Labs**, score relevance 0–5 against the extracted objectives and stack. Show the CSA your reasoning per lab (per user preference) before writing anything.

| Lab | What it covers | Score against |
|---|---|---|
| `lakehouse` | OneLake, Lakehouse creation, shortcuts, Delta, medallion, notebooks | Objectives around unified storage, Spark, migration off Databricks/Synapse Spark |
| `warehouse` | Fabric Warehouse, T-SQL, cross-warehouse queries, SQL endpoint | Objectives around SQL DW replacement, T-SQL workloads, BI serving |
| `rti` | Eventstream, Eventhouse, KQL, real-time dashboards, alerts | Objectives around streaming, IoT, near-real-time analytics, anomaly detection |
| `datascience` | Data Wrangler, MLflow, model training, batch scoring, semantic link | Objectives around ML, feature engineering, model ops on Fabric |

### 3c — Security / Platform & Governance labs

| Lab | What it covers | Score against |
|---|---|---|
| `admin-tenant-settings` | Admin portal, tenant settings, delegation, domains, admin monitoring, admin APIs | Objectives around tenant configuration, governing the estate, configuration drift |
| `security-workspace-to-column` | Workspace roles, item permissions, OneLake security, RLS, CLS, masking, enforcement boundary | Objectives around access model, "who can see what", security baseline review |
| `partner-access` | Entra B2B, external data sharing, groups, service principals, access review and revocation | Objectives around contractors, delivery partners, external collaboration, offboarding |
| `governance-catalogue` | Endorsement, lineage, sensitivity labels, Purview Unified Catalog, scanning | Objectives around cataloguing, classification, discoverability, stalled governance adoption |

Output a table with `lab | score | rationale | include?`. Any lab scored ≥ 3 is included by default; the CSA can override. **Record excluded labs with a `reason` in `workshop.yaml`** — being explicit about what was deliberately left out is as valuable to the customer as what was included.

## Step 4 — Draft the plan

Fill the single template `templates/workshop-plan.md` and `templates/workshop.yaml` with:
- Selected labs only (excluded labs recorded with a `reason` in `workshop.yaml`).
- Time budget per lab derived from `duration_days` and lab complexity.
- Per-lab `include_topics` / `exclude_topics` / `customer_angle`.
- Prereqs derived from selected labs + customer stack.
- Agenda formatted as bullets with a one-sentence rationale per item (per user preference).
- Everything kept concise — the workshop plan is one file, bullet-first.

## Step 5 — CSA review gate

Present both artefacts (`workshop-plan.md` and `workshop.yaml`). CSA can:
- Approve as-is → proceed to Step 6.
- Edit either → re-render.
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
2. The lab skill for the module selected in Step 3a:
   - `/vbd-lab-foundation` — Foundation labs (lakehouse / warehouse / rti / datascience)
   - `/vbd-lab-security` — Security labs (admin / access model / partner access / governance)
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
