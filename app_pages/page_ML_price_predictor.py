import streamlit as st

def page_ML_price_predictor_content():
    # Define the paths to the images
    base_path = "/workspace/heritage-housing2/outputs/ml_pipeline/predict_sale_price/v14_test/"
    sale_price_feat_importance = f"{base_path}features_importance.png"
    model_performance_evaluation = f"{base_path}model_performance_evaluation.png"
    
    # Display the images
    st.write("### Feature Importance")
    st.image(sale_price_feat_importance, caption="Feature Importance", use_column_width=True)

    st.write("### Model Performance Evaluation")
    st.image(model_performance_evaluation, caption="Model Performance Evaluation", use_column_width=True)


