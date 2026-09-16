# vbd-fabric-skills

Reusable skills for CSAs to plan and generate **Fabric Value-Based Delivery (VBD) upskilling workshops** with customer-relevant content, verified against the current Fabric roadmap and Microsoft Learn docs.

## Why

The Fabric VBD "IP release" content on SharePoint ([`Data and AI/Fabric/1 - Upskilling`](https://microsoft.sharepoint.com/teams/ASDIPRelease)) is static: `.pptx` decks + `.docx` lab guides + `Assets/` sample data (retail WWI dataset, NY taxi data). It ages badly and rarely matches the customer's industry.

These skills let a CSA:
- Drop a scoping-call transcript in and get a proposal, agenda, prereqs and content plan.
- Generate a shareable customer repo with labs, notebooks, scripts and industry-relevant data.
- Guarantee every lab step is verified against current Fabric docs and roadmap at generation time.

## Source coverage

The **Foundation VBD Discovery Labs** are covered end-to-end by `/vbd-lab-foundation` (mirrors [SharePoint `02 - Discovery Labs`](https://microsoft.sharepoint.com/teams/ASDIPRelease/IP%20Release/Data%20and%20AI/Fabric/1%20-%20Upskilling/1%20-%20Foundation)):

| Lab | Original SharePoint asset | Skill output |
|---|---|---|
| 01 Lakehouse | `Lakehouse Tutorial.docx` + WWI sample + Delta table notebooks | `labs/01-lakehouse/` |
| 02 Data Warehouse | `Fabric Data Warehouse Tutorial.docx` + T-SQL scripts | `labs/02-warehouse/` |
| 03 Real-Time Intelligence | `Real-time Intelligence Tutorial.docx` + KQL scripts | `labs/03-rti/` |
| 04 Data Science | `Data Science Tutorial.docx` + NY taxi notebooks | `labs/04-datascience/` |

The **Security / Platform & Governance VBD** is covered by `/vbd-lab-security`. It has no SharePoint predecessor — it targets customers who already run a production Fabric estate and need the platform reviewed rather than introduced:

| Lab | Covers | Skill output |
|---|---|---|
| 01 Admin and tenant settings | Admin portal, delegation, domains, admin monitoring, admin APIs | `labs/01-admin-tenant-settings/` |
| 02 Security workspace to column | Workspace roles, item permissions, OneLake security, RLS, CLS, masking, enforcement boundary | `labs/02-security-workspace-to-column/` |
| 03 Partner and contractor access | Entra B2B, external data sharing, groups, service principals, review and revocation | `labs/03-partner-access/` |
| 04 Governance and cataloguing | Endorsement, lineage, sensitivity labels, Purview Unified Catalog, scanning | `labs/04-governance-catalogue/` |

Remaining modules (Data Factory, Data Warehouse, RTI, Data Science, Power BI as their own VBDs) will be added as `/vbd-lab-<module>` skills.

### Choosing a module

`/vbd-plan` Step 3 scores the candidate labs. As a rule of thumb: **Foundation teaches people to build; Security reviews what they have already built.** A customer with several use cases already in production scores 0–1 on every Foundation lab.

## How to use (CSA workflow)

1. **`/vbd-plan`** — paste transcript in chat, or point at a Teams meeting via WorkIQ. Skill produces a single `workshop-plan.md` (proposal + agenda + prereqs) and `workshop.yaml`. CSA reviews and edits.
2. **`/vbd-data`** — reads `workshop.yaml`, generates industry-relevant dataset.
3. **`/vbd-lab-foundation`** or **`/vbd-lab-security`** (and future `/vbd-lab-<module>`) — reads plan + data, authors labs. Every lab passes `components/freshness` verification before writing.
4. **`/vbd-repo-build`** — assembles the final shareable repo; pushes to GitHub only on explicit CSA approval.

All skills work in both **Microsoft Scout** and **GitHub Copilot** (VS Code / CLI). See [`.github/prompts/`](./.github/prompts) for the Copilot entry points.

## Repo layout

```
vbd-fabric-skills/
├── skills/                     ← CSA-invoked skills
│   ├── vbd-plan/
│   ├── vbd-data/
│   ├── vbd-lab-foundation/     ← build-layer labs (green-field customers)
│   ├── vbd-lab-security/       ← review-layer labs (customers already in production)
│   └── vbd-repo-build/
├── templates/                  ← skeletons skills fill in
│   ├── workshop.yaml
│   ├── workshop-plan.md
│   ├── lab-readme.md
│   ├── repo-readme.md          ← customer-facing repo landing page
│   ├── remediation-list.md     ← primary deliverable for review-style VBDs
│   └── notebook.ipynb
├── components/                 ← shared helpers imported by skills
│   ├── freshness/              ← MS Learn + roadmap verifier (mandatory gate)
│   ├── transcript-loader/      ← paste / WorkIQ / email-thread normaliser
│   ├── data-gen/               ← industry-aware synthetic data
│   └── fabric-api/             ← optional Fabric REST wrappers
├── examples/
│   └── contoso-health-fabric-vbd/  ← worked example: 3-day Foundation VBD for a healthcare payer
└── .github/prompts/            ← GitHub Copilot entry points
```

## Freshness guarantee

Every generated lab embeds a verification footer:

> _Content verified against Microsoft Learn on 2026-09-15. Fabric release pinned: 2026-09. Any preview features are called out inline._

The verifier lives in [`components/freshness`](./components/freshness). It hits Microsoft Learn, the [Fabric public roadmap](https://roadmap.fabric.microsoft.com) and release notes. Labs are not written to disk until verification passes (or unresolved items become explicit TODO markers with citations).

## Design docs

- Architecture and open questions: [`docs/architecture.md`](./docs/architecture.md)
- `workshop.yaml` schema: [`templates/workshop.yaml`](./templates/workshop.yaml)
- Adding a new module skill: [`docs/adding-a-lab-skill.md`](./docs/adding-a-lab-skill.md)
