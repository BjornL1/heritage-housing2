import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Code from CI walkthrough project 02
@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_housing_data():
    df = pd.read_csv("outputs/datasets/cleaned/HousePricesCleaned.csv")
    return df

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_inherited_house_data():
    df = pd.read_csv(
        "inputs/datasets/raw/house-prices/house-price/inherited_houses.csv")
    return df

def load_pkl_file(file_path):
    return joblib.load(filename=file_path)