# Fabric Foundation VBD - Lakehouse Lab Tutorial

> Converted from `Lakehouse Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs).
> Screenshots have been stripped; refer to `sources.yaml` in this folder for the Microsoft Learn URLs cited throughout.

## Contents

- Introduction

- Module 1: Getting Started

- Create a Fabric workspace

- Module 2: Build your first Lakehouse in Fabric

- Create a lakehouse

- Data Ingestion

- Building a report

- Module 3: Ingest, Prep and Analyze

- Data Ingestion

- Data Preparation

- Building a report

- Module 4: Clean up resources

## Objective

- Create a Fabric workspace for the lab assets.
- Build the `wwilakehouse` Lakehouse.
- Ingest `dimension_customer.csv` with Dataflow Gen2.
- Load the Wide World Importers sample files into OneLake.
- Transform raw Parquet files into Delta tables.
- Create aggregate tables with PySpark and Spark SQL.
- Add Lakehouse tables to the default semantic model.
- Build and save a Power BI report from DirectLake data.

## Microsoft Learn references

- https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview
- https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16
- https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16
- https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16
- https://app.fabric.microsoft.com/
- https://powerbi.com/
- https://assetsprod.microsoft.com/en-us/wwi-sample-dataset.zip
- https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/optimize-write-for-apache-spark

## Modules

### Module 1: Getting Started

#### Step 1: Create a Fabric workspace

- Sign in to Microsoft Fabric at https://app.fabric.microsoft.com/.
- Select **Workspaces** > **New workspace**.
- Name the workspace `Fabric Lakehouse Tutorial` plus a unique suffix.
- Optionally add a description.
- Expand **Advanced**.
- Select **Trial**, **Fabric capacity**, or **Power BI Premium capacity** as available.
- Select **Apply**.

**Explanation:** The workspace contains the lakehouse, dataflows, pipelines, notebooks, semantic models, and reports for the lab.
**Checkpoint:** The workspace opens and appears in the Workspaces list.

### Module 2: Build your first Lakehouse in Fabric

#### Step 2: Create a lakehouse

- Open the `Fabric Lakehouse Tutorial` workspace from https://powerbi.com/.
- Select **New item**.
- Select **Lakehouse** under **Store data**.
- Enter `wwilakehouse` as the name.
- Leave **Lakehouse schemas** unchecked if the option appears.
- Select **Create**.

**Explanation:** `wwilakehouse` is the central OneLake item for raw files, Delta tables, notebook work, SQL endpoint queries, and DirectLake reporting.
**Checkpoint:** The new `wwilakehouse` item opens in the Lakehouse experience.

#### Step 3: Ingest `dimension_customer.csv` with Dataflow Gen2

- Download `dimension_customer.csv` from the lab **Data** folder.
- In `wwilakehouse`, select **Get data** > **New Dataflow Gen2**.
- Select **Import from a Text/CSV file**.
- If upload works, choose **Upload file**, upload `dimension_customer.csv`, select **Next**, then select **Create**.
- If upload is unavailable, cancel the wizard, upload the file to the Lakehouse **Files** area, reopen the dataflow, select **Get data from another source**, choose the `wwilakehouse` file, then select **Create**.
- Select **Use first row as headers**.
- Rename the query `dimension_customer`.
- Open the **Data destination** settings.
- Select `wwilakehouse` as the destination Lakehouse.
- Create or select the table `dimension_customer`.
- Remove spaces and uppercase characters from the table name if the UI appends them.
- Turn off **Use automatic settings**.
- Select **Replace** and **Dynamic schema**.
- Select **Save settings**.
- Select **Publish**.
- Rename the dataflow `Load Lakehouse Table` from **Properties**.
- Select **Refresh now**.

**Explanation:** Dataflow Gen2 gives a low-code route from CSV to a managed Lakehouse table. The destination settings make refreshes replace the table cleanly during the lab.
**Checkpoint:** The `dimension_customer` table appears under **Tables** in `wwilakehouse` after refresh.

#### Step 4: Query and model `dimension_customer`

- Open `wwilakehouse`.
- Refresh the Lakehouse explorer if the table does not appear.
- Select `dimension_customer` to preview data.
- Switch to **SQL analytics endpoint**.
- Select **New SQL query**.
- Run this query.

```sql
SELECT BuyingGroup, Count(*) AS Total FROM dimension_customer GROUP BY BuyingGroup
```

- Open the **Reporting** tab.
- Select **Manage default semantic model**.
- Add `dimension_customer` to the default semantic model.
- Select **Confirm**.

**Explanation:** The SQL analytics endpoint exposes Lakehouse tables through T-SQL for quick validation. Adding the table to the semantic model makes it available to Power BI.
**Checkpoint:** The query returns totals by `BuyingGroup`, and `dimension_customer` is selected in the semantic model.

#### Step 5: Build the quick customer report

- Return to the workspace item view.
- Open the `wwilakehouse` default semantic model.
- Select **Explore this data** > **Auto-create a report**.
- Review the generated visuals.
- Select **Save**.
- Give the report a clear name.

**Explanation:** Auto-create quickly proves that the Lakehouse table can feed Power BI without building a report by hand.
**Checkpoint:** A saved report based on `dimension_customer` appears in the workspace.

### Module 3: Ingest, Prep and Analyze

#### Step 6: Create the ingestion pipeline

- Return to the `Fabric Lakehouse Tutorial` workspace.
- Select **New item** > **Data pipeline**.
- Name the pipeline `IngestDataFromSourceToLakehouse`.
- Select **Create**.
- Select **Copy Data Assistant**.
- Choose **HTTP** as the source.
- Configure the source URL `https://assetsprod.microsoft.com/en-us/wwi-sample-dataset.zip`.
- Create a connection named `wwisampledata`.
- Set **Data gateway** to **None**.
- Set **Authentication kind** to **Anonymous**.
- Enable **Binary copy**.
- Set **Compression type** to **ZipDeflate (.zip)**.
- Choose the `wwilakehouse` destination from OneLake data hub.
- Set **Root folder** to **Files**.
- Set destination **File format** to **Binary**.
- Select **Save + Run**.
- Monitor the **Output** tab until the activity succeeds.
- Open `wwilakehouse`.
- Refresh the explorer.
- Rename the generated GUID folder to `wwi-raw-data`.

**Explanation:** The pipeline copies the complete Wide World Importers sample once into the Lakehouse **Files** area. Renaming the folder gives the notebooks a stable path.
**Checkpoint:** `Files/wwi-raw-data/WideWorldImportersDW` exists in `wwilakehouse`.

#### Step 7: Import and open the Delta table notebook

- Download the notebooks from the lab **Scripts** folder.
- Switch to the **Data engineering** workload.
- Select **Import notebook**.
- Select **Upload** in the **Import status** pane.
- Upload all downloaded notebooks.
- Return to the workspace item view.
- Open `wwilakehouse`.
- Select **Open notebook** > **Existing notebook**.
- Open `01 - Create Delta Tables`.
- Confirm the notebook is linked to `wwilakehouse` in the explorer.

**Explanation:** The notebook converts raw WWI Parquet files into Delta tables. Fabric Live Pool starts Spark automatically when the first cell runs.
**Checkpoint:** `01 - Create Delta Tables` opens with `wwilakehouse` attached.

#### Step 8: Write `fact_sale` as a partitioned Delta table

- Enable the first notebook cell settings for V-order and Optimize Write.
- Run the cell.
- Run the fact table transformation cell.

```python
from pyspark.sql.functions import col, year, month, quarter table_name = 'fact_sale'

df = spark.read.format("parquet").load('Files/wwi-raw-data/WideWorldImportersDW/parquet/full/fact_sale_1y_full/')

df = df.withColumn('Year', year(col("InvoiceDateKey")))

df = df.withColumn('Quarter', quarter(col("InvoiceDateKey")))

df = df.withColumn('Month', month(col("InvoiceDateKey")))

df.write.mode("overwrite").format("delta").partitionBy("Year","Quarter").save("Tables/" + table_name)
```

**Explanation:** The code reads raw Parquet, adds date parts, and writes `fact_sale` as a Delta table partitioned by `Year` and `Quarter`. Optimize Write helps avoid excessive small files.
**Checkpoint:** The `fact_sale` table appears under **Tables** after refreshing `wwilakehouse`.

#### Step 9: Write the dimension tables as Delta tables

- Run the notebook cell that defines `loadFullDataFromSource`.
- Keep the dimension table list unchanged.
- Refresh `wwilakehouse` after the cell finishes.

```python
from pyspark.sql.types import * def loadFullDataFromSource(table_name):

df = spark.read.format("parquet").load('Files/wwi-raw-data/WideWorldImportersDW/parquet/full/' + table_name)

df = df.select([c for c in df.columns if c != 'Photo'])

df.write.mode("overwrite").format("delta").save("Tables/" + table_name)

full_tables = [ 'dimension_city', 'dimension_date', 'dimension_employee', 'dimension_stock_item'

] for table in full_tables:

loadFullDataFromSource(table)
```

**Explanation:** The helper function applies the same load pattern to each dimension table and drops the unused `Photo` column.
**Checkpoint:** `dimension_city`, `dimension_date`, `dimension_employee`, and `dimension_stock_item` appear under **Tables**.

#### Step 10: Open the business transformation notebook

- Return to the workspace item view.
- Open `wwilakehouse`.
- Select **Open notebook** > **Existing notebook**.
- Open `02 - Data Transformation - Business`.
- Confirm `wwilakehouse` is attached.
- Set the environment to **Workspace default** if a session error appears.
- Select **Run all**.

**Explanation:** This notebook creates curated aggregate tables from the raw Delta tables. It shows both PySpark and Spark SQL paths over the same OneLake data.
**Checkpoint:** The notebook finishes without errors.

#### Step 11: Create `aggregate_sale_by_date_city` with PySpark

- Run the PySpark aggregation cell.

```python
df_fact_sale = spark.read.table("wwilakehouse.fact_sale")

df_dimension_date = spark.read.table("wwilakehouse.dimension_date")

df_dimension_city = spark.read.table("wwilakehouse.dimension_city")

sale_by_date_city = df_fact_sale.alias("sale") \ .join(df_dimension_date.alias("date"), df_fact_sale.InvoiceDateKey == df_dimension_date.Date, "inner") \ .join(df_dimension_city.alias("city"), df_fact_sale.CityKey == df_dimension_city.CityKey, "inner") \ .select("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "city.City", "city.StateProvince", "city.SalesTerritory", "sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")\ .groupBy("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "city.City", "city.StateProvince", "city.SalesTerritory")\ .sum("sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")\ .withColumnRenamed("sum(TotalExcludingTax)", "SumOfTotalExcludingTax")\ .withColumnRenamed("sum(TaxAmount)", "SumOfTaxAmount")\ .withColumnRenamed("sum(TotalIncludingTax)", "SumOfTotalIncludingTax")\ .withColumnRenamed("sum(Profit)", "SumOfProfit")\ .orderBy("date.Date", "city.StateProvince", "city.City")

sale_by_date_city.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/aggregate_sale_by_date_city")
```

**Explanation:** The PySpark path joins fact and dimension tables, groups sales by date and city, and persists a reusable aggregate.
**Checkpoint:** `aggregate_sale_by_date_city` appears under **Tables**.

#### Step 12: Create `aggregate_sale_by_date_employee` with Spark SQL

- Run the Spark SQL aggregation cell.

```sql
%%sql CREATE OR REPLACE TEMPORARY VIEW sale_by_date_employee AS SELECT DD.Date, DD.CalendarMonthLabel , DD.Day, DD.ShortMonth Month, CalendarYear Year ,DE.PreferredName, DE.Employee ,SUM(FS.TotalExcludingTax) SumOfTotalExcludingTax ,SUM(FS.TaxAmount) SumOfTaxAmount ,SUM(FS.TotalIncludingTax) SumOfTotalIncludingTax ,SUM(Profit) SumOfProfit FROM wwilakehouse.fact_sale FS INNER JOIN wwilakehouse.dimension_date DD ON FS.InvoiceDateKey = DD.Date INNER JOIN wwilakehouse.dimension_Employee DE ON FS.SalespersonKey = DE.EmployeeKey GROUP BY DD.Date, DD.CalendarMonthLabel, DD.Day, DD.ShortMonth, DD.CalendarYear, DE.PreferredName, DE.Employee ORDER BY DD.Date ASC, DE.PreferredName ASC, DE.Employee ASC sale_by_date_employee = spark.sql("SELECT * FROM sale_by_date_employee")

sale_by_date_employee.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/aggregate_sale_by_date_employee")
```

**Explanation:** The SQL path creates a temporary view and writes the result back as a Delta table, giving SQL-first users the same outcome as the PySpark path.
**Checkpoint:** `aggregate_sale_by_date_employee` appears under **Tables**.

#### Step 13: Prepare the semantic model

- Open `wwilakehouse`.
- Switch to **SQL analytics endpoint**.
- Refresh if the tables are not visible.
- Open the **Model** view.
- Select **Reporting** > **Manage default semantic model**.
- Select every table.
- Select **Confirm**.
- Drag `fact_sale.CityKey` to `dimension_city.CityKey`.
- Set **Cardinality** to **Many to one (*:1)**.
- Set **Cross filter direction** to **Single**.
- Leave **Make this relationship active** checked.
- Check **Assume referential integrity**.
- Select **Save**.
- Add these relationships:
  - `StockItemKey` from `fact_sale` to `dimension_stock_item`
  - `Salespersonkey` from `fact_sale` to `dimension_employee.EmployeeKey`
  - `CustomerKey` from `fact_sale` to `dimension_customer.CustomerKey`
  - `InvoiceDateKey` from `fact_sale` to `dimension_date.Date`

**Explanation:** Relationships turn separate Lakehouse tables into a model that Power BI can navigate correctly.
**Checkpoint:** The model shows fact-to-dimension relationships for city, stock item, employee, customer, and date.

#### Step 14: Build the Power BI report

- Select **New report**.
- Add a text box titled `WW Importers Profit Reporting`.
- Increase the title font size to 20 and place it in the upper left.
- Add a card from `fact_sales.Profit`.
- Add a clustered bar chart with `fact_sales.Profit` and `dimension_city.SalesTerritory`.
- Add a stacked area chart with `fact_sales.Profit`, `dimension_date.FiscalMonthNumber`, and `dimension_stock_item.BuyingPackage`.
- Add a stacked column chart with `fact_sales.Profit` and `dimension_employee.Employee`.
- Select **File** > **Save**.
- Name the report `Profit Reporting`.
- Select **Save**.

**Explanation:** DirectLake lets Power BI analyze the Lakehouse files directly without importing or duplicating the data.
**Checkpoint:** The `Profit Reporting` report is saved in the workspace.

### Module 4: Clean up resources

#### Step 15: Delete the workspace

- Return to the `Fabric Lakehouse Tutorial <suffix you added to make it unique>` workspace item view.
- Select **Workspace settings**.
- Select **Other** > **Delete this workspace**.
- Select **Delete** on the warning.

**Explanation:** Removing the workspace clears the lab Lakehouse, dataflow, pipeline, notebooks, semantic model, and report in one action.
**Checkpoint:** The workspace no longer appears in the Workspaces list.
