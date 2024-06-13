import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import date
from src.data_management import (
    load_housing_data,
    load_pkl_file,
    load_inherited_house_data
)
from src.machine_learning.evaluate_regression import regression_performance
from src.machine_learning.predictive_analysis_ui import predict_sale_price

def page_sale_price_predictor_body():
    # Load predict sale price files
    vsn = 'v12_test'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/regression_pipeline.pkl"
    )
    sale_price_features = (
        pd.read_csv(
            f"outputs/ml_pipeline/predict_sale_price/{vsn}/X_train.csv")
        .columns
        .to_list()
    )

    st.write("### Sale Price Predictor Interface")
    st.success(
        f"* The client is interested in predicting the potential sale "
        f" prices"
        f" for properties in Ames, Iowa, and specifically, she wants to"
        f" determine a potential value for the properties she inherited "
        f" (Business Requirement 2). \n"
    )
    st.info(
        f"The price prediction will be based on four "
        f" features of the property in question, which the client can input"
        f" using the selections below. These features were identified by"
        f" the machine learning model as the best features to predict Sale "
        f" Price. They are similar to, but may differ slightly from, the "
        f" variables "
        f" identified as most correlated in the initial data analysis. This "
        f" is because the model will carry out more complex analysis on the "
        f" variables behind the scenes and identify the best variables to use"
        f" for the prediction of the Sale Price. \n\n More information on the "
        f" machine learning model and feature importance can be found on the "
        f" **ML: Price Prediction** page. \n\n"
        f"**Information on categorical features used in the prediction**\n\n"
        f"* Overall Quality: 1 - Very Poor to 10 - Very Excellent.\n\n"
        f"All three numerical features are measured in square feet."
    )
    st.write("---")

    # Generate Live Data
    X_live = DrawInputsWidgets(sale_price_features)

    # predict on live data
    if st.button("Run Predictive Analysis"):
        sale_price_prediction = predict_sale_price(X_live, sale_price_features, sale_price_pipe)
        st.write(f"Predicte Sale Price: {sale_price_prediction[0]}")
    
    st.write("---")

    st.write("### Price prediction for the client's inherited properties:")
    in_df = load_inherited_house_data()
    in_df = in_df.filter(sale_price_features)

    st.write("* Features of Inherited Homes")
    st.write(in_df)

    if st.button("Run Prediction on Inherited Homes"):
        inherited_price_prediction = predict_sale_price(
            in_df, sale_price_features, sale_price_pipe)
        total_value = inherited_price_prediction.sum()
        total_value = float(total_value.round(1))
        total_value = '${:,.2f}'.format(total_value)

        st.write(f"* The total value of the inherited homes is estimated"
                 f" to be:")
        st.write(f"## **{total_value}**")

def DrawInputsWidgets(sale_price_features):
    # load dataset
    df = load_housing_data()
    percentageMin, percentageMax = 0.2, 2.5

    # specify the four features for user input
    user_input_features = ["OverallQual", "TotalBsmtSF", "2ndFlrSF", "GarageArea"]
    X_live = pd.DataFrame([], index=[0])

    for feature in user_input_features:
        if feature in df.columns:
            if feature == "OverallQual":
                st_widget = st.number_input(
                    label=f'{feature}',
                    min_value=1,
                    max_value=10,
                    value=int(df[feature].median()),
                    step=1
                )
            elif df[feature].dtype == 'int64' or df[feature].dtype == 'float64':
                min_value = int(df[feature].min() * percentageMin)
                max_value = int(df[feature].max() * percentageMax)
                median_value = int(df[feature].median())
                st_widget = st.number_input(
                    label=f'{feature}',
                    min_value=min_value,
                    max_value=max_value,
                    value=median_value,
                    step=20
                )
            else:
                unique_values = df[feature].unique()
                st_widget = st.selectbox(
                    label=f'{feature}',
                    options=unique_values
                )
            X_live[feature] = st_widget

    # Fill the remaining features with default values
    for feature in sale_price_features:
        if feature not in user_input_features:
            if feature in df.columns:
                if df[feature].dtype in ['int64', 'float64']:
                    default_value = df[feature].median()
                else:
                    default_value = df[feature].mode()[0]
            else:
                # Set a generic default value for missing features
                default_value = 0 if feature not in df.columns or df[feature].dtype in ['int64', 'float64'] else 'None'
            X_live[feature] = default_value

    return X_live

if __name__ == "__main__":
    page_sale_price_predictor_body()

