# Fabric Foundation VBD - Data Warehouse Lab Tutorial

> Converted from `Fabric Data Warehouse Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs).
> Screenshots have been stripped; Microsoft Learn URLs are cited inline throughout.

> **Freshness-verified 2026-09-15** — Cross-checked against Microsoft Learn. Fixes applied per `.vbd/freshness-audit-2026-09-15.md`. Preview features are called out inline where relevant.

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
- Load `dimension_customer` from `wwilakehouse`.
- Create `dimension_city` and `fact_sale` tables with T-SQL.
- Load Parquet data into Warehouse tables with a pipeline.
- Transform sales data with a stored procedure.
- Explore data with the visual query builder.
- Build a Power BI report and test Warehouse time travel and clone features.

## Microsoft Learn references

- https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehousing
- https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview
- https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-introduction
- https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16
- https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16
- https://app.fabric.microsoft.com/
- https://powerbi.com/
- https://powerbi.com/
- https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehousing
- https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-introduction

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

#### Step 3: Load `dimension_customer`

- Return to the workspace item view.
- Select **New item** > **Data pipeline**.
- Name the pipeline `Load Customer Data`.
- Select **Create**.
- Select **Pipeline activity**.
- Add **Copy data**.
- Set the activity name to `CD Load dimension_customer`.
- On **Source**, select **More** under **Connection**.
- Search for `wwilakehouse` and select the Lakehouse you created in the Lakehouse tutorial.
- Set **File path - Directory** to `/wwi-raw-data/WideWorldImportersDW/tables`.
- Set **File path - File name** to `dimension_customer.parquet`.
- Set **File format** to **Parquet**.
- Select **Preview data**.
- On **Destination**, select `WideWorldImporters`.
- Set **Table option** to **Auto create table**.
- Set schema to `dbo`.
- Set table name to `dimension_customer`.
- Select **Run** > **Save and run**.
- Monitor **Output** until the copy activity completes.

**Explanation:** The pipeline copies a Lakehouse Parquet file into a Warehouse table so SQL and Power BI can use it directly.
**Checkpoint:** `dbo.dimension_customer` exists in `WideWorldImporters`.

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
/* -

1. Drop the dimension_city table if it already exists.
2. Create the dimension_city table.
3. Drop the fact_sale table if it already exists.
4. Create the fact_sale table.

*/ --dimension_city DROP TABLE IF EXISTS [dbo].[dimension_city];

CREATE TABLE [dbo].[dimension_city] ( [CityKey] [int] NULL, [WWICityID] [int] NULL, [City] [varchar](8000) NULL, [StateProvince] [varchar](8000) NULL, [Country] [varchar](8000) NULL, [Continent] [varchar](8000) NULL, [SalesTerritory] [varchar](8000) NULL, [Region] [varchar](8000) NULL, [Subregion] [varchar](8000) NULL, [Location] [varchar](8000) NULL, [LatestRecordedPopulation] [bigint] NULL, [ValidFrom] [datetime2](6) NULL, [ValidTo] [datetime2](6) NULL, [LineageKey] [int] NULL );

--fact_sale DROP TABLE IF EXISTS [dbo].[fact_sale];

CREATE TABLE [dbo].[fact_sale] ( [SaleKey] [bigint] NULL, [CityKey] [int] NULL, [CustomerKey] [int] NULL, [BillToCustomerKey] [int] NULL, [StockItemKey] [int] NULL, [InvoiceDateKey] [datetime2](6) NULL, [DeliveryDateKey] [datetime2](6) NULL, [SalespersonKey] [int] NULL, [WWIInvoiceID] [int] NULL, [Description] [varchar](8000) NULL, [Package] [varchar](8000) NULL, [Quantity] [int] NULL, [UnitPrice] [decimal](18, 2) NULL, [TaxRate] [decimal](18, 3) NULL, [TotalExcludingTax] [decimal](29, 2) NULL, [TaxAmount] [decimal](38, 6) NULL, [Profit] [decimal](18, 2) NULL, [TotalIncludingTax] [decimal](38, 6) NULL, [TotalDryItems] [int] NULL, [TotalChillerItems] [int] NULL, [LineageKey] [int] NULL, [Month] [int] NULL, [Year] [int] NULL, [Quarter] [int] NULL );
```

**Explanation:** The script defines the two remaining tables needed for sales analysis: one dimension and one fact table.
**Checkpoint:** `fact_sale`, `dimension_city`, and the saved `Create Tables` query appear in Object explorer.

#### Step 6: Load `dimension_city` and `fact_sale`

- Create a new data pipeline.
- Name it `Copy data to dimension city and fact sale`.
- Open **Copy assistant**.
- Select `wwilakehouse` as the Lakehouse source.
- Browse to `OneLake -> wwilakehouse -> files section -> /wwi-raw-data/WideWorldImportersDW/tables`.
- Select `dimension_city.parquet`.
- Choose `WideWorldImporters` as the destination Warehouse.
- Load to existing table `dbo.dimension_city`.
- Keep **Enable staging** checked.
- Clear **Start data transfer immediately**.
- Rename the activity `Copy dimension city`.
- Add another copy activity with **Use copy assistant**.
- Select `wwilakehouse` as the source.
- Select `fact_sale.parquet`.
- Choose `WideWorldImporters` as the destination.
- Load to existing table `dbo.fact_sale`.
- Delete mappings for `Month`, `Year`, and `Quarter`.
- Keep **Enable staging** checked.
- Clear **Start data transfer immediately**.
- Rename the activity `Copy Fact Sale`.
- Run the pipeline.
- Monitor completion.

**Explanation:** The two copy activities populate the Warehouse schema from the Lakehouse files. The mapping cleanup prevents target-only date part columns from blocking the load.
**Checkpoint:** `dbo.dimension_city` and `dbo.fact_sale` contain rows.

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
