# components/freshness

**Mandatory verification gate for every /vbd-* skill.** No lab, proposal, or agenda is written to disk until it passes freshness verification (or unresolved claims are marked TODO with citations).

## What it checks

| Source | What we validate | How |
|---|---|---|
| [Microsoft Learn — Fabric](https://learn.microsoft.com/fabric) | Feature names, UI paths, code samples, API endpoints, KQL/SQL constructs | HTTP fetch + LLM claim-to-doc match; cite exact URL |
| [Fabric public roadmap](https://roadmap.fabric.microsoft.com) | Feature status: GA / preview / rolling out / deprecated / coming soon | Roadmap JSON feed |
| [Fabric release notes](https://learn.microsoft.com/fabric/fundamentals/whats-new) | Renames, moves, changed defaults since template authoring | HTTP fetch |
| [Fabric REST API reference](https://learn.microsoft.com/rest/api/fabric/articles) | Endpoint shape, auth, required fields | HTTP fetch |
| [Fabric known issues](https://learn.microsoft.com/fabric/fundamentals/known-issues) | Active bugs that would break a lab step | HTTP fetch |

## Verification contract

Skills call `freshness.verify(draft)` where `draft` is the in-memory lab content. The function returns:

```yaml
verified_at: 2026-09-15T12:16:00Z
fabric_release_pinned: 2026-09
strictness: strict
checks:
  - claim: "Create a Lakehouse from workspace + button"
    source: https://learn.microsoft.com/fabric/data-engineering/create-lakehouse
    status: verified                # verified | outdated | deprecated | preview | unknown
  - claim: "Copilot in Notebooks generally available"
    source: roadmap:copilot-notebooks
    status: preview
    action: added-preview-banner
    banner: "This feature is in public preview as of {{fabric_release_pinned}}."
  - claim: "Dataflow Gen1 available in workspace ribbon"
    source: release-notes:2026-08
    status: deprecated
    action: rewrite-with-dataflow-gen2
todos: []                            # unresolved after retry cap
summary:
  total: 42
  verified: 39
  preview: 2
  deprecated: 1
  todos: 0
```

## Behaviour by status

- `verified` → cite the URL as a footnote in the lab step.
- `preview` → keep the step, add a preview banner + roadmap link.
- `outdated` / `deprecated` → skill rewrites the step and re-verifies (up to 3 attempts).
- `unknown` → mark as TODO in the lab with a citation to what we searched.

## Configurable behaviour (from `workshop.yaml.freshness`)

- `allow_preview_features: false` → strip preview content entirely.
- `allow_roadmap_futures: false` → no "coming soon" callouts in the proposal.
- `strictness: strict` → fail the whole lab if any status is `outdated`/`unknown`.
- `regions_to_check` → only trust features listed as available in those tenant regions.

## Implementation notes

- Cache Learn responses for the session — same doc URL should not be fetched twice per generation.
- Batch claims per Learn article to reduce round-trips.
- Log all HTTP calls to `.vbd/freshness-audit.jsonl` for auditability.

## Adding a new source

Drop a resolver under `resolvers/` and register in `sources.yaml`. The verifier is source-agnostic — resolvers just have to return `{status, url, evidence}`.
