# Lab 02: Data Warehouse — T-SQL over the gold layer

> **Module:** Warehouse · **Duration:** ~3h · **Personas:** data engineer, BI analyst
>
> _Content verified against Microsoft Learn on 2026-09-15. Fabric release pinned: 2026-09._

## Learning objectives

- Create a Fabric Warehouse item and understand the difference between Warehouse and Lakehouse SQL endpoint.
- Cross-database query the Lakehouse `gold_claims_by_provider_month` from the Warehouse.
- Materialise a Warehouse-owned aggregate via a stored procedure.
- Expose the Warehouse as a semantic model in Direct Lake mode.

## Customer context

Finance's existing tooling speaks T-SQL. The gold layer lives in the Lakehouse; the Warehouse gives finance a familiar surface without duplicating data.

## Prerequisites

- Lab 01 complete — `gold_claims_by_provider_month` exists.
- Contributor role on `contoso-vbd-jan2027`.

## Steps

### Step 1: Create the Warehouse

**+ New item → Warehouse** → `wh_claims_analytics`.

_Ref:_ [Create a Fabric Warehouse](https://learn.microsoft.com/fabric/data-warehouse/create-warehouse)

✅ **Checkpoint** — Warehouse SQL editor opens with `wh_claims_analytics` as the current context.

### Step 2: Cross-database query the Lakehouse gold

```sql
SELECT TOP 10 provider_id, month, total_paid
FROM lh_claims_bronze.dbo.gold_claims_by_provider_month
ORDER BY total_paid DESC;
```

_Ref:_ [Cross-warehouse queries](https://learn.microsoft.com/fabric/data-warehouse/query-warehouse)

### Step 3: Create Warehouse tables

Run [`scripts/01-create-tables.sql`](scripts/01-create-tables.sql).

### Step 4: Load with `INSERT ... SELECT`

Run [`scripts/02-load-tables.sql`](scripts/02-load-tables.sql).

### Step 5: Create + run aggregate stored procedure

Run [`scripts/03-create-aggregate-proc.sql`](scripts/03-create-aggregate-proc.sql), then `EXEC dbo.usp_refresh_provider_summary;`.

### Step 6: Expose as a Direct Lake semantic model

Warehouse toolbar → **New semantic model** → include `dim_provider` and `fact_provider_month_summary`. Open in Power BI; build a matrix visual: provider × month → total paid.

_Ref:_ [Direct Lake over Warehouse](https://learn.microsoft.com/fabric/direct-lake/overview)

## Troubleshooting

- **Cross-database query fails with `Object not found`** — the Lakehouse SQL endpoint hasn't synced the new table yet. Wait 30s and retry, or refresh the endpoint object explorer.
- **`INSERT ... SELECT` slow** — batch size too small; the sample scripts use a single set-based statement, which is optimal on Fabric Warehouse.

## What's next

Move to the **Real-Time Intelligence lab** ([`../03-rti/README.md`](../03-rti/README.md)) for the fraud alert pipeline.

---

<sub>Freshness report: [`../../.vbd/freshness-foundation.yaml`](../../.vbd/freshness-foundation.yaml)</sub>
