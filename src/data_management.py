import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Code from CI walkthrough project 02
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_housing_data():
    df = pd.read_csv("/workspace/heritage-housing2/outputs/datasets/cleaned/HousePricesCleaned.csv")
    return df
