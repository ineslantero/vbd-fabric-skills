# Fabric Foundation VBD - Data Warehouse Lab Tutorial

> Converted from `Fabric Data Warehouse Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs).
> Screenshots have been stripped; Microsoft Learn URLs are cited inline throughout.

> **Freshness-verified 2026-10-01** — Cross-checked against Microsoft Learn. Fixes applied per `.vbd/freshness-audit-2026-09-15.md`. Preview features are called out inline where relevant.

## Contents

- Introduction

- Module 1: Create a workspace (This step is not needed if the workspace is already created for every user upon provisioning of trial tenant)

- Module 2: Build your first data warehouse

- Create a data warehouse

- Data ingestion

- Building a report

- Module 3: Extending the solution

- Creating tables in the data warehouse

- Loading data using Pipeline

- Data transformation using a stored procedure

- Using the visual query builder

- Create a Power BI report

- Time Travel in Data Warehouse

- Clone Table in Data Warehouse

- Module 4: Clean up resources

## Objective

- Create a workspace for Warehouse lab assets.
- Create the `WideWorldImporters` Warehouse.
- Load `dimension_customer` from the Lakehouse built in the Lakehouse lab.
- Create `dimension_city` and `fact_sale` tables with T-SQL (CSV-aligned schemas).
- Load `dimension_city` and `fact_sale` from the Lakehouse with a Copy pipeline.
- Transform sales data with a stored procedure.
- Explore data with the visual query builder.
- Build a Power BI report and test Warehouse time travel and clone features.

## Microsoft Learn references

- https://learn.microsoft.com/fabric/data-warehouse/data-warehousing
- https://learn.microsoft.com/fabric/data-warehouse/tutorial-introduction
- https://learn.microsoft.com/fabric/data-warehouse/ingest-data
- https://learn.microsoft.com/fabric/data-warehouse/query-warehouse
- https://learn.microsoft.com/fabric/data-warehouse/time-travel
- https://learn.microsoft.com/fabric/data-warehouse/clone-table

## Modules

### Module 1: Create a workspace

#### Step 1: Create a Fabric workspace

- Sign in to Microsoft Fabric at https://app.fabric.microsoft.com/.
- Select **Workspaces** > **New workspace**.
- Name the workspace `Data Warehouse Tutorial` plus a unique suffix.
- Optionally add a description.
- Expand **Advanced**.
- Choose **Fabric capacity** under **License mode** and pick an F-SKU, or choose **Trial**.
- Select **Apply**.

**Explanation:** The workspace keeps the Warehouse, pipeline, semantic model, and reports together. Skip this step if a lab workspace already exists.
**Checkpoint:** The `Data Warehouse Tutorial` workspace opens.

### Module 2: Build your first data warehouse

#### Step 2: Create the `WideWorldImporters` Warehouse

- Open the `Data Warehouse Tutorial` workspace from https://powerbi.com/.
- Select **New item**.
- Select **Warehouse** under **Store data**.
- Enter `WideWorldImporters`.
- Select **Create**.

**Explanation:** The Warehouse provides a relational SQL surface over Fabric storage for T-SQL development and reporting.
**Checkpoint:** The `WideWorldImporters` build page appears.

#### Step 3: Load `dimension_customer` from the Lakehouse

The Lakehouse lab produced a Delta table `dimension_customer` inside `wwilakehouse` (via the Dataflow Gen2). Copy it into the Warehouse so T-SQL can own it.

- Return to the workspace item view.
- Select **New item** > **Data pipeline**.
- Name the pipeline `Load Customer Data`.
- Select **Create**.
- Add a **Copy data** activity.
- Set the activity name to `CD Load dimension_customer`.
- **Source** → **Connection** = `wwilakehouse` (the Lakehouse from the previous lab).
- **Source type** = **Table**, and select `dimension_customer` from **Tables** (not **Files**).
- Preview data to confirm rows load.
- **Destination** = `WideWorldImporters`.
- Set **Table option** to **Auto create table**, schema `dbo`, table name `dimension_customer`.
- Select **Run** > **Save and run**.
- Monitor **Output** until the copy activity completes.

**Explanation:** The pipeline copies a managed Lakehouse Delta table into a Warehouse table. Using the Lakehouse's Tables surface (not Files) means we never need to pin a Parquet path — the Lakehouse SQL endpoint already knows the schema.
**Checkpoint:** `dbo.dimension_customer` exists in `WideWorldImporters` with the five CSV columns (`CustomerKey`, `Customer`, `BuyingGroup`, `Category`, `PostalCode`).

#### Step 4: Build the quick customer report

- Open `WideWorldImporters` as a Warehouse.
- From the Warehouse ribbon, select **New semantic model**.
- Name it `WideWorldImporters_model`.
- Select `dimension_customer`.
- Select **Confirm**.
- Return to the workspace item view.
- Open the `WideWorldImporters_model` semantic model.
- Select **Explore this data** > **Auto-create a report**.
- Select **Save**.
- Name the report `Customer Quick Summary`.
- Select **Save**.

**Explanation:** Since Sept 2025, Fabric no longer auto-creates default semantic models — you now create them explicitly.
**Checkpoint:** `Customer Quick Summary` appears in the workspace.

### Module 3: Extending the solution

#### Step 5: Create Warehouse tables

- Open the `WideWorldImporters` Warehouse.
- Select **New SQL query**.
- Paste and run the table creation script.
- Rename the query `Create Tables`.
- Refresh the object explorer.

```sql
-- Drop and recreate dimension_city aligned with the Lakehouse CSV.
DROP TABLE IF EXISTS [dbo].[dimension_city];

CREATE TABLE [dbo].[dimension_city] (
    [CityKey]        INT          NULL,
    [City]           VARCHAR(200) NULL,
    [StateProvince]  VARCHAR(100) NULL,
    [Country]        VARCHAR(100) NULL,
    [SalesTerritory] VARCHAR(100) NULL
);

-- Drop and recreate fact_sale aligned with the Lakehouse CSV.
DROP TABLE IF EXISTS [dbo].[fact_sale];

CREATE TABLE [dbo].[fact_sale] (
    [SaleKey]              BIGINT        NULL,
    [CityKey]              INT           NULL,
    [CustomerKey]          INT           NULL,
    [SalespersonKey]       INT           NULL,
    [InvoiceDateKey]       DATE          NULL,
    [Quantity]             INT           NULL,
    [UnitPrice]            DECIMAL(18,2) NULL,
    [TaxAmount]            DECIMAL(18,2) NULL,
    [TotalExcludingTax]    DECIMAL(18,2) NULL,
    [TotalIncludingTax]    DECIMAL(18,2) NULL,
    [Profit]               DECIMAL(18,2) NULL
);
```

**Explanation:** The schemas mirror the CSVs loaded in the Lakehouse lab. Keeping the Warehouse and Lakehouse columns identical means Step 6 can `INSERT ... SELECT` straight across without column mapping.
**Checkpoint:** `fact_sale`, `dimension_city`, and the saved `Create Tables` query appear in Object explorer.

#### Step 6: Load `dimension_city` and `fact_sale` from the Lakehouse

Two paths — pick one.

**Option A (recommended): cross-database `INSERT ... SELECT`.** Fabric Warehouse can query the Lakehouse SQL endpoint directly in the same workspace. One SQL script, no pipeline.

```sql
INSERT INTO [dbo].[dimension_city]
SELECT CityKey, City, StateProvince, Country, SalesTerritory
FROM [wwilakehouse].[dbo].[dimension_city];

INSERT INTO [dbo].[fact_sale]
SELECT SaleKey, CityKey, CustomerKey, SalespersonKey,
       InvoiceDateKey, Quantity, UnitPrice, TaxAmount,
       TotalExcludingTax, TotalIncludingTax, Profit
FROM [wwilakehouse].[dbo].[fact_sale];
```

**Option B: Copy pipeline from Lakehouse Tables.** Useful if the Lakehouse lives in a different workspace or the learner wants to practise pipelines.

- Create a data pipeline named `Copy data to dimension_city and fact_sale`.
- Add a **Copy data** activity, source = `wwilakehouse`, source type = **Table**, select `dimension_city`.
- Destination = `WideWorldImporters`, load to existing table `dbo.dimension_city`.
- Add a second Copy activity for `fact_sale` with the same pattern.
- Keep **Enable staging** checked. Clear **Start data transfer immediately**.
- Run the pipeline and monitor completion.

**Explanation:** Both paths reuse the Lakehouse Delta tables you already loaded — no Parquet download, no file-path pinning, no column reshaping. Option A is one script; Option B shows the no-code pipeline pattern.
**Checkpoint:** `dbo.dimension_city` and `dbo.fact_sale` return non-zero `SELECT COUNT(*)`.

#### Step 7: Create the aggregate stored procedure

- Select **Home** > **New SQL query**.
- Paste and run the procedure script.
- Rename the query `Create Aggregate Procedure`.
- Refresh Object explorer.

```sql
--Drop the stored procedure if it already exists.

DROP PROCEDURE IF EXISTS [dbo].[populate_aggregate_sale_by_city] GO --Create the populate_aggregate_sale_by_city stored procedure.

CREATE PROCEDURE [dbo].[populate_aggregate_sale_by_city] AS BEGIN --If the aggregate table already exists, drop it. Then create the table.

DROP TABLE IF EXISTS [dbo].[aggregate_sale_by_date_city];

CREATE TABLE [dbo].[aggregate_sale_by_date_city] ( [Date] [DATETIME2](6), [City] [VARCHAR](8000), [StateProvince] [VARCHAR](8000), [SalesTerritory] [VARCHAR](8000), [SumOfTotalExcludingTax] [DECIMAL](38,2), [SumOfTaxAmount] [DECIMAL](38,6), [SumOfTotalIncludingTax] [DECIMAL](38,6), [SumOfProfit] [DECIMAL](38,2)

);

--Reload the aggregated dataset to the table.

INSERT INTO [dbo].[aggregate_sale_by_date_city] SELECT FS.[InvoiceDateKey] AS [Date], DC.[City], DC.[StateProvince], DC.[SalesTerritory], SUM(FS.[TotalExcludingTax]) AS [SumOfTotalExcludingTax],          SUM(FS.[TaxAmount]) AS [SumOfTaxAmount], SUM(FS.[TotalIncludingTax]) AS [SumOfTotalIncludingTax], SUM(FS.[Profit]) AS [SumOfProfit] FROM [dbo].[fact_sale] AS FS INNER JOIN [dbo].[dimension_city] AS DC ON FS.[CityKey] = DC.[CityKey] GROUP BY FS.[InvoiceDateKey],         DC.[City], DC.[StateProvince], DC.[SalesTerritory] ORDER BY FS.[InvoiceDateKey], DC.[StateProvince], DC.[City];

END
```

**Explanation:** The stored procedure recreates a reporting aggregate from `fact_sale` and `dimension_city` whenever it runs.
**Checkpoint:** `populate_aggregate_sale_by_city` appears under `dbo` stored procedures.

#### Step 8: Run the aggregate stored procedure

- Select **Home** > **New SQL query**.
- Paste the execution command.
- Rename the query `Run Create Aggregate Procedure`.
- Select **Run**.
- Refresh Object explorer after 2-3 minutes.
- Preview the aggregate table.

```sql
--Execute the stored procedure to create the aggregate table.

EXEC [dbo].[populate_aggregate_sale_by_city];
```

**Explanation:** Running the procedure materializes the aggregate table used by later report exploration.
**Checkpoint:** `aggregate_sale_by_date_city` is available and returns preview rows.

#### Step 9: Use the visual query builder

- Select **Home** > **New visual query**.
- Drag `fact_sale` to the design pane.
- Select **Reduce rows** > **Keep top rows**.
- Enter `10,000` and select **OK**.
- Drag `dimension_city` to the design pane.
- Select **Combine** > **Merge queries as new**.
- Set left table to `dimension_city`.
- Set right table to `fact_sale`.
- Select `CityKey` in both tables.
- Set **Join kind** to **Inner**.
- Select **OK**.
- Expand `fact_sale`.
- Select `TaxAmount`, `Profit`, and `TotalIncludingTax`.
- Select **Transform** > **Group by**.
- Change to **Advanced**.
- Group by `Country`, `StateProvince`, and `City`.
- Add `SumOfTaxAmount`, `SumOfProfit`, and `SumOfTotalIncludingTax` as Sum aggregations.
- Rename the query `Sales Summary`.

**Explanation:** The visual query builder lets learners create joins, filters, and aggregates without typing SQL.
**Checkpoint:** The `Sales Summary` visual query shows sales totals by geography.

#### Step 10: Build the Warehouse report

- From the Warehouse ribbon, select **New semantic model**.
- Name it `WideWorldImporters_sales_model`.
- Select `dimension_city` and `fact_sale`.
- Select **Confirm**.
- Open **Model** view.
- Drag `fact_sale.CityKey` to `dimension_city.CityKey`.
- Set **Cardinality** to **Many to one (*:1)**.
- Set **Cross filter direction** to **Single**.
- Leave **Make this relationship active** checked.
- Check **Assume referential integrity**.
- Select **Confirm**.
- Select **Home** > **New report**.
- Add a column chart with `fact_sales.Profit` and `dimension_city.SalesTerritory`.
- Add an Azure Map with `dimension_city.StateProvince` as **Location** and `fact_sale.Profit` as **Size**.
- Add a table with `SalesTerritory`, `StateProvince`, `Profit`, and `TotalExcludingTax`.
- Select **File** > **Save**.
- Name the report `Sales Analysis`.
- Select **Save**.

**Explanation:** Since Sept 2025, Fabric no longer auto-creates default semantic models — you now create them explicitly. The relationship lets report visuals combine fact and dimension fields correctly.
**Checkpoint:** `Sales Analysis` is saved in the workspace.

#### Step 11: Query historical Warehouse versions

- Open a new SQL query.
- Check the current `PostalCode` for `CustomerKey = 234`.
- Update the same row twice.
- Run `SELECT CURRENT_TIMESTAMP;` and copy the returned value.
- Query earlier states with `OPTION (FOR TIMESTAMP AS OF ...)`, using an AS OF timestamp about 2 minutes before that value.

```sql
SELECT * FROM [dbo].[dimension_customer] where CustomerKey =  234;

update [dbo].[dimension_customer] set PostalCode = 75252 where CustomerKey =  234;

update [dbo].[dimension_customer] set PostalCode = 76227 where CustomerKey =  234;

SELECT CURRENT_TIMESTAMP;

-- Replace the timestamp below with a value about 2 minutes before the value returned above.
SELECT CustomerKey, PostalCode FROM [dbo].[dimension_customer] where CustomerKey =  234 OPTION (FOR TIMESTAMP AS OF '<captured timestamp minus about 2 minutes>');
```

**Explanation:** Time travel lets you query prior table versions within the Warehouse retention window.
**Checkpoint:** The `PostalCode` value changes depending on the timestamp selected.

#### Step 12: Clone `dimension_customer`

- Right-click `dimension_customer` in **Explorer**.
- Select **Clone table**.
- Review the populated source schema and table name.
- Keep **Table state** as current, or choose a past point in time.
- Choose the destination schema.
- Edit the destination table name if needed.
- Expand **SQL statement** to review the generated T-SQL.
- Select **Clone**.

**Explanation:** A zero-copy clone creates new table metadata that references the same OneLake data files, so it is fast and storage-efficient.
**Checkpoint:** The cloned table appears in Object explorer.

### Module 4: Clean up resources

#### Step 13: Delete the workspace

- Return to the `Data Warehouse Tutorial` workspace item view.
- Select **Workspace settings**.
- Select **Other** > **Delete this workspace**.
- Select **Delete** on the warning.

**Explanation:** Removing the workspace deletes the Warehouse, pipelines, semantic models, and reports created for the lab.
**Checkpoint:** The workspace is no longer listed.
