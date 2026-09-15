# Lab 01: Lakehouse — Claims medallion on Fabric

> **Module:** Lakehouse · **Duration:** ~5h · **Personas:** data engineer, data architect
>
> _Content verified against Microsoft Learn on 2026-09-15. Fabric release pinned: 2026-09._

## Learning objectives

By the end of this lab you will be able to:

- Create a Fabric workspace assigned to your F-SKU capacity.
- Create a Lakehouse and understand OneLake, Files vs. Tables, and shortcuts.
- Ingest CSV claims data into a bronze Delta table via a notebook.
- Transform bronze → silver with data-quality rules and typed columns.
- Aggregate silver → gold for downstream Warehouse and Power BI consumption.
- Query the Lakehouse via its SQL analytics endpoint.

## Customer context

You'll build the medallion on **de-identified synthetic claims data** shaped like Contoso's real estate: `claims`, `members`, `providers`, `procedures`, `diagnoses`. The point is to prove the migration off the Synapse dedicated pool works with your schema — the code you write here is the code you'll take home.

## Prerequisites

- Completed [`prerequisites.md`](../../prerequisites.md).
- Access to workspace **`contoso-vbd-jan2027`**.
- Sample data loaded — see [`../../data/README.md`](../../data/README.md).

## Steps

### Step 1: Create the workspace

In the Fabric portal, create a workspace `contoso-vbd-jan2027` and assign it to the F64 capacity your admin created. Verify from the workspace **Settings → License info** that the SKU is displayed.

✅ **Checkpoint** — you can see the workspace under **My workspaces** and it shows `Fabric capacity: F64`.

_References:_
- [Create a workspace](https://learn.microsoft.com/fabric/fundamentals/create-workspaces)
- [OneLake overview](https://learn.microsoft.com/fabric/onelake/onelake-overview)

### Step 2: Create the Lakehouse

Inside the workspace, **+ New item → Lakehouse**. Name it `lh_claims_bronze`. Note the two default folders — **Files** (unmanaged) and **Tables** (managed Delta).

✅ **Checkpoint** — Lakehouse opens with an explorer showing empty `Files/` and `Tables/`.

_References:_
- [Create a Lakehouse](https://learn.microsoft.com/fabric/data-engineering/create-lakehouse)

### Step 3: Ingest bronze data

Two paths — pick one and note the trade-off:

**Option A (default): upload the CSV set.** In the Lakehouse explorer, right-click `Files/` → **Upload folder** and pick `data/bronze/` from the workshop repo. This mirrors how you'd do a one-off migration.

**Option B: shortcut to your ADLS Gen2.** In `Files/`, **+ New shortcut → Azure Data Lake Storage Gen2**, point at a Contoso ADLS path with equivalent data. This is the pattern for keeping data in place — no copy, no duplication of storage cost.

✅ **Checkpoint** — `Files/bronze/claims/*.csv` are visible in the explorer.

_References:_
- [OneLake shortcuts](https://learn.microsoft.com/fabric/onelake/onelake-shortcuts)
- [Load data with a notebook](https://learn.microsoft.com/fabric/data-engineering/lakehouse-notebook-load-data)

### Step 4: Bronze → silver via notebook

Open [`scripts/01-bronze-to-silver.ipynb`](scripts/01-bronze-to-silver.ipynb). Read the setup cell, then complete each TODO:

- Read `Files/bronze/claims/*.csv` into a DataFrame.
- Cast `claim_amount` to decimal, `claim_date` to date, drop rows where `member_id IS NULL`.
- Write to `Tables/silver_claims` as a managed Delta table with `mode('overwrite')`.

✅ **Checkpoint** — `Tables/silver_claims` appears in the explorer and `SELECT COUNT(*)` returns roughly 500 000.

_References:_
- [Delta Lake tables](https://learn.microsoft.com/fabric/data-engineering/lakehouse-and-delta-tables)

### Step 5: Silver → gold aggregate

Open [`scripts/02-silver-to-gold.ipynb`](scripts/02-silver-to-gold.ipynb). Build `Tables/gold_claims_by_provider_month` — sum of paid amount, count of claims, per provider per month.

✅ **Checkpoint** — gold table exists and returns ~24k rows for the synthetic year.

### Step 6: Query via the SQL analytics endpoint

From the Lakehouse, top-right dropdown → **SQL analytics endpoint**. Run:

```sql
SELECT provider_id, month, total_paid
FROM gold_claims_by_provider_month
ORDER BY total_paid DESC
LIMIT 10;
```

⚠️ **Preview feature** — SQL endpoint auto-refresh for new tables can lag by up to 30s. If the table isn't visible, refresh the object explorer. ([roadmap card](https://roadmap.fabric.microsoft.com))

✅ **Checkpoint** — top 10 providers by spend returned.

_References:_
- [SQL analytics endpoint](https://learn.microsoft.com/fabric/data-warehouse/data-warehousing#sql-analytics-endpoint-of-the-lakehouse)

### Step 7: Direct Lake Power BI teaser

From the Lakehouse toolbar → **New semantic model** → include the three gold tables. In Power BI, build a simple report on `total_paid` by provider. You'll return to this in the Warehouse lab (Day 2).

_References:_
- [Direct Lake overview](https://learn.microsoft.com/fabric/direct-lake/overview)

## Troubleshooting

- **Notebook won't attach to session** — capacity paused or throttled. Check with your Fabric admin.
- **Shortcut option missing** — you need at least Contributor role on the workspace + the tenant setting `Users can create Fabric items` enabled.
- **`Tables/` folder greyed out** — you're viewing a Lakehouse without Tables enabled; recreate it.
- **Direct Lake fallback to DirectQuery** — semantic model exceeded row/column guardrails; check the [Direct Lake limits](https://learn.microsoft.com/fabric/direct-lake/directlake-overview#considerations-and-limitations).

## What's next

Day 2 opens with the **Warehouse lab** ([`../02-warehouse/README.md`](../02-warehouse/README.md)) — you'll expose this gold layer via T-SQL for finance's existing tooling.

---

<sub>Freshness report: [`../../.vbd/freshness-foundation.yaml`](../../.vbd/freshness-foundation.yaml)</sub>
