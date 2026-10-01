---
name: vbd-lab-security
description: Author the Fabric Platform, Security and Governance labs (admin and tenant settings, security from workspace to column, external partner access, governance and cataloguing) tailored to the customer in workshop.yaml.
inputs:
  - workshop.yaml
  - data/ (from /vbd-data)
outputs:
  - labs/01-admin-tenant-settings/        README + tenant inventory script
  - labs/02-security-workspace-to-column/ README + RLS/CLS/masking scripts + enforcement-boundary notebook + solutions
  - labs/03-partner-access/               README + access audit script + onboarding/offboarding runbook
  - labs/04-governance-catalogue/         README + catalogue restart plan
  - remediation-list.md
  - .vbd/freshness-security.yaml
---

# /vbd-lab-security

Authors the **Security VBD** listed as a future module in the repo README. Unlike `/vbd-lab-foundation`, this module has **no SharePoint predecessor** — the Foundation Discovery Labs are build-layer content aimed at data engineers, and they score 0–1 against a platform-engineering and security audience.

## When to use this instead of `/vbd-lab-foundation`

Run the Step 3 scoring in `/vbd-plan`. If the objectives cluster around any of these, Foundation is the wrong module:

- Tenant configuration, admin delegation, or configuration drift
- Access model design — who can see what, at which layer
- Onboarding contractors, delivery partners, or external organisations
- Catalogue, endorsement, classification, or lineage adoption
- A security baseline that exists but has drifted

**Typical trigger:** the customer already has a production Fabric estate. Foundation teaches people to *build*; this module reviews what they have *already built*. A customer with several use cases live does not need a Lakehouse tutorial.

## What it produces

Four labs, each mapped to one agenda item:

| Lab | Covers | Hands-on artefact |
|---|---|---|
| 01 Admin and tenant settings | Admin portal, tenant settings, delegation, domains, admin monitoring, admin APIs | Tenant inventory script producing diffable JSON |
| 02 Security from workspace to column | Workspace roles, item permissions, OneLake security, RLS, CLS, masking, **enforcement boundary** | T-SQL scripts + a Spark notebook that demonstrates the boundary |
| 03 Access for contractors and partners | Entra B2B guests, external data sharing, groups, service principals, review and revocation | Access audit script flagging non-group and external grants |
| 04 Governance and cataloguing | Endorsement, lineage, sensitivity labels, Purview Unified Catalog, metadata scanning | Catalogue restart commitment |

## The deliverable is a remediation list, not a repo

This is the structural difference from `/vbd-lab-foundation`. Foundation labs teach a capability; these labs **audit an existing estate**. The output that matters is a prioritised, owner-assigned list of changes to the customer's current baseline.

Populate `templates/remediation-list.md` and treat it as the primary deliverable. Each lab must end in a **decision checkpoint** that writes at least one row into it. A lab that produces no remediation rows has not done its job.

## Authoring rules

1. **Review, do not introduce.** Write for an audience that already runs the platform. "Here is where your current value is probably wrong" beats "here is what this feature does."
2. **Every lab ends in a decision**, not a completed exercise. Record the decision, the owner and the priority.
3. **Prove enforcement by querying as a restricted principal.** Never assert that a control works — have the attendee observe it. Require test identities in `prerequisites.md`.
4. **Freshness gate — mandatory.** Call `components/freshness.verify(draft)` before writing. This module's surfaces are renamed more often than any other area of Fabric; see *Volatility* below.
5. **Emit `.vbd/freshness-security.yaml`.**

## Lab 02 — the step you must not cut

Step 5 of lab 02 is the highest-value content in the module and the most common serious misconception in the field:

> SQL row-level security, column-level permissions and dynamic data masking protect access through the **SQL analytics endpoint only**. They do **not** protect direct reads of the same Delta data through Spark or OneLake.

Author it as a **demonstration**, not a statement. The attendee applies SQL controls in step 4, then opens a notebook as the same restricted identity and reads the data they were just denied. Seeing it changes designs; being told it does not.

Then have them audit their own estate: which of their controls are SQL-only, and who holds Spark or OneLake access to those tables. Note that Admin, Member and Contributor all receive default Spark/OneLake `ReadAll`, while Viewer does not — so "we gave the partner Contributor so they could read one table" is a bypass of every SQL-layer control.

Cite: https://learn.microsoft.com/fabric/onelake/security/sql-analytics-endpoint-onelake-security

## Data requirements

Ask `/vbd-data` for a schema that makes access control **arguable in the customer's own domain**. Generic retail data produces generic discussions. The fact table needs at least:

- A **column that is obviously sensitive** in that industry → column-level security target (salary band, credit limit, clinical code).
- **Contact or identity columns** → masking targets, and a masking-is-not-security discussion.
- **A natural segmentation key** present on more than one fact table → row-level security, and the chance to demonstrate the most common RLS defect: binding the predicate to one table and forgetting the other.
- **A derivable sensitive value** (`balance = total - paid`) → demonstrates that column-level security does not protect a value computable from columns left readable.
- **At least one dimension key with no matching fact rows** → produces a legitimate empty result set, which is how a misconfigured predicate looks in production and is routinely misdiagnosed.

## Volatility — re-verify before every delivery

This module ages faster than any other. Renames observed in a single 12-month window:

| Was | Is now |
|---|---|
| Microsoft Purview Hub | OneLake catalog — Govern tab |
| OneLake data access roles | OneLake security (now GA) |
| Service principals can use Fabric APIs | Service principals can call Fabric public APIs |
| Share content with external users | Users can invite guest users to collaborate through item sharing and permissions |
| Classic Purview Data Catalog | Microsoft Purview Unified Catalog (**Data Map was *not* renamed — still separate**) |

Tenant setting names appear verbatim in `prerequisites.md`, which the customer actions days before delivery. A stale name there produces a failed prerequisite and lost workshop time. **Verify tenant setting names on every single delivery**, not just when the content is first authored.

Also check the active known-issues list — issues affecting workspace role assignment are common and will be mistaken for attendee error during labs 02 and 03. Flag any live one in `prerequisites.md` *and* at the point of use.

## Prerequisites this module forces

Surface these as blockers in `prerequisites.md`; each stops a lab outright:

- **A tenant administrator present live** for lab 01. Without one it degrades to a demo against a Microsoft tenant and loses the review value.
- **Tenant settings enabled and group-scoped**, actioned at least one working day ahead — changes take up to 15 minutes to propagate and are not something to discover on the morning.
- **Two non-privileged test identities** for lab 02, and **one external identity** the customer is willing to invite and remove for lab 03.
- **A dedicated workspace, never production.** Labs 02 and 03 deliberately create restrictive permissions and invite an external identity.

## Exit

Summarise what was authored, the freshness report location, any TODOs, and remind the CSA that the remediation list is completed **live during the session** — not written afterwards from memory.
