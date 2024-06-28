import streamlit as st


def page_summary_content():
    """
    Displays contents of the project summary page
    """
    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terminology**\n"
        f"* Any factor that may impact the sale price is referred to as a\n"
        f"**feature** or **attribute**,\n"
        f" which can be represented, for example, by square footage or\n"
        f"kitchen quality.")

    st.info(
        f"**Project Background**\n"
        f"* A client in Germany requested an app to predict house sale\n"
        f" prices in Ames, Iowa.\n"
        f"* The client has inherited four properties and wants to avoid \n"
        f" financial losses.\n"
        f"* Additionally, the client seeks to identify key\n"
        f"features influencing house sales.\n"
        f"* To achieve this, the client seeks to use a machine learning\n"
        f"app to predict prices and reduce risk.")

    st.info(
        f"**Project Dataset**\n"
        f"* Since the request from the client is to predict\n"
        f" sale prices for the houses in general in Ames as well\n"
        f" the sale price for the inherited properties.\n"
        f"* The datasets are defined as\n"
        f" dataset 1 (DS1) which is the main set and\n"
        f" dataset 2 (DS2) for the inherited houses\n"
        f"* DS1: This dataset contains nearly 1500 rows and 24 columns.\n"
        f" Among these, 23 columns\n"
        f" represent various house attributes\n"
        f" (such as quality or square footage)\n"
        f" that will be analyzed.\n"
        f" The target variable in this dataset is the sale price.\n"
        f"* DS2: There are four rows of data in this data which will\n"
        f" be calculated by using the model output from dataset 1.\n")

    st.info(
        f"**Project Business Requirements**\n"
        f"* The requested app was specified according to the\n"
        f" following business requirements:\n"
        f"* BR1: Identify the most relevant house attributes\n"
        f" correlating with the sale price.\n"
        f"* BR2: Visualize data for business requirement\n"
        f" number one (mentioned above).\n"
        f"* BR3: Predict the sale price of the inherited houses\n"
        f"and any other house in Ames, Iowa.\n")

    st.write(
        f"* For additional information, please visit and read the\n"
        f"[Project README file]\n"
        f"(https://github.com/BjornL1/heritage-housing2/tree/main).")
