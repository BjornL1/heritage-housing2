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
        f"* **Lot area** can't be used as a variable to predict\n"
        f"  the sale price and is not matching the\n"
        f"  hypothesis assumption.\n"
        f"* **House size** (total square feet) is mostly correct,\n"
        f"  the most relevant variables are:\n"
        f"  **TotalBsmtSF, 2ndFlrSF**, and **GarageArea**.\n"
        f"* **YearBuilt** can't be used as a variable to predict\n"
        f"  the sale price and is not matching the\n"
        f"  hypothesis assumption.\n\n")
    st.info(
        f"**Hypothesis 3: Sale price evolution**\n"
        f"* We assume that sales price is increasing with\n"
        f"  an average of two percent per year and\n"
        f"  can be used to determine future price.\n\n"
        f"**Result**:\n"
        f"The simplified method yields an average\n"
        f"annual percent increase of approximately 1.26%\n"
        f"between 1950 and 2010. However, for the most recent\n"
        f"five years of this period, the variation is\n"
        f"significant, making the prediction more complex.\n"
        f"Therefore, this average cannot be reliably used as a\n"
        f"variable to predict the sale price, as it does not\n"
        f"match the hypothesis assumption.")
