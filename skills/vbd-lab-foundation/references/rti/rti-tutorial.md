# Fabric Foundation VBD - Real-Time Intelligence Lab Tutorial

> Converted from `Real-time Intelligence Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs).
> Screenshots have been stripped; Microsoft Learn URLs are cited inline throughout.

> **Freshness-verified 2026-09-15** — Cross-checked against Microsoft Learn. Fixes applied per `.vbd/freshness-audit-2026-09-15.md`. Preview features are called out inline where relevant.

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

## Objective

- Create a Fabric workspace for Real-Time Intelligence assets.
- Build an Eventhouse named `Tutorial`.
- Stream Bicycle rentals sample data through `TutorialEventstream`.
- Add a `Timestamp` field before ingestion.
- Store raw events in `RawData` and transformed events in `TransformedData`.
- Use KQL functions, update policies, and materialized views.
- Pin live KQL results to `TutorialDashboard`.
- Create a Power BI report and a Teams alert from real-time data.

## Microsoft Learn references

- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/overview
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/eventhouse
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/create-database
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/create-query-set
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/dashboard-real-time-create
- https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-premium-purchase
- https://app.fabric.microsoft.com/
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/event-stream-edit-button.png#lightbox
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/add-all-fields.png#lightbox
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/select-built-in-function.png#lightbox
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/pencil-on-event-house.png#lightbox
- https://learn.microsoft.com/en-us/fabric/fundamentals/copilot-real-time-intelligence
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/bikes-timechart.png#lightbox
- https://github.com/microsoft/fabric-samples/blob/main/docs-samples/real-time-intelligence/tutorial-commands-script.kql
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/media/tutorial/second-visual-report.png#lightbox

## Modules

### Module 1: Create a Fabric workspace

#### Step 1: Create a Fabric workspace

- Sign in to Fabric at https://app.fabric.microsoft.com/.
- Select **+ New Workspace**.
- Name the workspace `Fabric Real-time Intelligence Tutorial` plus a unique suffix.
- Optionally add a description.
- Expand **Advanced**.
- Select **Fabric capacity** under **License mode**.
- Choose a Fabric capacity you can access.
- Select **Apply**.

**Explanation:** The workspace holds the Eventstream, Eventhouse, KQL queryset, dashboard, Fabric Activator alert, semantic model, and report.
**Checkpoint:** The `Fabric Real-time Intelligence Tutorial` workspace opens.

### Module 2: Build your first Real-time Intelligence Solution in Fabric

#### Step 2: Create an Eventhouse

- In the workspace, select **New item** > **Eventhouse**.
- Enter `Tutorial` as the Eventhouse name.
- Select **Create**.

**Explanation:** Creating the Eventhouse also creates a KQL database named `Tutorial` for storing and querying streaming events.
**Checkpoint:** The `Tutorial` Eventhouse overview page appears.

#### Step 3: Create an Eventstream from Bicycle rentals

- Select **+ New item** > **Eventstream**.
- Name it `TutorialEventstream`.
- Select **Create**.
- In the editor, select **Use sample data** > **Bicycles**.
- Set **Source name** to `TutorialSource`.
- Select **Add**.

**Explanation:** The Bicycle rentals sample provides live bike location, occupancy, and timestamp-like data without requiring an external source.
**Checkpoint:** `TutorialEventstream` is created from `TutorialSource`.

#### Step 4: Add a `Timestamp` field

- Select **Open Eventstream**.
- Select **Edit**.
- On **Transform events or add destination**, select the down arrow.
- Select **Manage fields**.
- Connect the `TutorialEventstream` tile to the `ManageFields` tile.
- Open the pencil icon on `ManageFields`.
- Set **Operation name** to `TutorialTransform`.
- Select **Add all fields**.
- Select **+ Add field**.
- Choose **Built-in Date Time Function** > **SYSTEM.Timestamp()**.
- Set **Name** to `Timestamp`.
- Select **Add**.
- Confirm `Timestamp` appears in the field list.
- Select **Save**.

**Explanation:** The transform enriches each event with ingestion time so later KQL queries can render time charts and filter recent activity.
**Checkpoint:** The canvas shows a `TutorialTransform` tile, even though it still needs a destination.

#### Step 5: Create the `RawData` destination

- Hover over the right edge of `TutorialTransform`.
- Select the green plus icon.
- Select **Destinations** > **Eventhouse**.
- Open the pencil icon on the new Eventhouse tile.
- Set **Ingestion mode** to **Event processing before ingestion**.
- Set **Destination name** to `TutorialDestination`.
- Select the lab workspace.
- Set **Eventhouse** to `Tutorial`.
- Set **KQL Database** to `Tutorial`.
- Set **Destination table** to **Create new** and enter `RawData`.
- Set **Input data format** to **Json**.
- Keep **Activate ingestion after adding the data** checked.
- Select **Save**.
- Select **Publish**.

**Explanation:** The destination writes transformed stream events into the `RawData` table for KQL queries and downstream policies.
**Checkpoint:** Events begin landing in `Tutorial.RawData`.

#### Step 6: Move `RawData` to the Bronze folder

- Open the `Tutorial` KQL Database.
- Select `Tutorial_queryset`.
- Run the table folder command.

```kql
.alter table RawData (BikepointID:string,Street:string,Neighbourhood:string,Latitude:dynamic,Longitude:dynamic,No_Bikes:long,No_Empty_Docks:long,Timestamp:datetime) with (folder="Bronze")

Correct .alter table RawData (BikepointID:string,Street:string,Neighbourhood:string,Latitude:double,Longitude:double,No_Bikes:long,No_Empty_Docks:long,Timestamp:datetime) with (folder="Bronze")
```

**Explanation:** The Bronze folder labels `RawData` as the unrefined landing table. The corrected command captures `Latitude` and `Longitude` as numeric values.
**Checkpoint:** `RawData` appears under the Bronze folder.

#### Step 7: Create `TransformedData`

- Run the table creation command.

```kql
.create table TransformedData (BikepointID: int, Street: string, Neighbourhood: string, Latitude: dynamic, Longitude: dynamic, No_Bikes: long, No_Empty_Docks: long, Timestamp: datetime, BikesToBeFilled: long, Action: string) with (folder="Silver")
```

**Explanation:** `TransformedData` stores parsed and enriched records from `RawData` in the Silver folder.
**Checkpoint:** `TransformedData` appears under **Tables**.

#### Step 8: Create `TransformRawData`

- Open **+ New** > **Function**.
- Paste the function command.
- Run the command.

```kql
.create-or-alter function TransformRawData() { RawData

| parse BikepointID with * "BikePoints_" BikepointID:int

| extend BikesToBeFilled = No_Empty_Docks - No_Bikes

| extend Action = iff(BikesToBeFilled > 0, tostring(BikesToBeFilled), "NA")

}
```

**Explanation:** The function removes the `BikePoints_` prefix and calculates how many bikes are needed at each station.
**Checkpoint:** `TransformRawData` appears under **Functions**.

#### Step 9: Apply the update policy

- Select **Database**.
- Select **+ New** > **Table update policy**.
- Paste the update policy command.
- Run the command.

````kql
.alter table TransformedData policy update ```[{ "IsEnabled": true, "Source": "RawData", "Query": "TransformRawData()", "IsTransactional": false, "PropagateIngestionProperties": false }]```
````

**Explanation:** The update policy runs `TransformRawData()` whenever new rows arrive in `RawData`, then writes the results into `TransformedData`.
**Checkpoint:** New stream events start appearing in `TransformedData` after a short delay.

#### Step 10: Verify the transformation

- Query `RawData`.

```kql
RawData

| take 10
```

- Query `TransformedData`.

```kql
TransformedData

| take 10
```

- Compare `BikepointID` in both tables.

**Explanation:** The target table should contain parsed IDs and the new `BikesToBeFilled` and `Action` columns.
**Checkpoint:** `TransformedData.BikepointID` no longer includes the `BikePoints_` prefix.

#### Step 11: Write a KQL time chart query

- Enter and run the query with **Shift + Enter**.

```kql
TransformedData

| where BikepointID > 100 and Neighbourhood == "Chelsea"

| project Timestamp, No_Bikes

| render timechart
```

**Explanation:** The query filters Chelsea bike stations and renders available bikes over time.
**Checkpoint:** A time chart appears for Chelsea station activity.

#### Step 12: Create `AggregatedData`

- Create the materialized view.

```kql
.create-or-alter materialized-view with (folder="Gold") AggregatedData on table TransformedData { TransformedData

   | summarize arg_max(Timestamp,No_Bikes) by BikepointID

}
```

- Query the materialized view.

```kql
AggregatedData

| sort by BikepointID

| render columnchart with (ycolumns=No_Bikes,xcolumn=BikepointID)
```

**Explanation:** The materialized view keeps the latest bike count per station ready for fast dashboard queries.
**Checkpoint:** `AggregatedData` returns a column chart by `BikepointID`.

#### Step 13: Pin the first dashboard tile

- Run the `AggregatedData` column chart query again.
- Select **Pin to dashboard**.
- Set **Create new tile** to **In a new dashboard**.
- Set **Dashboard name** to `TutorialDashboard`.
- Set **Tile name** to `Recent bikes by Bikepoint ID`.
- Keep **Open dashboard after creation** selected.
- Select **Create**.

**Explanation:** Pinning turns a KQL result into a live dashboard tile.
**Checkpoint:** `TutorialDashboard` opens with `Recent bikes by Bikepoint ID`.

#### Step 14: Add a Chelsea tile

- Switch the dashboard from **Viewing** to **Editing**.
- Select **New tile**.
- Enter and run the query.

```kql
RawData

| where Neighbourhood == "Chelsea"
```

- Select **Apply changes**.
- Open the tile menu.
- Select **Tile options** > **Rename**.
- Rename the tile `Chelsea bikes`.

**Explanation:** A focused tile lets learners monitor a single neighbourhood before adding visual aggregation.
**Checkpoint:** `Chelsea bikes` appears on `TutorialDashboard`.

#### Step 15: Add an aggregation visual

- Select **Explore** on the `Chelsea bikes` tile.
- Select **+ Add** > **Aggregation**.
- Set **Operator** to **max**.
- Set **Column** to `No_Bikes`.
- Set **Display Name** to `Max_Bikes`.
- Select **+ Add grouping**.
- Group by `Street`.
- Select **Apply**.
- Change **Visual type** to **Bar chart**.
- Select **Pin to dashboard** > **In this dashboard**.
- Set **Tile Name** to `MaxBikes`.

**Explanation:** The aggregation turns event rows into a street-level comparison of maximum bike availability.
**Checkpoint:** The dashboard includes a `MaxBikes` bar chart.

#### Step 16: Add a map tile

- Select **New tile**.
- Enter and run the query.

```kql
RawData

| where Timestamp > ago(1h)
```

- Select **+ Add visual**.
- Set **Tile name** to `Bike locations Map`.
- Set **Visual type** to **Map**.
- Set **Define location by** to **Latitude and longitude**.
- Set **Latitude column** to `Latitude`.
- Set **Longitude column** to `Longitude`.
- Set **Label column** to `BikepointID`.
- Select **Apply changes**.
- Save the dashboard.

**Explanation:** The map uses the last hour of events to show where bike stations are reporting activity.
**Checkpoint:** `Bike locations Map` appears and the dashboard is saved.

#### Step 17: Build a Power BI report

- Browse to the `Tutorial` KQL database.
- Select `Tutorial_queryset`.
- Run the query.

```kql
RawData

| summarize arg_max(Timestamp, No_Bikes,  No_Empty_Docks, Neighbourhood, Lat=todouble(Latitude), Lon=todouble(Longitude)) by BikepointID
```

- Select **Create Power BI report**.
- Add a **Stacked column chart**.
- Drag `Neighbourhood` to **X-axis**.
- Drag `No_Bikes` to **Y-axis**.
- Drag `No_Empty_Docks` to **Y-axis**.
- Select **File** > **Save**.
- Name the report `TutorialReport`.
- Choose the `Fabric Real Time Intelligence Tutorial` workspace.
- Set sensitivity to **Public**.
- Select **Continue**.
- Select **Open the file in Power BI to view, edit, and get a shareable link**.

**Explanation:** The report uses a KQL query result as its model so Power BI can visualize the latest state of the stream.
**Checkpoint:** `TutorialReport` is saved in the workspace.

#### Step 18: Set an eventstream alert

- Select **Real-Time**.
- Open `TutorialEventstream`.
- Select **Set alert**.
- Set **Condition** to check each event where `No_Bikes` is less than `5`.
- Set **Action** to **Message me in Teams**.
- Set **Save location** to the lab workspace.
- Set **Item** to **Create a new item**.
- Set **New item name** to `Tutorial`.
- Select **Create**.

**Explanation:** Set alert creates a **Fabric Activator** item. Modern practice: define Activator objects and rules explicitly (rule example: `No_Bikes < 5` grouped by `BikepointID`).
**Checkpoint:** The alert is created and sends a Teams notification when the condition is met.

### Module 3: Clean up resources

#### Step 19: Delete the workspace

- Return to the `Fabric Real-time Analytics Solution Tutorial` workspace item view.
- Select **Workspace settings**.
- Select **General** > **Remove this workspace**.
- Scroll down.
- Select **Delete** on the warning.

**Explanation:** Removing the workspace clears the Eventstream, Eventhouse, KQL queryset, dashboard, Activator item, and Power BI report.
**Checkpoint:** The workspace no longer appears in the Workspaces list.
