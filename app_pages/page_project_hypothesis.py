import streamlit as st

def page_project_hypothesis_content():

    st.write("### Project Hypothesis and Validation Results")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Hypothesis 1: Sales price house attribute correlation**\n"
        f"* We assume that the following four features has the\n" 
        f"strongest correlation:\n" 
        f"**lot area**, **size**, **quality** and **age**\n\n"
        f"**Hypothesis 2: Determine sales price**\n"
        f"* We assume that the following variables will\n" 
        f"be sufficient to confidently predict the price:\n"
        f"**lot area**,**house size** (total square feet),\n"
        f"**overall quality** and the **build year**\n\n"
        f"**Hypothesis 3: Sale price evolution:**\n"
        f"* We assume that sales price is increasing with\n"
        f"an average of two percent on average per year")


    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Code-Institute-Solutions/churnometer).")
    
