# vbd-fabric-skills

Reusable skills for CSAs to plan and generate **Fabric Value-Based Delivery (VBD) upskilling workshops** with customer-relevant content, verified against the current Fabric roadmap and Microsoft Learn docs.

## Why

The Fabric VBD "IP release" content on SharePoint ([`Data and AI/Fabric/1 - Upskilling`](https://microsoft.sharepoint.com/teams/ASDIPRelease/IP%20Release/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FIP%20Release%2FData%20and%20AI%2FFabric%2F1%20%2D%20Upskilling&viewid=971b6985%2D5ac6%2D47e5%2Da6dc%2D5c0664b149a9&FolderCTID=0x012000F569B1CB3A2B2D499B8B6646AC5C92E3&share=cgrQu2H2GlJNRJQZc4aGoRH4EgUC5%5Fu%5FUusLmp6kQLXJk6%2Dg%5FA)) is static: `.pptx` decks + `.docx` lab guides + `Assets/` sample data (retail WWI dataset, NY taxi data). It ages badly and rarely matches the customer's industry.

These skills let a CSA:
- Drop a scoping-call transcript in and get a proposal, agenda, prereqs and content plan.
- Generate a shareable customer repo with labs, notebooks, scripts and industry-relevant data.
- Produce courses and labs with source-backed how-to steps, executable exercises, expected results, troubleshooting and safe cleanup.
- Record documentation review separately from authorised Fabric execution; never claim that a successful source fetch proves a lab ran.

## Source coverage

The **Foundation VBD Discovery Labs** are covered end-to-end by `/vbd-lab-foundation` (mirrors [SharePoint `02 - Discovery Labs`](https://microsoft.sharepoint.com/teams/ASDIPRelease/IP%20Release/Forms/AllItems.aspx?id=%2Fteams%2FASDIPRelease%2FIP%20Release%2FData%20and%20AI%2FFabric%2F1%20%2D%20Upskilling%2F1%20%2D%20Foundation%2FUpskilling%20on%20MS%20Fabric%20Foundation%2FAssets%2F02%20%2D%20Discovery%20Labs&viewid=971b6985%2D5ac6%2D47e5%2Da6dc%2D5c0664b149a9)):

| Lab | Original SharePoint asset | Skill output |
|---|---|---|
| 01 Lakehouse | `Lakehouse Tutorial.docx` + WWI sample + Delta table notebooks | `labs/01-lakehouse/` |
| 02 Data Warehouse | `Fabric Data Warehouse Tutorial.docx` + T-SQL scripts | `labs/02-warehouse/` |
| 03 Real-Time Intelligence | `Real-time Intelligence Tutorial.docx` + KQL scripts | `labs/03-rti/` |
| 04 Data Science | `Data Science Tutorial.docx` + NY taxi notebooks | `labs/04-datascience/` |

Additional modules (Lakehouse, Data Factory, Data Warehouse, RTI, Data Science, Security, Power BI as their own VBDs) will be added as `/vbd-lab-<module>` skills.

## How to use (CSA workflow)

1. **`/vbd-plan`** — paste transcript in chat, or point at a Teams meeting via WorkIQ. Skill produces a single `workshop-plan.md` (proposal + agenda + prereqs) and `workshop.yaml`. CSA reviews and edits.
2. **`/vbd-data`** — reads `workshop.yaml`, generates industry-relevant dataset.
3. **`/vbd-lab-foundation`** (and future `/vbd-lab-<module>`) — reads plan + data, authors labs. Every lab follows `components/freshness` source review and the practical learning contract before being marked ready.
4. **`/vbd-repo-build`** — assembles the final shareable repo; pushes to GitHub only on explicit CSA approval.

All four implemented skills work in both **Microsoft Scout** and **GitHub Copilot** (VS Code / CLI). The security skill directory is currently empty, not an installable fifth skill. [`.github/prompts/vbd-plan.prompt.md`](./.github/prompts/vbd-plan.prompt.md) is the planner's Copilot entry point.

## Practical course and lab contract

A course must explain a concept, demonstrate a worked example, let learners make an independent change, check an observable result and debrief the trade-off. Its plan links to the exact lab steps and budgets setup, guided practice, independent practice, checking and cleanup. Keep historical demonstration-led sessions distinct from new self-paced routes.

Each lab must include:

- An explicit starting state, feature-specific capacity/licence/region/permission requirements and a readiness check.
- Numbered how-to instructions with exact UI navigation/field values or runnable code using the actual repository data schema, plus the correct execution surface and persona.
- A Microsoft Learn procedure beside each substantive step, expected output, a checkpoint and a recovery hint. Verified Microsoft blog examples add dated design context, not substitute product requirements.
- A learner modification with acceptance criteria, standalone replay steps, cost boundaries, bounded execution and cleanup of only exercise-owned resources.
- Honest completion evidence: executed, observed, offline or blocked. Required unresolved procedure steps block a runnable-ready claim.

The contract is carried by [`templates/workshop.yaml`](./templates/workshop.yaml), the [course template](./templates/workshop-plan.md), the [lab template](./templates/lab-readme.md) and the [assembly quality gate](./skills/vbd-repo-build/SKILL.md). These are authoring templates/instructions, not an implemented renderer or test suite. When updating a legacy course, explicitly add missing learning fields instead of silently assuming it satisfies the contract.

## Install locally

Keep a complete local checkout: skill-relative `references/` and repository-level `templates/` / `components/` are required. Do not install only a detached `SKILL.md`.

Use the native [Copilot CLI skill registration](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills). From the repository root, register the whole directory so its shared resources remain in place:

```powershell
copilot skill add (Join-Path (Get-Location).Path 'skills')
copilot skill list --json
```

Confirm `vbd-plan`, `vbd-data`, `vbd-lab-foundation` and `vbd-repo-build` appear and are enabled. In an existing interactive session, use `/skills reload`, then `/skills info <name>`, or start a fresh session. Keep the checkout available locally and in the same location; a later pull updates this registered installation. Review upstream changes before updating and do not remove or overwrite a competing skill without checking its provenance. Older clients can use personal directories in `~/.copilot/skills` or `~/.agents/skills`, but must retain the complete checkout and resolve shared resources correctly.

For Scout, register each of the same four names through its local skill management tools. The registered instructions must identify the complete checkout, load that skill's `SKILL.md`, and resolve shared resources there; CLI directory registration alone is not a Scout registration. Registration is local and does not publish anything to GitHub.

## Repo layout

```
vbd-fabric-skills/
├── skills/                     ← CSA-invoked skills
│   ├── vbd-plan/
│   ├── vbd-data/
│   ├── vbd-lab-foundation/
│   └── vbd-repo-build/
├── templates/                  ← skeletons skills fill in
│   ├── workshop.yaml
│   ├── workshop-plan.md
│   ├── lab-readme.md
│   └── notebook.ipynb
├── components/                 ← shared helpers imported by skills
│   ├── freshness/              ← MS Learn + roadmap verifier (mandatory gate)
│   └── transcript-loader/      ← paste / WorkIQ / email-thread normaliser
└── .github/prompts/            ← GitHub Copilot planner entry point
```

## Source review and execution evidence

[`components/freshness`](./components/freshness) defines the mandatory manual/tool-assisted review workflow. It is not an implemented automatic verifier. Fetch the relevant Learn procedures, feature availability guidance and Microsoft blog context; record the actual review date, supported claims and unresolved issues.

Generated lab footers link to the shipped `FRESHNESS.md` rollup and state execution status independently. A release reference is not a Fabric runtime version lock. Strict review blocks unresolved required steps; an optional blocked extension can remain clearly excluded after review. Never replace missing runtime evidence with a blanket "verified" claim.

## Design docs

- Architecture and open questions: [`docs/architecture.md`](./docs/architecture.md)
- `workshop.yaml` schema: [`templates/workshop.yaml`](./templates/workshop.yaml)
- Adding a new module skill: [architecture extension guidance](./docs/architecture.md#extension-adding-a-new-module-skill)
