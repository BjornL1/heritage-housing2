import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_test1 import page_test1_content
from app_pages.page_test2 import page_test2_content

app = MultiPage(app_name= "HeritageHousing") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("TestFirstPage", page_test1_content)
app.add_page("TestSecondPage", page_test2_content)
app.add_page("TrendlinePlottingPage", trendlines_page)

app.run() # Run the  app