import streamlit as st
import os

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
