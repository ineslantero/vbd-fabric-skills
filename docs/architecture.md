# vbd-fabric-skills — architecture

Design record for the reusable Fabric VBD skill family. See [`../README.md`](../README.md) for user-facing usage.

## Concepts

- **Skill** — instruction set + helpers Scout/Copilot load on demand (`/skill-name`). The verb.
- **Template** — static file with placeholders. The shape.
- **Component** — helper library that multiple skills import. The plumbing.

## Skills

| Skill | Role | Consumes | Produces |
|---|---|---|---|
| `/vbd-plan` | Orchestrator | Transcript (chat paste / WorkIQ / email thread) | `proposal.md`, `agenda.md`, `prerequisites.md`, `workshop.yaml` |
| `/vbd-data` | Data generator | `workshop.yaml` | `data/` + `data/README.md` |
| `/vbd-lab-foundation` | Foundation Discovery Labs | `workshop.yaml` + `data/` | `labs/01-lakehouse`, `02-warehouse`, `03-rti`, `04-datascience` |
| `/vbd-lab-<module>` (future) | Per-module VBDs | Same | `labs/nn-<module>/` |
| `/vbd-repo-build` | Repo assembler | Everything above | `<repo_name>/` + `FRESHNESS.md`; optional GitHub push |

## Templates

- `templates/workshop.yaml` — handoff contract schema
- `templates/proposal.md`, `agenda.md`, `prerequisites.md`
- `templates/lab-readme.md`, `notebook.ipynb`

## Components

- `components/freshness/` — **mandatory verification gate**. Learn + roadmap + release notes + known issues + REST reference.
- `components/transcript-loader/` — normalises paste / WorkIQ / email into `.vbd/transcript.md`.
- `components/data-gen/` — industry-aware synthetic data generator.
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

Every generated artefact carries a verification footer and cites Microsoft Learn or the Fabric public roadmap. Preview features get banners; deprecated features are rewritten or excluded. The verifier is called by every skill — not optional.

Configurable via `workshop.yaml.freshness`:
- `allow_preview_features` (bool)
- `allow_roadmap_futures` (bool)
- `strictness: strict | balanced | permissive`
- `regions_to_check: []`

## Two-surface support

Same skills run in **Microsoft Scout** (via `m_get_skill` + `SKILL.md`) and **GitHub Copilot** (via `.github/prompts/*.prompt.md` and Copilot CLI custom skills). No duplication — Copilot entry points thin-wrap the same skill definitions.

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
