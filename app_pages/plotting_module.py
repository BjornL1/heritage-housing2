import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr, linregress
from statsmodels.nonparametric.smoothers_lowess import lowess


def plot_with_custom_trendlines(
        df,
        vars,
        correlation_methods,
        target='SalePrice'
        ):
    num_vars = len(vars)
    plt.figure(figsize=(16, 6 * num_vars))

    for i, (var, corr_method) in enumerate(zip(vars, correlation_methods), 1):
        x = df[var]
        y = df[target]

        if corr_method == 'Pearson':
            coef, _ = pearsonr(x, y)
            slope, intercept, _, _, _ = linregress(x, y)
            line = slope * x + intercept
        elif corr_method == 'Spearman':
            coef, _ = spearmanr(x, y)
            lowess_smoothed = lowess(y, x, frac=0.3)

        plt.subplot(num_vars, 1, i)
        sns.scatterplot(x=x, y=y, label='Data points')

        if corr_method == 'Pearson':
            plt.plot(
                x,
                line,
                color='red',
                label=f'{corr_method} trendline (r={coef:.2f})'
                )
        elif corr_method == 'Spearman':
            plt.plot(
                lowess_smoothed[:, 0], lowess_smoothed[:, 1],
                color='blue', label=f'{corr_method} trendline (r={coef:.2f})'
            )

        plt.xlabel(var)
        plt.ylabel(target)
        plt.title(f'{var} vs {target} with {corr_method} Trendline')
        plt.legend()

    plt.tight_layout()
    plt.show()
