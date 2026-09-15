# Contoso Health — Fabric VBD agenda

**Duration:** 3 days · **Mode:** hybrid (onsite London, remote observers welcome) · **Times:** Europe/London

## Day 1 — Foundation & Lakehouse

- **09:00–09:30 · Welcome & objectives recap** — Align on outcomes and success criteria captured on the scoping call.
- **09:30–12:30 · Foundation lab** — Workspaces, OneLake, capacity, tenant admin; shortcuts mapping to Contoso's ADLS Gen2 estate.
- **12:30–13:30 · Lunch**
- **13:30–17:30 · Lakehouse lab (part 1)** — Ingest de-identified claims to bronze, transform to silver via notebook, introduce Delta.
- **17:30–17:45 · Day 1 wrap** — Recap decisions, park items for Day 2, share Day 2 prereqs.

## Day 2 — Warehouse, Real-Time Intelligence & Direct Lake

- **09:00–10:30 · Lakehouse lab (part 2)** — Gold aggregate; Direct Lake semantic model over the lakehouse (embedded PBI demo).
- **10:30–13:00 · Data Warehouse lab** — T-SQL over the Warehouse item; expose gold to finance's existing SQL tooling.
- **13:00–14:00 · Lunch**
- **14:00–17:30 · Real-Time Intelligence lab** — Eventstream → KQL DB → Activator; end-to-end fraud alert pipeline.
- **17:30–17:45 · Day 2 wrap** — Confirm RTI patterns adopted; capture open architectural questions.

## Day 3 — Data Science & governance lightning talk

- **09:00–12:30 · Data Science lab** — Train and register a readmission-risk model; batch score against gold.
- **12:30–13:30 · Lunch**
- **13:30–14:30 · Governance & PHI handling lightning talk** — Row/column security, PHI redaction patterns; scoping for the follow-on Security VBD.
- **14:30–16:30 · Customer working session** — Contoso teams draft their own migration backlog with CSA support.
- **16:30–17:00 · Close-out & next steps** — Agree follow-on VBD topics, ownership, and dates.

## Notes

- Bullet-first with one-sentence rationale per item, as agreed.
- All lab timings assume the customer has completed [`prerequisites.md`](./prerequisites.md).
- Remote observers join via the Teams link in the calendar invite; onsite room booked at Contoso HQ.
