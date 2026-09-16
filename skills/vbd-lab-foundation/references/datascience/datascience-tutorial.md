# Fabric Foundation VBD - Data Science Lab Tutorial

> Converted from `Data Science Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs).
> Screenshots have been stripped; Microsoft Learn URLs are cited inline throughout.

> **Freshness-verified 2026-09-15** — Cross-checked against Microsoft Learn. Fixes applied per `.vbd/freshness-audit-2026-09-15.md`. Preview features are called out inline where relevant.

## Contents

- Introduction

- Prerequisites

- The Data Science end-to-end scenario

- Different components of Data science scenario

- Import tutorial notebooks

- Attach a lakehouse to the notebooks.

- Module 1: Ingest data into Fabric lakehouse

- __Sample Data__

- __Upload the csv file to lakehouse__

- Module 2: Explore data

- __Read raw data from the Lakehouse__

- __Create a pandas DataFrame from the dataset__

- __Use Data Wrangler to perform initial data cleaning__

- __Drop duplicate rows__

- __Drop rows with missing data__

- __Drop Columns__

- __Add code to notebook__

- __Explore the data__

- __Determine categorical, numerical, and target attributes__

- __The five-number summary__

- __Distribution of exited and nonexited customers__

- __Distribution of numerical attributes__

- __Perform feature engineering__

- __Use Data Wrangler to perform one-hot encoding__

- __Summary of observations from the exploratory data analysis__

- __Create a delta table for the cleaned data__

- Module 3: Train and register machine learning models

- __Load the data__

- __Generate experiment for tracking and logging the model using MLflow__

- __Set experiment and autologging specifications__

- __Import scikit-learn and LightGBM__

- __Prepare training, validation and test datasets__

- __Save test data to a delta table__

- __Apply SMOTE to the training data to synthesize new samples for the minority class__

- __Model training__

- __Experiments artifact for tracking model performance__

- __Assess the performances of the trained models on the validation dataset__

- __Show True/False Positives/Negatives using the Confusion Matrix__

- Module 4: Perform batch scoring and save predictions to a Lakehouse

- __Load the test data__

- __PREDICT with the Transformer API__

- __Instantiate MLFlowTransformer object__

- __PREDICT with the Spark SQL API__

- __PREDICT with a user-defined function (UDF)__

- __Write model prediction results to the lakehouse__

- Module 5: Visualize predictions with a Power BI report

- __Create a semantic model__

- __Add new measures__

- __Create new report__

- __The Power BI report shows:__

- __Summary__

## Objective

- Import the Data Science tutorial notebooks.
- Attach a Lakehouse to each notebook.
- Upload `churn.csv` into the Lakehouse **Files** area.
- Clean customer churn data with Data Wrangler and notebook code.
- Engineer features and save cleaned data as a Delta table.
- Train Random Forest and LightGBM models with MLflow tracking.
- Score test data with Fabric PREDICT options.
- Build a Power BI report over `customer_churn_test_predictions`.

## Microsoft Learn references

- https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview
- https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-premium-purchase
- https://learn.microsoft.com/en-us/fabric/enterprise/buy-subscription
- https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial
- https://mlflow.org/docs/latest/index.html
- https://docs.delta.io/latest/index.html
- https://seaborn.pydata.org/
- https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-explore-notebook/preview.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-explore-notebook/drop-duplicate.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-explore-notebook/drop-missing.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-explore-notebook/drop-columns.png#lightbox
- https://mlflow.org/docs/latest/index.html
- https://aka.ms/fabric/create-environment
- https://learn.microsoft.com/en-us/fabric/data-engineering/library-management#scenario-1-admin-sets-default-libraries-for-the-workspace
- https://learn.microsoft.com/en-us/fabric/data-engineering/environment-workspace-migration
- https://aka.ms/fabric-autologging
- https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html
- https://imbalanced-learn.org/stable/over_sampling.html#smote-adasyn
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-train-models/filter-workspace.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-train-models/experiment-runs.png#lightbox
- https://aka.ms/samples/frauddectection
- https://learn.microsoft.com/en-us/fabric/data-science/model-scoring-predict
- https://learn.microsoft.com/fabric/data-science/tutorial-data-science-train-models
- https://aka.ms/fabric/predict-from-model-item
- https://learn.microsoft.com/en-us/fabric/data-science/tutorial-data-science-batch-scoring
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/churn-rate.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/card-churn.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/age.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/number-of-products.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/new-credit-score.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/change-title.png#lightbox
- https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/germany-spain-france.png#lightbox

## Modules

### Module 1: Set up the notebooks and Lakehouse

#### Step 1: Check prerequisites

- Confirm access to Power BI Premium, Fabric F SKU, or Fabric Trial capacity.
- Confirm a Power BI workspace is assigned to that capacity.
- Confirm an existing Fabric Lakehouse is available, or create one from the Lakehouse tutorial.

**Explanation:** The notebooks need Spark-backed Fabric capacity and a Lakehouse for files, Delta tables, and predictions.
**Checkpoint:** You can open a Fabric workspace with a Lakehouse attached to capacity.

#### Step 2: Import the tutorial notebooks

- Open or create a workspace named `Data Science Tutorial`.
- Confirm the workspace default runtime is **Fabric Runtime 1.3** or newer.
- Download notebooks 1-4 (`.ipynb`) from the lab **Scripts** folder.
- Select **Import** > **Notebook** > **From this computer**.
- Select **Upload** in the **Import Status** pane.
- Upload all four Jupyter notebooks.
- Confirm the notebooks imported successfully.
- Open each notebook to validate it loads.
- If a notebook contains output, select **Edit** > **Clear all outputs**.

**Explanation:** The lab is driven by notebooks, so importing clean copies gives learners a repeatable starting point.
**Checkpoint:** The four imported notebooks appear in the `Data Science Tutorial` workspace.

#### Step 3: Attach a Lakehouse to each notebook

- Open the first notebook, `1 Ingest data`.
- Remove any previously attached Lakehouse items.
- Select **Lakehouses** > **Add lakehouse**.
- Choose **New** to create a Lakehouse, or choose **Existing lakehouse**.
- Ensure the Lakehouse is in the same workspace.
- Select **Create** or **Add**.
- Confirm the Lakehouse pane shows **Tables** and **Files**.
- Repeat this attachment step for each notebook used in Modules 1-4.

**Explanation:** The default Lakehouse controls where notebook code reads files and writes Delta tables.
**Checkpoint:** Each notebook opens with the same Lakehouse attached.

#### Step 4: Upload `churn.csv`

- Open the Lakehouse attached to the notebooks.
- Go to **Files**.
- Select **Upload files**.
- Download `churn.csv` from `https://synapseaisolutionsa.blob.core.windows.net/public/bankcustomerchurn/churn.csv`, then upload it.
- Confirm the file appears in **Files**.

**Explanation:** The bank churn dataset contains 10,000 customers with geography, gender, age, tenure, balance, salary, product count, credit card status, active member status, and `exited` churn status.
**Checkpoint:** `churn.csv` is visible in the Lakehouse **Files** area.

### Module 2: Explore data

#### Step 5: Read raw data from the Lakehouse

- Open the `2-explore-cleanse-data` notebook.
- Confirm the same Lakehouse from Module 1 is attached.
- Run the notebook cells that read `churn.csv` from **Files**.
- Confirm the Spark DataFrame loads.

**Explanation:** Spark reads the raw file from OneLake so the same data can be cleaned, transformed, and saved as Delta.
**Checkpoint:** The raw churn data displays in the notebook.

#### Step 6: Create a pandas DataFrame

- Convert the Spark DataFrame to a pandas DataFrame named `df`.
- Display the first rows.
- Import required analysis libraries, including NumPy, pandas, seaborn, and Matplotlib.
- Display summary statistics.

**Explanation:** pandas and seaborn are convenient for local exploratory analysis and visualization once the sample data is in memory.
**Checkpoint:** `df` exists and the notebook shows summary output.

#### Step 7: Open Data Wrangler

- Wait until the notebook kernel is idle.
- On the **Home** tab, open the **Data Wrangler** dropdown, then select `df`.
- Review the generated descriptive overview.
- Select columns to see the Summary pane update.

**Explanation:** Data Wrangler provides click-driven profiling and cleaning while generating reusable notebook code.
**Checkpoint:** Data Wrangler opens on `df` and shows column summaries.

#### Step 8: Drop duplicate rows

- Expand **Find and replace**.
- Select **Drop duplicate rows**.
- Select `RowNumber` and `CustomerId` as comparison columns.
- Review the preview.
- Select **Apply**.

**Explanation:** Duplicate customer identifiers can distort churn counts and model training.
**Checkpoint:** A duplicate-removal step appears in the Data Wrangler cleaning steps.

#### Step 9: Drop rows with missing data

- Select **Drop missing values** from **Find and replace**.
- Choose **Select all** for target columns.
- Review the preview.
- Select **Apply**.

**Explanation:** Removing incomplete rows keeps the starter model flow simple and avoids null-handling distractions.
**Checkpoint:** A missing-value removal step appears in the cleaning steps.

#### Step 10: Drop unused columns

- Expand **Schema**.
- Select **Drop columns**.
- Select `RowNumber`, `CustomerId`, and `Surname`.
- Review the red-highlighted preview columns.
- Select **Apply**.

**Explanation:** These identifiers do not help explain churn and can introduce noise or leakage.
**Checkpoint:** `RowNumber`, `CustomerId`, and `Surname` are removed from the preview.

#### Step 11: Add Data Wrangler code to the notebook

- Select **Preview code for all steps**.
- Review the combined generated code.
- Select **Add code to notebook**.
- Run the new notebook cell manually.
- If you skipped Data Wrangler, run the optional code cell that performs the same cleaning with `inplace=True`.

**Explanation:** Data Wrangler only adds code; it does not apply the transformation until the generated notebook cell runs.
**Checkpoint:** The cleaned DataFrame is available for exploration.

#### Step 12: Explore the cleaned data

- Display summaries and visualizations of the cleaned data.
- Determine categorical, numerical, and target attributes.
- Create the five-number summary for numerical attributes with box plots.
- Plot exited versus nonexited customers across categorical attributes.
- Plot frequency distributions for numerical attributes.

**Explanation:** Exploratory data analysis highlights class balance, feature ranges, and candidate predictors before model training.
**Checkpoint:** The notebook shows summaries, box plots, categorical distributions, and histograms.

#### Step 13: Engineer features and one-hot encode

- Generate new attributes from existing fields.
- On the **Home** tab, open the **Data Wrangler** dropdown, then select `df`.
- Expand **Formulas**.
- Select **One-hot encode**.
- Select `Geography` and `Gender`.
- Add the generated code to the notebook, or copy it into a new cell.
- If you skipped Data Wrangler, run the optional one-hot encoding code cell.

**Explanation:** Feature engineering and one-hot encoding turn business attributes into model-ready numeric columns.
**Checkpoint:** `df_clean` includes encoded geography and gender fields such as `Geography_Germany`, `Geography_Spain`, and `Geography_France`.

#### Step 14: Save the cleaned Delta table

- Review the EDA observations:
  - Most customers are from France, while Spain has the lowest churn rate.
  - Most customers have credit cards.
  - Age above 60 and credit score below 400 appear but are not treated as outliers here.
  - Very few customers have more than two bank products.
  - Inactive customers have a higher churn rate.
  - Gender and tenure do not appear to drive churn strongly.
- Run the notebook cell that saves the cleaned data as a Delta table.

**Explanation:** The cleaned Delta table becomes the stable input for model training in the next notebook.
**Checkpoint:** The cleaned churn table is available in the Lakehouse **Tables** area.

### Module 3: Train and register machine learning models

#### Step 15: Install session libraries

- Open the `03 – train-evaluate` notebook.
- Run the first cell that installs `imbalanced-learn` with `%pip install`.
- Restart or continue after the PySpark kernel restart.
- Re-run the install after any notebook session restart.

**Explanation:** SMOTE comes from `imblearn`, and notebook-scoped library installs do not persist across sessions. Use a Fabric environment for shared library management.
**Checkpoint:** The notebook can import `imblearn` without `ModuleNotFoundError`.

#### Step 16: Load the cleaned data

- Attach the same Lakehouse used in Module 2.
- Load the cleaned Delta table.
- Confirm the target column and feature columns are present.

**Explanation:** Training starts from the prepared table rather than the raw CSV.
**Checkpoint:** The training notebook displays the cleaned data.

#### Step 17: Configure MLflow tracking

- Generate the experiment for model tracking and logging.
- Set model parameters and scoring metrics.
- Confirm autologging is active (Fabric enables it by default when you `import mlflow`). Set the experiment name via `mlflow.set_experiment('bank-churn-experiment')`.

**Explanation:** Fabric integrates MLflow experiments and runs into the workspace so parameters, metrics, and models remain traceable.
**Checkpoint:** The experiment named `bank-churn-experiment` is created or updated in the workspace.

#### Step 18: Prepare training, validation, and test sets

- Import scikit-learn and LightGBM.
- Use `train_test_split` to split the dataset.
- Save the test data to a Delta table for the scoring notebook.
- Apply SMOTE only to the training data.

**Explanation:** Validation and test data must keep their original class distribution so model quality reflects production-like imbalance.
**Checkpoint:** Training, validation, and test datasets exist, and test data is saved to the Lakehouse.

#### Step 19: Train and compare models

- Train a Random Forest model with maximum depth 4 and 4 features.
- Train a Random Forest model with maximum depth 8 and 6 features.
- Train a LightGBM model.
- Open the workspace.
- Filter to show experiments.
- Open `bank-churn-experiment`.
- Review logged runs, parameters, metrics, and models.

**Explanation:** Comparing multiple runs helps select the best churn model while preserving reproducible training metadata.
**Checkpoint:** The experiment shows runs for both Random Forest configurations and LightGBM.

#### Step 20: Assess model performance

- Load the trained models from the experiment, or use the in-memory trained models.
- Score the validation dataset.
- Compare performance metrics.
- Plot confusion matrices for:
  - Random Forest Classifier with maximum depth 4 and 4 features
  - Random Forest Classifier with maximum depth 8 and 6 features
  - LightGBM

**Explanation:** Confusion matrices expose true positives, false positives, true negatives, and false negatives, which are essential for churn intervention decisions.
**Checkpoint:** Validation metrics and confusion matrices are visible for all three models.

### Module 4: Perform batch scoring and save predictions to a Lakehouse

#### Step 21: Load the test data

- Open the scoring notebook from the imported notebook set.
- Attach the same Lakehouse used in Module 3.
- Load the test Delta table saved during training.

**Explanation:** The scoring notebook uses held-out data so predictions can be reviewed separately from training.
**Checkpoint:** The test DataFrame loads successfully.

#### Step 22: Score with the Transformer API

- Identify the registered LightGBM model `lgbm_sm` version `1`.
- Create an `MLFlowTransformer` object.
- Provide all test DataFrame input columns.
- Set the output column name to `predictions`.
- Run the Transformer API prediction cell.

**Explanation:** PREDICT with the **Transformer API** (`MLFlowTransformer`) wraps the registered MLflow model for scalable Spark batch scoring.
**Checkpoint:** The output DataFrame includes a `predictions` column.

#### Step 23: Score with Spark SQL and UDF options

- Run the Spark SQL API cell that invokes `PREDICT`.
- Run the PySpark user-defined function cell that invokes `PREDICT`.
- Compare the results with the Transformer API output.

**Explanation:** Fabric PREDICT supports multiple calling patterns so teams can score from SQL-first or Python-first workflows.
**Checkpoint:** All scoring paths produce prediction results for the test data.

#### Step 24: Write predictions to the Lakehouse

- Write the model prediction results back to the Lakehouse.
- Use the `customer_churn_test_predictions` table name.
- Refresh the Lakehouse **Tables** area.

**Explanation:** Persisted predictions become reusable for Power BI reporting and downstream analysis.
**Checkpoint:** `customer_churn_test_predictions` appears in the Lakehouse.

### Module 5: Visualize predictions with a Power BI report

#### Step 25: Create the semantic model

- Open the workspace.
- Filter item type to **Lakehouse**.
- Select the Lakehouse used in previous modules.
- Select **New semantic model**.
- Name it `bank churn predictions`.
- Select `customer_churn_test_predictions`.
- Select **Confirm**.

**Explanation:** The semantic model exposes scored churn predictions to Power BI report authors.
**Checkpoint:** The `bank churn predictions` semantic model is created.

#### Step 26: Add the churn measures

- Open the `bank churn predictions` semantic model.
- Select **Open data model**.
- Switch to editing mode.
- Select **New measure**.
- Replace `Measure =` with the churn rate formula.

```DAX
Churn Rate = AVERAGE(customer_churn_test_predictions[predictions])
```

- Apply the formula.
- Format the measure as **Percentage** with 1 decimal place.
- Add the customer count measure.

```DAX
Customers = COUNT(customer_churn_test_predictions[predictions])
```

- Add the Germany churn measure.

```DAX
Germany Churn = CALCULATE(AVERAGE(customer_churn_test_predictions[predictions]),FILTER(customer_churn_test_predictions, customer_churn_test_predictions[Geography_Germany] = TRUE()))
```

- Repeat for Spain and France.

```DAX
Spain Churn = CALCULATE(AVERAGE(customer_churn_test_predictions[predictions]),FILTER(customer_churn_test_predictions, customer_churn_test_predictions[Geography_Spain] = TRUE()))

France Churn = CALCULATE(AVERAGE(customer_churn_test_predictions[predictions]),FILTER(customer_churn_test_predictions, customer_churn_test_predictions[Geography_France] = TRUE()))
```

**Explanation:** Measures summarize predictions into report-ready churn metrics overall and by geography.
**Checkpoint:** `Churn Rate`, `Customers`, `Germany Churn`, `Spain Churn`, and `France Churn` appear in the model.

#### Step 27: Create the report

- Select **Create report**.
- Add a text box titled `Bank Customer Churn`.
- Add a card for `Churn Rate`.
- Add a line and stacked column chart with `age` on the x-axis, `Churn Rate` on column y-axis, and `Customers` on line y-axis.
- Add a line and stacked column chart with `NumOfProducts` on x-axis, `Churn Rate` on column y-axis, and `Customers` on line y-axis.
- Add a stacked column chart with `NewCreditsScore` on x-axis and `Churn Rate` on y-axis.
- Rename the visual title from `NewCreditsScore` to `Credit Score`.
- Add a clustered column chart with `Germany Churn`, `Spain Churn`, and `France Churn` in that order on the y-axis.

**Explanation:** The report connects model predictions to customer segments that business users can act on.
**Checkpoint:** The report canvas contains the churn card and the age, product, credit score, and geography visuals.

#### Step 28: Review the report insights

- Review whether customers with more than two products show higher churn.
- Compare churn in Germany, France, and Spain.
- Review churn by age bands, especially ages 45-60.
- Review churn by credit score.
- Save the report.

**Explanation:** The sample report demonstrates how prediction outputs can guide further investigation, not production decisions by itself.
**Checkpoint:** The saved report highlights churn patterns by product count, geography, age, and credit score.

