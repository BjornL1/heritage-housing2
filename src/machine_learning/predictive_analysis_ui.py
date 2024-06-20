import streamlit as st


def predict_sale_price(X_live, property_features, sale_price_pipeline):
    # from live data, subset features related to this pipeline
    X_live_sale_price = X_live.filter(property_features)

    sale_price_prediction = sale_price_pipeline.predict(X_live_sale_price)

    return sale_price_prediction
