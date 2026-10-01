---
name: vbd-lab-foundation
description: Author practical Fabric Foundation Discovery Labs (Lakehouse, Warehouse, RTI, Data Science) with source-backed procedures, runnable exercises and completion evidence.
inputs:
  - workshop.yaml
  - data/ (from /vbd-data)
outputs:
  - labs/01-lakehouse/     README + notebooks
  - labs/02-warehouse/     README + T-SQL scripts
  - labs/03-rti/           README + KQL + optional event generator
  - labs/04-datascience/   README + ingest, explore, train and predict notebooks
  - .vbd/freshness-foundation.yaml
---

# /vbd-lab-foundation

Use the reference tutorials as a starting curriculum, not as current procedural authority. Preserve the intended learning outcomes; replace obsolete UI, code and dependencies with verified Microsoft Learn procedures. A lab is not complete if it merely tells learners to "configure", "explore" or "discuss" a feature without showing how.

## Resolve resources

`references/` is relative to this skill directory. `templates/` and `components/` are relative to the vbd-fabric-skills repository root (two levels above this skill's real directory). When installed through a link, resolve the link target first. Do not look for shared resources in the customer's repository or invent missing helper APIs.

## The four labs

| Lab | Reference | Input and output |
|---|---|---|
| Lakehouse | `references/lakehouse/lakehouse-tutorial.md` | Repository CSVs -> Files -> Delta tables -> Spark and SQL checks |
| Warehouse | `references/warehouse/warehouse-tutorial.md` | Documented Lakehouse tables -> Warehouse tables/views -> repeatable SQL result |
| RTI | `references/rti/rti-tutorial.md` | Verified built-in sample or bounded synthetic source -> Eventhouse table -> KQL result/dashboard |
| Data Science | `references/datascience/datascience-tutorial.md` | Synthetic fact/dim inputs -> split/train/evaluate -> tracked run -> scored rows |

## Authoring loop

1. Read the approved `workshop.yaml`, data README and actual input files. Map the selected module's teaching outcome, learning route and time budget to a concrete output artifact.
2. Read its reference tutorial and `templates/lab-readme.md`. Identify old assumptions and external dependencies. Do not copy reference sample rows, private scoping details or obsolete download links.
3. Use `components/freshness/README.md` to review current public Learn procedures and relevant Microsoft blog examples. This is a documented workflow, not an implemented `freshness.verify()` call. Record sources and what they support; source review is not runtime execution.
4. Establish the starting state: workspace role, item permissions, feature-specific capacity/licence/region/settings, input files, expected schema, learner-specific names and an explicit readiness check. Never assume a trial enables every AI feature. Separate administrator setup from learner steps.
5. Include a complete Step 0 for ingestion. Show where to download or find each repository file, the Files destination, exact load action/code, table names/types and row-count check. If a previous lab provides the input, offer a precise standalone bootstrap route; do not say "load the tables" without instructions.
6. Write the end-to-end **How to do it** sequence. Every step needs the persona, UI surface or notebook kernel/SQL endpoint, exact navigation and field values, runnable code where relevant, expected output, a validation action, a failure/recovery hint and a nearby Learn citation. Explain why after the action. Use screenshots only as a supplement.
7. Add an independent **Your turn** exercise: change a filter, column, relationship, model setting or threshold; predict its effect; run it; compare evidence with explicit acceptance criteria. Include a hint. Worked code must execute end-to-end; clearly mark exercise TODOs and never leave them in prerequisite/bootstrap code.
8. Add bounded execution and safe rerun/cleanup instructions. Describe overwrite/append behaviour, stop streams and Spark sessions, undo only exercise-specific grants and remove only learner-owned items. No production mutations, live external recipients, committed credentials or implicit paid-capacity creation.
9. Reconcile the course: the plan's explain -> demonstrate -> practise -> check -> debrief sequence links to the actual lab step ranges, and the time budget includes setup, practice and cleanup. Put over-budget extensions in the self-paced route instead of quietly extending the taught day.
10. Review all snippets against real repository column/table names and public documentation. Run existing local checks if available; only run Fabric workloads with explicit permission and a suitable environment. Mark execution as not-run when unavailable. Required unresolved steps block a runnable-ready claim.
11. Emit a source/evidence report following the freshness contract and provide a publishable `FRESHNESS.md` rollup through `/vbd-repo-build`. The lab footer links to that shipped file, not a private `.vbd` audit file.

## Workload-specific procedure checks

### Lakehouse and Warehouse

- State when code runs in a Spark notebook, SQL analytics endpoint or Warehouse query editor; these are not interchangeable execution surfaces.
- Map file columns to exact table names and data types. Show a count and a known aggregate/join result with a deterministic expected value or an explained tolerance.
- Specify schemas explicitly where supported and show how to locate the resulting object. Cross-item queries must name prerequisites and permissions.
- Security exercises use an actual least-privileged identity for allow/deny tests. A workspace administrator seeing rows does not prove row-level security works for a viewer.

### RTI

Use the verified built-in sample as the low-setup route. If a customer-relevant generator is needed, make it an optional bounded extension:

- Check the [custom endpoint source documentation](https://learn.microsoft.com/fabric/real-time-intelligence/event-streams/add-source-custom-app) and follow the supported protocol, authentication and sample code for the endpoint actually configured. Do not assume an arbitrary `requests.post()` to a copied endpoint with a key is supported.
- Explain source creation, publish, destination mapping and where connection information is found. Read secrets at runtime from an approved store or an interactive prompt; never save them in notebooks or outputs.
- Use a fixed seed, finite event count, explicit pacing and a cancellation method that works while the loop is running. A later notebook "stop cell" cannot interrupt a busy synchronous cell.
- Demonstrate a KQL count/time-range check, one learner filter change and how to stop the producer and clean up exercise destinations. Do not enable alert delivery or invite recipients without approval.

### Data Science

- Name the target and input types; use a deterministic split without target leakage, include a baseline and evaluate on held-out data.
- Specify runtime/library requirements from current docs, where to run each cell, how to inspect the MLflow run and how to compare scored row counts.
- Show expected output shape and a reasonable metric condition, not an invented exact stochastic score. Use a fixed seed; record any remaining variability.

## Required lab shape

Populate every required section in `templates/lab-readme.md`: outcome and route, why, prerequisites, data/dependencies, numbered procedure, independent exercise, troubleshooting, cleanup/rerun, completion evidence and sources. Every step's checkpoint is mandatory. A source list at the end supplements but never replaces step-linked citations.

Preserve accessible language: imperative verbs, one action per numbered instruction, short explanations after actions. Keep enough detail for an unfamiliar learner to reproduce the result without the trainer's unstated knowledge.

Use a learner-specific safe prefix, for example `contoso_lab01_lh_<alias>`; clearly replace `<alias>` before execution. Never overwrite a shared object to avoid a name collision.

## Exit

Report labs and course sections updated, source-review date, execution status, unresolved blockers and the location of the evidence rollup. Distinguish executed, observed, offline and blocked outcomes; do not claim tenant execution from a successful documentation fetch.
