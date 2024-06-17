import streamlit as st
import os
import pandas as pd
from src.data_management import load_pkl_file
from src.machine_learning.evaluate_regression import (
    regression_performance,
    regression_evaluation_plots
)

def page_ML_price_predictor_content():
    # Define the paths to the images using relative paths
    base_path = "outputs/ml_pipeline/predict_sale_price/v14_test/"
    sale_price_feat_importance = os.path.join(base_path, "features_importance.png")
    model_performance_evaluation = os.path.join(base_path, "model_performance_evaluation.png")
    
    # Check if files exist
    if not os.path.isfile(sale_price_feat_importance):
        st.write("Feature Importance image not found at:", sale_price_feat_importance)
    if not os.path.isfile(model_performance_evaluation):
        st.write("Model Performance Evaluation image not found at:", model_performance_evaluation)
    
    # Display the images
    st.write("### Feature Importance")
    st.image(sale_price_feat_importance, caption="Feature Importance", use_column_width=True)

    st.write("### Model Performance Evaluation")
    st.image(model_performance_evaluation, caption="Model Performance Evaluation", use_column_width=True)

 # Load regression pipeline and data files
    version = 'v14_test'
    sale_price_pipe = load_pkl_file(
        f"outputs/ml_pipeline/predict_sale_price/{version}/regression_pipeline.pkl"
    )
    X_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_train.csv")
    X_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/X_test.csv")
    y_train = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_train.csv").squeeze()
    y_test = pd.read_csv(
        f"outputs/ml_pipeline/predict_sale_price/{version}/y_test.csv").squeeze()

    # Display pipeline performance
    st.write("### Pipeline Performance")
    regression_performance(X_train=X_train, y_train=y_train,
                           X_test=X_test, y_test=y_test,
                           pipeline=sale_price_pipe)

    # Display performance plots
    st.write("**Performance Plot**")
    regression_evaluation_plots(X_train=X_train, y_train=y_train,
                                X_test=X_test, y_test=y_test,
                                pipeline=sale_price_pipe,
                                alpha_scatter=0.5)

# Run the app
if __name__ == "__main__":
    page_ML_price_predictor_content()