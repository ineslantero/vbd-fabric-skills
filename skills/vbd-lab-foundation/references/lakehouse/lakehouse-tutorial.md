# Fabric Foundation VBD - Lakehouse Lab Tutorial

> Converted from `Lakehouse Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs) and restructured for the CSV-first flow used by `/vbd-lab-foundation`.
>
> Screenshots have been stripped; Microsoft Learn URLs are cited inline throughout.

> **Freshness-verified 2026-10-01** — Cross-checked against Microsoft Learn. Fixes applied per `.vbd/freshness-audit-2026-09-15.md`. Preview features are called out inline where relevant.

## Contents

- Introduction
- Module 1: Getting Started
  - Create a Fabric workspace
- Module 2: Build your first Lakehouse in Fabric
  - Create a lakehouse
  - Upload the CSV dataset to Files
  - Ingest `dimension_customer.csv` with Dataflow Gen2
- Module 3: Load, Transform, Analyze
  - Load CSVs as Delta tables (notebook)
  - Transform into business aggregates (notebook)
  - Query via SQL analytics endpoint
  - Build the semantic model with insight-driving DAX
  - Build the Power BI report
- Module 4: Clean up resources

## Objective

- Create a Fabric workspace for the lab assets.
- Build the `wwilakehouse` Lakehouse.
- Bulk upload the sample CSVs to the Lakehouse Files area.
- Ingest `dimension_customer.csv` through a low-code Dataflow Gen2.
- Load the remaining CSVs as Delta tables with a notebook.
- Transform raw tables into business aggregates with a second notebook.
- Create an explicit Power BI semantic model with two DAX measures that surface new insight.
- Build and save a Direct Lake report that uses those measures.

## Microsoft Learn references

- https://learn.microsoft.com/fabric/get-started/microsoft-fabric-overview
- https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview
- https://learn.microsoft.com/fabric/data-engineering/load-data-lakehouse
- https://learn.microsoft.com/fabric/data-factory/tutorial-end-to-end-introduction
- https://learn.microsoft.com/fabric/data-factory/dataflow-gen2-data-destinations-and-managed-settings
- https://learn.microsoft.com/fabric/data-engineering/lakehouse-notebook-load-data
- https://learn.microsoft.com/fabric/data-engineering/lakehouse-and-delta-tables
- https://learn.microsoft.com/fabric/data-warehouse/data-warehousing
- https://learn.microsoft.com/fabric/direct-lake/overview
- https://learn.microsoft.com/dax/time-intelligence-functions-dax

## Sample data

The lab ships with five CSV files under `data/` at the repo root. For WWI-shaped data these are:

- `fact_sale.csv` — invoice-line facts; fields: `SaleKey`, `CityKey`, `CustomerKey`, `StockItemKey`, `SalespersonKey`, `InvoiceDateKey`, `Quantity`, `UnitPrice`, `TaxAmount`, `TotalExcludingTax`, `TotalIncludingTax`, `Profit`.
- `dimension_customer.csv` — fields: `CustomerKey`, `Customer`, `BuyingGroup`, `Category`, `PostalCode`.
- `dimension_city.csv` — fields: `CityKey`, `City`, `StateProvince`, `Country`, `SalesTerritory`.
- `dimension_employee.csv` — fields: `EmployeeKey`, `Employee`, `PreferredName`, `IsSalesperson`.
- `dimension_date.csv` — fields: `Date`, `CalendarYear`, `CalendarMonthNumber`, `CalendarMonthLabel`, `Day`, `ShortMonth`, `FiscalMonthNumber`.

> `/vbd-lab-foundation` re-skins these entity names for the customer (e.g. `fact_sale` → `fact_claim`, `dimension_customer` → `dimension_member`). Keep the shape; swap the vocabulary.

## Modules

### Module 1: Getting Started

#### Step 1: Create a Fabric workspace

- Sign in to Microsoft Fabric at https://app.fabric.microsoft.com/.
- Select **Workspaces** > **New workspace**.
- Name the workspace `Fabric Lakehouse Tutorial` plus a unique suffix.
- Expand **Advanced**.
- Under **License mode**, select **Trial** or **Fabric capacity** and pick a capacity you can access.
- Select **Apply**.

**Explanation:** The workspace will contain the Lakehouse, dataflow, notebooks, semantic model and report for the lab.
**Checkpoint:** The workspace opens and appears in the Workspaces list.

### Module 2: Build your first Lakehouse in Fabric

#### Step 2: Create a lakehouse

- Open the workspace.
- Select **New item** > **Lakehouse** under **Store data**.
- Enter `wwilakehouse` as the name.
- Keep **Lakehouse schemas** checked (default). Tables will be created under the `dbo` schema.
- Select **Create**.

**Explanation:** `wwilakehouse` is the central OneLake item for raw files, Delta tables, notebooks, SQL endpoint queries and Direct Lake reporting.
**Checkpoint:** The `wwilakehouse` item opens in the Lakehouse experience.

#### Step 3: Upload the CSV dataset to Files

- In `wwilakehouse`, right-click **Files** > **Upload** > **Upload files**.
- Select **all CSVs except `dimension_customer.csv`** from the lab `data/` folder:
  - `fact_sale.csv`
  - `dimension_city.csv`
  - `dimension_employee.csv`
  - `dimension_date.csv`
- Confirm the upload.
- Refresh the Lakehouse explorer.

**Explanation:** `Files/` is the unmanaged OneLake area for raw drops. Bulk upload is the fastest path for a one-off migration dump and mirrors the typical "lift-and-shift" starting point. `dimension_customer.csv` is deliberately held back so that Step 4 can show the low-code Dataflow path.
**Checkpoint:** All four CSVs appear directly under `Files/` in the Lakehouse explorer.

#### Step 4: Ingest `dimension_customer.csv` with Dataflow Gen2

- In `wwilakehouse`, select **Get data** > **New Dataflow Gen2**.
- Select **Import from a Text/CSV file**.
- Choose **Upload file**, upload `dimension_customer.csv`, select **Next**, then **Create**.
- Select **Use first row as headers**.
- Rename the query `dimension_customer`.
- Open the **Data destination** settings.
- Select `wwilakehouse` as the destination Lakehouse.
- Create or select the table `dimension_customer`.
- Turn off **Use automatic settings**.
- Select **Replace** and **Dynamic schema**.
- Select **Save settings**.
- Select **Publish**.
- Rename the dataflow `Load dimension_customer` from **Properties**.
- Select **Refresh now**.

**Explanation:** Dataflow Gen2 is the low-code route from CSV to a managed Lakehouse table — the path analysts reach for when they do not want to write code. Doing it for one dimension here makes the trade-off versus the notebook load (next step) explicit.
**Checkpoint:** The `dimension_customer` table appears under **Tables** in `wwilakehouse` after refresh.

### Module 3: Load, Transform, Analyze

#### Step 5: Load the uploaded CSVs as Delta tables (notebook)

- Download `01 - Create Delta Tables.ipynb` from the lab **Scripts** folder.
- Select **Import notebook** > **Upload**, then open `01 - Create Delta Tables`.
- Confirm `wwilakehouse` is the attached Lakehouse.
- Run all cells.

The notebook loops through the four CSVs in `Files/` and writes each as a managed Delta table under `Tables/`:

```python
from pyspark.sql.functions import col, year, month, quarter

csvs = {
    "fact_sale":         "Files/fact_sale.csv",
    "dimension_city":    "Files/dimension_city.csv",
    "dimension_employee":"Files/dimension_employee.csv",
    "dimension_date":    "Files/dimension_date.csv",
}

for table, path in csvs.items():
    df = (spark.read
            .option("header", "true")
            .option("inferSchema", "true")
            .csv(path))
    if table == "fact_sale":
        df = (df
              .withColumn("Year",    year(col("InvoiceDateKey")))
              .withColumn("Quarter", quarter(col("InvoiceDateKey")))
              .withColumn("Month",   month(col("InvoiceDateKey"))))
        (df.write.mode("overwrite")
           .format("delta")
           .partitionBy("Year", "Quarter")
           .saveAsTable(table))
    else:
        (df.write.mode("overwrite")
           .format("delta")
           .saveAsTable(table))
```

**Explanation:** `Files/` was the landing zone; `Tables/` is the managed Delta tier. Partitioning `fact_sale` by `Year`/`Quarter` keeps later aggregates and Power BI queries efficient. The dimensions do not need partitioning.
**Checkpoint:** `fact_sale`, `dimension_city`, `dimension_employee`, `dimension_date` and `dimension_customer` (from Step 4) all appear under **Tables**.

#### Step 6: Transform into business aggregates (notebook)

- Download `02 - Data Transformation - Business.ipynb`.
- Import, open, and run it.

The notebook produces two aggregates — one via PySpark, one via Spark SQL — so SQL-first and Python-first attendees see the same outcome through their preferred lens:

```python
df_fact      = spark.read.table("wwilakehouse.fact_sale")
df_date      = spark.read.table("wwilakehouse.dimension_date")
df_city      = spark.read.table("wwilakehouse.dimension_city")

sale_by_date_city = (df_fact.alias("sale")
    .join(df_date.alias("date"), df_fact.InvoiceDateKey == df_date.Date)
    .join(df_city.alias("city"), df_fact.CityKey == df_city.CityKey)
    .groupBy("date.Date", "date.CalendarMonthLabel", "date.CalendarYear",
             "city.City", "city.StateProvince", "city.SalesTerritory")
    .sum("TotalExcludingTax", "TaxAmount", "TotalIncludingTax", "Profit")
    .withColumnRenamed("sum(TotalExcludingTax)",  "SumOfTotalExcludingTax")
    .withColumnRenamed("sum(TaxAmount)",          "SumOfTaxAmount")
    .withColumnRenamed("sum(TotalIncludingTax)",  "SumOfTotalIncludingTax")
    .withColumnRenamed("sum(Profit)",             "SumOfProfit"))

(sale_by_date_city.write.mode("overwrite").format("delta")
    .option("overwriteSchema", "true")
    .saveAsTable("aggregate_sale_by_date_city"))
```

```sql
%%sql
CREATE OR REPLACE TABLE wwilakehouse.aggregate_sale_by_date_employee
USING DELTA AS
SELECT DD.Date, DD.CalendarMonthLabel, DD.CalendarYear,
       DE.PreferredName, DE.Employee,
       SUM(FS.TotalExcludingTax) AS SumOfTotalExcludingTax,
       SUM(FS.TaxAmount)         AS SumOfTaxAmount,
       SUM(FS.TotalIncludingTax) AS SumOfTotalIncludingTax,
       SUM(FS.Profit)            AS SumOfProfit
FROM wwilakehouse.fact_sale FS
JOIN wwilakehouse.dimension_date     DD ON FS.InvoiceDateKey  = DD.Date
JOIN wwilakehouse.dimension_employee DE ON FS.SalespersonKey  = DE.EmployeeKey
GROUP BY DD.Date, DD.CalendarMonthLabel, DD.CalendarYear, DE.PreferredName, DE.Employee;
```

**Explanation:** The aggregates are curated gold tables — materialised joins and `GROUP BY`s that reporting will hit directly. Doing this once in the Lakehouse keeps Power BI responsive and avoids re-computing joins per visual.
**Checkpoint:** `aggregate_sale_by_date_city` and `aggregate_sale_by_date_employee` both appear under **Tables**.

#### Step 7: Query via the SQL analytics endpoint

- From the Lakehouse, top-right dropdown > **SQL analytics endpoint**.
- Select **New SQL query**.
- Run:

```sql
SELECT TOP 10 City, StateProvince, SUM(SumOfProfit) AS Profit
FROM aggregate_sale_by_date_city
GROUP BY City, StateProvince
ORDER BY Profit DESC;
```

**Explanation:** The SQL endpoint exposes Lakehouse tables as T-SQL — a quick way for SQL-first users to validate the gold layer before touching Power BI.
**Checkpoint:** The query returns the top 10 cities by profit.

#### Step 8: Build the semantic model with insight-driving DAX

- From the Lakehouse ribbon, select **New Power BI semantic model**.
- Name it `wwilakehouse_reporting_model`.
- Select every table.
- Select **Confirm**.
- Open the **Model** view.
- Add these relationships (Many-to-one, Single filter, Assume referential integrity):
  - `fact_sale.CityKey`      → `dimension_city.CityKey`
  - `fact_sale.CustomerKey`  → `dimension_customer.CustomerKey`
  - `fact_sale.SalespersonKey` → `dimension_employee.EmployeeKey`
  - `fact_sale.InvoiceDateKey` → `dimension_date.Date`
- Mark `dimension_date` as a date table (`Date` column).
- Add the two DAX measures below under the `fact_sale` table.

```DAX
// Measure 1 — Rolling 3-Month Profit
//
// Shows a 3-month trailing profit per date context. Smooths monthly spikes and
// highlights trend rather than noise. Uses the standard DATESINPERIOD time
// intelligence pattern and depends on `dimension_date` being a marked date table.

Profit 3M Rolling =
VAR CurrentDate = MAX ( dimension_date[Date] )
VAR Window =
    DATESINPERIOD ( dimension_date[Date], CurrentDate, -3, MONTH )
RETURN
    CALCULATE ( SUM ( fact_sale[Profit] ), Window )
```

```DAX
// Measure 2 — Profit YoY %
//
// Profit growth versus the same period last year, as a percentage. Surfaces
// genuine performance change rather than absolute dollars and makes the matrix
// visual readable across territories of very different size.

Profit YoY % =
VAR CurrentProfit  = SUM ( fact_sale[Profit] )
VAR PriorProfit    =
    CALCULATE (
        SUM ( fact_sale[Profit] ),
        SAMEPERIODLASTYEAR ( dimension_date[Date] )
    )
RETURN
    DIVIDE ( CurrentProfit - PriorProfit, PriorProfit )
```

- Set `Profit 3M Rolling` format to currency, 0 decimals.
- Set `Profit YoY %` format to percentage, 1 decimal.
- Save the model.

**Explanation:** Since Sept 2025 Fabric no longer auto-creates default semantic models — you create them explicitly. The two measures above are what make the model worth building: a plain `SUM(Profit)` tells you nothing new; a 3-month rolling trend and a YoY delta tell the story every reader actually wants.
**Checkpoint:** Both measures appear in the fields list on the `fact_sale` table and return values in a quick card test.

#### Step 9: Build the Power BI report

- Open `wwilakehouse_reporting_model` > **Explore this data** or **New report**.
- Add a text box titled `WW Importers Profit Reporting` (size 20, upper-left).
- Add a card showing `Profit YoY %`.
- Add a line chart with `dimension_date[CalendarMonthLabel]` on the axis and both `fact_sale[Profit]` and `Profit 3M Rolling` as values — the gap between the two tells the story at a glance.
- Add a matrix: rows `dimension_city[SalesTerritory]`, columns `dimension_date[CalendarYear]`, values `Profit YoY %`. Apply conditional formatting (red → white → green) on the YoY measure.
- Add a stacked column chart with `fact_sale[Profit]` by `dimension_employee[Employee]`.
- Select **File** > **Save**, name the report `Profit Reporting`.

**Explanation:** The report is Direct Lake — Power BI analyses the Delta tables in OneLake directly, without import. The two DAX measures do the analytical work; the visuals are deliberately simple.
**Checkpoint:** The `Profit Reporting` report is saved in the workspace and the YoY matrix shows a clear red/green pattern.

### Module 4: Clean up resources

#### Step 10: Delete the workspace

- Return to the workspace item view.
- Select **Workspace settings** > **Other** > **Delete this workspace**.
- Select **Delete** on the warning.

**Explanation:** Removing the workspace clears the Lakehouse, dataflow, notebooks, semantic model and report in one action.
**Checkpoint:** The workspace no longer appears in the Workspaces list.
