import streamlit as st


def page_project_hypothesis_content():

    st.write("### Project Hypothesis and Validation Results")

    st.info(
        f"**Hypothesis feature selection criteria**\n"
        f" In the first correlation we set a correlation\n"
        f" threshold at 0.6 for either Spearman or Pearson correlation\n"
        f" to check how many and which values has the strongest correlation\n"
        f" Note that high correlation between two variables indicates\n"
        f" a strong relationship, but it doesn't guarantee that the\n"
        f" predictive power of a model using those variables will be\n"
        f" equally strong.\n")

    st.info(
        f"**Hypothesis 1: Sales price house attribute correlation**\n"
        f"* We assume that the following four features have the\n"
        f"  strongest correlation:\n"
        f"  **lot area**, **size**, **quality** and **age**\n\n"
        f"**Result**:\n"
        f"* **Lot area** is not above the correlation threshold\n"
        f"  and is not matching the hypothesis assumption.\n"
        f"* **Size** (building area) is correct, four values related to\n"
        f"  area (buildings) represent strong correlation:\n"
        f"  **GrLivArea, GarageArea, TotalBsmtSF**, and **1stFlrSF**.\n"
        f"* **Quality** is strongly correlated with sale price\n"
        f"  through **OverallQual**.\n"
        f"* **Age** is strongly correlated with sale price\n"
        f"  through **YearBuilt**.\n\n")
    st.info(
        f"**Hypothesis 2: Determine sales price**\n"
        f"* We assume that the following variables will\n"
        f"  be sufficient to confidently predict the price:\n"
        f"  **lot area**, **house size** (total square feet),\n"
        f"  **overall quality**, and the **build year**.\n\n"
        f"**Result**:\n"
        f" The most relevant house attributes are:\n"
        f"* **OverallQual**\n"
        f"* **TotalBsmtSF**\n"
        f"* **2ndFlrSF**\n"
        f"* **GarageArea**\n"
        f"* 'Lot area' can't be used as a variable to predict\n"
        f"  the sale price and is not matching the\n"
        f"  hypothesis assumption.\n"
        f"* 'YearBuilt'can't be used as a variable to predict\n"
        f"  the sale price and is not matching the\n"
        f"  hypothesis assumption.\n\n")
    st.info(
        f"**Hypothesis 3: Predictive power of key housing features:n**\n"
        f"* We assume that the four features with the highest predictive" 
        f" power presented in Hypothesis 2 are sufficient to achieve" 
        f" an R² score of 0.8 and can be used as reliable indicators" 
        f" of predictive power\n\n"
        f"**Result**:\n"
        f"The assumption was correct in this case, the" 
        f" four features can be used to confidently" 
        f" predict house sale prices. The R² score of 0.901 on" 
        f" the training set and 0.841 on the test set suggests that" 
        f" the model explains a significant portion of the" 
        f" variance in sale prices, which is a positive" 
        f" indication. This means that these four features are" 
        f" indeed very important and provide substantial" 
        f" power.")
