import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.trendlines_page import trendlines_page
from app_pages.page_predict_sale_price import page_sale_price_predictor_body
from src.data_management import load_housing_data  # Import the load_heritage_housing_data function

# load pages scripts
from app_pages.page_summary import page_summary_content
from app_pages.page_test2 import page_test2_content
from app_pages.plotting_module import plot_with_custom_trendlines
from app_pages.page_ML_price_predictor import page_ML_price_predictor_content

app = MultiPage(app_name="HeritageHousing")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Project Summary", page_summary_content)
app.add_page("TestSecondPage", page_test2_content)
app.add_page("TrendlinePlottingPage", trendlines_page)
app.add_page("Sale Price Predictor", page_sale_price_predictor_body)  # Add the sale price predictor page
app.add_page("ML Price Predictor", page_ML_price_predictor_content)   # Add the ML predictor page


app.run()  # Run the app