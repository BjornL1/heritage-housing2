import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.trendlines_page import trendlines_page
from app_pages.page_predict_sale_price import page_sale_price_predictor_body
from src.data_management import load_housing_data  


from app_pages.page_summary import page_summary_content
from app_pages.page_project_hypothesis import page_project_hypothesis_content
from app_pages.plotting_module import plot_with_custom_trendlines
from app_pages.page_ML_price_predictor import page_ML_price_predictor_content

app = MultiPage(app_name="House Sale Price Predictor") 

app.add_page("Project Summary", page_summary_content)
app.add_page("Sale Price Correlation", trendlines_page)
app.add_page("Sale Price Predictor", page_sale_price_predictor_body)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_content)  
app.add_page("ML Price Predictor", page_ML_price_predictor_content)   

app.run()