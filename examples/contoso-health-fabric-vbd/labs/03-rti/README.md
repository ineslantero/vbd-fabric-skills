# Lab 03: Real-Time Intelligence — Fraud alerts on the claims stream

> **Module:** RTI · **Duration:** ~5h · **Personas:** data engineer, data architect
>
> _Content verified against Microsoft Learn on 2026-09-15. Fabric release pinned: 2026-09._

## Learning objectives

- Stand up an **Eventstream** ingesting a synthetic claims stream.
- Land data in an **Eventhouse (KQL database)** with a Delta shortcut back to OneLake.
- Query with **KQL** for windowed anomaly detection.
- Build a **Real-Time Dashboard** on top of the KQL DB.
- Trigger a **Data Activator** rule when a fraud pattern is detected.

## Customer context

Contoso's highest-value objective: near-real-time fraud alerts. The pattern below (Eventstream → KQL DB → Activator) is the reference architecture we'll walk end-to-end.

## Prerequisites

- Lab 01 complete.
- Real-Time Hub visible in the workspace.

## Steps

### Step 1: Create the Eventstream

**+ New item → Eventstream** → `es_claims_stream`. Source: **Sample data → Bicycle rentals** for now (we'll swap for the synthetic claims stream in Step 2).

_Ref:_ [Eventstream overview](https://learn.microsoft.com/fabric/real-time-intelligence/event-streams/overview)

### Step 2: Swap in the synthetic claims source

Replace the sample source with a **Custom endpoint** and post events from [`scripts/producer.py`](scripts/producer.py) (runs locally, uses the endpoint URL from the Eventstream UI).

### Step 3: Create the Eventhouse

**+ New item → Eventhouse** → `eh_claims_rt`. It provisions a default KQL DB. Add a destination in the Eventstream that lands into the KQL DB table `claims_raw`.

_Ref:_ [Eventhouse overview](https://learn.microsoft.com/fabric/real-time-intelligence/eventhouse)

### Step 4: KQL for anomaly detection

Open the KQL DB query pane, run [`scripts/kql-anomaly.kql`](scripts/kql-anomaly.kql). It flags providers whose 5-minute claim volume exceeds 3σ of their 30-day baseline.

### Step 5: Real-Time Dashboard

**+ New item → Real-Time Dashboard** → add the KQL query as a tile. Filter by provider.

_Ref:_ [Real-Time Dashboards](https://learn.microsoft.com/fabric/real-time-intelligence/dashboard-real-time-create)

### Step 6: Activator rule

Open the dashboard → **Set alert** on the anomaly tile → creates a **Data Activator** rule that emails the fraud ops team when the threshold is breached.

⚠️ **Preview feature** — Activator integration paths still evolving; some UI wording may differ. Check the [roadmap card](https://roadmap.fabric.microsoft.com) for the current status.

_Ref:_ [Data Activator introduction](https://learn.microsoft.com/fabric/real-time-intelligence/data-activator/activator-introduction)

## Troubleshooting

- **No events landing in KQL DB** — check Eventstream destination status; verify KQL DB table schema matches producer payload.
- **KQL query fails on `series_decompose_anomalies`** — you're on an older KQL DB image; supported since Fabric release 2024-11.

## What's next

The **Data Science lab** ([`../04-datascience/README.md`](../04-datascience/README.md)) picks up the gold layer for the readmission model.

---

<sub>Freshness report: [`../../.vbd/freshness-foundation.yaml`](../../.vbd/freshness-foundation.yaml)</sub>
