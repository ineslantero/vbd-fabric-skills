---

# Freshness audit — Foundation Discovery Labs
**Date:** 2026-09-15
**Auditor:** Scout research subagent
**Fabric release pinned:** learn.microsoft.com/fabric live docs as of 2026-09-15 (semantic-models.md rev 2026-07-06; direct-lake-overview.md rev 2026-09-09; activator-introduction.md rev 2026-08-28; data-wrangler.md rev 2026-09-02).

> Note: my sandbox does not allow file writes, so this report is returned inline. Save it to `vbd-fabric-skills\.vbd\freshness-audit-2026-09-15.md` manually.

## Summary
- Total distinct freshness claims checked: **~32**
- ❌ Outdated / deprecated: **11**
- ⚠️ Preview / caveat / drifted UI: **7**
- ✅ Verified current (not listed below): **~14**
- ❓ Needs manual verification: **2**

---

## Findings per lab

### Lakehouse (`lakehouse-tutorial.md`)

#### ❌ "Add Lakehouse tables to the default semantic model" / "Manage default semantic model"
- **Location:** Objective bullet (line 40); Step 4 (lines 121–124); Step 5 (line 132); Step 13 (lines 283–286).
- **Original claim:** "Open the Reporting tab. Select **Manage default semantic model**. Add `dimension_customer` to the default semantic model."
- **Current state:** As of **5 Sept 2025**, Fabric no longer auto-creates default semantic models on new lakehouses/warehouses/mirrored DBs. By **30 Nov 2025** all existing default models were decoupled into independent semantic models. The **Manage default semantic model** entry point is gone.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models (note block, top of page).
- **Recommended fix:** Replace with: "From the Lakehouse ribbon select **New Power BI semantic model**, name it `wwilakehouse_model`, pick the tables to include, then **Confirm**." Link: https://learn.microsoft.com/en-us/fabric/data-warehouse/create-semantic-model.

#### ❌ "Leave **Lakehouse schemas** unchecked if the option appears"
- **Location:** Step 2 (line 79).
- **Original claim:** Guidance to leave schemas off.
- **Current state:** Schemas are **enabled by default** on new lakehouses and are a prerequisite for materialized lake views and schema shortcuts. Leaving them off blocks several current features.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-schemas ("Schemas are enabled by default when you create a lakehouse in the Fabric portal").
- **Recommended fix:** "Keep **Lakehouse schemas** checked (default). Tables will be created under the `dbo` schema."

#### ❌ Advanced workspace "Trial / Fabric capacity / Power BI Premium capacity" wording
- **Location:** Step 1 (line 65).
- **Current state:** The Advanced pane now exposes **License mode** with options *Trial*, *Fabric capacity*, *Pro*, *Premium Per User*. Standalone "Power BI Premium (per capacity)" P SKUs have been retired for new purchases; capacity assignment is via F SKU or Trial.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces (Advanced settings → Workspace type / License mode).
- **Recommended fix:** "Under **License mode**, select **Trial** or **Fabric capacity** and pick a capacity you can access."

#### ❌ WWI sample dataset URL is dead
- **Location:** Objective (line 51); Step 6 (line 151).
- **Original claim:** `https://assetsprod.microsoft.com/en-us/wwi-sample-dataset.zip`
- **Current state:** URL 301-redirects to `partner.microsoft.com/access-denied`. The pipeline step will fail.
- **Recommended fix:** Use the version documented in the current Fabric lakehouse tutorial, which sources the same WWI sample dataset via the Learn-hosted asset. Verify against https://learn.microsoft.com/en-us/fabric/data-engineering/tutorial-build-lakehouse and https://github.com/microsoft/fabric-samples for a maintained mirror. `❓ needs manual verification of exact replacement URL — current MS Learn tutorial page could not be fetched in this session.`

#### ⚠️ "Switch to the **Data engineering** workload" via experience switcher
- **Location:** Step 7 (line 173).
- **Current state:** Fabric has consolidated the persona/experience switcher; workloads are surfaced through the left-nav workload panel and via **New item**. The verb "Switch to the Data engineering workload" is no longer a step users perform.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces (workspace-driven navigation, no persona switcher).
- **Recommended fix:** Delete the step; users can select **Import notebook** directly from the Lakehouse or workspace **New item** menu.

#### ⚠️ Pipeline "Copy Data Assistant" naming
- **Location:** Step 6 (line 149).
- **Current state:** UI now labels it **Copy assistant** (dropped "Data"). Not blocking.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-factory/create-first-dataflow-gen2 and related Copy activity docs.

#### ⚠️ DirectLake fallback assumption in Step 14
- **Location:** Step 14 explanation (line 315).
- **Current state:** Direct Lake still applies; but Direct Lake on OneLake is now the recommended flavor (Direct Lake on SQL still exists). The "Direct Lake" reference in this tutorial is accurate but the modern nomenclature distinguishes "Direct Lake on OneLake" vs "on SQL analytics endpoint".
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview.
- **Fix:** Optional — reword as "Direct Lake mode analyzes Delta tables in OneLake directly, without importing data."

---

### Warehouse (`warehouse-tutorial.md`)

#### ❌ "Manage default semantic model" (twice)
- **Location:** Step 4 (lines 121–124); Step 10 (lines 267–269).
- **Current state:** Same as Lakehouse finding — the default semantic model surface is gone; you must explicitly create a Power BI semantic model.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models; https://learn.microsoft.com/en-us/fabric/data-warehouse/create-semantic-model.
- **Recommended fix:** "From the Warehouse ribbon select **New semantic model**, name it, select `dimension_customer` (and later `fact_sale`/`dimension_city`), then **Confirm**."

#### ❌ "Choose **Premium capacity** under **License mode**"
- **Location:** Step 1 (line 73).
- **Current state:** "Premium capacity" is no longer a Fabric workspace license mode; use **Fabric capacity** or **Trial**.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces (License mode section).
- **Recommended fix:** "Choose **Fabric capacity** under **License mode** and pick an F-SKU (or **Trial**)."

#### ❌ SharePoint IP links in Microsoft Learn references
- **Location:** Lines 51, 53, 59, 60.
- **Current state:** `microsofteur.sharepoint.com/…/TridentPrivatePreview/…` and `TridentOnboardingCoreTeam` links are internal SharePoint URLs that fail for external customers and belong to the pre-GA "Trident" project name.
- **Recommended fix:** Replace with public Learn docs: https://learn.microsoft.com/en-us/fabric/data-warehouse/data-warehousing and https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-introduction.

#### ⚠️ `OPTION (FOR TIMESTAMP AS OF ...)` time-travel example uses 2024 timestamps
- **Location:** Step 11 (lines 305–309).
- **Current state:** Syntax still current for Warehouse time travel. Timestamps are illustrative but confusingly hard-coded to Aug-2024 — will not return rows in a 2026 lab.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-warehouse/time-travel.
- **Recommended fix:** Show `SELECT CURRENT_TIMESTAMP;` first, then reuse that captured value (or ~2 minutes earlier) as the AS OF timestamp.

#### ⚠️ Clone Table UI path — "**Table tools**" vs table context menu
- **Location:** Step 12 (line 318).
- **Current state:** Clone-table entry point today is the table **… (More options) → Clone table** in Object explorer, or Query editor **New SQL query** using `CREATE TABLE … AS CLONE OF …`. "Table tools" ribbon phrasing is stale.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-warehouse/clone-table.
- **Recommended fix:** "Right-click `dimension_customer` in **Explorer** → **Clone table**."

---

### RTI (`rti-tutorial.md`)

#### ❌ "Activator" naming and workspace-remove phrasing
- **Location:** Workspace explanation (line 112 references "Activator alert"); Step 19 phrasing.
- **Current state:** The product is now branded **Fabric Activator** (was "Data Activator"). Both "Activator" and "Fabric Activator" are acceptable; the tutorial's naming is fine but references to Reflex/Data Activator should be normalized. Also, the item type for an alert is called an **Activator** item.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/activator-introduction (page title: "What is Fabric Activator?").
- **Recommended fix:** Use "Fabric Activator" on first mention.

#### ❌ Real-Time hub → Sample scenarios → Bicycle rentals create flow
- **Location:** Step 3 (lines 128–139).
- **Current state:** The current official RTI tutorial creates the Eventstream first (**+ New item → Eventstream**), then inside the eventstream editor adds a source from **Sample data → Bicycles**. The "**Real-Time** > **+ Add data** > **Sample scenarios**" landing-page tile no longer exists as described; sample data is added from within the eventstream editor.
- **MS Learn sources:** https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/create-manage-an-eventstream and https://learn.microsoft.com/en-us/fabric/real-time-intelligence/tutorial-introduction ("Get data in the Real-Time hub" step is now via eventstream editor).
- **Recommended fix:** Rewrite: "Select **+ New item → Eventstream**, name it `TutorialEventstream`, select **Create**, then in the editor select **Use sample data → Bicycles**, source name `TutorialSource`, **Add**."

#### ❌ "Set alert" from an eventstream directly to Teams
- **Location:** Step 18 (lines 408–421).
- **Current state:** The eventstream **Set alert** button creates a **Fabric Activator** item; "Message me in Teams" is still available but is now one of several Activator actions. Docs recommend defining Activator objects/rules rather than a one-off alert.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/activator-introduction (Core architecture → Rules, Actions).
- **Recommended fix:** Note that "Set alert" creates a Fabric Activator item; rule is now expressed as `No_Bikes < 5` on an object grouped by `BikepointID`.

#### ❌ "Dashboard" auto-refresh vs Real-Time Dashboard renaming
- **Location:** Step 13 tile name references "Real-Time Dashboard".
- **Current state:** "Real-Time Dashboard" is still the product name (used consistently in learn.microsoft.com/en-us/fabric/real-time-intelligence/dashboard-real-time-create). ✅ Actually current. (Kept in the ✅ bucket.)

#### ⚠️ KQL Database `TutorialDestination` — Ingestion mode UI label
- **Location:** Step 5 (line 172).
- **Current state:** The label **Data ingestion mode: Event processing before ingestion** was renamed **Ingestion mode: Event processing before ingestion** and now also offers **Direct ingestion** as the default. Not breaking.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-destination-eventhouse.
- **Recommended fix:** Reword to "Set **Ingestion mode** to **Event processing before ingestion**."

#### ⚠️ `Tutorial_queryset` auto-creation
- **Location:** Step 6 (line 185), Step 17 (line 384).
- **Current state:** Eventhouse now creates a **queryset** and an embedded **KQL queryset** tab automatically. The name may not be `<KQLdb>_queryset` in current UI; it's typically the KQL database name. Non-blocking but flag.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/real-time-intelligence/create-query-set.

#### ⚠️ SharePoint-based screenshot / GitHub sample link
- **Location:** GitHub URL line 94: `https://github.com/microsoft/fabric-samples/blob/main/docs-samples/real-time-intelligence/tutorial-commands-script.kql`. This path currently resolves (verify) but repo layout has changed multiple times.
- **Recommended:** Pin to a specific commit SHA in `sources.yaml`.

---

### Data Science (`datascience-tutorial.md`)

#### ❌ "Manage default semantic model" implied via `New semantic model` step
- **Location:** Step 25 (lines 434–442).
- **Original claim:** Directly creating a **New semantic model** from the Lakehouse is still supported — **no change needed here**. But the tutorial's underlying assumption elsewhere (that Lakehouse auto-provisions one) is stale. ✅ Step 25 itself is current per https://learn.microsoft.com/en-us/fabric/data-warehouse/create-semantic-model.

#### ❌ "Switch to Fabric from the experience switcher"
- **Location:** Step 2 (line 172).
- **Current state:** The experience switcher has been removed; Fabric is now the default surface. Users no longer explicitly switch to a persona.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces (no persona-switcher step), and Data Wrangler doc still shows an old screenshot but the doc note treats it as legacy.
- **Recommended fix:** Delete this bullet.

#### ⚠️ "Verify the workspace uses Spark version 3 or higher"
- **Location:** Step 2 (line 174).
- **Current state:** Fabric Runtime 1.3 (Spark 3.5) is GA and Runtime 1.4 (Spark 3.5.x + Delta 3.x) is available. "Spark 3 or higher" is trivially true; step is meaningless today.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-engineering/runtime.
- **Recommended fix:** "Confirm the workspace default runtime is Fabric Runtime 1.3 or newer."

#### ⚠️ "Select **Data Wrangler** from the notebook ribbon"
- **Location:** Step 7 (line 236); Step 13 (line 301).
- **Current state:** The current path is **Home tab → Data Wrangler dropdown → choose DataFrame**. Also, Data Wrangler can be launched inline from a cell that outputs a DataFrame. The tutorial's wording is close but not literal.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler ("In the notebook ribbon 'Home' tab, use the Data Wrangler dropdown…").
- **Recommended fix:** "On the **Home** tab, open the **Data Wrangler** dropdown, then select `df`."

#### ⚠️ MLflow autologging — "Enable autologging" step is redundant
- **Location:** Step 17 (line 351).
- **Current state:** Autolog is enabled automatically when a Data Science notebook runs `import mlflow`. Fabric MLflow 3 now also captures **GenAI traces** by default (`log_traces=True`).
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-science/mlflow-autologging (Configuration section: "Microsoft Fabric calls `mlflow.autolog()` to instantly enable tracking").
- **Recommended fix:** Reword: "Confirm autologging is active (Fabric enables it by default). Set the experiment name via `mlflow.set_experiment('bank-churn-experiment')`."

#### ⚠️ "SynapseML Transformer API wraps the registered MLflow model"
- **Location:** Step 22 explanation (line 411).
- **Current state:** The `MLFlowTransformer` class is provided in Fabric under `synapse.ml.predict` and remains supported. The user-visible naming in current docs is **PREDICT with the Transformer API**, not "SynapseML Transformer API".
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-science/model-scoring-predict (Limitations + Call PREDICT).
- **Recommended fix:** "The Transformer API (`MLFlowTransformer`) wraps the registered MLflow model for Spark batch scoring." Confirm PREDICT flavor list matches (`LightGBM` ✓).

#### ⚠️ Local `C:\Users\LabUser\Documents\LabFiles\…` path for `churn.csv`
- **Location:** Step 4 (line 205).
- **Current state:** Hard-coded lab image path may not exist in newer lab VMs. Non-Fabric issue but customer-facing.
- **Recommended fix:** Reference the churn dataset via a public URL: `https://synapseaisolutionsa.blob.core.windows.net/public/bankcustomerchurn/churn.csv` (as used in current MS Learn DS tutorial).
- **Source:** https://learn.microsoft.com/en-us/fabric/data-science/tutorial-data-science-explore-notebook.

#### ❓ `%pip install imbalanced-learn` inline install
- **Location:** Step 15 (lines 330–334).
- **Current state:** Notebook-scoped `%pip install` still works. However Fabric now offers **workspace environments** with pinned libraries as the recommended pattern.
- **MS Learn source:** https://learn.microsoft.com/en-us/fabric/data-engineering/environment-workspace-migration.
- **Fix:** Non-blocking — mention environments as preferred.

---

## Cross-cutting fixes

- **Default semantic model deprecation** (❌) — apply the same fix to **Lakehouse Step 4, Step 5, Step 13** and **Warehouse Step 4, Step 10**. Use `New semantic model` / `New Power BI semantic model` ribbon action. Single source: https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models.
- **Workspace License mode wording** (❌) — Lakehouse Step 1 and Warehouse Step 1: drop "Power BI Premium capacity" and standardize on **Trial** or **Fabric capacity**. Source: https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces.
- **Experience switcher removal** (⚠️) — Lakehouse Step 7 and Data Science Step 2 both instruct users to switch workload/experience; drop or reword.
- **"Manage default semantic model" ribbon** — every mention is now dead UI. Search all four files for that string.
- **Product renaming** — "Data Activator" → **Fabric Activator** (RTI intro references).

## Learn URLs that should be added to `sources.yaml`

Common:
- https://learn.microsoft.com/en-us/fabric/data-warehouse/semantic-models
- https://learn.microsoft.com/en-us/fabric/data-warehouse/create-semantic-model
- https://learn.microsoft.com/en-us/fabric/fundamentals/create-workspaces
- https://learn.microsoft.com/en-us/fabric/fundamentals/direct-lake-overview
- https://blog.fabric.microsoft.com/blog/sunsetting-default-semantic-models-microsoft-fabric
- https://blog.fabric.microsoft.com/blog/decoupling-default-semantic-models-for-existing-in-microsoft-fabric

Lakehouse:
- https://learn.microsoft.com/en-us/fabric/data-engineering/lakehouse-schemas
- https://learn.microsoft.com/en-us/fabric/data-engineering/runtime
- https://learn.microsoft.com/en-us/fabric/data-engineering/tutorial-build-lakehouse

Warehouse:
- https://learn.microsoft.com/en-us/fabric/data-warehouse/time-travel
- https://learn.microsoft.com/en-us/fabric/data-warehouse/clone-table
- https://learn.microsoft.com/en-us/fabric/data-warehouse/tutorial-introduction

RTI:
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/data-activator/activator-introduction
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/create-manage-an-eventstream
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/event-streams/add-destination-eventhouse
- https://learn.microsoft.com/en-us/fabric/real-time-intelligence/tutorial-introduction

Data Science:
- https://learn.microsoft.com/en-us/fabric/data-science/mlflow-autologging
- https://learn.microsoft.com/en-us/fabric/data-science/mlflow-3-overview
- https://learn.microsoft.com/en-us/fabric/data-science/model-scoring-predict
- https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler
- https://learn.microsoft.com/en-us/fabric/data-science/tutorial-data-science-explore-notebook

---

## Gaps / uncertainties

- **WWI sample dataset replacement URL** (Lakehouse Step 6): confirmed old URL is dead but could not fetch current `tutorial-build-lakehouse` page in this session to pin the replacement. Requires manual verification.
- **`fabric-samples` repo path** for RTI `tutorial-commands-script.kql`: link resolves at the moment but this repo reorganizes often; pin a commit SHA.
- **Data engineering "workload"** existence: the workload panel still exists but the persona/experience switcher has been consolidated — the exact UI copy at 2026-09-15 may differ from what's in the Learn `create-workspaces` doc. Flagged ⚠️, not ❌.
- **`data-activator/data-activator-introduction` old URL** now 301-redirects to `real-time-intelligence/data-activator/activator-introduction` — confirms the docs move; page title is "What is Fabric Activator?".
