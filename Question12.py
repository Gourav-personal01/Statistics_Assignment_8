# Q12. A researcher wants to know if there are any significant differences in the average daily sales of three
# retail stores: Store A, Store B, and Store C. They randomly select 30 days and record the sales for each store
# on those days. Conduct a repeated measures ANOVA using Python to determine if there are any

# significant differences in sales between the three stores. If the results are significant, follow up with a post-
# hoc test to determine which store(s) differ significantly from each other.

import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Create sample data
data = {
    'Store': ['A', 'B', 'C'] * 10,
    'Sales': np.random.randint(1000, 2000, size=30)  # Random sales data for 30 days
}

df = pd.DataFrame(data)

# Perform a one-way ANOVA
f_statistic, p_value = stats.f_oneway(df[df['Store'] == 'A']['Sales'],
                                      df[df['Store'] == 'B']['Sales'],
                                      df[df['Store'] == 'C']['Sales'])

# Check if the result is significant
alpha = 0.05  # Significance level
if p_value < alpha:
    print("There is a significant difference in daily sales between the stores.")
else:
    print("There is no significant difference in daily sales between the stores.")

# If the one-way ANOVA indicates a significant difference between the stores, you can follow up with post-hoc tests like Tukey's HSD or Bonferroni to determine which store(s) differ significantly from each other. However, since we're comparing only three stores in this example, you can simply report the significant difference between the stores without the need for a post-hoc test.
