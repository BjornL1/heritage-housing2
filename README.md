# HOUSE SALE PRICE PREDICTOR

This website is designed to predict house sale prices by training a machine learning model using existing data on house attributes and their corresponding sale prices.

![I am responsive image](docs/readme_images/page_amiresponsive.png)

Link to site: [House Sale Price Predictor](https://bl1-heritage-housing-d4f44a67aec9.herokuapp.com/)

## Table of Content

- [House Sale Price Predictor](#house-sale-price-predictor)
  - [Table of Content](#table-of-content)
  - [Dataset Content](#dataset-content)
  - [Business Requirements](#business-requirements)
  - [Background](#background)
  - [Work methodology](#work-methodology)
  - [Problem definition](#problem-definition)
  - [Requirements](#requirements)
  - [User stories](#user-stories)
  - [Hypothesis, validation and result](#hypothesis-validation-and-result)
  - [The rationale to map the business requirements to the Data Visualisations and ML tasks](#the-rationale-to-map-the-business-requirements-to-the-data-visualisations-and-ml-tasks)
  - [ML Business Case](#ml-business-case)
    - [Predict Sale Price](#predict-sale-price)
    - [Regression Model Details](#regression-model-details)
  - [Dashboard Design](#dashboard-design)
    - [Page 1: Quick project summary](#page-1-quick-project-summary)
    - [Page 2: Sale Price Correlation](#page-2-sale-price-correlation)
    - [Page 3: Sale Price Predictor](#page-3-sale-price-predictor)
    - [Page 4: Project Hypothesis and Validation](#page-4-project-hypothesis-and-validation)
    - [Page 5: ML Price Predictor](#page-5-ml-price-predictor)
  - [Testing](#testing)
     -[CI Python Linter](#business-requirements)
     -[Manual testing](#manual-testing)
  - [Unfixed Bugs](#unfixed-bugs)
  - [PEP8 Compliance Testing](#pep8-compliance-testing)
  - [Deployment](#deployment)
    - [Heroku](#heroku)
    - [Main Data Analysis and Machine Learning Libraries](#main-data-analysis-and-machine-learning-libraries)
  - [Credits](#credits)
    - [Sources of code](#sources-of-code)
  - [Acknowledgements](#acknowledgements)

Link to the site:
[HOUSE SALE PRICE PREDICTOR](https://bl1-heritage-housing-d4f44a67aec9.herokuapp.com/)


## Dataset Content

* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset has almost 1.5 thousand rows and represents housing records from Ames, Iowa, indicating house profile (Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built) and its respective sale price for houses built between 1872 and 2010.

|Variable|Meaning|Units|
|:----|:----|:----|
|1stFlrSF|First Floor square feet|334 - 4692|
|2ndFlrSF|Second-floor square feet|0 - 2065|
|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|0 - 8|
|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Minimum Exposure; No: No Exposure; None: No Basement|
|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|
|BsmtFinSF1|Type 1 finished square feet|0 - 5644|
|BsmtUnfSF|Unfinished square feet of basement area|0 - 2336|
|TotalBsmtSF|Total square feet of basement area|0 - 6110|
|GarageArea|Size of garage in square feet|0 - 1418|
|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|
|GarageYrBlt|Year garage was built|1900 - 2010|
|GrLivArea|Above grade (ground) living area square feet|334 - 5642|
|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|
|LotArea| Lot size in square feet|1300 - 215245|
|LotFrontage| Linear feet of street connected to property|21 - 313|
|MasVnrArea|Masonry veneer area in square feet|0 - 1600|
|EnclosedPorch|Enclosed porch area in square feet|0 - 286|
|OpenPorchSF|Open porch area in square feet|0 - 547|
|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|
|WoodDeckSF|Wood deck area in square feet|0 - 736|
|YearBuilt|Original construction date|1872 - 2010|
|YearRemodAdd|Remodel date (same as construction date if no remodelling or additions)|1950 - 2010|
|SalePrice|Sale Price|34900 - 755000|

## Business Requirements

In the following sections the business requirements will be explained, firstly a section describing the background followed by a problem statement, finally a description of the business case.

### Background

Our client, going by the alias 'Lydia Doe', has received an inheritance from a deceased great-grandfather. Included in the inheritance are four houses located in Ames, Iowa, USA. Lydia seeks assistance in maximizing the sales price for these inherited properties. To achieve this goal, she has chosen to enlist the help of a Data Practitioner. Her reasons for doing so include:

- Lydia lacks knowledge about the value of the properties and wishes to avoid the risk of inaccurate pricing estimation. Given the potential for significant financial gains or losses when selling the four properties, she seeks assistance to ensure optimal pricing strategies.
- Additionally, Lydia is keen on predicting the sale price of any house in Ames, Iowa, for potential future property ownership in the area 

From searching the Internet, Lydia found a public dataset with house prices for Ames, Iowa, and will provide us with that. We will build a Data Web App to predict the sales price from the four houses based on the house attributes. 

### Work methodology

To achieve our goal, we will use the Cross-Industry Standard Process for Data Mining (CRISP-DM) workflow. This workflow is documented and reflected in the logical order in which the files were created, aligning with the stages of the CRISP-DM process. While the framework guides us to create files and work in a specific sequence, we also incorporate agile principles. This allows us to iterate and refine our solution, ensuring we deliver an optimal final product that meets the client's requirements.

The following steps defines the CRISP-DM workflow, after each a point, a corresponding file or readme section is defined to explain the overall connection (best fit) between the stages and files and methods described in this project.

- Business Understanding: Readme -  Background and Problem definition chapters.
- Data Understanding:     01 - DataCollection.ipynb
- Data Preparation:       02 - DataCleaning.ipynb, 03 - CorrelationStudy.ipynb
- Modeling:               04 - FeatureEngineering.ipynb
- Evaluation:             05 - ModelEvaluteRegr_PredictPrice.ipynb
- Deployment:             Streamlit App, deployed on Heroku (locally run with app.py) 

### Problem definition

While the client is well-versed in the determinants of property worth in her own area, it's crucial to understand the unique drivers of value in Ames, Iowa. The client worries that her personal expertise may not be adequate to accurately assess the value, potentially resulting in erroneous appraisals and financial losses.


### Requirements

* 1. - The client is interested in identifying which house attributes have the strongest correlation with the sale price. 

* 2. - The client expects data visualizations of the correlated variables against the sale price to demonstrate this.

* 3. - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


### User stories

- User Story 1: As a user, I want to view the attributes correlated to the sale price, so that I can identify the key features for upcoming sales.
- User Story 2: As a user, I want to be able to determine the likely sale price of a home based on certain features, so that I can gain insight into the likely values of a given home in the area.
- User Story 3: As a user, I want to be able to view the four main key features with a threshold score of 0.8, so that I can easily see the features that are most relevant from a predictive power score perspective.

## Hypothesis validation and result

1. Hypothesis: Sales price house attribute correlation:
   We assume that associoated variables for the following four features has the strongest correlation: lot area, property size, condition and age of the property:
    - Validation: Evaluate the available house attributes in a correlation study, mention the the values above 0,6 for either Spearman or Pearson correlation.
    - Result: From the calculations we can see that some of our assesement of features were correct, below is the details explained:     
    * OverallQual - Correct, associated to condition.
    * GrLivArea - Correct, associated to size.
    * GarageArea - Correct, associated to size.   
    * TotalBsmtSF - Correct, associated to size.  
    * YearBuilt -  Correct, associated to age.
    * 1stFlrSF - Correct, associated to size.

    * Note: **lot area** is not part of property size so in this case the assumption was incorrect.  

2. Hypothesis: Determine sales price:
   We assume that the following variables will be sufficient to confidently predict the price: lot area, house size (1stFlrSF ), overall quality and the build year.
   - Validation: Use a machine learning model and optimization procedures to ensure the application of appropriate methods.
   - Result: We noticed also in this case a partial match to the assumption.
    * OverallQual - Correct, aligns with the hypothesis.
    * TotalBsmtSF - Incorrect compared to the hypothesis.
    * 2ndFlrSF - Incorrect compared to the hypothesis.
    * GarageArea - Correct, aligns with the hypothesis.

3.  Hypothesis: Predictive power of key housing features:
   We assume that the four features with the highest predictive power presented in Hypothesis 2 are sufficient to achieve an R² score of 0.8 and can be used as reliable indicators of predictive power.
   - Validation: Review the result from the trained models in Hypothesis 2 and display it in the streamlit app.
   - Result: Correct, the four features can be used to confidently predict house sale prices. The R² score of 0.901 on the training set and 0.841 on the test set suggests that the model explains a significant portion of the variance in sale prices, which is a positive indication. This means that these four features are indeed very important and provide substantial predictive power.

## The rationale to map the business requirements to the Data Visualisations and ML tasks

 Business Requirement 1: Correlation Study
- Task 1: Inspect the data provided by the client to ensure it is clean and ready for analysis.
- Task 2: Conduct correlation studies to identify which variables have the strongest impact on house sale prices.
- Task 3: Plot significant variables against sale prices to visualize their relationships.

Business Requirement 2: Data Visualization
- Task 1: Apply data handling techniques to prepare various data types for visualization.
- Task 2: Identify and use the most suitable trendlines or plots based on the distribution and characteristics of the data.
- Task 3: Create clear and informative visualizations to highlight the correlations between house attributes and sale prices.

Business Requirement 3: Predictive Modeling
- Task 1: Implement a predictive model to estimate house sale prices.
- Task 2: Handle missing data effectively to ensure accurate predictions for all variables.
- Task 3: Provide the client with a tool or method to predict the sale prices of her four inherited houses and any other house in Ames, Iowa.

## ML Business Case

#### Predict Sale Price
We aim to develop a machine learning model to predict the sale price, in dollars, for homes in Ames, Iowa. The target variable is continuous. We will initially consider a regression model, which is supervised and unidimensional.

Our ideal outcome is to enable the client to reliably predict the sale price of any home in Ames, Iowa, with particular emphasis on the inherited properties the client is concerned about.

**Success Metrics**:
An R² score of at least 0.8 on both the training and test sets.
The model will be considered a failure if, after 12 months of usage, its predictions are off by 30% or more, 20% of the time, and/or if the R² score drops below 0.8.

**Output**:
A continuous value representing the sale price in dollars.

**Target Users**:
Private parties/homeowners who want to estimate the value of their homes.
Real estate agents who need to provide quick estimates to prospective clients during live communications.

**Data Source**:
The training data comes from a public dataset containing approximately 1500 property sales records. It includes one target feature: sale price, and 23 other variables considered as features.

### Regression Model Details
Initially, we implemented the suggested model from feature engineering by strictly following value/threshold selection criteria. During this process, we observed that the Extra Trees Regressor initially indicated better performance. However, upon performing feature importance and regression tests, the results were significantly off compared to our initial correlation study and Predictive Power Score (PPS) analysis. While the correlation study and PPS analysis might not always perfectly reflect the final model performance, the discrepancy was substantial enough to warrant further investigation.

To address this, we reduced the number of transformations (log transformer in particular) by examining the distribution and skewness of the variables, specifically looking for right-skewness and similar patterns. After reducing the transformations, the grid search results indicated that the Gradient Boosting Regressor was more appropriate. This model provided feature importance results that were more consistent with our expectations and aligned rationally with the correlation study and PPS scores.

To ensure the reliability of the Gradient Boosting Regressor, which showed an R² score above the acceptable business requirement limit for both the training and test sets, we performed additional analysis. Despite the Extra Trees Regressor showing slightly higher scores in the initial test, the selected dominant features from the Gradient Boosting Regressor made more sense. This step was crucial to prevent issues such as overfitting and to confirm the robustness of our model.

In the images below you will find images from ExtraTreeRegression.

<details>
<summary>Regression Score (ExtraTreeRegression)</summary>
<img src="docs/readme_images/extra_tree_regr2score.png" width="60%">
</details>



<details>
<summary>Feature Importance (ExtraTreeRegression)</summary>
<img src="docs/readme_images/extra_tree_regr_feat_imp.png" width="60%">
</details>

**Gradient Boosting Regressor - further testing**
We noticed that the feature importance for OverallQual was significantly higher than any other feature in the dataset. While our model evaluation scores for both the training and test sets were high, we wanted to ensure the model's stability and robustness. To investigate this, we employed three methods: Partial Dependence Plot (PDP), checking model performance without OverallQual, and Permutation Importance. These methods can provide a comprehensive understanding of the feature's impact and help verify the model's reliability.

After conducting the tests, we can conclude that:

* OverallQual is consistently identified as the most important feature across all methods, with substantial influence on the model's predictions.
* GrLivArea, TotalBsmtSF, and 2ndFlrSF are also important, though less influential than OverallQual.
* The PDP and feature importance plots provide consistent insights, showing a clear, positive relationship between OverallQual and SalePrice.
* The permutation importance method further validates the model's balanced reliance on multiple features, ensuring robustness and interpretability.
* These findings suggest that OverallQual is a crucial predictor of house prices in the dataset, but the model also benefits from incorporating other significant features. This balanced importance distribution helps in building a robust and generalizable model.



## Dashboard Design

### Page 1: Quick project summary
- Project Terminology
   - Description of factors that may impact the sale (features and attributes).
- Project Background
   - A short background about the motivation and request to initiate the project.
- Project Dataset
   - Description of the scope of the dataset.
- Project Business Requirements
   - This section outlines the business requirements derived from the project background.
- Link to the readme file.

<details>
<summary>Project Summary Page</summary>
<img src="docs/readme_images/page_summary.png" width="60%">
</details>

### Page 2: Sale Price Correlation
- This page displays the result connected to **Business Requirement 1** and 
**Business Requirement 2**
   -  Information of the business requirement criteria
   -  Explanation of the correlation study (Spearman and Pearson) and correlation score threshold.
   -   Information for histogram and scatterplots for the most relevant 
   house attributes.
   - Information and threshold values selected for power predictive score heatmap and bar plot visualization.

- Checkboxes:
   -  CB: "View Sale Price Dataset": Present 10 rows of the dataset.
   -  CB: "Pearson Correlation Ranking": Present Pearson heatmap and barplot.
   -  CB: "Spearman Correlation Ranking": Present Spearman heatmap and barplot.
   -  CB: "Combined Correlation Ranking": The combined Spearman and Pearson heatmap and barplot.
   -  CB: "Correlation Plots of Variables vs Sale Price": Present correlation, single variable to sale price.
   -  CB: "Predictive Power Score: Plot predictive power score.

<details>
<summary>Sale Price Correlation Snapshot</summary>
<img src="docs/readme_images/page_sale_price_corr.png" width="60%">
</details>


<details>
<summary>Sale Price Varibles vs Sale Price </summary>
<img src="docs/readme_images/page_sale_sale_price_varplots.png" width="60%">
</details>






### Page 3: Sale Price Predictor
- This page displays the result connected to **Business Requirement 3**
   -  Information on the business requirement criteria.
   -  Explanation of which features were selected to use as predictors.
   -  Information regarding details of the features.
   -  Presentation field for predicting house price and inherited houses.

- Input fields predict house price
   - IF: "OverallQual"  : Set a value between 1 to 10.
   - IF: "TotalBsmtSF"  : Set a value, max 15275.
   - IF: "2ndFlrSF"     : Set a value, max 5162.
   - IF: "GarageArea"   : Set a value, max 3545.

- Buttons
   - BN: "Run Predictive Analysis": Perform calculation and present it
   - BN: "Run Prediction on Inherited Homes"

<details>
<summary>Sale Price Prediction Snapshot</summary>
<img src="docs/readme_images/page_sale_price_predictor.png" width="60%">
</details>

### Page 4: Project Hypothesis and Validation
- Introduction to hypothesis feature selection criteria.
- Hypothesis 1,2 and 3 presented and their result.

<details>
<summary>Project Hypothesis Snapshot</summary>
<img src="docs/readme_images/page_hypothesis.png" width="60%">
</details> passed the test without any errors found, the test was performed on the files in the app_pages and 
src/machine_learning.
 

### Page 5: ML Price Predictor
- Discuss the steps taken during feature engineering, including checking for missing values, validating analysis types, and applying transformations to address data skewness and normalize distributions.
- Describe how the machine learning pipeline was constructed, detailing the integration of data preprocessing, feature selection, and model training stages.
- Provide metrics and results that demonstrate the effectiveness of the pipeline. 
- Feature importance result.

<details>
<summary>Feature importance</summary>
<img src="docs/readme_images/feature_importance_plot.png" width="60%">
</details> 



### Manual testing

- Browser Testing
   - The Website was tested on Google Chrome, Firefox, Microsoft Edge, and Safari browsers with no issues noted.

- Device Testing
   - The website was viewed on a variety of devices such as Laptop(PC), iPhone 11, and iPad to ensure responsiveness on various screen sizes. The website performed as intended.

## Unfixed Bugs

* No known bugs.

## Deployment

### Heroku

* The App live link is: <https://bl1-heritage-housing-d4f44a67aec9.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

- Pandas: To read data from the house records documented in CSV files and present them as tables.

- Matplotlib: In the data cleaning notebook to visulize the missing values with object variables missing data, to enable plotting  create the figure and subplots with plt.subplots. To set titles for each subplot and adjust the layout with plt.tight_layout and plt.show.

- Seaborn: To create the box plots that we mentioned in the previous point(Matplotlib) with sns.boxplot.

- Feature-engine: To use Categorical imputation for missing values in the Data cleaning notebook.

- Sklearn (linear_model): To evaluate linear regression model in the Machine learning notebook.  

- Ydata-profiling: To create profiling report for the house, used in the Correlation Study notebook to view and analyze data initially before the correlation study.

- Numpy: To handle mask of data in the heatmap visualisation, used in the Correlation Study notebook.

- Scipy: To handle the computation of the trendlines for pearson and spearman used in the Correlation Study notebook.

- PPS: To calculate the predictive power score and investigate pps score threshold value in Feature Engineering notebook. 

- StreamLit: To create the web app for user interaction.

## Credits

* In some sections code is inspired by sections form the code institute course, in these cases a comment is added 
  close to the code section.

* In the Feature Engineering notebook, the Shapiro-Wilk normality test was performed, providing insight on how to apply the correct syntax, e.g., `stats.shapiro`, for a variable by using the [SciPy manual](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html) v.14.0 in the section for 'scipy.stats'.

## Acknowledgements (optional)

* Thanks to my mentor Mo Shami for his support and advice.