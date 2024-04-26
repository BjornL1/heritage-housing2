# ![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## Template Instructions

Welcome,

This is the Code Institute student template for the Heritage Housing project option in Predictive Analytics. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions. Click the `Use this template` button above to get started.

You can safely delete the Template Instructions section of this README.md file,  and modify the remaining paragraphs for your own project. Please do read the Template Instructions at least once, though! It contains some important information about the IDE and the extensions we use.

## How to use this repo

1. Use this template to create your GitHub project repo

2. Log into the cloud-based IDE with your GitHub account.

3. On your Dashboard, click on the Create button

4. Paste in the URL you copied from GitHub earlier

5. Click Create

6. Wait for the workspace to open. This can take a few minutes.

7. Open a new terminal and `pip3 install -r requirements.txt`

11. Open the jupyter_notebooks directory and click on the notebook you want to open.

12. Click the kernel button and choose Python Environments.

Note that the kernel says Python 3.8.18 as it inherits from the workspace so it will be Python-3.8.18 as installed by our template. To confirm this you can use `! python --version` in a notebook code cell.

## Cloud IDE Reminders

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In your Cloud IDE, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with *Regenerate API Key*.

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


### Problem definition

While the client is well-versed in the determinants of property worth in her own area, it's crucial to understand the unique drivers of value in Ames, Iowa. The client worries that her personal expertise may not be adequate to accurately assess the value, potentially resulting in erroneous appraisals and financial losses.


### Requirements

* 1 - The client is interested in discovering how the house attributes correlate with the sale price. Therefore, the client expects data visualisations of the correlated variables against the sale price to show that.
* 2 - The client is interested in predicting the house sale price from her four inherited houses and any other house in Ames, Iowa.


## Hypothesis, validation and result
* List here your project hypothesis(es) and how you envision validating it (them).

1. Sales price house attribute correlation:
   We assume that the following three features has the strongest correlation: location, size and the condition of the property:
    - Validation: Evaluate each attribute in a correlation study.
    - Result:  


2. Sales price evolution:
   We assume that sales price is increasing with two percent on average per year:
   - Validation: Evaluate sales price development in a correlation (predict power score?) study.
   - Result: 


## The rationale to map the business requirements to the Data Visualisations and ML tasks
* List your business requirements and a rationale to map them to the Data Visualisations and ML tasks.

  Business requirement 1: Correlation study and Data visualisation
    - We will inspect the provided data received from the client.
    - We will conduct a correlation study (TBC) to understand which variables are most relevant for house sale price impact.
    - We will plot the significant variables against price development.


  Business requirement 2: Classification, Regression, Cluster, Data analysis

   - We want to predict the house prices.
   - We want to create a regression model. 
   - TBC
   - TBC    



## ML Business Case
* In the previous bullet, you potentially visualised an ML task to answer a business requirement. You should frame the business case using the method we covered in the course.
//

### Predict Sales price
#### Regression Model
   * We want an ML model to predict ........., in months, for a prospect expected to churn. A target variable is a discrete number. We consider a regression model, which is supervised and uni-dimensional.
   * Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
   * The model success metrics are
   * At least 0.7 for R2 score, on train and test set
   * The ML model is considered a failure if:
      * after 12 months of usage, the model's predictions are 50% off more than 30% of the time. Say, a prediction is >50% off if predicted 10 months and the actual value was 2 months.
   * The output is defined as a continuous value for tenure in months. It is assumed that this model will predict tenure if the Predict Churn Classifier predicts 1 (yes for churn). If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).

Heuristics: Currently, there is no approach to predict the tenure levels for a prospect.
The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
Train data - filter data where Churn == 1, then drop the Churn variable. Target: tenure; features: all other variables, but total charges and customerID
Classification Model
Before the analysis, we visualized a Regressor pipeline to predict Churn; however, the performance didn’t meet the requirement (at least 0.7 for R2 score, on train and test set)
We used a technique to convert the ML task from Regression to Classification. We discretized the target into 3 ranges: <4 months, 4-20 months and +20 months.
The classification pipeline can detect a prospect that would likely churn in less than four months and a prospect that would likely churn in more than 20 months.
A target variable is categorical and contains 3 classes. We consider a classification model, which is supervised and uni-dimensional.
Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
The model success metrics are
At least 0.8 Recall for <4 months, on train and test set
The ML model is considered a failure if:
after 3 months of usage, more than 30% of customers that were expected to churn in <4 months do not churn
The output is defined as a class, which maps to a range of tenure in months. It is assumed that this model will predict tenure if the Predict Churn Classifier predicts 1 (yes for churn). If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).
Heuristics: Currently, there is no approach to predict the tenure levels for a prospect.
The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
Train data - filter data where Churn == 1, then drop the Churn variable. Target: tenure; features: all other variables, but total charges and customerID
Cluster Analysis
Clustering Model
We want an ML model to cluster similar customer behaviour. It is an unsupervised model.
Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
The model success metrics are
at least 0.45 for the average silhouette score
The ML model is considered a failure if the model suggests from more than 15 clusters (might become too difficult to interpret in practical terms)

The output is defined as an additional column appended to the dataset. This column represents the cluster's suggestions. It is a categorical and nominal variable, represented by numbers, starting at 0.
Heuristics: Currently, there is no approach to grouping similar customers
The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
Train data - features: all variables, but customerID, TotalCharges, Churn, and tenure
//


Predict Churn
Classification Model
We want an ML model to predict if a prospect will churn based on historical data from the customer base, which doesn't include tenure and total charges since these values are zero for a prospect. The target variable is categorical and contains 2-classes. We consider a classification model. It is a supervised model, a 2-class, single-label, classification model output: 0 (no churn), 1 (yes churn)
Our ideal outcome is to provide our sales team with reliable insight into onboarding customers with a higher sense of loyalty.
The model success metrics are
at least 80% Recall for Churn, on train and test set

The ML model is considered a failure if:
after 3 months of usage, more than 30% of newly onboarded customers churn (it is an indication that the offers are not working or the model is not detecting potential churners)
Precision for no Churn is lower than 80% on train and test set. (We don't want to offer a free discount to many non-churnable prospects)

The model output is defined as a flag, indicating if a prospect will churn or not and the associated probability of churning. If the prospect is online, the prospect will have already provided the input data via a form. If the prospect talks to a salesperson, the salesperson will interview to gather the input data and feed it into the App. The prediction is made on the fly (not in batches).

Heuristics: Currently, there is no approach to predict churn on prospects
The training data to fit the model comes from the Telco Customer. This dataset contains about 7 thousand customer records.
Train data - target: Churn; features: all other variables, but tenure, total charges and customerID


## Dashboard Design
* List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items that your dashboard library supports.
* Eventually, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but eventually you needed to use another plot type)


//
Page 1: Quick project summary
Quick project summary
Project Terms & Jargon
Describe Project Dataset
State Business Requirements


Page 2: Customer Base Churn Study
Before the analysis, we knew we wanted this page to answer business requirement 1, but we couldn't know in advance which plots would need to be displayed.
After data analysis, we agreed with stakeholders that the page will:
State business requirement 1
Checkbox: data inspection on customer base (display the number of rows and columns in the data, and display the first ten rows of the data)
Display the most correlated variables to churn and the conclusions
Checkbox: Individual plots showing the churn levels for each correlated variable
Checkbox: Parallel plot using Churn and correlated variables


Page 3: Prospect Churnometer
State business requirement 2
Set of widgets inputs, which relates to the prospect profile. Each set of inputs is related to a given ML task to predict prospect Churn, Tenure and Cluster.
"Run predictive analysis" button that serves the prospect data to our ML pipelines, and predicts if the prospect will churn or not, if so, when. It also shows to which cluster the prospect belongs and the cluster's profile. For the churn and tenure predictions, the page will inform the associated probability for churning and tenure level.


Page 4: Project Hypothesis and Validation
Before the analysis, we knew we wanted this page to describe each project hypothesis, the conclusions, and how we validated each. After the data analysis, we can report that:
1 - We suspect customers are churning with low tenure levels
Correct. The correlation study at Churned Customer Study supports that.
2 - A customer survey showed our customers appreciate fibre Optic.
A churned user typically has Fiber Optic, as demonstrated by a Churned Customer Study. The insight will be taken to the survey team for further discussions and investigations.


Page 5: Predict Churn
Considerations and conclusions after the pipeline is trained
Present ML pipeline steps
Feature importance
Pipeline performance


Page 6: Predict Tenure
Considerations and conclusions after the pipeline is trained
Present ML pipeline steps
Feature importance
Pipeline performance


Page 7: Cluster Analysis
Considerations and conclusions after the pipeline is trained
Present ML pipeline steps
Silhouette plot
Clusters distribution across Churn levels
Relative Percentage (%) of Churn in each cluster
The most important features to define a cluster
Cluster Profile
//

## Unfixed Bugs

* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not valid reason to leave bugs unfixed.

## Deployment

### Heroku

* The App live link is: <https://YOUR_APP_NAME.herokuapp.com/>
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.

## Main Data Analysis and Machine Learning Libraries

* Here you should list the libraries you used in the project and provide example(s) of how you used these libraries.

## Credits

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism.
* You can break the credits section up into Content and Media, depending on what you have included in your project.

### Content

* The text for the Home page was taken from Wikipedia Article A
* Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

* The photos used on the home and sign-up page are from This Open Source site
* The images used for the gallery page were taken from this other open-source site

## Acknowledgements (optional)


* In case you would like to thank the people that provided support through this project.

