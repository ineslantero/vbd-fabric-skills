# Fabric Foundation VBD - Real-Time Intelligence Lab Tutorial

> Converted from `Real-time Intelligence Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs).
> Screenshots have been stripped; refer to `sources.yaml` in this folder for the Microsoft Learn URLs cited throughout.

## Contents

- Introduction

- Real-time Intelligence

- Scenario

- Prerequisites

- Module 1: Create a Fabric workspace

- Module 2: Build your first Real-time Intelligence Solution in Fabric

- Create an Eventhouse

- Create an Eventstream

- __Create a destination for the timestamp transformation__

- Transform data in your KQL Database

- __Move raw data table to a bronze folder__

- __Create target table__

- __Create function with transformation logic__

- __Apply update policy__

- __Verify transformation__

- Query streaming data using KQL

- __Write a KQL query__

- __Create a materialized view__

- Create a Real-Time Dashboard

- __Create a Real-Time Dashboard__

- __Add a new tile to the dashboard__

- __Explore the data visually by adding an aggregation__

- __Add a map tile__

- Create a Power BI report

- __Build a Power BI report__

- __Add visualizations to the report__

- __Save the report__

- Set an alert on your event stream

- __Set an alert on the eventstream__

- Module 3: Clean up resources

# Introduction

##### What is Fabric?

Fabric provides a one-stop shop for all the analytical needs for every enterprise. It covers the complete spectrum of services including data movement, data lake, data engineering, data integration and data science, real time intelligence, and business intelligence. With Fabric, there is no need to stitch together different services from multiple vendors. Instead, the customer enjoys an end-to-end, highly integrated, single comprehensive product that is easy to understand, onboard, create and operate. There is no other product on the market that offers the breadth, depth, and level of integration that Fabric offers. Additionally, Microsoft Purview is included by default in every tenant to meet compliance and governance needs.

To get an overview over the components and concepts of Fabric read *Fabric - Overview and Concepts.*

##### The purpose of this tutorial

While many concepts in Fabric may be familiar to data and analytics professionals it can be challenging to apply those concepts in a new environment. This tutorial has been designed to walk step-by-step through an end-to-end scenario from data acquisition to data consumption to build a basic understanding of the Fabric UX, the various workloads and their integration points, and the Fabric professional and citizen developer experiences.

The tutorials are not intended to be a reference architecture, an exhaustive list of features and functionality, or a recommendation of specific best practices*.*

# Real-time Intelligence

Real-time Intelligence is a portfolio of capabilities that provides an end-to-end analytics streaming solution across Fabric experiences. It supplies high velocity, low latency data analysis, and is optimized for time-series data, including automatic partitioning and indexing of any data format and structure, such as structured data, semi-structured (JSON), and free text.

Real-time Intelligence delivers high performance when it comes to your increasing volume of data. It accommodates datasets as small as a few gigabytes or as large as several petabytes and allows you to explore data from different sources and a variety of data formats.

*Figure 1: End-to-end Scenario - Real-time Intelligence* Real-time Intelligence includes integration with other Fabric experiences such as Lakehouse, Data Warehouse, Pipelines, Dataflows and Event Streaming on data sources and ingestion side. On the data exposition and consumption, Real-time Intelligence integrates with Power BI, and Notebooks.

You can use Real-time Intelligence for a range of solutions, such as IoT analytics and log analytics, and in a number of scenarios including manufacturing operations, oil and gas, automotive, and more.

In this tutorial, you learn how to:

- Set up your environment
- Get data in the Real-Time hub
- Transform events
- Publish an Eventstream
- Use update policies to transform data in Eventhouse
- Create a KQL Query
- Create an alert based on a KQL query
- Create a Real-Time dashboard
- Explore data visually in the Real-Time dashboard
- Create a Power BI report from a KQL query
- Set an alert on the eventstream

### Scenario

The sample data you'll use in this tutorial is a set of bicycle data, containing information about bike ID, location, timestamp, and more. You'll learn how to set up resources, ingest data, set alerts on the data, and visualize the data to extract insights.

- Bike rental data: Contains London-based bike movements, occupancies, and tracks user patterns.

The sample end-to-end solution includes these components:

- __Eventstream:__ An Eventstream is the engine for data ingestion and processing of your real-time data into Microsoft Fabric. You can transform your data and route it via filters to various destinations. Read more about [event streams.](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/overview)
- __Eventhouse:__ An Eventhouse is where data is stored and analyzed. An Eventhouse is designed to handle real-time data streams efficiently. An Eventhouse can hold one or more KQL databases. They're tailored to large volumes of time-based, streaming events with structured, semi structured, and unstructured data. Read more about [Eventhouse](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/eventhouse).
- __KQL Database:__ A KQL Database is where data is stored and managed. It allows you to query data in real-time, providing a powerful tool for data exploration and analysis. The KQL database supports various data policies and transformations. Read more about [KQL databases.](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/create-database)
- __KQL Queryset:__ A KQL Queryset is used to run queries, view, and customize query results on data from a [KQL queryset.](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/create-query-set)
- __Real-Time Dashboard:__ A Real-Time Dashboard provides an up-to-the-second snapshot of various goals and data points in a collection of tiles. Each tile has an underlying query and a visual representation. It allows you to visualize data in real-time, providing insights and enabling data exploration. Read more about [Real-Time dashboards](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/dashboard-real-time-create).
- __Power BI:__ is used to create real-time reports that display data from Eventstreams and KQL Databases managed by Real-Time Intelligence.

### Prerequisites

- Power BI Premium subscription. For more information, see [*How to purchase Power BI Premium*](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-premium-purchase).
- Workspace

# Module 1: Create a Fabric workspace

Before you can begin building the real-time intelligence solution, you will need to use the experience switcher on the bottom left side of your home page to switch to Fabric.

Once you are there you will create a workspace where you will build out the remainder of the tutorial. In this module, you will learn to:

-

	- Create a Fabric workspace

In this step, you create a Fabric workspace in the Fabric service. The workspace will contain all the artifacts needed for real-time intelligence including KQL Database, Eventstream, Eventhouse, Power BI datasets, and reports.

1. Sign in to [Fabric](https://app.fabric.microsoft.com/) .
2. Select __\+ New Workspace__.

1. Fill out the __Create a workspace__form as follows:
	1. __Name:__Enter *Fabric Real-time Intelligence Tutorial*, and some characters for uniqueness.
	2. __Description__: Optionally, enter a description for the workspace.

1. Expand the __Advanced__section.
2. Choose __Fabric capacity__in the__License Mode__section.
3. Choose a Fabric capacity you have access to__.__

1. Select __Apply.__The workspace will be created and opened.

# Module 2: Build your first Real-time Intelligence Solution in Fabric

The intent of this module is to quickly build end to end journey of building a real-time Intelligence solution, ingesting streaming data from Eventstream and then using the KQL Database for creating a real-time refreshing Power BI report.

## Create an Eventhouse

1. In the upper left corner of the Fabric Workspace home page, select __New item > Eventhouse__

1.  Enter __Tutorial__ as the eventhouse name. A KQL database is created simultaneously with the same name.
2. Select __Create__. When provisioning is complete, the Eventhouse system overview page is shown.

## Create an Eventstream

In this part of the tutorial, you browse the Real-Time hub, create an eventstream, transform events, and create a destination to send the transformed events to a KQL database.

-

	1. Select __Real-Time__ on the left navigation bar.

____ -

	1. In the __Real-time Hub__, Select \+__Add data__ in the top-right corner of the page.

-

	1. On the __Data sources__page, select__Sample scenarios__category, and then select__Connect__on the__Bicycle rentals__ tile.

-

	1. On the __Connect data source__page, for__Source name__, enter__TutorialSource__. In the__Stream details__section, select the pencil button, and change the name of the eventstream to__TutorialEventstream__, and then select__Next__.

-

	1. On the __Review \+ connect__page, review settings, and select__Connect__.

__Transform events - add a timestamp__

1. On the __Review \+ connect__page, select__Open Eventstream__. Note: You can also browse to the eventstream from the__My data streams__by selecting the stream and then by selecting__Open Eventstream__.

1. From the menu ribbon, select __Edit__. The authoring canvas, which is the center section, turns yellow and becomes active for changes.

[](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/event-stream-edit-button.png#lightbox)

1. In the eventstream authoring canvas, select the down arrow on the __Transform events or add destination__tile, and then select__Manage fields__. The tile is renamed to ManageFields.

1. Hover over the right edge of the __TutorialEventstream__tile. Click and drag the connector to the left side of the__ManageFields__ tile. You have now connected the eventstream to a new transformation tile.

1. Click on the pencil button of __ManageFields__tile. In the__Manage fields__ pane, do the following actions:
	1. In __Operation name__, enter__TutorialTransform__.
	2. Select __Add all fields__

[](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/add-all-fields.png#lightbox)

-

	1. Select __\+ Add field__.
	2. From the __Field__dropdown, select__Built-in Date Time Function__>__SYSTEM.Timestamp()__

[](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/select-built-in-function.png#lightbox)

-

	1. In __Name__, enter__Timestamp__.
	2. Select __Add__.

-

	1. Confirm that __Timestamp__is added to the field list and select__Save__.

-

	1. The __TutorialTransform__ tile now displays but with an error, because the destination isn't configured yet.

### __Create a destination for the timestamp transformation__

1. Hover over the right edge of the __TutorialTransform__ tile and select the green plus icon.

1. Select __Destinations__>__Eventhouse__. A new tile is created entitled *Eventhouse*.

1. Select the pencil icon on the *Eventhouse* tile.

[](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/pencil-on-event-house.png#lightbox)

1. Enter the following information in the __Eventhouse__ pane:

__Field__ __Value__ __Data ingestion mode__*Event processing before ingestion*__Destination name__*TutorialDestination*__Workspace__ Select the workspace in which you created your resources.

__Eventhouse__*Tutorial*__KQL Database__*Tutorial*__Destination table__*Create new* - enter *RawData* as table name__Input data format__ *Json*

1. Ensure that the box __Activate ingestion after adding the data__ is checked.
2. Select __Save__.

1. From the menu ribbon, select __Publish__.

The eventstream is now set up to transform events and send them to a KQL database.

## Transform data in your KQL Database

In this part of the tutorial, you learn how to use an update policy to transform data in a KQL Database in Real-Time Intelligence. Update policies are automation mechanisms triggered when new data is written to a table. They eliminate the need for special orchestration by running a query to transform the ingested data and save the result to a destination table. Multiple update policies can be defined on a single table, allowing for different transformations and saving data to multiple tables simultaneously. The target tables can have a different schema, retention policy, and other policies from the source table.

### __Move raw data table to a bronze folder__

In this step, you move the raw data table into a Bronze folder to organize the data in the KQL database.

1. From the menu ribbon, click on the __Fabric Real Time Intelligence Tutorial workspace__and select the Tutorial__KQL__ __Database.__
2. In the KQL Database, under KQL databases, select the __Tutorial_queryset__.

1. __Copy/paste__the following command to move table into a Bronze folder. Click__Run.__

.alter table RawData (BikepointID:string,Street:string,Neighbourhood:string,Latitude:dynamic,Longitude:dynamic,No_Bikes:long,No_Empty_Docks:long,Timestamp:datetime) with (folder="Bronze")

Correct .alter table RawData (BikepointID:string,Street:string,Neighbourhood:string,Latitude:double,Longitude:double,No_Bikes:long,No_Empty_Docks:long,Timestamp:datetime) with (folder="Bronze")

### __Create target table__

In this step, you create a target table that will be used to store the data that is transformed with the update policy.

1. __Copy/paste__the following command to create a new table called__TransformedData__with a specified schema. Click__Run.__

.create table TransformedData (BikepointID: int, Street: string, Neighbourhood: string, Latitude: dynamic, Longitude: dynamic, No_Bikes: long, No_Empty_Docks: long, Timestamp: datetime, BikesToBeFilled: long, Action: string) with (folder="Silver")

1. Run the command to create the table. You should now see another table under the __Tables__node in the object tree called__TransformedData__.

### __Create function with transformation logic__

In this step, you create a stored function that holds the transformation logic to be used in the update policy. The function parses the *BikepointID* column and adds two new calculated columns.

1. From the menu ribbon, click on the __Fabric Real Time Intelligence Tutorial workspace__and select the Tutorial KQL__Database__.

1. Select __\+New__>__Function__.

1. Edit the function so that it matches the following code, or __copy/paste__ the following command into the query editor.

.create-or-alter function TransformRawData() \{ RawData

| parse BikepointID with \* "BikePoints_" BikepointID:int

| extend BikesToBeFilled = No_Empty_Docks - No_Bikes

| extend Action = iff(BikesToBeFilled > 0, tostring(BikesToBeFilled), "NA")

\}

1. Run the command to create the function. You should now see the function __TransformRawData__under the__Functions__ node in the object tree.

### __Apply update policy__

In this step, you apply an update policy to the target table to transform the data. The update policy uses the stored function *TransformRawData()* to parse the *BikepointID* column and adds two new calculated columns.

1. From the menu ribbon, select __Database__.
2. Select __\+ New__>__Table update policy__.

1. Edit the policy so that it matches the following code, or __copy/paste__ the following command into the query editor.

.alter table TransformedData policy update \`\`\`\[\{ "IsEnabled": true, "Source": "RawData", "Query": "TransformRawData()", "IsTransactional": false, "PropagateIngestionProperties": false \}\]\`\`\`

1. __Run__the command to create the update policy.

### __Verify transformation__

In this step, you verify that the transformation was successful by comparing the output from the source and target tables.

__	Note:__It might take few seconds to see data in the transformed table.

1. __Copy/paste__the following query into the query editor to view 10 arbitrary records in the source table.__Run__ the query.

RawData

| take 10

1. __Copy/paste__the following query into the query editor to view 10 arbitrary records in the target table.__Run__ the query.

TransformedData

| take 10

Notice that the BikepointID column in the target table no longer contains the prefix "BikePoints_".

## Query streaming data using KQL

In this part of the tutorial, you learn how to query your streaming data using KQL. You write a KQL query and visualize the data in a time chart.

### __Write a KQL query__

The name of the table you created from the update policy in a previous step is *TransformedData*. Use this (case-sensitive) name as the data source for your query.

__Tip__If you have a sufficient subscription, you can use the Copilot feature to help you write queries. Copilot provides queries based on data in your table and natural language prompts. For more information, see [__Copilot for Real-Time Intelligence (preview)__](https://learn.microsoft.com/en-us/fabric/fundamentals/copilot-real-time-intelligence)

1. Enter the following query. Then press __Shift \+ Enter__ to run the query.

TransformedData

| where BikepointID > 100 and Neighbourhood == "Chelsea"

| project Timestamp, No_Bikes

| render timechart

This query creates a time chart that shows the number of bikes in the Chelsea neighborhood as a time chart.

[](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/bikes-timechart.png#lightbox)

### __Create a materialized view__

In this step, you create a materialized view, which returns an up-to-date result of the aggregation query (always fresh). Querying a materialized view is more performant than running the aggregation directly over the source table.

1. __Copy/paste__and__run__ the following command to create a materialized view that shows the most recent number of bikes at each bike station:

.create-or-alter materialized-view with (folder="Gold") AggregatedData on table TransformedData \{ TransformedData

   | summarize arg_max(Timestamp,No_Bikes) by BikepointID

\}

1. __Copy/paste__and__run__ the following query to see the data in the materialized view visualized as a column chart:

AggregatedData

| sort by BikepointID

| render columnchart with (ycolumns=No_Bikes,xcolumn=BikepointID)

You will use this query in the next step to create a Real-Time dashboard.

__Important__If you have missed any of the steps used to create the tables, update policy, function, or materialized views, use this script to create all required resources: [__Tutorial commands script__](https://github.com/microsoft/fabric-samples/blob/main/docs-samples/real-time-intelligence/tutorial-commands-script.kql).

## Create a Real-Time Dashboard

In this part of the tutorial, you learn how to create a __Real-Time Dashboard__ in Real-Time Intelligence. You create a Kusto Query Language (KQL) query, create a Real-Time Dashboard, add a new tile to the dashboard, and explore the data visually by adding an aggregation.

### __Create a Real-Time Dashboard__

1. In your KQL queryset, __copy/paste,__and__run__ the following query. This query might already have been run from the previous section in this tutorial. This query returns a column chart showing the most recent number of bikes by *BikepointID*.

AggregatedData

| sort by BikepointID

| render columnchart with (ycolumns=No_Bikes,xcolumn=BikepointID)

1. Select __Pin to dashboard__.

1. Enter the following information:

__Field__ __Value__ __Create new tile__*In a new dashboard*__Dashboard name__*TutorialDashboard*__Tile name__*Recent bikes by Bikepoint ID*__Open dashboard after creation__ *Selected*

1. Select __Create__.

Since you've selected __Open dashboard after creation__, the new Real-Time dashboard, *TutorialDashboard*, opens with the *Recent bikes by Bikepoint* tile. You can also access the Real-Time dashboard by browsing to your workspace and selecting the desired item.

### __Add a new tile to the dashboard__

1. On the top menu bar, toggle from __Viewing__mode to__Editing__ mode.

1. Select __New tile__

1. In the query editor, enter the following query and__run__:

RawData

| where Neighbourhood == "Chelsea"

1. From the menu ribbon, Select __Apply changes__. A new tile is created.

1. Rename the tile by selecting the __More menu \[...\]__on the top right corner of the tile > Tile options >__Rename__.

1. Enter the new name *Chelsea bikes* to rename the tile.

### __Explore the data visually by adding an aggregation__

1. On the new __Chelsea bikes__tile, select the__Explore__ icon.

1. Select __\+ Add__>__Aggregation__.

1. Select __Operator__>__max__and__Column__ > *No_Bikes*.
2. Under __Display Name__, enter *Max_Bikes*.
3. Select __\+ Add grouping__.

1. Select __Group by__ > *Street*.
2. Select __Apply__.

Notice that the query elements are updated to include the __max(No_Bikes) by Street__ aggregation. The resulting table changed to show the total count of bike locations by street.

1. Change the __Visual type__to__Bar chart__.
2. Select __Pin to dashboard__>__In this dashboard__> Tile Name:__MaxBikes__

### __Add a map tile__

1. Select __New tile__.

1. In the query editor, enter and__run__ the following query:

RawData

| where Timestamp > ago(1h)

1. Above the results pane, select __\+ Add visual__.

1. In the __Visual formatting__ pane, enter the following information:

__Field__ __Value__Tile name *Bike locations Map*__Visual type__*Map*__Define location by__*Latitude and longitude*__Latitude column__*Latitude*__Longitude column__*Longitude*__Label column__ *BikepointID*

1. Select __Apply changes__. You can resize the tiles and zoom in on the map as desired.

1. Save the dashboard by selecting the __Save__ icon on the top left corner of the dashboard.

## Create a Power BI report

A Power BI report is a multi-perspective view into a semantic model, with visuals that represent findings and insights from that semantic model. In this section, you use a KQL query output to create a new Power BI report.

### __Build a Power BI report__

1. Browse to the KQL database you created in a previous step, named *Tutorial*.
2. In the object tree, under the KQL database name, select the query workspace called __Tutorial_queryset__.

1. Copy and paste the following query into the query editor and click Run. The output of this query is used as the semantic model for building the Power BI report.

RawData

| summarize arg_max(Timestamp, No_Bikes,  No_Empty_Docks, Neighbourhood, Lat=todouble(Latitude), Lon=todouble(Longitude)) by BikepointID

1. Select __Create Power BI report__. The Power BI report editor opens with the query result available as a data source named__Kusto Query Result__.

### __Add visualizations to the report__

1. In the report editor, select __Visualizations__>__Stacked column chart__ icon.
2. Drag the following fields from __Data__>__Kusto Query Result__to the__Visualizations__ pane.
	- __Neighbourhood__>__X-axis__
	- __No_Bikes__>__Y-axis__
	- __No_Empty_Docks__>__Y-axis__

[](https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/second-visual-report.png#lightbox)

### __Save the report__

1. In the top left corner of the ribbon, select __File__>__Save__.

1. Enter the name *TutorialReport*. Choose your workspace *Fabric Real Time Intelligence Tutorial* and set sensitivity as Public.
2. Select __Continue__.

1. Select __Open the file in Power BI to view, edit, and get a shareable link.__

__		__

## Set an alert on your event stream

In this part of the tutorial, you learn how to set an alert on your eventstream to receive a notification in Teams when the number of bikes falls below a certain threshold.

### __Set an alert on the eventstream__

1. From the left navigation bar, select __Real-Time__.

1. Select the eventstream you created in the previous tutorial named *TutorialEventstream*. The eventstream details page opens.

1. Select __Set alert__

1. A new pane opens. Fill in the fields as follows:

__Field__ __Value__ __Condition__ Check On each event when Field No_Bikes Condition Is less than Value 5 __Action__ __Message me in Teams__ __Save location__ Workspace The workspace in which you created resources Item Create a new item New item name Tutorial

1. Select __Create__.

The alert is set and you receive a notification in Teams when the condition is met.

# Module 3: Clean up resources

Once you finish the tutorial, you might want to delete all resources you created. You can delete the eventstream, eventhouse, KQL queryset, Real-Time dashboard, Fabric Activator, and Power BI report items individually, or you can delete the entire workspace.

-

	1. Select Fabric Real-time Analytics Solution Tutorial in the left-hand navigation menu to return to the workspace artifact view

-

	1. Below the workspace name and description at the top of the workspace header, select Workspace settings.

##### Select General > Remove this workspace. Scroll down.

____ -

	1. Select __Delete__on the warning.
