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

Resolve shared `templates/` and `components/` from the vbd-fabric-skills repository root, two levels above this skill's real directory. For a linked local installation, resolve the link target rather than the customer's current directory.

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
- Learning route per module: demonstration, guided hands-on, independent hands-on or offline design; record whether each attendee has an authorised training environment.
- Setup owner, feature-specific capacity/licence/region constraints, least-privilege test identities, and whether administrator-only actions can be demonstrated safely.
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

Fill the single template `templates/workshop-plan.md` and `templates/workshop.yaml` with:
- Selected labs only (excluded labs recorded with a `reason` in `workshop.yaml`).
- Time budget per lab derived from `duration_days` and lab complexity.
- Per-lab `include_topics` / `exclude_topics` / `customer_angle`.
- Prereqs derived from selected labs + customer stack.
- Agenda formatted as bullets with a one-sentence rationale per item (per user preference).
- Everything kept concise — the workshop plan is one file, bullet-first.
- A course walkthrough for every included module: explain the concept, demonstrate a worked example, let the learner make a concrete change, check an observable result, then debrief the trade-off. Link the example and practice to actual lab step ranges.
- Populate each included module's `teaching` and `learning` fields in the handoff template. Include the starting state, complete standalone setup route, expected artifact, acceptance criteria, challenge, fallback, sources and cleanup. Missing fields in an older plan must be resolved explicitly, not silently interpreted as hands-on.
- Budget explanation, setup, guided practice, independent practice, checking/debrief and cleanup. Their sum must equal the module duration; all modules, breaks and lunch must fit the advertised day. Move excess material into clearly timed self-paced extensions.
- Keep an existing demonstration-only route and historical delivery dates intact when revising a delivered course. Add a separately labelled follow-along/self-paced route with its real prerequisites; "no preparation to watch" is not "no prerequisites to execute".

## Step 5 — CSA review gate

Present both artefacts (`workshop-plan.md` and `workshop.yaml`). CSA can:
- Approve as-is → proceed to Step 6.
- Edit either → re-render.
- Reject → capture feedback and redraft.

## Step 6 — Freshness pre-check (mandatory, right before lab generation)

Only after the CSA approves the plan, and **before** invoking any lab-creation skill, follow the source-review workflow in `components/freshness/README.md` (not an implemented automatic API) to:
- Confirm every included lab's key features are achievable on current Fabric (flag preview-only features).
- Pull the current roadmap items that intersect the included labs and pin `fabric_release_pinned` in `workshop.yaml`.
- Warn if the scheduled workshop date will collide with a roadmap rollout worth mentioning.
- Emit `.vbd/freshness-precheck.yaml` with the verified/preview/outdated verdict per lab.
- Link Microsoft Learn procedures to worked examples and include relevant verified Microsoft blog context. Record actual source access dates and distinguish documentation review from a Fabric execution test. `fabric_release_pinned` is a documentation release reference, not a runtime lock.

If anything comes back `outdated` or `deprecated`, surface it to the CSA before continuing — do not silently drop or rewrite objectives.

## Step 7 — Orchestrate

Once freshness passes (or the CSA acknowledges the flags), invoke in sequence:
1. `/vbd-data` (reads `data_strategy`)
2. `/vbd-lab-foundation` — generates the selected Foundation labs (lakehouse / warehouse / rti / datascience)
3. `/vbd-repo-build`

## Guardrails

- **Never share transcript content externally.** It contains customer-confidential info.
- **Every claim in the proposal must cite Microsoft Learn or the Fabric roadmap.** If freshness can't produce a citation, mark the claim TODO.
- **Practical readiness is separate from source currency.** A course needs executable procedures and learner evidence, not just an agenda and reading list. Unknown prerequisites or required procedure steps block a hands-on-ready claim.
- **Do not confuse observation with execution.** Record executed, observed, offline and blocked outcomes separately. Preview/region restrictions require an explicit fallback, not an invented UI route.
- **Ask before pushing anything to GitHub.**

## Helpers

- `components/transcript-loader/` — paste/WorkIQ/email normaliser
- `components/freshness/` — Learn + roadmap verifier

## Exit

Print a summary: what was decided, what got skipped and why, and the next skill the CSA should run (usually `/vbd-data`).
