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

# Introduction

### What is Fabric?

Fabric provides a one-stop shop for all the analytical needs for every enterprise. It covers the complete spectrum of services including data movement, data lake, data engineering, data integration and data science, real time analytics, and business intelligence. With Fabric, there is no need to stitch together different services from multiple vendors. Instead, the customer enjoys an end-to-end, highly integrated, single comprehensive product that is easy to understand, onboard, create and operate. There is no other product on the market that offers the breadth, depth, and level of integration that Fabric offers. Additionally, Microsoft Purview is included by default in every tenant to meet compliance and governance needs.

To get an overview of the components and concepts of Fabric read [Fabric - Overview and Concepts](https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview).

### The purpose of this tutorial

While many concepts in Fabric may be familiar to data and analytics professionals it can be challenging to apply those concepts in a new environment. This tutorial has been designed to walk step-by-step through an end-to-end scenario from data acquisition to data consumption to build a basic understanding of the Fabric UX, the various workloads and their integration points, and the Fabric professional and citizen developer experiences.

The tutorials are not intended to be a reference architecture, an exhaustive list of features and functionality, or a recommendation of specific best practices.

### The lakehouse end-to-end scenario

Traditionally, organizations have been building modern data warehouses for their transactional and structured data processing/analytics needs and data lakehouses for big data (semi/unstructured data) processing/analytics needs. These two systems ran in parallel, creating silos, data duplicity and increased total cost of ownership.

Fabric with its unification of data store and standardization on Delta Lake format allows you to eliminate silos, remove data duplicity, and drastically reduce total cost of ownership.

With the flexibility Fabric provides, you can implement either lakehouse or data warehouse architectures or combine these two together to get the best of both the worlds in simple implementation. In this tutorial, you are going to take an example of retail organization and build its lakehouse from start to finish. The same approach can be taken to implement a lakehouse for any organization from any industry.

In this tutorial, you will take on the role of a developer at the fictional Wide World Importers company from retail domain and complete the following steps:

- Sign into your Power BI online account, or if you don’t have an account yet, sign up for a free trial.
- Build and implement an end-to-end lakehouse for your organization:
	- Create a Fabric workspace
	- Quickly create a lakehouse – an optional module to implement medallion architecture (Bronze, Silver, and Gold)
	- Ingest, Transform and load data into the lakehouse – bronze, silver and gold zones as delta lake tables for medallion architecture
	- Explore OneLake, OneCopy of your data across lake mode and warehouse mode
	- Connect to your lakehouse using TDS/SQL endpoint
	- Create Power BI report using DirectLake – to analyze sales data across different dimensions
	- Orchestrate and schedule data ingestion and transformation flow with Pipeline
- Cleanup resources by deleting the workspace and other items

### The lakehouse end-to-end architecture

__Data Sources__– Fabric makes it easy and quick to connect to Azure Data Services, other cloud platforms, and on- premises data sources to ingest data from.

__Ingestion__– With 200\+ native connectors as part of the Fabric pipeline and with drag and drop data transformation with dataflow, you can quickly build insights for your organization. Shortcut is a new feature in Fabric that provides a way to connect to existing data without having to copy or move it.

__Transform and Store__– Fabric standardizes on Delta Lake format, that means all the engines of Fabric can read and work on the same dataset stored in OneLake – no need for data duplicity. This storage allows you to build lakehouses using a medallion architecture or data mesh based on your organizational need. For transformation, you can choose either low-code or no-code experience with pipelines/dataflows or notebook/Spark for a code first experience.

__Consume__– Data from Lakehouse can be consumed by Power BI, industry leading business intelligence tool, for reporting and visualization. Each Lakehouse comes with a built-in TDS/SQL endpoint for easily connecting to and querying data in the Lakehouse tables from other reporting tools, when needed. When a Lakehouse is created a secondary item, called a Warehouse, will be automatically generated at the same time with the same name as the Lakehouse and this Warehouse item provides you with the TDS/SQL endpoint.

### The sample data

For sample data, we are going to use [Wide World Importers (WWI) sample database](https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16). For our lakehouse end-to-end scenario, we have generated sufficient data for a sneak peek into the scale and performance capabilities of the Fabric platform.

Wide World Importers (WWI) is a wholesale novelty goods importer and distributor operating from the San Francisco Bay area. As a wholesaler, WWI's customers are mostly companies who resell to individuals. WWI sells to retail customers across the United States including specialty stores, supermarkets, computing stores, tourist attraction shops, and some individuals. WWI also sells to other wholesalers via a network of agents who promote the products on WWI's behalf. You can learn more about their company profile and operation [here.](https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16)

Typically, you would bring data from transactional systems (or line of business applications) into a lakehouse, however for simplicity of this tutorial, we are going to use the dimensional model provided by WWI as our initial data source. We are going to use it as the source to ingest the data into a lakehouse and transform it through different stages (Bronze, Silver, and Gold) of a medallion architecture.

### The data model

While the WWI dimensional model contains multiple fact tables, for simplicity in explanation we will focus on the Sale Fact table and its related dimensions only, as below, to demonstrate this end-to-end lakehouse scenario:

### End-to-end data and transformation flow

Earlier, we described the [Wide World Importers (WWI) sample data](https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16) which we are going to leverage in building this end to end lakehouse. For this implementation, this sample data is in an Azure Data storage account in Parquet file format for all the tables, however in your real-world implementation data would likely come from varieties of sources and in a variety of formats.

__Data Source__– Source data is in Parquet file format in an un-partitioned structure, stored in a folder for each table. For the purpose of this tutorial, we will set up pipeline to copy/ingest the complete historical or onetime data to the lakehouse.

__Lakehouse__– For this implementation and for the simplicity’s sake, we are going to create one lakehouse, ingest data into Files section of the lakehouse and then create delta lake tables in the Tables section of the lakehouse.

You will find an optional module at the end of this tutorial which covers creating the lakehouse with medallion architecture (Bronze, Silver, and Gold) and talks about its recommended approach.

__Transform__– For data preparation and transformation, we are going to demonstrate the use of Notebooks/Spark for code first users as well as demonstrate Pipelines/Dataflow for low-code/no-code users.

__Consume__– To demonstrate data consumption you will learn how you can use the DirectLake feature of Power BI to create reports/dashboards and directly query data from the lakehouse. Further, to demonstrate how you can make your data available to third party reporting tools, you can use TDS/SQL endpoint to connect to Warehouse and run SQL-based queries for analytics.

# Module 1: Getting Started

Before you can begin building the lakehouse, you will need to create a workspace where you will build out the remainder of the tutorial.

__Imp: You can skip this Module if the workspace has already been setup for you as part of lab setup__

## Create a Fabric workspace

In this step, you create a Fabric workspace. The workspace contains all the items needed for this lakehouse tutorial, which includes lakehouse, dataflows, Data Factory pipelines, the notebooks, Power BI semantic models, and reports.

1. Sign in to [Microsoft fabric](https://app.fabric.microsoft.com/)
2. Select __Workspaces__and__New workspace__.

1. Fill out the __Create a workspace__form as follows:
	1. __Name:__Enter *Fabric Lakehouse Tutorial*, and some characters for uniqueness.
	2. __Description__: Optionally, enter a description for the workspace.

-

	1. __Advanced__: Under__License mode__, select__Trial__capacity. You can also choose__Fabric capacity__with F64 SKU or a Power BI__Premium capacity__ with P1 SKU if you have access to them. These SKUs provide you access to all the Fabric capabilities..

1. Select __Apply.__The workspace will be created and opened.

# Module 2: Build your first Lakehouse in Fabric

The intent of this module is to quickly build end to end journey of building a lakehouse, ingesting data for a table, applying transformation whenever required and then using ingested data into the lakehouse delta table for creating reports.

## Create a lakehouse

1. In the [Fabric](https://powerbi.com/) select __Workspaces__in the left-hand menu.
2. Search for your workspace(__Fabric Lakehouse Tutorial__) by typing in the search textbox at the top and click on your workspace to open it.
3. From the top left of the screen, select New Item.

1. In the __New item__section, select__Lakehouse__located under__Stored Data__to create a lakehouse.

1. Enter __wwilakehouse__in the__Name__box. Please do not check__Lakehouse schemas__ checkbox if its enabled for you

1. Click __Create__. The new lakehouse will be created and automatically opened.

## Data Ingestion

1. Download the ‘dimension_customer.csv’ file found in __Data__ folder. The File will provided you as part of the lab content. Please check with instructor.
2. In the lakehouse Click on Get data menu option  , Click on __New Dataflow Gen2__.

1. On the new dataflow page, click on __Import from a Text/CSV file__.

__*If you encounter problems with file uploads, like lacking a SharePoint Online license or uninitialized OneDrive for Business, skip 4&5 and follow steps 6-9. If upload options is available, proceed to Step 4 & 5 and   ignore steps 6-9*__

1. On the __Connect to data source__wizard, click on__Upload file__radio button and then drag and drop the data file that you downloaded in step 1 of this module.
2. Clicking __Next__Once the file is uploaded, click__Next__on the next screen will open the__Preview file data__page, click on__Create__to proceed and return back to dataflow canvas.

__**__ __*Ignore 6-9 step if you that the upload file option working*__

1. Cancel the “Connect to data source” window without proceeding, Close the dataflow, navigate to the lakehouse within your workspace and choose the “upload file” feature to upload the data file you acquired in the first step of this module.

____

1. After uploading the file, open the dataflow, select the "Get data from another Source" option, and pick the lakehouse established in the previous steps.

1. Open the file section, select the data file from the lakehouse you've uploaded, and click on create.

____

1. Select "__Use the first row as headers__"  from the Home section in the Power Query home tab to set your column headers.

1. In the Name field of the query settings pane, type __dimension_customer__. Then, click on the gear icon in the Data destination field at the bottom of the query settings pane.If the upload file option worked for you the data destination will be automatically selected else No Data destination will be selected, click the plus sign and choose lakehouse.
2. If necessary, on the __Connect to data destination__screen, sign into your account. Click__Next__.
3. Navigate to the __wwilakehouse__in your workspace.
4. If the __dimension_customer __table does not exist, select the__New table__setting and enter the Table name of

__dimension_customer__. If the table already exists, select the__Existing table__setting and select__dimension_customer__from the table list in the object explorer. Select__Next__.

__Note__– UI adds <space>Number at the end of the table name by default. Table names must be lower case and must not contain space. Please name it appropriately and remove any space from the table name.

For initial dataflow creation, turn off "Use automatic settings" in the Destination Settings Tab to select the '__Replace__' update option and__Dynamic schema__in the schema options on publish and Click__Save settings__

15. This will return you to the canvas of the dataflow. You can easily and quickly transform the data based on your business requirements using this nice and intuitive graphical user interface. For the purpose of this module, we will not make any changes here. To proceed, click on __Publish__at bottom right of the screen.

1. A spinning circle next to the dataflow's name indicates publishing is in progress in the item view. When publishing is complete, select the __...__and select__Properties__. Rename the dataflow to__Load Lakehouse Table__and select__Save__.

1. Select the __Refresh now__option next to the data flow name to refresh the dataflow. This option runs the data flow and moves data from the source file to lakehouse table. While it's in progress, you see a spinning circle under__Refreshed__ column in the item view.

1. Once the dataflow’s refresh is completed, you can go to the lakehouse, refresh the explorer view in case you don’t see the table(__refresh it twice in case you see an unidentified folder__) and you will notice__dimension_customer__

1. Select the table to preview its data. You can also use the SQL analytics endpoint of the lakehouse to query the data with SQL statements. Select __SQL analytics endpoint__from the__Lakehouse__ dropdown menu at the top right of the screen.

20. Select the __dimension_customer__table to preview its data or select__New SQL query__ to write your SQL statements.

21. The following sample query aggregates the row count based on the *BuyingGroup* column of the *dimension_customer* table. SQL query files are saved automatically for future reference, and you can rename or delete these files based on your need.

To run the script, click on the __Run__icon at the top of the script file.

SELECT BuyingGroup, Count(\*) AS Total FROM dimension_customer GROUP BY BuyingGroup

22. Previously all the lakehouse tables and views were automatically added to the semantic model. With recent updates, for new Lakehouse's, we must manually add our tables to the semantic model. Open  lakehouse and switch to the __SQL analytics endpoint__ view.

23. From the __Reporting__tab, select__Manage default semantic model__and select the tables that you want to add to the semantic model. In this case, select the__dimension_customer__ table.

## Building a report

1. Click on the workspace name on the left to get to the item  view of the workspace, click on __wwilakehouse__default semantic model, which gets created automatically with the same name of the lakehouse when you create a lakehouse.

1. On the semantic model screen, you can view all the tables. You will have options to create reports either from scratch, paginated report or let Power BI do magic for you by automatically creating a report based on your data. For the purpose of this module, click on __Auto-create a report__under__Explore this data__. In the next module, we will create a report from scratch.

1. Since the table is a dimension and there are no measures in it, Power BI smartly creates a measure for the row sum and aggregates it across different columns and creates different charts as below.

You can save this report for the future by clicking on __Save__button at the top ribbon and giving it a name. You can further make changes to this report to meet your requirement by including or excluding additional tables or columns.

__*Generally, report visuals load quickly. If they are slow or not rendering, save the report with a new name to resolve the issue.*__

# Module 3: Ingest, Prep and Analyze

This module is going to build on the work you completed in the previous module and ingest additional tables (dimensions and fact) of the dimensional model of Wide World Importers (WWI) as mentioned in the Introduction section of this document. Next, you will use notebooks with Spark runtime to transform and prepare the data. Finally, you will create Power BI data model and create a report from scratch.

## Data Ingestion

In this section, you will use __Copy data activity__of__Data Factory pipeline__to ingest sample data from source (Azure storage account) to the__Files__section of the lakehouse you created earlier.

1. Select __Workspaces__in the left navigation pane, and then select your new workspace from the__Workspaces__ menu. The items view of your workspace appears.
2. From the __New item__option in the workspace ribbon, select__Data pipeline__.

3. In the __New pipeline__dialog box, specify the name as__IngestDataFromSourceToLakehouse__and select__Create__. A new data factory pipeline is created and opened.

4. For the __New pipeline__, specify the name as__IngestDataFromSourceToLakehouse__and click on__Create__. This will create a new data factory pipeline and open it on the screen to work on it.

1. Select the Copy Data Assistant

1. Next, set up an HTTP connection to import the sample World Wide Importers data into the Lakehouse. From the list of __New sources__, Type__Http__in the search bar__ __and select it.

1. In the __Connect to data source__window, enter the details from the table below and select__Next__.

__Expand table__ __Property__ __Value__ URL [https://assetsprod.microsoft.com/en-us/wwi-sample-dataset.zip](https://assetsprod.microsoft.com/en-us/wwi-sample-dataset.zip)

Connection Create a new connection Connection name wwisampledata Data gateway None Authentication kind Anonymous

1. In the next step, enable the __Binary copy__and choose__ZipDeflate (.zip)__as the__Compression type__since the source is a .zip file. Keep the other fields at their default values and click__Next__.

1. In the __Connect to data destination__window, choose the lakehouse from OneLake data hub tab and specify the__Root folder__as__Files__and click__Next__. This will write the data to the *Files* section of the lakehouse.

1. Choose the __File format__as__Binary__for the destination. Click__Next__and then__Save\+Run__. You can schedule pipelines to refresh data periodically. In this tutorial, we only run the pipeline once. The data copy process takes approximately 10-15 minutes to complete.

1. You can monitor the pipeline execution and activity in the __Output__tab. You can also view detailed data transfer information by selecting the glasses icon next to the pipeline name, which appears when you hover over the name.__This step may tale 15-30 mins depending on fabric region.__

1. After the successful execution of the pipeline, go to your lakehouse (__wwilakehouse__) and open the explorer to see the imported data.

1. Ensure the folder named WideWorldImportersDW is visible in the Explorer view and includes data for every table. If the files do not appear, please click on the refresh icon located under the home tab.

1. The data is created under the __Files__section of the lakehouse explorer. A new folder with GUID contains all the needed data. Rename the GUID to__wwi-raw-data__

## Data Preparation

Now since we have raw data already ingested from source to the __Files__section of the lakehouse, you can take this data, transform, and prepare it to create delta tables.

1. Download the set of notebooks found in the Scripts folder

1. Click on worklaods located on the eft pane of the screen, select __Data engineering__.
2. Select __Import notebook__from the__New__section at the top of the landing page.

1. Select __Upload__from the__Import status__pane that opens on the right side of the screen.
2. Select all the notebooks that were downloaded and/or unzipped in step 1 of this section.
3. Select __Open__. A notification indicating the status of the import will appear in the top right corner of the browser window.

1.

After the import of notebooks is successful, you can go to items view of the workspace and see these newly imported notebooks. Click on __wwilakehouse__lakehouse to open it.

2. Once the __wwilakehouse__lakehouse is opened, select__Open notebook__>__Existing notebook__ from the top navigation menu

1. From the list of existing notebooks, select the __01 - Create Delta Tables__notebook and select__Open.__

1. In the open notebook in the lakehouse __Explorer__, you see the notebook is already linked to your opened lakehouse.

__Note__ Fabric provides these unique capabilities for writing optimized delta lake files:

- Verti-Parquet – Fabric includes Microsoft ’s unique VertiParquet IP. VertiParquet

transparently optimizes the Delta Lake files in a way that is highly optimized by Fabric compute engines, often resulting in 3x-4x compression improvement and up to 10x performance acceleration over Delta Lake files not optimized using VertiParquet while still maintaining full Delta Lake format compliance.

- [Optimize write](https://learn.microsoft.com/en-us/azure/synapse-analytics/spark/optimize-write-for-apache-spark) – Apache Spark performs most efficiently when using standardized larger file sizes. The relation between the file size, the number of files, the number of Spark

workers and Spark’s configurations play a critical role in performance. Ingestion workloads into Delta Lake tables may have the inherited characteristic of constantly writing lots of small files; this scenario is commonly known as the "small files problem". To overcome this problem, Spark in Fabric includes an Optimize Write feature that reduces the number of files written and aims to increase individual file size of the written data. It dynamically optimizes partitions while generating files with a default 128 MB size. The target file size may be changed per workload requirements using configurations.

1. Before you write data as Delta lake tables in the Tables section of the lakehouse, you use two Fabric features (V-order and Optimize Write) for optimized data writing and for improved reading performance. To enable these features in your session, set these configurations in the first cell of your notebook.

To start the notebook and execute all the cells in sequence, select Run all on the top ribbon (under Home). Or, to only execute code from a specific cell, select the Run icon that appears to the left of the cell upon hover, or press SHIFT \+ ENTER on your keyboard while control is in the cell.

When running a cell, you didn't have to specify the underlying Spark pool or cluster details because Fabric provides them through Live Pool. Every Fabric workspace comes with a default Spark pool, called Live Pool. This means when you create notebooks, you don't have to worry about specifying any Spark configurations or cluster details. When you execute the first notebook command, the live pool is up and running in a few seconds. And the Spark session is established and it starts executing the code. Subsequent code execution is almost instantaneous in this notebook while the Spark session is active.

1. Next, you read raw data from the Files section of the lakehouse, and add more columns for different date parts as part of the transformation. Finally, you use partition By Spark API to partition the data before writing it as Delta table format based on the newly created data part columns (Year and Quarter).

from pyspark.sql.functions import col, year, month, quarter table_name = 'fact_sale'

df = spark.read.format("parquet").load('Files/wwi-raw-data/WideWorldImportersDW/parquet/full/fact_sale_1y_full/')

df = df.withColumn('Year', year(col("InvoiceDateKey")))

df = df.withColumn('Quarter', quarter(col("InvoiceDateKey")))

df = df.withColumn('Month', month(col("InvoiceDateKey")))

df.write.mode("overwrite").format("delta").partitionBy("Year","Quarter").save("Tables/" \+ table_name)

1. After the fact tables load, you can move on to loading data for the rest of the dimensions. The following cell creates a function to read raw data from the __Files__ section of the lakehouse for each of the table names passed as a parameter. Next, it creates a list of dimension tables. Finally, it loops through the list of tables and creates a Delta table for each table name that's read from the input parameter. Note that the script drops the column named Photo in this example because the column isn't used.

from pyspark.sql.types import \* def loadFullDataFromSource(table_name):

df = spark.read.format("parquet").load('Files/wwi-raw-data/WideWorldImportersDW/parquet/full/' \+ table_name)

df = df.select(\[c for c in df.columns if c != 'Photo'\])

df.write.mode("overwrite").format("delta").save("Tables/" \+ table_name)

full_tables = \[ 'dimension_city', 'dimension_date', 'dimension_employee', 'dimension_stock_item'

\] for table in full_tables:

loadFullDataFromSource(table)

1. To validate the created tables, right-click and select refresh on the __wwilakehouse__ lakehouse. The tables appear.

1. Please go the items view of the workspace again and click on __wwilakehouse__lakehouse to open it.

1. Now, open the second notebook. In the lakehouse view, click on __Open notebook__>__Existing notebook__on the ribbon at the top.

1. From the list of existing notebooks, select the __02 - Data Transformation - Business__notebook to open it.

1. Once the notebook is opened, in the __Lakehouse explorer__you will notice the notebook is already linked to your opened lakehouse. Click__Run all__to execute the notebook . In case you are getting a session error make sure the environment is set to__Workspace default__.

1. An organization might have a group of data engineers working with Scala/Python while there might be other groups of data engineers preferring to work with SQL (Spark SQL or T-SQL) and all these while working on the

same copy of the data. Fabric makes it possible for these different groups, with varied experience and preference, to work and collaborate.

You are going to learn two different approaches, as below, to transform and generate business aggregates, and as a developer you can pick the one suitable for you or mix and match these approaches based on your preference without compromising on the performance:

-

	- Approach \#1 – Use PySpark to join and aggregates data for generating business aggregates. This approach would be preferable to someone with a programming (Python or PySpark) background.
	- Approach \#2 – Use Spark SQL to join and aggregates data for generating business aggregates. This approach would be preferable to someone with SQL background, transitioning to Spark.

1. __Approach \#1__– Use PySpark to join and aggregates data for generating business aggregates. In the below code, you are creating three different Spark dataframes, each referencing an existing delta table. Then, you are joining these tables using the dataframes, doing group by to generate aggregation, renaming few of the columns and finally writing it as delta table in the__Tables__section of the lakehouse to persist with the data.

df_fact_sale = spark.read.table("wwilakehouse.fact_sale")

df_dimension_date = spark.read.table("wwilakehouse.dimension_date")

df_dimension_city = spark.read.table("wwilakehouse.dimension_city")

sale_by_date_city = df_fact_sale.alias("sale") \\ .join(df_dimension_date.alias("date"), df_fact_sale.InvoiceDateKey == df_dimension_date.Date, "inner") \\ .join(df_dimension_city.alias("city"), df_fact_sale.CityKey == df_dimension_city.CityKey, "inner") \\ .select("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "city.City", "city.StateProvince", "city.SalesTerritory", "sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")\\ .groupBy("date.Date", "date.CalendarMonthLabel", "date.Day", "date.ShortMonth", "date.CalendarYear", "city.City", "city.StateProvince", "city.SalesTerritory")\\ .sum("sale.TotalExcludingTax", "sale.TaxAmount", "sale.TotalIncludingTax", "sale.Profit")\\ .withColumnRenamed("sum(TotalExcludingTax)", "SumOfTotalExcludingTax")\\ .withColumnRenamed("sum(TaxAmount)", "SumOfTaxAmount")\\ .withColumnRenamed("sum(TotalIncludingTax)", "SumOfTotalIncludingTax")\\ .withColumnRenamed("sum(Profit)", "SumOfProfit")\\ .orderBy("date.Date", "city.StateProvince", "city.City")

sale_by_date_city.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/aggregate_sale_by_date_city")

1. __Approach \#2__– Use Spark SQL to join and aggregates data for generating business aggregates. In the below code, you are creating a temporary Spark view by joining 3 tables, doing group by to generate aggregation, renaming few of the columns. Finally, you are reading from the temporary Spark view and finally writing it as delta table in the Tables section of the lakehouse to persist with the data.

%%sql CREATE OR REPLACE TEMPORARY VIEW sale_by_date_employee AS SELECT DD.Date, DD.CalendarMonthLabel , DD.Day, DD.ShortMonth Month, CalendarYear Year ,DE.PreferredName, DE.Employee ,SUM(FS.TotalExcludingTax) SumOfTotalExcludingTax ,SUM(FS.TaxAmount) SumOfTaxAmount ,SUM(FS.TotalIncludingTax) SumOfTotalIncludingTax ,SUM(Profit) SumOfProfit FROM wwilakehouse.fact_sale FS INNER JOIN wwilakehouse.dimension_date DD ON FS.InvoiceDateKey = DD.Date INNER JOIN wwilakehouse.dimension_Employee DE ON FS.SalespersonKey = DE.EmployeeKey GROUP BY DD.Date, DD.CalendarMonthLabel, DD.Day, DD.ShortMonth, DD.CalendarYear, DE.PreferredName, DE.Employee ORDER BY DD.Date ASC, DE.PreferredName ASC, DE.Employee ASC sale_by_date_employee = spark.sql("SELECT \* FROM sale_by_date_employee")

sale_by_date_employee.write.mode("overwrite").format("delta").option("overwriteSchema", "true").save("Tables/aggregate_sale_by_date_employee")

1. You can validate created tables by right clicking and selecting refresh on __wwilakehouse__lakehouse and you will notice these aggregate tables appear.

If you notice both these above approaches (1 and 2) produce a similar outcome, however based on developer background and preference, one approach can be picked up over the other without any need for the developer to learn a new technology and compromising on the performance.

Further, you would have noticed that you are writing data as delta lake files and then the automatic table discovery and registration feature of Fabric picks it up and registers it in the metastore. That means, you don’t need to explicitly call CREATE TABLE statement to create tables to use with SQL.

## __Building a report__

Power BI is natively integrated in the whole Fabric experience and this native integration brings unique mode of accessing the data, called DirectLake, from the lakehouse to provide the most performant query and reporting experience. DirectLake mode is a groundbreaking new engine capability to analyze very large datasets in Power BI. The technology is based on the idea of loading parquet-formatted files directly from a data lake without having to query a data warehouse or lakehouse endpoint and without having to import or duplicate data into a Power BI dataset.

DirectLake is a fast path to load the data from the data lake straight into the Power BI engine, ready for analysis.

In traditional DirectQuery mode, the Power BI engine queries the data directly from the data source every time it is queried and hence query performance depends on the speed data can be retrieved from the data source. It avoids having to copy the data i.e., any changes at the source are immediately reflected in the query results while in the import mode, on the other hand, performance is much better because the data is readily available in memory without having to query the data source each time, but the Power BI engine must first copy the data into the dataset at refresh time. Any changes at the source are only picked up during the next data refresh.

DirectLake mode now eliminates this import requirement by loading the data files directly into memory. Because there is no explicit import process, it is possible to pick up any changes at the source as they occur, thus combining the advantages of DirectQuery and import mode while avoiding their disadvantages. DirectLake mode is therefore the ideal choice for analyzing very large datasets as well as datasets with frequent updates at the source.

1. From your __wwilakehouse__lakehouse, select__SQL analytics endpoint__from the__Lakehouse__ dropdown menu at the top right of the screen.

1. From the SQL analytics endpoint pane, you should be able to see all the tables you created. If you don't see them yet, select the __Refresh__icon at the top. Next, select the__Model__ tab at the bottom to open the default Power BI semantic model.

2. While in the Model Tab, go to the Reporting tab within the upper ribbon, choose “Manage default semantic model”, select every table, and click confirm.

1. For this data model, you need to define the relationship between different tables so that you can create reports and visualizations based on data coming across different tables. From the __fact_sale __table, drag the__CityKey__field and drop it on the__CityKey__field in the__dimension_city __table to create a relationship. Check the “Assume

referential integrity” and click on __*Confirm *__to establish the relationship.__Note__– When defining relationships, please make sure you have many to one relationship from the fact to the dimension and not vice versa.

1. On the __New Relationship__settings:
	1. Table 1 will be populated with fact_sale and the column of CityKey.
	2. Table 2 will be populated with dimension_city and the column of CityKey.
	3. Cardinality: __Many to one (\*:1)__
	4. Cross filter direction: __Single__
	5. Leave the box next to __Make this relationship active__checked.
	6. Check the box next to __Assume referential integrity.__
	7. ____Select__Save.__
	8. Similarly, you need to add these relationships as well:
		- StockItemKey(fact_sale) – StockItemKey(dimension_stock_item)
		- Salespersonkey(fact_sale) – EmployeeKey(dimension_employee)
		- CustomerKey(fact_sale) – CustomerKey(dimension_customer)
		- InvoiceDateKey(fact_sale) – Date(dimension_date)

After adding these above relationships, your data model is ready, as above, for reporting. Click on __*New report *__to start creating reports/dashboards in Power BI.

1.

On the Power BI report canvas, you can create reports to meet your business requirements by dragging required columns from the __Data__pane to the canvas and using one or more of available visualizations.

2. Add a title:
	1. In the Ribbon, click the Text Box icon
	2. Type in __WW Importers Profit Reporting__
	3. Highlight the text and increase size to 20 and place in the upper left of the report page

1. Add a Card
	1. On the __Data__pane, expand__fact_sales __and check the box next to__Profit__. This will create a column chart and add the field to the Y-axis.
	2. With the bar chart selected, click the Card visual in the visualization pane. This will convert the visual to a card.
	3. Place the card under the title
2. Add a Bar chart
	1. On the __Data__pane, expand__fact_sales __and check the box next to__Profit__. This will create a column chart and add the field to the Y-axis.
	2. On the __Data__pane, expand__dimension_city __and check the box for__SalesTerritory__This will add the field to the X-axis.
	3. With the bar chart selected, click on the Clustered Bar Chart visual in the visualization pane. This will convert the column chart into a bar chart.

-

	1. Resize the Bar chart to fill in the area under the title and Card

1. Click anywhere on the blank canvas (or press the Esc key) so the bar chart visual is no longer selected.
2. Build a stacked area chart visual:
	1. On the __Visualizations__pane, select the__Stacked area chart__visual.
	2. Reposition and resize the stacked area chart to the right of the card and bar chart visuals created in the previous steps.
	3. On the __Data__pane, expand__fact_sales __and check the box next to__Profit.__Expand dimension_date and check the box next to __FiscalMonthNumber__. This will create a filled line chart showing profit by fiscal month.
	4. On the __Data__pane, expand__dimension_stock_item __and drag__BuyingPackage__into the Legend field well. This will add a line for each of the Buying Packages.
3. Click anywhere on the blank canvas (or press the Esc key) so the stacked area chart visual is no longer selected.
4. Build a column chart:
	1. On the __Visualizations__pane, select the__Stacked column chart__visual.

-

	1. On the __Data__pane, expand__fact_sales __and check the box next to__Profit__. This will add the field to the Y- axis.
	2. On the __Data__pane, expand__dimension_employee __and check the box next to__Employee__. This will add the field to the X-axis.

1. Click anywhere on the blank canvas (or press the Esc key) so the LINE chart visual is no longer selected.
2. From the ribbon, select __File > Save__.
3. Enter the name of your report as __Profit Reporting__.
4. Select __Save__

____

# Module 4: Clean up resources

You can delete individual reports, pipelines, warehouses, and other items or remove the entire workspace.

1. Select __Fabric Lakehouse Tutorial <suffix you added to make it unique>__in the left-hand navigation menu to return to the workspace item view.

1. Below the workspace name and description at the top of the workspace header, select __Workspace settings__.

1. Select __Other > Delete this workspace__.

1. Select __Delete__on the warning.
