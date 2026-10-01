# components/freshness

**Mandatory source-review workflow for every /vbd-* skill.** This directory contains guidance and a source registry, not an executable verifier: there is no implemented `freshness.verify()` function, resolver package or roadmap JSON client. Use available browsing tools to perform the checks and record actual evidence. Never report an automatic or tenant-executed check that did not happen.

## What to review

| Source | Use |
|---|---|
| [Microsoft Learn - Fabric](https://learn.microsoft.com/fabric) | Primary authority for feature names, prerequisites, exact UI procedures and code |
| [Fabric REST reference](https://learn.microsoft.com/rest/api/fabric/articles) | HTTP method, endpoint, authentication, body and response shape |
| [What's new](https://learn.microsoft.com/fabric/fundamentals/whats-new) | Dated product changes; follow through to feature documentation |
| [Fabric roadmap](https://roadmap.fabric.microsoft.com) | Future intent and rollout context, never proof of tenant availability |
| [Fabric known issues](https://learn.microsoft.com/fabric/fundamentals/known-issues) | Known blockers and documented workarounds |
| [Microsoft Fabric blog](https://blog.fabric.microsoft.com) | Dated worked examples and design context; cross-check operational claims against Learn |

## Review procedure

1. Extract each material claim, prerequisite, UI action, API and code sample from the proposed course and lab. Read the actual repository input schema before checking code.
2. Fetch the relevant Learn article and section. Follow redirects to canonical URLs; do not count search snippets, blocked pages or page titles as procedure verification.
3. Capture URL, section, date checked, claim supported and any conflict. Use the actual check date. Reuse a fetched page within the same review session; reassess before later delivery.
4. Verify at least one relevant Microsoft blog example per course where accessible. Date it and identify what it adds. If none can be verified, disclose that rather than inventing a link.
5. Map the source to each numbered lab step. Confirm the instructions specify identity, execution surface, input values, expected output, troubleshooting and cleanup. A reading list alone does not satisfy this gate.
6. Resolve contradictory or outdated instructions using the current feature documentation. Mark uncertain feature availability and tenant-specific UI differences explicitly. Never elevate an announcement or roadmap date into a GA claim.
7. Record documentation review and runtime execution separately. Static inspection of code is not a Fabric run. Runtime evidence requires an authorised environment, actual output and a date; do not provision resources or incur costs merely to improve a verification label.
8. Publish a sanitised `FRESHNESS.md` rollup with the deliverable. Keep private working evidence and transcripts out of customer/public repositories. Check all source and local navigation links.

## Evidence contract

The following is an example shape, not the result of a run:

```yaml
verified_at: <actual-ISO-8601-check-time>
fabric_release_pinned: <documentation-reference-YYYY-MM>
strictness: strict
checks:
  - claim: <specific-action-or-requirement>
    lab_step: <lab-id-and-step-number>
    source: <canonical-Microsoft-Learn-URL>
    source_section: <heading>
    checked_on: <YYYY-MM-DD>
    status: verified # verified | outdated | deprecated | preview | unknown
    evidence: <short-paraphrase-of-support-not-a-copied-article>
    execution_status: not-run # not-run | passed | failed | blocked
    execution_evidence: null # authorised environment/date/output only when actually run
    action: <correction-warning-or-blocker-if-needed>
todos: []
```

A `verified` status means the documented claim was supported by the fetched source. It does not mean the learner's tenant supports it, the UI was exercised or a capacity runtime was pinned.

## Blocking and preview rules

- `verified`: cite the relevant procedure beside the step and state the review date.
- `preview`: include the actual documented availability and access constraints. If `allow_preview_features` is false, omit from the runnable route and explain the resulting scope change.
- `outdated` or `deprecated`: correct and re-review; do not ship the old instruction as runnable.
- `unknown`: identify the unresolved claim and the attempted source. Never mark an inaccessible URL as verified.
- `strictness: strict`: unresolved required steps block readiness/publication.
- `balanced` or `permissive`: an unresolved optional extension may be explicitly excluded after CSA review; do not let a TODO stand in for a required executable step.
- `allow_roadmap_futures`: controls future-looking discussion only, not execution eligibility.
- `regions_to_check`: check feature-specific availability, not just whether Fabric exists in the region.

## Adding a source

Add a public source entry to `sources.yaml`, describe its authority and use available tools to inspect it. No resolver API is currently implemented. Prefer Learn for procedures and official Microsoft blogs for context; never send private scoping material to a public search service.
