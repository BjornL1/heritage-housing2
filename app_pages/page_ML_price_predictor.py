import streamlit as st
import os
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_regression import (
    regression_performance,
    regression_evaluation_plots
)

def page_ML_price_predictor_content():
    base_path = "outputs/ml_pipeline/predict_sale_price/v14_test/"
    sale_price_feat_importance = os.path.join(base_path, "feat_importance.png")
    model_performance_evaluation = os.path.join(base_path, "model_eval.png")

    # Check if files exist
    if not os.path.isfile(sale_price_feat_importance):
        st.write("Feature Importance image not found at:", sale_price_feat_importance)
    if not os.path.isfile(model_performance_evaluation):
        st.write("Model Evaluation image not found at:", model_performance_evaluation)
    
    st.write("### Prepare Model Pipeline")
    st.info(
         "**Feature Engineering Process**\n\n"
    "Prior to creating the pipeline, we conducted a comprehensive feature"
    " engineering analysis. This process involved transforming raw data into meaningful"
    " features to enhance the predictive power of our models."
    " During the feature engineering phase, we focused on several key steps:"
    " checking for missing values and validating analysis types."
    " Specifically, we applied various transformations such as logarithmic,"
    " power, Box-Cox, Yeo-Johnson, ordinal encoding, and Winsorization."
    " These transformations aimed to address data skewness, normalize distributions,"
    " and ultimately improve model performance."
    )

    st.write("### Create Model Pipeline")
    st.info(
    "**Implement Pipeline**\n\n"
    "* Create a model base to handle missing values and encoding strategies.\n"
    "* Identify hyperparameters and the most relevant features.\n"
    "* Split the data into training and testing sets.\n"
    "* Test Principal Component Analysis (PCA).\n"
    "* Create a PKL file for the best model."
)

    st.write("### Feature Importance")
    st.image(sale_price_feat_importance, use_column_width=True)
    st.write("### Model Performance Evaluation")
    st.image(model_performance_evaluation, use_column_width=True)

    # vsn = version, used to fit linter requirement of 79 characters.
    vsn = 'v14_test'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/regression_pipeline.pkl"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/y_train.csv").squeeze()
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{vsn}/y_test.csv").squeeze()

    # Display pipeline gathered below
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test,
                           pipeline=sale_price_pipe)

    st.write("**Performance Plot**")
    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test, y_test=y_test,
                                pipeline=sale_price_pipe,
                                alpha_scatter=0.5)


# Run the app
if __name__ == "__main__":
    page_ML_price_predictor_content()
