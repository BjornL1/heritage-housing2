import plotly.express as px
import numpy as np
import streamlit as st
from src.data_management import load_housing_data
import matplotlib.pyplot as plt
import seaborn as sns
import ppscore as pps
import pandas as pd
from scipy.stats import pearsonr, spearmanr

sns.set_style("whitegrid")


def page_sale_price_correlation():
    df = load_housing_data()
    vars_to_study = ['OverallQual', 'GrLivArea',
                     'GarageArea', 'TotalBsmtSF', 'YearBuilt', '1stFlrSF']

    st.write("### Property Sale Price Analysis")
    st.success(
        f"* The client is interested in understanding the correlation "
        f" between a property's attributes/features and the sale price."
        f" Therefore, the client expects data visualization of the correlated"
        f" variables against the sale prices for illustration "
        f" (Business Requirement 1), \n"
    )

    # Inspect data
    if st.checkbox("Inspect Sale Price Dataset"):
        st.write(
            f"* The dataset has {df.shape[0]} rows and {df.shape[1]} columns, "
            f"find below the first 10 rows.")
        st.write(df.head(10))
        st.write(
            f"**Information on Categorical Features**\n\n"
            f"* Basement Exposure: Gd - Good Exposure, Av - Average Exposure, "
            f" Mn - Minimum Exposure, "
            f" No - No Exposure, None - No Basement.\n\n"
            f"* Basement Finish Type: GLQ - Good Living Quarters, ALQ - "
            f" Average"
            f" Living Quarters, BLQ - Below Average Living Quarters, REC - "
            f" Average Rec Room, LwQ - Low  Quality, Unf - Unfinished, None - "
            f" No Basement.\n\n"
            f"* Garage Finish: Fin - Finished, RFn - Rough Finish, "
            f" Unf - Unfinished, None - No Garage.\n\n"
            f"* Kitchen Quality: Ex - Excellent, Gd - Good, TA - "
            f" Typical/Average, Fa - Fair, Po - Poor.\n\n"
            f"* Overall Condition: 1 - Very Poor to 10 - Very Excellent.\n\n"
            f"* Overall Quality: 1 - Very Poor to 10 - Very Excellent.\n\n"
        )

    st.write("---")

    st.write("### Correlation Study")
    st.write(
        f"A correlation study was conducted to better understand how "
        f"the variables are correlated to Sale Price. \n"
        f" Below, the results from the Pearson and Spearman correlations"
        f" are displayed in heatmaps. The features most correlated "
        f" with the Sale Price are then also displayed in a bar plot for"
        f" each correlation for simplicity. These figures show that"
        f" the most correlated variable are: **{vars_to_study}**. \n"
        f" Therefore, we also display scatterplots illustrating  the "
        f" correlation of each of these variables with the Sale Price."
    )

    # Pearson and Spearman Correlation
    correlations = calculate_correlations(df)

    st.info(
        f"*** Pearson Correlation *** \n\n"
        f"The Pearson Correlation evaluates the linear relationship between "
        f" two continuous variables."
    )

    if st.checkbox("Pearson Correlation Ranking"):
        display_heatmap(correlations[['Variable', 'Pearson']], 'Pearson Correlation with SalePrice', 'Pearson')

    st.info(
        f"*** Spearman Correlation *** \n\n"
        f"The Spearman correlation evaluates monotonic relationships."
    )

    if st.checkbox("Spearman Correlation Ranking"):
        display_heatmap(correlations[['Variable', 'Spearman']], 'Spearman Correlation with SalePrice', 'Spearman')

    st.info(
        f"*** Combined Rank of Pearson and Spearman Correlation *** \n\n"
        f"This combines the rankings of Pearson and Spearman correlations."
    )

    if st.checkbox("Combined Correlation Ranking"):
        display_heatmap(correlations[['Variable', 'Combined_Rank']], 'Combined Rank of Pearson and Spearman Correlation with SalePrice', 'Combined_Rank')

    st.info(
        f"*** Correlation Scatterplots *** \n\n"
        f"The correlation indicators above confirm that "
        f" Sale Price correlates most strongly with "
        f"the following variables: \n"
        f"* Sale Price tends to increase as Overall Quality "
        f" (OverallQual) goes up. \n"
        f"* Sale Price tends to increase as Groundlevel Living Area "
        f" (GrLivArea) increases. \n"
        f"* Sale Price tends to increase with increasing Garage Area "
        f" (GarageArea). \n"
        f"* Sale Price tends to increase with an increase in Total "
        f" Basement Area (TotalBsmtSF). \n"
        f"* Sale Price tends to increase with an increase in "
        f" Year Built (YearBuilt). \n"
        f"* Sale Price tends to increase with an increase in "
        f" 1st Floor Squarefootage (1stFlrSF). \n\n"
        f"The scatterplots below illustrate the trends of the"
        f" correlations for each variable."
    )

    # Correlation plots adapted from the Data Cleaning Notebook
    if st.checkbox("Correlation Plots of Variables vs Sale Price"):
        correlation_to_sale_price_hist_scat(df, vars_to_study)

    st.info(
        f"*** Predictive Power Score (PPS) ***  \n\n"
        f"Finally, the PPS detects linear or non-linear relationships "
        f"between two variables.\n"
        f"The score ranges from 0 (no predictive power) to 1 "
        f"(perfect predictive power). \n"
        f" To use the plot, find the row on the y-axis labeled 'SalePrice' "
        f" then follow along the row and see the variables, labeled on the "
        f" x-axis, with a pps of more"
        f" than 0.15 expressed on the plot. Overall Quality (OverallQual)"
        f" has the highest predictive power for the Sale Price target."
    )

    if st.checkbox("Predictive Power Score"):
        calc_display_pps_matrix(df)


def calculate_correlations(df):
    categorical_vars = df.select_dtypes(include=['object']).columns.tolist()
    numeric_vars = df.select_dtypes(include=[np.number]).columns.tolist()

    df_encoded = pd.get_dummies(df, columns=categorical_vars, drop_first=True)

    # Ensure 'SalePrice' is included in the numeric variables
    numeric_vars = df_encoded.select_dtypes(include=[np.number]).columns.tolist()
    if 'SalePrice' not in numeric_vars:
        numeric_vars.append('SalePrice')

    correlations = {'Variable': [], 'Pearson': [], 'Spearman': []}

    for var in numeric_vars:
        if var != 'SalePrice':  # Exclude the target variable itself
            x = df_encoded[var]
            y = df_encoded['SalePrice']

            pearson_coef, _ = pearsonr(x, y)
            spearman_coef, _ = spearmanr(x, y)

            correlations['Variable'].append(var)
            correlations['Pearson'].append(pearson_coef)
            correlations['Spearman'].append(spearman_coef)

    # Create a DataFrame with the correlation results
    correlation_df = pd.DataFrame(correlations)
    correlation_df['Abs_Pearson'] = correlation_df['Pearson'].abs()
    correlation_df['Abs_Spearman'] = correlation_df['Spearman'].abs()

    # Rank the variables based on absolute correlations
    correlation_df['Pearson_Rank'] = correlation_df['Abs_Pearson'].rank(ascending=False)
    correlation_df['Spearman_Rank'] = correlation_df['Abs_Spearman'].rank(ascending=False)
    correlation_df['Combined_Rank'] = (correlation_df['Pearson_Rank'] + correlation_df['Spearman_Rank']) / 2

    # Sort the DataFrame based on the combined rank
    correlation_df.sort_values(by='Combined_Rank', inplace=True)

    return correlation_df


def display_heatmap(df, title, column):
    df.set_index('Variable', inplace=True)
    mask = np.zeros_like(df, dtype=bool)
    mask[abs(df) < 0.2] = True
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(df, annot=True, mask=mask, cmap='viridis', annot_kws={"size": 10}, ax=ax)
    plt.title(title)
    st.pyplot(fig)


def correlation_to_sale_price_hist_scat(df, vars_to_study):
    """ Display correlation plot between variables and sale price with integrated trendlines using plotly """
    target_var = 'SalePrice'
    for col in vars_to_study:
        # Scatter plot with trendline
        fig = px.scatter(df, x=col, y=target_var, color='OverallQual', trendline='ols', title=f"{col} vs {target_var}")
        fig.update_layout(plot_bgcolor='white')  # Set background color to white
        st.plotly_chart(fig)
        st.write("\n\n")


def calc_display_pps_matrix(df):
    """ Calculate and display Predictive Power Score """
    pps_matrix_raw = pps.matrix(df)
    pps_matrix = pps_matrix_raw.filter(['x', 'y', 'ppscore']).pivot(
        columns='x', index='y', values='ppscore')
    heatmap_pps(df=pps_matrix, threshold=0.15, figsize=(12, 10), font_annot=10)

    pps_topscores = pps_matrix.iloc[19].sort_values(
        key=abs, ascending=False)[1:6]

    fig, axes = plt.subplots(figsize=(6, 3))
    axes = plt.bar(x=pps_topscores.index, height=pps_topscores)
    plt.xticks(rotation=90)
    plt.title("Predictive Power Score for Sale Price", fontsize=15, y=1.05)
    st.pyplot(fig)


def heatmap_pps(df, threshold, figsize=(20, 12), font_annot=8):
    """ Heatmap for predictive power score from CI template"""
    if len(df.columns) > 1:
        mask = np.zeros_like(df, dtype=bool)
        mask[abs(df) < threshold] = True
        fig, axes = plt.subplots(figsize=figsize)
        axes = sns.heatmap(df, annot=True, xticklabels=True, yticklabels=True,
                           mask=mask, cmap='rocket_r',
                           annot_kws={"size": font_annot},
                           linewidth=0.05, linecolor='grey')
        plt.ylim(len(df.columns), 0)
        st.pyplot(fig)



