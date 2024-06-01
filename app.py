import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.trendlines_page import trendlines_page
from src.data_management import load_housing_data  # Import the load_heritage_housing_data function

# load pages scripts
from app_pages.page_test1 import page_test1_content
from app_pages.page_test2 import page_test2_content
from app_pages.plotting_module import plot_with_custom_trendlines

app = MultiPage(app_name="HeritageHousing")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("TestFirstPage", page_test1_content)
app.add_page("TestSecondPage", page_test2_content)
app.add_page("TrendlinePlottingPage", trendlines_page)

# Load the data using the load_heritage_housing_data function
heritage_housing_data = load_housing_data()

# Display some information about the loaded data
st.write("Loaded Heritage Housing Data:")
st.write(heritage_housing_data)

app.run()  # Run the app