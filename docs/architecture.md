# vbd-fabric-skills — architecture

Design record for the reusable Fabric VBD skill family. See [`../README.md`](../README.md) for user-facing usage.

## Concepts

- **Skill** — instruction set + helpers Scout/Copilot load on demand (`/skill-name`). The verb.
- **Template** — static file with placeholders. The shape.
- **Component** — helper library that multiple skills import. The plumbing.
- **Practical learning contract** — the course's worked example and learner task must map to a reproducible lab, expected result and evidence, not just to a topic name.

## Skills

| Skill | Role | Consumes | Produces |
|---|---|---|---|
| `/vbd-plan` | Orchestrator | Transcript (chat paste / WorkIQ / email thread) | `workshop-plan.md`, `workshop.yaml` |
| `/vbd-data` | Data generator | `workshop.yaml` | `data/` + `data/README.md` |
| `/vbd-lab-foundation` | Foundation Discovery Labs | `workshop.yaml` + `data/` | `labs/01-lakehouse`, `02-warehouse`, `03-rti`, `04-datascience` |
| `/vbd-lab-<module>` (future) | Per-module VBDs | Same | `labs/nn-<module>/` |
| `/vbd-repo-build` | Repo assembler | Everything above | `<repo_name>/` + `FRESHNESS.md`; optional GitHub push |

## Templates

- `templates/workshop.yaml` — handoff contract schema
- `templates/workshop-plan.md` — single consolidated plan (proposal + agenda + prereqs)
- `templates/lab-readme.md`, `notebook.ipynb`

## Components

- `components/freshness/` — **mandatory source-review workflow**. Learn procedures + relevant Microsoft blogs + roadmap/release notes/known issues/REST reference. It contains instructions and a source registry, not executable verification functions.
- `components/transcript-loader/` — normalises paste / WorkIQ / email into `.vbd/transcript.md`.
- `components/data-gen/` — proposed extension; generation currently follows `/vbd-data` instructions, not an implemented helper library.
- `components/fabric-api/` — optional Fabric REST wrappers (future).

## Flow

```
                                            ┌─ components/freshness (mandatory gate on every write)
                                            │
transcript ─► /vbd-plan ─► workshop.yaml ───┼─► /vbd-data ─► data/
                                            │
                                            └─► /vbd-lab-foundation ─► labs/01..04/
                                                                        │
                                                                        ▼
                                                                /vbd-repo-build ─► repo/ (+ optional GH push)
```

## Freshness — the whole point

Every generated artifact records its source-review date and execution status separately. Cite Microsoft Learn beside operational steps and use verified Microsoft blogs for dated context. Preview features carry access constraints; deprecated instructions are replaced or excluded. A roadmap date does not prove tenant availability. No `freshness.verify()` function or resolver package is implemented: every skill follows the review workflow with available browsing tools.

`templates/workshop.yaml` now carries per-module `teaching` and `learning` metadata: concept, worked example, learner task, evidence, debrief, route, setup/role requirements, artifact, timed practice, fallback and cleanup. New courses populate all fields; older courses are upgraded explicitly. The six learning time components sum to the module duration. Demonstrations and offline alternatives are not counted as Fabric execution.

`templates/lab-readme.md` renders the matching how-to contract. The assembler checks every included lab for step-level sources, actual data/schema consistency, independent practice, expected output and safe cleanup. Source records roll up to a shipped `FRESHNESS.md`; lab links must not point to private `.vbd` files absent from the deliverable. Required unresolved procedures block a runnable-ready claim even if an optional extension may be deferred.

Configurable via `workshop.yaml.freshness`:
- `allow_preview_features` (bool)
- `allow_roadmap_futures` (bool)
- `strictness: strict | balanced | permissive`
- `regions_to_check: []`

## Two-surface support

Same skills run in **Microsoft Scout** (via `m_get_skill` + `SKILL.md`) and **GitHub Copilot** (via `.github/prompts/*.prompt.md` and Copilot CLI custom skills). No duplication — Copilot entry points thin-wrap the same skill definitions.

There are four implemented `SKILL.md` definitions. `skills/vbd-lab-security/` is empty and is not installed. Personal Copilot directory registrations and Scout registrations point to a complete local checkout, retaining skill references and shared templates/components. Resolve linked targets before resolving relative resources; see the root README installation procedure. Workspace-backed edits still use the provider's editing tools rather than a local synced copy.

## Open architectural decisions

- **Show module scoring reasoning to CSA?** (current default: yes)
- **Auto-orchestrate downstream skills after plan approval?** (current default: yes, but each step is a distinct tool call so CSA can interrupt)
- **Ship solutions in customer repo?** (`workshop.yaml.deliverable.include_solutions`, default `false`)
- **Deck regeneration** — currently out of scope; the SharePoint `.pptx` is still used. Reconsider once the lab-authoring pattern is stable.

## Extension: adding a new module skill

1. Copy `skills/vbd-lab-foundation/` to `skills/vbd-lab-<module>/`.
2. Update the SKILL.md front matter and content outlines.
3. Add module id to the accepted set in `templates/workshop.yaml` and in `/vbd-plan` module scorer.
4. Author templates for any module-specific artefacts (e.g. Data Factory pipeline JSON).
5. Register with `components/freshness` if it needs new source URLs.

## Extension: adding a new industry domain

1. Drop a YAML descriptor at `components/data-gen/domains/<slug>.yaml`.
2. Include tables, fields, distributions, referential integrity, default volumes.
3. Add example values so the LLM enrichment step produces realistic labels.
