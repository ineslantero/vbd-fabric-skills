# Fabric Foundation VBD - Data Warehouse Lab Tutorial

> Converted from `Fabric Data Warehouse Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs).
> Screenshots have been stripped; refer to `sources.yaml` in this folder for the Microsoft Learn URLs cited throughout.

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

# Introduction

__What is Fabric?__ Fabric provides a one-stop shop for all the analytical needs for every enterprise. It covers the complete spectrum of services including data movement, data lake, data engineering, data integration and data science, real time analytics, and business intelligence. With Fabric, there is no need to stitch together different services from multiple vendors. Instead, the customer enjoys an end-to-end, highly integrated, single comprehensive product that is easy to understand, onboard, create and operate. There is no other product on the market that offers the breadth, depth, and level of integration that Fabric offers. Additionally, Microsoft Purview is included by default in every tenant to meet compliance and governance needs.

To get an overview over the components and concepts of Fabric read [Fabric - ](https://microsofteur.sharepoint.com/:b:/r/teams/TridentPrivatePreview/Shared%20Documents/Documentation/Private%20Preview%20Documentation/End-to-End%20Scenarios/Overview%20and%20Concepts.pdf?csf=1&web=1&e=fJl62K)[Overview and Concepts](https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview)[.](https://microsofteur.sharepoint.com/:b:/r/teams/TridentPrivatePreview/Shared%20Documents/Documentation/Private%20Preview%20Documentation/End-to-End%20Scenarios/Overview%20and%20Concepts.pdf?csf=1&web=1&e=fJl62K)

__Purpose of this tutorial__ While many concepts in Fabric may be familiar to data and analytics professionals it can be challenging to apply those concepts in a new environment. This tutorial has been designed to walk step-by-step through an end-to-end scenario from data acquisition to data consumption to build a basic understanding of the Fabric UX, the various workloads and their integration points, and the Fabric professional and citizen developer experiences.

The tutorials are not intended to be a reference architecture, an exhaustive list of features and functionality, or a recommendation of specific best practices.

__The data warehouse tutorial__ In this tutorial, you will take on the role of a data warehouse developer at the fictional Wide World Importers company and complete the following steps:

- Sign into your Power BI online account, or if you don’t have an account yet, sign up for a free trial.
- Build and implement an end to end data warehouse for your organization:

o Enable Fabric in your tenant o Create a Fabric workspace o Quickly create a data warehouse, Ingest data from source to the data warehouse dimensional model o Transform the data to create aggregated datasets using T-SQL o Perform orchestration, data ingestion, and data transformation with pipelines o Query the data warehouse using T-SQL and a visual query editor o Create Power BI report using DirectLake mode to analyze the data in place

- Cleanup resources by deleting the workspace and other items

__The data warehouse end to end architecture__ __Data Sources__ – Fabric makes it easy and quick to connect to Azure Data Services, other cloud platforms, and on-premises data sources to ingest data from.

__Ingestion__ – With 200\+ native connectors as part of the Fabric pipeline and with drag and drop data transformation with dataflow, you can quickly build insights for your organization. Shortcut is a new feature in Fabric that provides a way to connect to existing data without having to copy or move it – more details about Shortcut later in this tutorial.

__Transform and Store__ – Fabric standardizes on Delta Lake format, that means all the engines of Fabric can read and work on the same dataset stored in OneLake – no need for data duplicity. This storage allows you to build a data warehouse or data mesh based on your organizational need. For transformation, you can choose either low-code or no code experience with pipelines/dataflows or use T-SQL for a code first experience.

__Consume__ – Data from the data warehouse can be consumed by Power BI, industry leading business intelligence tool, for reporting and visualization. Each data warehouse comes with a built-in TDS/SQL endpoint for easily connecting to and querying data from other reporting tools, when needed. When a data warehouse is created, a secondary item called a default dataset will be automatically generated at the same time with the same name of the data warehouse to start visualizing data with just a couple of mouse clicks.

__The sample data__ For sample data, we are going to use [Wide World Importers (WWI) sample database.](https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16) For our data warehouse end-to-end scenario, we have generated sufficient data for a sneak peek into the scale and performance capabilities of the Fabric platform.

Wide World Importers (WWI) is a wholesale novelty goods importer and distributor operating from the San Francisco Bay area. As a wholesaler, WWI's customers are mostly companies who resell to individuals. WWI sells to retail customers across the United States including specialty stores, supermarkets, computing stores, tourist attraction shops, and some individuals. WWI also sells to other wholesalers via a network of agents who promote the products on WWI's behalf. You can learn more about their company profile and operation [here.](https://learn.microsoft.com/en-us/sql/samples/wide-world-importers-what-is?view=sql-server-ver16)

Typically, you would bring data from transactional systems (or line of business applications) into a data lake or data warehouse staging area, however for simplicity of this tutorial, we are going to use the dimensional model provided by WWI as our initial data source. We are going to use it as the source to ingest the data into a data warehouse and transform it through T-SQL.

__The data model__ While the WWI dimensional model contains multiple fact tables, for simplicity in explanation we will focus on the Sale Fact table and its related dimensions only, as below, to demonstrate this end-to-end data warehouse scenario:

# Module 1: Create a workspace (This step is not needed if the workspace is already created for every user upon provisioning of trial tenant)

__Please make sure to complete the Lakehouse tutorial first before starting this one as this tutorial use the lakehouse as one of the data sources for the exercise__ Before you can begin building the warehouse, you will need to create a workspace where you will build out the remainder of the tutorial. In this module, you will learn to:

• 	Create a workspace The workspace will contain all the artifacts needed for data warehousing including Data Factory pipelines, the data warehouse, Power BI datasets, and reports.

1. Sign in to [Microsoft Fabric](https://app.fabric.microsoft.com/).
2. Select __Workspaces > New Workspace__.

1. Fill out the __Create a workspace__ form as follows:
	1. __Name:__Enter *Data Warehouse Tutorial*, and some characters for uniqueness.
	2. __Description__: Optionally, enter a description for the workspace.__* *__

1. Expand the __Advanced__section.__* *__
2. Choose __Premium capacity__in the__License Mode__section.__* *__
3. Choose a premium capacity you have access to__.* *__

1. Select __Apply.__The workspace will be created and opened.

# Module 2: Build your first data warehouse

The intent of this module is to quickly build end to end journey of building a data warehouse, ingesting data for a table and then using the data warehouse for creating a report.

## Create a data warehouse

1. In the [Power BI service ](https://powerbi.com/)select __Workspaces__ in the left-hand menu.
2. Search for the workspace you create in Module 1 by typing in the search textbox at the top and click on your workspace to open it.

1. In the upper left corner, select__New item__to display a full list of available items.

1. In the __Store Data__section, select__Warehouse__.

1. On the __New warehouse__dialog, enter__WideWorldImporters__ as the name.
2. Select __Create__.

When provisioning is complete the __Build a warehouse__ landing page will be shown.

##

## Data ingestion

1. Select __Data Warehouse Tutorial__ in the left-hand navigation menu to return to the workspace artifact view.

1. In the upper left corner, select__\+ New Item__to display a full list of available items.

1. In the __Get Data__section, select__Data pipeline__.

1. On the __New pipeline__dialog, enter__Load Customer Data__ as the name.

1. Select __Create__.
2. Select P__ipeline activity__from the__Build a data pipeline to organize and move your data__landing page.

1. Select __Copy data__from the__Move & transform__ section.

1. If necessary, select the newly created Copy data activity from the design canvas and follow the steps below to configure it.
2. On the __General__page, enter__CD Load dimension_customer__as the__Name__.

1. On the __Source__page Under__Connection__, select__More__

1. Type __wwilakehouse__in the searchbox to__select the lakehouse created in the lakehouse tutorial__. Make sure you are the owner of the lakehouse and is the one you created in the prior tutorial as multiple names will show up

1. On the __File Path__, configure the settings as follows:

____ __File path – Directory:__/wwi-raw-data/WideWorldImportersDW/tables__File path – File name:__ dimension_customer.parquet __File format:__ Parquet

1. Select__Preview data__next to the__File path__ setting to ensure there are no errors.

1. On the __Destination__page, select__WideWorldImporters__from the list.  If it is not available, then click on__More__to browse in OneLake data hub

1. Next to the __Table__ __option__setting, select__Auto create table__
2. In the first box (schema name) next to the __Table__setting, enter__dbo__.
3. In the second box(table name) next to the __Table__setting, enter__dimension_customer__.

1. From the ribbon, select __Run__.
2. Select __Save and run__ from the dialog box. The pipeline to load the dimension_customer table with start.
3. Monitor the copy activity’s progress on the __Output__ page and wait for it to complete.

## Building a report

1. Select __Data Warehouse Tutorial__ in the left-hand navigation menu to return to the workspace artifact view.

1. From the artifact list, select __WideWorldImporters__with the type of__Warehouse,__navigate to tab__Reporting__and click on__Manage default semantic model.__Select under Tables “dimension_customer” and click on __Confirm__.

1. Return to the workspace artifact view, from the artifact list, select __WideWorldImporters__with the type of__Semantic Model.__In the__Discover business insights__section, select__Explore this data > Auto-create a report__. A report will be generated from the dimension_customer table that was loaded in the previous section.

1. A report similar to one shown below will be generated.

1. From the ribbon, select __Save.__
2.

3. Enter __Customer Quick Summary__ in the name box.
4. Select __Save__.

# Module 3: Extending the solution

Now that you have see how to build a data warehouse, load a table, and generate a report it is time to extend the solution by exploring additional methods for loading data, querying data, and building reports.

## Creating tables in the data warehouse

1. Select __Workspaces__ in the left-hand menu of the [Power BI service.](https://powerbi.com/)
2. Select the workspace created in __Module 1:__ __Getting started__, such as__Data Warehouse Tutorial__.
3. From the artifact list, select __WideWorldImporters__with the type of__Warehouse__.

1. From the ribbon, select __New SQL query__.

1. In the query editor, paste the code below.

__Note:__In case of issues with copy/paste formatting, a text file containing the script called__Create Tables.txt__ can be accessed from the Scripts folder[.](https://microsoft.sharepoint.com/:f:/t/TridentOnboardingCoreTeam/Epv9NZihfm5PikuZDBuBsF8BJK9gkVYPHRlHBuZT3b7frQ?e=bRAHR7)

/\* -

	1. Drop the dimension_city table if it already exists.
	2. Create the dimension_city table.
	3. Drop the fact_sale table if it already exists.
	4. Create the fact_sale table.

\*/ --dimension_city DROP TABLE IF EXISTS \[dbo\].\[dimension_city\];

CREATE TABLE \[dbo\].\[dimension_city\] ( \[CityKey\] \[int\] NULL, \[WWICityID\] \[int\] NULL, \[City\] \[varchar\](8000) NULL, \[StateProvince\] \[varchar\](8000) NULL, \[Country\] \[varchar\](8000) NULL, \[Continent\] \[varchar\](8000) NULL, \[SalesTerritory\] \[varchar\](8000) NULL, \[Region\] \[varchar\](8000) NULL, \[Subregion\] \[varchar\](8000) NULL, \[Location\] \[varchar\](8000) NULL, \[LatestRecordedPopulation\] \[bigint\] NULL, \[ValidFrom\] \[datetime2\](6) NULL, \[ValidTo\] \[datetime2\](6) NULL, \[LineageKey\] \[int\] NULL );

--fact_sale DROP TABLE IF EXISTS \[dbo\].\[fact_sale\];

CREATE TABLE \[dbo\].\[fact_sale\] ( \[SaleKey\] \[bigint\] NULL, \[CityKey\] \[int\] NULL, \[CustomerKey\] \[int\] NULL, \[BillToCustomerKey\] \[int\] NULL, \[StockItemKey\] \[int\] NULL, \[InvoiceDateKey\] \[datetime2\](6) NULL, \[DeliveryDateKey\] \[datetime2\](6) NULL, \[SalespersonKey\] \[int\] NULL, \[WWIInvoiceID\] \[int\] NULL, \[Description\] \[varchar\](8000) NULL, \[Package\] \[varchar\](8000) NULL, \[Quantity\] \[int\] NULL, \[UnitPrice\] \[decimal\](18, 2) NULL, \[TaxRate\] \[decimal\](18, 3) NULL, \[TotalExcludingTax\] \[decimal\](29, 2) NULL, \[TaxAmount\] \[decimal\](38, 6) NULL, \[Profit\] \[decimal\](18, 2) NULL, \[TotalIncludingTax\] \[decimal\](38, 6) NULL, \[TotalDryItems\] \[int\] NULL, \[TotalChillerItems\] \[int\] NULL, \[LineageKey\] \[int\] NULL, \[Month\] \[int\] NULL, \[Year\] \[int\] NULL, \[Quarter\] \[int\] NULL );

1. Select __Run__ to execute the query.

1. To save this query for reference later, right-click on the query tab just above the editor and select __Rename__.

1. Type __Create Tables__ to change the name of the query.

1. Click __Rename__to save the query with a given name

1. Validate the table was created successfully by clicking the __refresh__button on the ribbon.

1. In the __Object explorer__verify that you can see the newly created__Create Tables__query,__fact_sale__table, and__dimension_city__ table.

## Loading data using Pipeline

1. From the Data factory experience , select __New Data Pipeline__

1. Name the Pipeline __Copy data to dimension city and fact sale,__once pipeline is created, choose tile 'Copy data assistant' to get into the data assistant

1. In the copy data assistant window, search for __wwilakehouse__ and select the lakehouse you own as it will show multiple lakehouse

1. Navigate to OneLake -> wwilakehouse -> files section -> /wwi-raw-data/WideWorldImportersDW/tables

Select the file __dimension_city.parquet__ as the source file. Click next

1. In destination choose warehouse __WideWorldImporters__. Select the one you own as multiple warehouses with the same name will show up

1. Load to existing table __dbo.dimension_city__. Click next

1. Make sure __enable staging__ is enabled. Click next

1. Make sure option __Start data transfer immediately__ is unchecked as we will run it later. Click ok

1. Rename the copy data activity as __Copy dimension city__ in the general tab of the copy activity.

1. Add one more copy data activity to the canvas. Choose __Use copy assistant__ option

1. Select __wwilakehouse__as the lakehouse source. Make sure to select the one you own ad multiple lakehouse will show up.

12. Navigate to OneLake -> wwilakehouse -> files section -> /wwi-raw-data/WideWorldImportersDW/tables

Select __fact_sale.parquet __as the source file. Click next

1. Choose __Wideworksimporters__ warehouse as the target destination . Make sure to select the one you own as multiples will show up.

1. In the mappings tab , Make sure to delete the mapping for __Month , Year and Quarter__ as the source file doesn’t contain these columns. Click Next

1. Make sure the __enable staging option__ is checked, Click Next

1. Make sure __Start data transfer immediately__ checkbook is unchecked , Click ok

1. Rename the copy activity as __Copy Fact Sale__

1. Now that we have both the copy activity defined, Run the entire pipeline by clicking the Run option from the ribbon

1. Monitor the pipeline for successful completion.

1. Validate in the warehouse WideWorldImporters that the tables have been loaded successfully

## Data transformation using a stored procedure

1. From the __Home__tab of the ribbon, select__New SQL query__.

1. In the query editor, paste the code below.

__Note:__In case of issues with copy/paste formatting, a text file containing the script called__Create Aggregate Procedure.txt__ from the Scripts folder [.](https://microsoft.sharepoint.com/:f:/t/TridentOnboardingCoreTeam/Epv9NZihfm5PikuZDBuBsF8BJK9gkVYPHRlHBuZT3b7frQ?e=bRAHR7)

--Drop the stored procedure if it already exists.

DROP PROCEDURE IF EXISTS \[dbo\].\[populate_aggregate_sale_by_city\] GO --Create the populate_aggregate_sale_by_city stored procedure.

CREATE PROCEDURE \[dbo\].\[populate_aggregate_sale_by_city\] AS BEGIN --If the aggregate table already exists, drop it. Then create the table.

DROP TABLE IF EXISTS \[dbo\].\[aggregate_sale_by_date_city\];

CREATE TABLE \[dbo\].\[aggregate_sale_by_date_city\] ( \[Date\] \[DATETIME2\](6), \[City\] \[VARCHAR\](8000), \[StateProvince\] \[VARCHAR\](8000), \[SalesTerritory\] \[VARCHAR\](8000), \[SumOfTotalExcludingTax\] \[DECIMAL\](38,2), \[SumOfTaxAmount\] \[DECIMAL\](38,6), \[SumOfTotalIncludingTax\] \[DECIMAL\](38,6), \[SumOfProfit\] \[DECIMAL\](38,2)

);

--Reload the aggregated dataset to the table.

INSERT INTO \[dbo\].\[aggregate_sale_by_date_city\] SELECT FS.\[InvoiceDateKey\] AS \[Date\], DC.\[City\], DC.\[StateProvince\], DC.\[SalesTerritory\], SUM(FS.\[TotalExcludingTax\]) AS \[SumOfTotalExcludingTax\],          SUM(FS.\[TaxAmount\]) AS \[SumOfTaxAmount\], SUM(FS.\[TotalIncludingTax\]) AS \[SumOfTotalIncludingTax\], SUM(FS.\[Profit\]) AS \[SumOfProfit\] FROM \[dbo\].\[fact_sale\] AS FS INNER JOIN \[dbo\].\[dimension_city\] AS DC ON FS.\[CityKey\] = DC.\[CityKey\] GROUP BY FS.\[InvoiceDateKey\],         DC.\[City\], DC.\[StateProvince\], DC.\[SalesTerritory\] ORDER BY FS.\[InvoiceDateKey\], DC.\[StateProvince\], DC.\[City\];

END

1. To save this query for reference later, right-click on the query tab just above the editor and select __Rename__.

1. Type __Create Aggregate Procedure__ to change the name of the query.

1. Click on __Rename__to save the query with given name
2. Select __Run__ to execute the query.

1. Click the __refresh__button on the ribbon.

1. In the __Object explorer__verify that you can see the newly created stored procedure by expanding the__StoredProcedures__node under the__dbo__ schema.

1. From the __Home__tab of the ribbon, select__New SQL query__.
2. In the query editor, paste the code below.

__Note:__In case of issues with copy/paste formatting, a text file containing the script called__Run Aggregate Procedure.txt__ can be accessed from the Scripts folder .

--Execute the stored procedure to create the aggregate table.

EXEC \[dbo\].\[populate_aggregate_sale_by_city\];

1. To save this query for reference later, right-click on the query tab just above the editor and select __Rename__.
2. Type __Run Create Aggregate Procedure__ to change the name of the query.
3. Select __Run__ to execute the query.
4. Click the __refresh__button on the ribbon. The query will take between 2 and 3 minutes to execute.
5. In the __Object explorer__, load the data preview to validate the data loaded successfully by clicking on the__aggregate_sale_by_city__table in the__Explorer__.

## Using the visual query builder

1. From the __Home__tab of the ribbon, select__New visual query__.

1. Drag the __fact_sale__ table from the explorer to the query design pane.

1. Limit the dataset size by selecting __Reduce rows > Keep top rows__ from the transformations ribbon.

1. In the __Keep top rows__dialog enter__10,000__.
2. Select __OK__.
3. Drag the __dimension_city__ table from the explorer to the query design pane.
4. From the transformations ribbon, select the dropdown next to __Combine__and select__Merge queries as new__.

1. On the __Merge__ settings page:
	1. __Left table for merge:__dimension_city
	2. __Right table for merge:__ fact_sale
	3. Select the __CityKey__field in the__dimension_city__ table by clicking on the column name in the header row to indicate the join column.
	4. Select the __CityKey__field in the__fact_sale__ table by clicking on the column name in the header row to indicate the join column.
	5. __Join kind:__Inner

Select __OK__.

2. With the __Merge__step selected, select the__Expand__button next to__fact_sale__on the header of the data grid then select only__TaxAmount, Profit,__and__TotalIncludingTax.__

1. Select __OK__.
2. Select __Transform >__ __Group by__ from the transformations ribbon.

1. On the __Group by__settings page:
	1. Change to __Advanced__.
	2. __Group by__(if necessary, select__Add grouping__to add additional group by columns)__:__ i. Country
		1. StateProvince
		2. City
	3. __New column name__(if necessary, select__Add aggregation__to add additional aggregate columns and operations)__:__
		1. __SumOfTaxAmount__with__Operation__of__Sum__and__Column__of__TaxAmount__
		2. __SumOfProfit__with__Operation__of__Sum__and__Column__of__Profit__iii.__SumOfTotalIncludingTax__with__Operation__of__Sum__and__Column__of__TotalIncludingTax__

Select __OK__.

1. Right-click on __Visual query 1__in the explorer and select__Rename__.

1. Type __Sales Summary__ to change the name of the query.
2. Press __Enter__ on the keyboard or click off anywhere outside the tab to save the change.

## Create a Power BI report

1. Navigate to tab __Reporting,__update__Manage default semantic model__to__ __add Tables “dimension_city” & “fact_sale” & click __Confirm__.  .

Select the __Model__ view from the options in the bottom left corner, just outside the canvas

1. From the __fact_sale __table, drag the__CityKey__field and drop it on the__CityKey__field in the__dimension_city __table to create a relationship.

1. On the __Create Relationship__settings:
-

		1. Table 1 will be populated with fact_sale and the column of CityKey.
		2. Table 2 will be populated with dimension_city and the column of CityKey.
		3. Cardinality: __Many to one (\*:1)__
		4. Cross filter direction: __Single__
		5. Leave the box next to__Make this relationship active__checked.__ __
		6. Check the box next to __Assume referential integrity.__	__ __

__ __Select__Confirm__.

1. From the __Home__tab of the ribbon, select__New report__.
2. Build a column chart visual:
-

		1. On the __Data__pane, expand__fact_sales__and check the box next to__Profit__. This will create a column chart and add the field to the Y-axis.
		2. On the __Data__pane, expand__dimension_city__and check the box next to__SalesTerritory__. This will add the field to the X-axis.
		3. Reposition and resize the column chart to take up the top left quarter of the canvas by dragging the anchor points on the corners of the visual.

1. Click anywhere on the blank canvas (or press the Esc key) so the column chart visual is no longer selected.
2. Build a map visual:
	1. On the __Visualizations__pane, select the__Azure Map for Power BI__visual.__Azure Map__ visual needs to be enabled by PowerBI admin

-

	1. From the __Data__pane, drag__StateProvince__from the__dimension_city__table to the__Location__bucket on the__Visualizations__ pane.
	2. From the __Data__pane, drag__Profit__from the__fact_sale__table to the__Size__bucket on the__Visualizations__pane.

-

	1. If necessary, reposition and resize the map to take up the bottom left quarter of the canvas by dragging the anchor points on the corners of the visual.

1. Click anywhere on the blank canvas (or press the Esc key) so the map visual is no longer selected.
2. Build a table visual:
-

		1. On the __Visualizations__pane, select the__Table__ visual.

- -

		1. From the __Data__pane, check the box next to__SalesTerritory__on the__dimension_city __table.
		2. From the __Data__pane, check the box next to__StateProvince__on the__dimension_city __table.
		3. From the __Data__pane, check the box next to__Profit__on the__fact_sale __table.
		4. From the __Data__pane, check the box next to__TotalExcludingTax__on the__fact_sale __table.
		5. Reposition and resize the column chart to take up the right half of the canvas by dragging the anchor points on the corners of the visual.

1. From the ribbon, select __File > Save__.
2. Enter the name of your report as __Sales Analysis__.
3. Select __Save__.

## Time Travel in Data Warehouse

What is time travel?

Time travel in a data warehouse is a low-cost and efficient capability to quickly query prior versions of data. Microsoft Fabric currently allows retrieval with default retention period of 30 days.

The guide below will demonstrate Time travel using the OPTION clause to specify the *FOR TIMESTAMP AS OF* query hint. The column “PostalCode” will be updated twice and then one can travel back in time to query the prior state of data as persisted in past

1. Execute the following query in a new query editor. Current postal code for customer key (234) is 90584

SELECT \* FROM \[dbo\].\[dimension_customer\] where CustomerKey =  234;

1. Update PostalCode for customer key (234) to 75252

update \[dbo\].\[dimension_customer\] set PostalCode = 75252 where CustomerKey =  234;

1. Update PostalCode for customer key (234) to 76227

update \[dbo\].\[dimension_customer\] set PostalCode = 76227 where CustomerKey =  234;

1. Get current time as shown in screenshot below. Copy the timestamp value

SELECT CURRENT_TIMESTAMP;

Copy the timestamp value and for simpler querying of prior versions, make the millisecond component to 000 as shown below.

2024-08-30T20:00:06.177 -----------------à 2024-08-30T20:00:06.__000__

1. Time travel using queries below, and observe the prior values for field “PostalCode”

Latest Status as of 20:00:06 SELECT CustomerKey, PostalCode FROM \[dbo\].\[dimension_customer\] where CustomerKey =  234 OPTION (FOR TIMESTAMP AS OF '2024-08-30T20:00:06.000');

Prior Status as of 19:52:00 SELECT CustomerKey, PostalCode FROM \[dbo\].\[dimension_customer\] where CustomerKey =  234 OPTION (FOR TIMESTAMP AS OF '2024-08-30T19:52:00.000');

Prior Status as of 19:45:00 SELECT CustomerKey, PostalCode FROM \[dbo\].\[dimension_customer\] where CustomerKey =  234 OPTION (FOR TIMESTAMP AS OF '2024-08-30T19:45:00.000');

##

## Clone Table in Data Warehouse

Microsoft Fabric offers the capability to create near-instantaneous zero-copy clones with minimal storage costs. A zero-copy clone creates a replica of the table by copying the metadata, while still referencing the same data files in OneLake. The metadata is copied while the underlying data of the table stored as parquet files is not copied. The creation of a clone is similar to creating a table within a Warehouse in Microsoft Fabric.

1. Clone the “dimension_customer” table. When you select the table, and select on more options, you get the Clone table menu. This menu is also available via Table tools in the ribbon.

1. On clone table pane, you can see the source table schema and name is already populated. The table state as current, creates clone of the source table as of its current state. You can also clone table from a past point in time. You can choose destination schema and edit pre-populated destination table name. You can also see the generated T-SQL statement when you expand SQL statement section. When you select the Clone button, a clone of the table is generated and you can see it in Explorer.

# Module 4: Clean up resources

You can delete individual reports, pipelines, warehouses, and other items or remove the entire workspace.

1. Select __Data Warehouse Tutorial__ in the left-hand navigation menu to return to the workspace artifact view.

1. Below the workspace name and description at the top of the workspace header, select __Workspace settings__.__ __

__ __

1. Select __Other > Delete this workspace__.

1. Select __Delete__on the warning.
