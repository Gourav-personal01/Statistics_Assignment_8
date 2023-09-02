# Q5. In a two-way ANOVA, how would you calculate the main effects and interaction effects using Python?

import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create sample data
data = {'A': [1, 1, 2, 2, 3, 3],
        'B': [1, 2, 1, 2, 1, 2],
        'Y': [4, 6, 7, 8, 11, 13]}

df = pd.DataFrame(data)

# Fit a two-way ANOVA model
model = ols('Y ~ A + B + A:B', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Extract main effects and interaction effect
main_effect_A = anova_table.loc['A', 'sum_sq'] / anova_table.loc['A', 'df']
main_effect_B = anova_table.loc['B', 'sum_sq'] / anova_table.loc['B', 'df']
interaction_effect = anova_table.loc['A:B', 'sum_sq'] / anova_table.loc['A:B', 'df']

# Print the results
print("Main Effect A:", main_effect_A)
print("Main Effect B:", main_effect_B)
print("Interaction Effect:", interaction_effect)
