import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, linregress
from statsmodels.nonparametric.smoothers_lowess import lowess
import streamlit as st
import ppscore as pps
from src.data_management import load_housing_data


sns.set_style("whitegrid")

# Function to plot a variable - SalePrice with Pearson and Spearman trendlines


def plot_with_custom_trendlines(df, vars, target='SalePrice'):
    num_vars = len(vars)
    plt.figure(figsize=(16, 6 * num_vars))

    for i, var in enumerate(vars, 1):
        x = df[var]
        y = df[target]

        plt.subplot(num_vars, 1, i)
        sns.scatterplot(x=x, y=y, label='Data points')

        if var == 'TotalBsmtSF':
            # Pearson correlation
            pearson_coef, _ = pearsonr(x, y)
            slope_pearson, intercept_pearson, _, _, _ = linregress(x, y)
            line_pearson = slope_pearson * x + intercept_pearson
            plt.plot(x, line_pearson, color='red', label=f'Pearson trendline (r={pearson_coef:.2f})')
        else:
            # Spearman correlation
            spearman_coef, _ = spearmanr(x, y)
            lowess_smoothed = lowess(y, x, frac=0.3)
            plt.plot(lowess_smoothed[:, 0], lowess_smoothed[:, 1], 
                     color='blue', 
                     label=f'Spearman trendline (r={spearman_coef:.2f})')
        
        plt.xlabel(var)
        plt.ylabel(target)
        plt.title(f'{var} vs {target} with Trendline')
        plt.legend()
    
    plt.tight_layout()
    st.pyplot(plt)  # Use st.pyplot to display the plot in Streamlit

def page_sale_price_correlation():
    df = load_housing_data()
    vars_to_study = ['OverallQual', 'GrLivArea', 'GarageArea', 'TotalBsmtSF', 'YearBuilt', '1stFlrSF']

    st.write("### House Attributes Data")
    st.info(
        f"* In order to get a deeper understanding"
        f" of the different house attributes and which"
        f" values are used for each, a table of the first ten" 
        f" rows of data is displayed by clicking on" 
        f" the 'View Sale Price Dataset' below."
    )

    # Inspect data
    if st.checkbox("View Sale Price Dataset"):
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

    st.write("### Correlation Study (BR1, BR2)")
    st.write(
        f"* In the development phase of the project, the first two business"
        f" requirements were stated as follows;\n"
        f"* BR1:The client is interested in identifying which house" 
        f" attributes have the strongest correlation with the sale price.\n"
        f"* BR2: The client expects data visualizations of the correlated"
        f"  variables against the sale price to demonstrate this"
        f" the most correlated variable are: **{vars_to_study}**. \n"
        f" To display the variables we will use Pearson, Spearman and"
        f" Power Predictive score illustrations"
    )

    # Pearson and Spearman Correlation
    correlations = calculate_correlations(df)

    st.info(
        f"*** Pearson Correlation *** \n\n"
        f"The Pearson correlation coefficient measures"
        f" the strength and direction of the linear" 
        f" relationship between two continuous" 
        f" variables, with values" 
        f" ranging from -1 (perfect negative correlation) to" 
        f" +1 (perfect positive correlation)." 
        f" A value of 0 indicates no linear relationship between the variables."
    )

    if st.checkbox("Pearson Correlation Ranking"):
        display_heatmap(correlations[['Variable', 'Pearson']], 'Pearson Correlation with SalePrice', 'Pearson')

    st.write("---")

    st.info(
        f"*** Spearman Correlation *** \n\n"
        f"The Spearman correlation coefficient measures"
        f" the strength and direction of the monotonic relationship"
        f" between two ranked variables, with values"
        f" ranging from -1 (perfect negative correlation) to"
        f" +1 (perfect positive correlation)."
        f" A value of 0 indicates no monotonic relationship between the variables."
    )

    if st.checkbox("Spearman Correlation Ranking"):
        display_heatmap(correlations[['Variable', 'Spearman']], 'Spearman Correlation with SalePrice', 'Spearman')

    st.write("---")

    st.info(
        f"*** Combined Rank of Pearson and Spearman Correlation *** \n\n"
        f"This displayes the combines the rankings of Pearson and Spearman"
        f" correlations."
    )

    if st.checkbox("Combined Correlation Ranking"):
        display_heatmap(correlations[['Variable', 'Combined_Rank']], 'Combined Rank of Pearson and Spearman Correlation with SalePrice', 'Combined_Rank')

    st.write("---")

    st.info(
        f"*** Data Distribution and Trendline Plots *** \n\n"
        f"To visualize the data distribution and present the trend, "
        f"we provide plots to understand historical changes and illustrate "
        f"the relationship between each variable and Sale Price. "
        f"The trendlines in the plots represent these relationships. \n\n"
        f"For all variables except TotalBsmtSF, the Spearman trendline "
        f"best explains the correlation with Sale Price. However, for TotalBsmtSF, "
        f"we use the Pearson trendline because the Spearman trendline "
        f"displayed an overfitted curve and misleading correlation."
    )

    # Correlation plots adapted from the Data Cleaning Notebook
    if st.checkbox("Correlation Plots of Variables vs Sale Price"):
        plot_with_custom_trendlines(df, vars_to_study)

    st.write("---")

    st.info(
    f"*** Predictive Power Score (PPS) ***\n\n"
    f"* The Predictive Power Score (PPS) is a metric used to measure the "
    f"strength of the predictive relationship between two variables. "
    f"Unlike traditional correlation metrics like Pearson or Spearman, "
    f"PPS can capture both linear and non-linear relationships. "
    f"It ranges from 0 (no predictive power) to 1 (perfect predictive power).\n\n"
    f"* PPS is particularly useful in identifying important features for "
    f"machine learning models and understanding complex data relationships. "
    f"In the plots below, we illustrate the PPS for various "
    f"features in relation to the Sale Price. "
    f"Features with a PPS higher than 0.15 are considered to have "
    f"significant predictive power."
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
