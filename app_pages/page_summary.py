import streamlit as st

def page_summary_content():
    """
    Displays contents of the project summary page
    """
    st.write("### Quick Project Summary")

    st.info(
        f"**Project Terminology**\n"
        f"* Any factor that may impact the sale price is referred to as a **feature** or **attribute**,\n"
        f" which can be represented, for example, by square footage or kitchen quality.")
      
    st.info(
        f"**Project Background**\n"
        f"* A client in Germany requested an app to predict house sale prices in Ames, Iowa.\n"
        f"* The client has inherited four properties and wants to avoid financial losses. \n"
        f"* Additionally, the client seeks to identify key features influencing house sales.\n"
        f"* To achieve this, the client seeks to use a machine learning app to predict prices and reduce risk.")
    
    st.info(
        f"**Project Dataset**\n"
        f"* Since the request from the client is to predict sale prices and also predict\n" 
        f" to predict the sale price for the inherited properties, the datasets are defined as\n"
        f" dataset 1 (DS1) which is the main set and dataset 2 (DS2) for the inherited houses\n"
        f"*DS1: This dataset contains nearly 1500 rows and 24 columns. Among these, 23 columns\n"
        f" represent various house attributes (such as quality or square footage) that will be\n"
        f" analyzed. The target variable in this dataset is the sale price.\n"
        f"* DS2: There are four rows of data in this data which will be calculated by using\n" 
        f"the input in dataset 1\n")
       
    st.info(
        f"**Project Business Requirements**\n"
        f"* The requested app was specified according to the following business requirements:\n"
        f"* BR1: Identify the most relevant house attributes correlating with the sale price.\n"
        f"* BR2: Visualize data for business requirement number one (mentioned above).\n"
        f"* BR3: Predict the sale price of the inherited houses and any other house in Ames, Iowa.\n")
    
    st.write(
    "* For additional information, please visit and **read** the\n"
    "[Project README file](https://github.com/Code-Institute-Solutions/churnometer).")