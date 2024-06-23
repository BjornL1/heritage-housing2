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
    
    st.write("### Quick Project Summary")
    st.info(
        f"**Project Terminology**\n"
        f"**Feature Engineering Process**\n\n"
        f"Prior to creating the pipeline, we conducted a feature" 
        f"engineering analysis."
        f"This involved transforming raw data into meaningful" 
        f"features that could enhance the predictive power of our models."
        f"The feature engineering process included handling" 
        f"missing values, encoding categorical variables, creating" 
        f"new features, and scaling numerical features."
        f"Once the features were engineered, we proceeded" 
        f"to create the pipeline to streamline the data" 
        f"preprocessing and model training processes.\n\n"
        f"Here are the key steps that was handled in the" 
        f"feature engineering:\n\n"
        f"1. **Handling Missing Values**:\n"
        f"   - We identified columns with missing values and applied" 
        f"appropriate strategies such as mean/median imputation for numerical" 
        f"variables and mode imputation for categorical variables.\n\n"
        f"2. **Encoding Categorical Variables**:\n"
        f"   - We converted categorical variables into numerical format" 
        f"using techniques like one-hot encoding or label encoding,"
        f"making them suitable for machine learning algorithms.\n\n"
        f"3. **Creating New Features**:\n"
        f"   - We generated new features based on existing data. For example," 
        f"creating interaction terms, polynomial features, or aggregating" 
        f"information from multiple columns to create new features.\n\n"
        f"4. **Scaling Numerical Features**:\n"
        f"   - We standardized or normalized numerical features to ensure" 
        f"they have a similar scale, which can improve model performance.\n"
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
