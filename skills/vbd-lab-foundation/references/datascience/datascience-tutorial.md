# Fabric Foundation VBD - Data Science Lab Tutorial

> Converted from `Data Science Tutorial.docx` (SharePoint IP Release - Fabric Foundation Discovery Labs).
> Screenshots have been stripped; refer to `sources.yaml` in this folder for the Microsoft Learn URLs cited throughout.

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

# Introduction

__Note__– If you are new to Fabric, we would encourage you to go through this documentation to get an overview of different Fabric concepts and features: [Fabric - Overview](https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview)

The lifecycle of a Data science project typically includes (often, iteratively) the steps listed below:

-

	- Business understanding
	- Data acquisition
	- Data exploration, cleansing, preparation, and visualization
	- Model training and experiment tracking
	- Model scoring and generating insights.

The goals and success criteria of each stage listed above depend on collaboration, data sharing and documentation. The Fabric Data science experience consists of multiple native-built features that enable collaboration, data acquisition, sharing, and consumption in a seamless way.

In these tutorials, you take the role of a data scientist who has been given the task to explore, clean, and transform a dataset containing the churn status of 10,000 customers at a bank. You then build a machine learning model to predict which bank customers are likely to leave.

In this tutorial, you will learn to perform the following activities:

1. Use the Fabric notebooks for data science scenarios.
2. Ingest data into Fabric lakehouse
3. Load existing data from the lakehouse delta tables.
4. Clean and transform Data using Apache Spark and Python based tools.
5. Create experiments and runs to Train a machine learning model.
6. Register and track trained models using MLflow and the Fabric UI.
7. Run scoring at scale and save predictions and inference results to the lakehouse.
8. Visualize predictions in PowerBI using Direc

# Prerequisites

1. Power BI Premium subscription([*How to purchase Power BI Premium*](https://learn.microsoft.com/en-us/power-bi/enterprise/service-admin-premium-purchase)*)* or Fabric F Sku([Buy a Microsoft Fabric subscription - Microsoft Fabric | Microsoft Learn](https://learn.microsoft.com/en-us/fabric/enterprise/buy-subscription)) or Fabric Trial capacity ([Fabric trial capacity - Microsoft Fabric | Microsoft Learn](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial)).
2. A Power BI Workspace with assigned premium/F/Trial capacity.
3. An existing Fabric Lakehouse. Create a Lakehouse by following, *How to Create a lakehouse *in the lakehouse tutorial document.

# The Data Science end-to-end scenario

# Different components of Data science scenario

__Data Sources__– Fabric makes it easy and quick to connect to Azure Data Services, other cloud platforms, and on-premises data sources to ingest data from. Using Fabric Notebooks you can ingest data from the inbuilt Lakehouse, Data Warehouse, Power BI Datasets as well as various Apache Spark and Python supported custom data sources. In this document we will focus on ingesting and loading data from Lakehouse.

__Explore, Clean & Prepare –__The Data Science experience on Fabric supports data cleansing, transformation, exploration and featurization by leveraging built-in experiences on Spark as well as Python based tools like Data Wrangler and SemPy Library. This tutorial will showcase data exploration using python library seaborn and data cleansing and preparation using Apache Spark .

__Models & Experiments__– Fabric enables you to train, evaluate and score machine learning models by using built-in Experiment and Model artifacts with seamless integration with [MLflow](https://mlflow.org/docs/latest/index.html) for experiment tracking and model registration/deployment. Fabric also features capabilities for model prediction at scale (PREDICT) to gain and share business insights.

__Storage__– Fabric standardizes on [Delta Lake](https://docs.delta.io/latest/index.html), that means all the engines of Fabric can interact with the same dataset stored in lakehouse. This storage layer allows you to store both structured and unstructured data that support both file-based storage as well as tabular format. The datasets and files stored can be easily accessed via all Fabric workload artifacts like notebooks and pipelines.

__Expose Analysis and Insights__– Data from Lakehouse can be consumed by Power BI, industry leading business intelligence tool, for reporting and visualization. Data persisted in the lakehouse can also be visualized in notebooks using Spark or Python native visualization libraries like matplotlib, seaborn, plotly, and more. Data can also be visualized using SemPy library that supports built-in rich, task-specific visualizations for the semantic data model, for dependencies and their violations, and for classification and regression use cases.

# Import tutorial notebooks

We will utilize the notebook artifact in the Data Science experience to demonstrate various Fabric capabilities. The notebooks are available as jupyter notebook files that can be imported to your Fabric- enabled workspace.

1. Use the experience switcher in the bottom left side of the home page to switch to Fabric.

1. Go to an existing Workspace or Create a new workspace named __Data Science Tutorial__ (*How to Create a lakehouse) *

1. Please verify the Workspace is using Spark version 3 or higher (Navigate to workspace settings to verify)

1. Download the notebooks 1-4 (.ipynb) files for this tutorial from the Scripts folder(Ask the instructor or admin for the path where the files are located).

1. Within the __Data Science Tutorial__workspace created select__Import > Notebook > From this computer.__
2. A right pane should open named *Import Status* click on the __Upload Button__ and select all the Jupyter notebooks from the Scripts folder. Check the notifications as well to make sure the notebooks imported successfully.

1. The imported notebooks would now be available in your workspace for use.

1. Open the notebooks one by one to validate it opens OK.
2. If the imported notebook includes output, select the __Edit__menu, then select__Clear all outputs__.

# Attach a lakehouse to the notebooks.

To demonstrate Fabric lakehouse features, the first four modules in this tutorial require attaching a default lakehouse to the notebooks. Below are the steps to add an existing or new lakehouse to a notebook in a Fabric-enabled workspace.

1. Open the notebook for the first module “*1 Ingest data*” in the workspace.
2. Remove any previously attached Lakehouse’s to the notebook (if there is any). Click on Lakehouse’s, and click on the attached lakehouse and select the __Remove all lakehouse__ option.

1. Click on Lakehouse’s, and Select __Add lakehouse__ in the left pane.

1. Create a new lakehouse or use an existing lakehouse. __Make sure the Lakehouse resides in the same workspace.__
2. To create a new lakehouse, select __New__. Give the lakehouse a name and select__Create__.
3. To use an existing lakehouse, select __Existing lakehouse__to open the__Data hub__dialog box. Select the lakehouse you want to use and then select__Add__.

1. Once a lakehouse is added it will be visible in the lakehouse pane on notebook UI where *Tables*

and *Files *stored in the lakehouse can be viewed.

__*Note: *__*The steps defined above need to be performed for each notebook, before executing all notebook accompanying this tutorial* *Figure 2: Attach a lakehouse to notebook*

# Module 1: Ingest data into Fabric lakehouse

In this tutorial, you'll ingest data into Fabric lakehouse in delta lake format. Some important terms to understand:

- __Lakehouse__ - A lakehouse is a collection of files/folders/tables that represent a database over a data lake used by the Spark engine and SQL engine for big data processing and that includes enhanced capabilities for ACID transactions when using the open-source Delta formatted tables.
- __Delta Lake__ - Delta Lake is an open-source storage layer that brings ACID transactions, scalable metadata management, and batch and streaming data processing to Apache Spark. A Delta Lake table is a data table format that extends Parquet data files with a file-based transaction log for ACID transactions and scalable metadata management.

In this tutorial, you will upload a csv file to a lakehouse. The churn.csv file is located in the following path:

__*C:\\Users\\LabUser\\Documents\\LabFiles\\Fabric\\Fabric\\1 - Upskilling\\1 - Foundation\\02 - Discovery Labs\\04 - Data Science Lab*__

## __Sample Data__

__Bank churn data__ The dataset contains churn status of 10,000 customers. It also includes attributes that could impact churn such as:

- Credit score
- Geographical location (Germany, France, Spain)
- Gender (male, female)
- Age
- Tenure (years of being bank's customer)
- Account balance
- Estimated salary
- Number of products that a customer has purchased through the bank
- Credit card status (whether a customer has a credit card or not)
- Active member status (whether an active bank's customer or not)

The dataset also includes columns such as row number, customer ID, and customer surname that should have no impact on customer's decision to leave the bank. The event that defines the customer's churn is the closing of the customer's bank account. The column exited in the dataset refers to customer's abandonment. There isn't much context available about these attributes so you have to proceed without having background information about the dataset. The aim is to understand how these attributes contribute to the exited status.

## __Upload the csv file to lakehouse__

1. In the first step of this module, we open the lakehouse we created before and we go to the File section. We then go to ‘Upload Files’ and upload the churn.csv file from the following path:

__*C:\\Users\\LabUser\\Documents\\LabFiles\\Fabric\\Fabric\\1 - Upskilling\\1 - Foundation\\02 - Discovery Labs\\04 - Data Science Lab*__ You should then be able to see it in the Files section:

# Module 2: Explore data

In this tutorial, you'll learn how to conduct exploratory data analysis (EDA) to examine and investigate the data while summarizing its key characteristics through the use of data visualization techniques.

You'll use *seaborn*, a Python data visualization library that provides a high-level interface for building visuals on dataframes and arrays. For more information about *seaborn*, see [Seaborn: Statistical Data Visualization](https://seaborn.pydata.org/).

You'll also use [Data Wrangler](https://learn.microsoft.com/en-us/fabric/data-science/data-wrangler), a notebook-based tool that provides you with an immersive experience to conduct exploratory data analysis and cleaning.

The main steps in this tutorial are:

1. Read the data stored from a delta table in the lakehouse.
2. Convert a Spark DataFrame to Pandas DataFrame, which python visualization libraries support.
3. Use Data Wrangler to perform initial data cleaning and transformation.
4. Perform exploratory data analysis using *seaborn.*

__Note__: The python commands/script used in each step of this tutorial can be found in the accompanying notebook: *2-explore-cleanse-data* Prerequisites:

- Complete Part 1: Ingest Data
- Attach the same lakehouse you used in Part 1 to this notebook
- Navigate to workspace settings to verify

## __Read raw data from the Lakehouse__

Read raw data from the Files section of the lakehouse. You uploaded this data in the previous module. Make sure you have attached the same lakehouse you used in Part 1 to this notebook before you run this code.

## __Create a pandas DataFrame from the dataset__

Convert the spark DataFrame to pandas DataFrame for easier processing and visualization.

Explore the raw data with display, do some basic statistics and show chart views. Note that you first need to import the required libraries such as Numpy, Pnadas, Seaborn, and Matplotlib for data analysis and visualization.

Display summary:

## __Use Data Wrangler to perform initial data cleaning__

*Data Wrangler* is a notebook-based tool that provides an immersive experience to conduct exploratory data analysis and cleansing.

To explore and transform any pandas Dataframes in your notebook, launch Data Wrangler directly from the notebook.

__Note:__ Data Wrangler can not be opened while the notebook kernel is busy. The cell execution must complete prior to launching Data Wrangler.

1.  In the notebook’s top ribbon select Data Wrangler. You'll see a list of activated pandas DataFrames available for editing.

2.  Select the DataFrame you wish to open in Data Wrangler. Since this notebook only contains one DataFrame, df, select df.

Data Wrangler launches and generates a descriptive overview of your data. The table in the middle shows each data column. The Summary panel next to the table shows information about the DataFrame. When you select a column in the table, the summary updates with information about the selected column. In some instances, the data displayed and summarized will be a truncated view of your DataFrame. When this happens, you'll see warning image in the summary pane. Hover over this warning to view text explaining the situation.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-explore-notebook/preview.png#lightbox)

Each operation you do can be applied in a matter of clicks, updating the data display in real time and generating code that you can save back to your notebook as a reusable function.

The rest of this section walks you through the steps to perform data cleaning with Data Wrangler.

## __Drop duplicate rows__

On the left panel is a list of operations (__such as Find and replace, Format, Formulas, Numeric__) you can perform on the dataset.

1. Expand __Find and replace__and select__Drop duplicate rows.__

1. A panel appears for you to select the list of columns you want to compare to define a duplicate row. Select __RowNumber__and__CustomerId.__

In the middle panel is a preview of the results of this operation. Under the preview is the code to perform the operation. In this instance, the data appears to be unchanged. But since you're looking at a truncated view, it's a good idea to still apply the operation.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-explore-notebook/drop-duplicate.png#lightbox)

1. Select __Apply__ (either at the side or at the bottom) to go to the next step.

## __Drop rows with missing data__

Use Data Wrangler to drop rows with missing data across all columns.

1. Select __Drop missing__ __values__from__Find and replace.__

1. Choose __Select all__from the__Target__ columns.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-explore-notebook/drop-missing.png#lightbox)

1. Select __Apply__ to go on to the next step.

## __Drop Columns__

Use Data Wrangler to drop columns that you don't need.

1. Expand __Schema__and select__Drop columns.__

1. Select __RowNumber, CustomerId, Surname.__ These columns appear in red in the preview, to show they're changed by the code (in this case, dropped.)

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-explore-notebook/drop-columns.png#lightbox)

1. Select Apply to go on to the next step.

## __Add code to notebook__

Each time you select Apply, a new step is created in the Cleaning steps panel on the bottom left. At the bottom of the panel, select Preview code for all steps to view a combination of all the separate steps.

Select Add code to notebook at the top left to close Data Wrangler and add the code automatically. The __Add code to notebook__ wraps the code in a function, then calls the function.

__Note:__  The code generated by Data Wrangler won't be applied until you manually run the new cell.

__Run Data Wrangler code:__ __Optional:__ If you didn't use Data Wrangler, you can instead use this next code cell.

This code is similar to the code produced by Data Wrangler, but adds in the argument inplace=True to each of the generated steps. By setting inplace=True, pandas will overwrite the original DataFrame instead of producing a new DataFrame as an output.

## __Explore the data__

Display some summaries and visualizations of the cleaned data.

## __Determine categorical, numerical, and target attributes__

Use this code to determine categorical, numerical, and target attributes.

## __The five-number summary__

Show the five-number summary (the minimum score, first quartile, median, third quartile, the maximum score) for the numerical attributes, using box plots.

## __Distribution of exited and nonexited customers__

Show the distribution of exited versus nonexited customers across the categorical attributes.

## __Distribution of numerical attributes__

Show the frequency distribution of numerical attributes using histogram.

## __Perform feature engineering__

Perform feature engineering to generate new attributes based on current attributes:

## __Use Data Wrangler to perform one-hot encoding__

Data Wrangler can also be used to perform one-hot encoding. To do so, re-open Data Wrangler. This time, select the df_clean data.

1.  Expand Formulas and select One-hot encode.

2.  A panel appears for you to select the list of columns you want to perform one-hot encoding on. Select __Geography__and__Gender__.

You could copy the generated code, close Data Wrangler to return to the notebook, then paste into a new cell. Or, select Add code to notebook at the top left to close Data Wrangler and add the code automatically.

__Option:__ If you didn't use Data Wrangler, you can instead use this next code cell:

## __Summary of observations from the exploratory data analysis__

- Most of the customers are from France comparing to Spain and Germany, while Spain has the lowest churn rate comparing to France and Germany.
- Most of the customers have credit cards.
- There are customers whose age and credit score are above 60 and below 400, respectively, but they can't be considered as outliers.
- Very few customers have more than two of the bank's products.
- Customers who aren't active have a higher churn rate.
- Gender and tenure years don't seem to have an impact on customer's decision to close the bank account.

## __Create a delta table for the cleaned data__

You'll use this data in the next notebook of this series.

# Module 3: Train and register machine learning models

In this tutorial, you'll learn to train multiple machine learning models to select the best one in order to predict which bank customers are likely to leave.

In this tutorial, you'll:

- Train Random Forest and LightGBM models.
- Use Microsoft Fabric's native integration with the MLflow framework to log the trained machine learning models, the used hyperaparameters, and evaluation metrics.
- Register the trained machine learning model.
- Assess the performances of the trained machine learning models on the validation dataset.

[MLflow](https://mlflow.org/docs/latest/index.html) is an open source platform for managing the machine learning lifecycle with features like Tracking, Models, and Model Registry. MLflow is natively integrated with the Fabric Data Science experience.

__Note__: The python commands/script used in each step of this tutorial can be found in the accompanying notebook: *03 – train-evaluate*__Install custom libraries__ For this notebook, you'll install imbalanced-learn (imported as *imblearn*) using *%pip install*. Imbalanced-learn is a library for Synthetic Minority Oversampling Technique (SMOTE) which is used when dealing with imbalanced datasets. The PySpark kernel will be restarted after *%pip install*, so you'll need to install the library before you run any other cells.

You'll access SMOTE using the* imblearn* library. Install it now using the in-line installation capabilities (e.g., *%pip, %conda*).

__Important:__ Run this install each time you restart the notebook.

When you install a library in a notebook, it's only available for the duration of the notebook session and not in the workspace. If you restart the notebook, you'll need to install the library again.

If you have a library you often use, and you want to make it available to all notebooks in your workspace, you can use a [Fabric environment](https://aka.ms/fabric/create-environment) for that purpose. You can create an environment, install the library in it, and then your workspace admin can attach the environment to the workspace as its default environment. For more information on setting an environment as the workspace default, see [Admin sets default libraries for the workspace](https://learn.microsoft.com/en-us/fabric/data-engineering/library-management#scenario-1-admin-sets-default-libraries-for-the-workspace).

For information on migrating existing workspace libraries and Spark properties to an environment, see [Migrate workspace libraries and Spark properties to a default environment](https://learn.microsoft.com/en-us/fabric/data-engineering/environment-workspace-migration).

## __Load the data__

Prior to training any machine learning model, you need to load the delta table from the lakehouse in order to read the cleaned data you created in the previous notebook.

## __Generate experiment for tracking and logging the model using MLflow__

This section demonstrates how to generate an experiment, specify the machine learning model and training parameters as well as scoring metrics, train the machine learning models, log them, and save the trained models for later use.

Extending the MLflow autologging capabilities, autologging works by automatically capturing the values of input parameters and output metrics of a machine learning model as it is being trained. This information is then logged to your workspace, where it can be accessed and visualized using the MLflow APIs or the corresponding experiment in your workspace.

All the experiments with their respective names are logged and you'll be able to track their parameters and performance metrics. To learn more about autologging, see [Autologging in Microsoft Fabric](https://aka.ms/fabric-autologging).

## __Set experiment and autologging specifications__

## __Import scikit-learn and LightGBM__

With your data in place, you can now define the machine learning models. You'll apply Random Forest and LightGBM models in this notebook. Use scikit-learn and lightgbm to implement the models within a few lines of code.

## __Prepare training, validation and test datasets__

Use the *train_test_split* function from *scikit-learn* to split the data into training, validation, and test sets.

## __Save test data to a delta table__

Save the test data to the delta table for use in the next notebook.

## __Apply SMOTE to the training data to synthesize new samples for the minority class__

The data exploration in part 2 showed that out of the 10,000 data points corresponding to 10,000 customers, only 2,037 customers (around 20%) have left the bank. This indicates that the dataset is highly imbalanced. The problem with imbalanced classification is that there are too few examples of the minority class for a model to effectively learn the decision boundary. SMOTE is the most widely used approach to synthesize new samples for the minority class. Learn more about SMOTE [here](https://imbalanced-learn.org/stable/references/generated/imblearn.over_sampling.SMOTE.html) and [here](https://imbalanced-learn.org/stable/over_sampling.html#smote-adasyn).

__Tip:__ Note that SMOTE should only be applied to the training dataset. You must leave the test dataset in its original imbalanced distribution in order to get a valid approximation of how the machine learning model will perform on the original data, which is representing the situation in production.

__Tip:__ You can safely ignore the MLflow warning message that appears when you run this cell. If you see a ModuleNotFoundError message, you missed running the first cell in this notebook, which installs the imblearn library. You need to install this library each time you restart the notebook. Go back and re-run all the cells starting with the first cell in this notebook.

## __Model training__

- Train the model using Random Forest with maximum depth of 4 and 4 features

- Train the model using Random Forest with maximum depth of 8 and 6 features

- Train the model using LightGBM

## __Experiments artifact for tracking model performance__

The experiment runs are automatically saved in the experiment artifact that can be found from the workspace. They're named based on the name used for setting the experiment. All of the trained machine learning models, their runs, performance metrics, and model parameters are logged.

To view your experiments:

1. On the left panel, select your workspace.
2. On the top right, filter to show only experiments, to make it easier to find the experiment you're looking for.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-train-models/filter-workspace.png#lightbox)

1. Find and select the experiment name, in this case bank-churn-experiment. If you don't see the experiment in your workspace, refresh your browser.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-train-models/experiment-runs.png#lightbox)

## __Assess the performances of the trained models on the validation dataset__

Once done with machine learning model training, you can assess the performance of trained models in two ways.

- Open the saved experiment from the workspace, load the machine learning models, and then assess the performance of the loaded models on the validation dataset.

- Directly assess the performance of the trained machine learning models on the validation dataset.

Depending on your preference, either approach is fine and should offer identical performances. In this notebook, you'll choose the first approach in order to better demonstrate the MLflow autologging capabilities in Microsoft Fabric.

## __Show True/False Positives/Negatives using the Confusion Matrix__

Next, you'll develop a script to plot the confusion matrix in order to evaluate the accuracy of the classification using the validation dataset. The confusion matrix can be plotted using SynapseML tools as well, which is shown in Fraud Detection sample that is available [here](https://aka.ms/samples/frauddectection).

- Confusion Matrix for Random Forest Classifier with maximum depth of 4 and 4 features

- Confusion Matrix for Random Forest Classifier with maximum depth of 8 and 6 features

- Confusion Matrix for LightGBM

# Module 4: Perform batch scoring and save predictions to a Lakehouse

In this tutorial, you'll learn to import the registered LightGBMClassifier model that was trained in part 3 using the Microsoft Fabric MLflow model registry, and perform batch predictions on a test dataset loaded from a lakehouse.

Microsoft Fabric allows you to operationalize machine learning models with a scalable function called PREDICT, which supports batch scoring in any compute engine. You can generate batch predictions directly from a Microsoft Fabric notebook or from a given model's item page. Learn about [PREDICT](https://learn.microsoft.com/en-us/fabric/data-science/model-scoring-predict).

To generate batch predictions on the test dataset, you'll use version 1 of the trained LightGBM model that demonstrated the best performance among all trained machine learning models. You'll load the test dataset into a spark DataFrame and create an MLFlowTransformer object to generate batch predictions. You can then invoke the PREDICT function using one of following three ways:

- Transformer API from SynapseML
- Spark SQL API
- PySpark user-defined function (UDF)

Prerequisites

- Complete [Part 3: Train and register machine learning models](https://learn.microsoft.com/fabric/data-science/tutorial-data-science-train-models).
- Attach the same lakehouse you used in Part 3 to this notebook.

## __Load the test data__

Load the test data that you saved in Part 3.

## __PREDICT with the Transformer API__

To use the Transformer API from SynapseML, you'll need to first create an MLFlowTransformer object.

## __Instantiate MLFlowTransformer object__

The MLFlowTransformer object is a wrapper around the MLFlow model that you registered in Part 3. It allows you to generate batch predictions on a given DataFrame. To instantiate the MLFlowTransformer object, you'll need to provide the following parameters:

- The columns from the test DataFrame that you need as input to the model (in this case, you would need all of them).
- A name for the new output column (in this case, predictions).
- The correct model name and model version to generate the predictions (in this case, lgbm_sm and version 1).

Now that you have the MLFlowTransformer object, you can use it to generate batch predictions.

## __PREDICT with the Spark SQL API__

The following code invokes the PREDICT function with the Spark SQL API.

## __PREDICT with a user-defined function (UDF)__

The following code invokes the PREDICT function with a PySpark UDF.

Note that you can also generate PREDICT code from a model's item page. Learn about [PREDICT](https://aka.ms/fabric/predict-from-model-item).

## __Write model prediction results to the lakehouse__

Once you have generated batch predictions, write the model prediction results back to the lakehouse.

# Module 5: Visualize predictions with a Power BI report

In this tutorial, you create a Power BI report from the predictions data generated in [Part 4: Perform batch scoring and save predictions to a lakehouse](https://learn.microsoft.com/en-us/fabric/data-science/tutorial-data-science-batch-scoring).

You'll learn how to:

- Create a semantic model from the predictions data.
- Add new measures to the data from Power BI.
- Create a Power BI report.
- Add visualizations to the report.

## __Create a semantic model__

Create a new semantic model linked to the predictions data you produced in part 4:

1. On the left, select your workspace.
2. On the top left, select __Lakehouse__ as a filter.

1. Select the lakehouse that you used in the previous parts of the tutorial series.
2. Select __New semantic model__ on the top ribbon.

1. Give the semantic model a name, such as "bank churn predictions." Then select the *customer_churn_test_predictions* dataset.
2. Select __Confirm.__

## __Add new measures__

- Go to semantic model bank churn predictions and click on the Open Data Model button at the top ribbon.

- Now add a few measures to the semantic model:
	1. Click on the data set and change to __editing__ mode

-

	1. Add a new measure for the churn rate.
		1. Select __New measure__in the top ribbon. This action adds a new item named__Measure__to the__*customer_churn_test_predictions*__ dataset and opens a formula bar above the table.

- -

		1. To determine the average predicted churn rate, replace Measure = in the formula bar with:

Churn Rate = AVERAGE(customer_churn_test_predictions\[predictions\])

- -

		1. To apply the formula, select the check mark in the formula bar. The new measure appears in the   data table. The calculator icon shows it was created as a measure.

- -

		1. Change the format from General to Percentage in the Properties panel.
		2.  Scroll down in the Properties panel to change the Decimal places to 1.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/churn-rate.png#lightbox)

-

	1. Add a new measure that counts the total number of bank customers. You'll need it for the rest of the new measures.
		1. Select __New measure__in the top ribbon to add a new item named Measure to the__*customer_churn_test_predictions*__ dataset. This action also opens a formula bar above the table.
		2. Each prediction represents one customer. To determine the total number of customers, replace __Measure =__ in the formula bar with:

Customers = COUNT(customer_churn_test_predictions\[predictions\])

- -

		1. To apply the formula, select the check mark in the formula bar.

	1. Add the churn rate for Germany.
		1. Select New measure in the top ribbon to add a new item named Measure to the customer_churn_test_predictions dataset. This action also opens a formula bar above the table.
		2. To determine the churn rate for Germany, replace Measure = in the formula bar with:

Germany Churn = CALCULATE(AVERAGE(customer_churn_test_predictions\[predictions\]),FILTER(customer_churn_test_predictions, customer_churn_test_predictions\[Geography_Germany\] = TRUE()))

This filters the rows down to the ones with Germany as their geography (Geography_Germany equals one).

- -

		1. To apply the formula, select the check mark in the formula bar.

	1. Repeat the above step to add the churn rates for France and Spain.

	- Spain's churn rate:

Spain Churn = CALCULATE(AVERAGE(customer_churn_test_predictions\[predictions\]),FILTER(customer_churn_test_predictions, customer_churn_test_predictions\[Geography_Spain\] = TRUE()))

-

	- France's churn rate:

France Churn = CALCULATE(AVERAGE(customer_churn_test_predictions\[predictions\]),FILTER(customer_churn_test_predictions, customer_churn_test_predictions\[Geography_France\] = TRUE()))

## __Create new report__

Once you're done with all operations, move on to the Power BI report authoring page by selecting Create report on the top ribbon.

Once the report page appears, add these visuals:

1. Select the text box on the top ribbon and enter a title for the report, such as "Bank Customer Churn". Change the font size and background color in the Format panel. Adjust the font size and color by selecting the text and using the format bar.
2. In the Visualizations panel, select the Card icon. From the Data pane, select Churn Rate. Change the font size and background color in the Format panel. Drag this visualization to the top right of the report.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/card-churn.png#lightbox)

1. In the Visualizations panel, select the Line and stacked column chart icon. Select age for the x-axis, Churn Rate for column y-axis, and Customers for the line y-axis.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/age.png#lightbox)

1. In the Visualizations panel, select the Line and stacked column chart icon. Select NumOfProducts for x-axis, Churn Rate for column y-axis, and Customers for the line y-axis.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/number-of-products.png#lightbox)

1. In the Visualizations panel, select the Stacked column chart icon. Select NewCreditsScore for x-axis and Churn Rate for y-axis.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/new-credit-score.png#lightbox)

Change the title "NewCreditsScore" to "Credit Score" in the Format panel.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/change-title.png#lightbox)

1. In the Visualizations panel, select the Clustered column chart card. Select Germany Churn, Spain Churn, France Churn in that order for the y-axis.

[](https://learn.microsoft.com/en-us/fabric/data-science/media/tutorial-data-science-create-report/germany-spain-france.png#lightbox)

__Note:__

- This report represents an illustrated example of how you might analyze the saved prediction results in Power BI. However, for a real customer churn use-case, the you may have to do more thorough ideation of what visualizations to create, based on your subject matter expertise, and what your firm and business analytics team has standardized as metrics.

## __The Power BI report shows:__

- Bank customers who use more than two of the bank products have a higher churn rate, although few customers had more than two products. The bank should collect more data, but also investigate other features that correlate with more products (review the plot in the bottom left panel).
- Bank customers in Germany have a higher churn rate than in France and Spain (review the plot in the bottom right panel), suggesting that an investigation into what encouraged customers to leave could become helpful.
- There are more middle aged customers (between 25-45), and customers between 45-60 tend to exit more.
- Finally, customers with lower credit scores would most likely leave the bank for other financial institutions. The bank should look for ways to encourage customers with lower credit scores and account balances to stay with the bank.

## __Summary__

In the above set of tutorials, we demonstrated a sample end-to-end scenario on the Fabric data science experience by implementing each step from data ingestion, cleansing and preparation to training machine learning models and generating insights, and consuming those insights using visualization tools like Power BI.
