import streamlit as st
from app_pages.plotting_module import plot_with_custom_trendlines
from src.data_management import load_housing_data  # Import your data loading function

def trendlines_page():
    st.title("Trendline Plots Page")

    # Load your housing data
    df = load_housing_data()

    # Define the variables and correlation methods
    variables = ['GarageArea', 'YearBuilt', 'TotalBsmtSF', '1stFlrSF', 'OverallQual', 'GrLivArea']
    correlation_methods = ['Pearson', 'Spearman', 'Pearson', 'Spearman', 'Spearman', 'Spearman']

    # Display a checkbox to show the trendline plots
    if st.checkbox("Show Trendline Plots"):
        st.write("Generating trendline plots...")
        plot_with_custom_trendlines(df, variables, correlation_methods)
        st.write("Trendline plots generated successfully!")