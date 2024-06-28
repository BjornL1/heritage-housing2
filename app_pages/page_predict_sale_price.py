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
    vsn = 'v15_test'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/regression_pipeline.pkl"
    )
    sale_price_features = (
        pd.read_csv(
            f"outputs/ml_pipeline/predict_sale_price/{vsn}/X_train.csv")
        .columns
        .to_list()
    )

    st.write("### Sale Price Predictor Interface (BR3)")
    st.info(
        f"* Using machine learning we detected that the four"
        f" most relevant house attributes are:\n"
        f"**OverallQual**, **TotalBsmtSF**,\n"
        f"**2ndFlrSF** and **GarageArea**.\n"
        f" By implementing the two features below to run"
        f" predictive analysis on house sale prices, we have completed"
        f" the third business requirement:\n"
        f"* BR3: The client is interested in predicting the house"
        f" sale price from her four inherited houses and any"
        f" other house in Ames, Iowa.")

    st.info(
        f"* It should be noted that, although a strong"
        f" a strong feature correlation with sale price"
        f" is often suitable for predicting the sale price,"
        f" it does not necessarily guarantee good prediction results"
        f" features of the property in question, which the client can input.\n"
        f"* If only the correlation score is used as a factor for predicting"
        f" the sale price, it can lead to overfitting, suffer from"
        f" multicollinearity, represent a non-causal relationship,"
        f" or fail to capture important nuances.")

    st.info(
        f" Selected house attributes details\n"
        f"* OverallQual:1-10 (1 very poor, 10 very excellent)\n"
        f"* TotalBsmtSF:0-15275 (square footage)\n"
        f"* 2ndFlrSF:0-5162 (square footage)\n"
        f"* GarageArea:0-3545 (square footage)")

    st.write("---")

    st.write("### Sale Price Predictor Tool:")
    X_live = DrawInputsWidgets(sale_price_features)

    if st.button("Run Predictive Analysis"):
        sale_price_prediction = predict_sale_price(
            X_live, sale_price_features, sale_price_pipe)
        formatted_price = '${:,.2f}'.format(sale_price_prediction[0])
        st.write("* The model has predicted a sale value of:")
        st.write(f"**{formatted_price}**")

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

        st.write(f"* The total value of the inherited homes estimation is:")
        st.write(f"**{total_value}**")


def DrawInputsWidgets(sale_price_features):
    df = load_housing_data()
    percentageMin, percentageMax = 0.2, 2.5

    # Specify the four features for user input
    user_input_features = [
        "OverallQual", "TotalBsmtSF", "2ndFlrSF", "GarageArea"]
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
            elif (df[feature].dtype == 'int64' or
                  df[feature].dtype == 'float64'):
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
                default_value = 0 if feature not in df.columns or \
                    df[feature].dtype in ['int64', 'float64'] else 'None'
            X_live[feature] = default_value

    return X_live


if __name__ == "__main__":
    page_sale_price_predictor_body()
