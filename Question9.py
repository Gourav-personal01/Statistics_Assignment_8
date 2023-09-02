# Q9. A researcher wants to compare the mean weight loss of three diets: A, B, and C. They collect data from
# 50 participants who were randomly assigned to one of the diets. Conduct a one-way ANOVA using Python
# to determine if there are any significant differences between the mean weight loss of the three diets.
# Report the F-statistic and p-value, and interpret the results.

# Answer - 

# Null Hypothesis HO - There is a significant change
# Alternate Hypotheis H1 - There is a No significant change


import numpy as np
from scipy import stats

# Example data for different groups (treatment levels)
group1 = np.random.randint(10, 19, size=50)
group2 = np.random.randint(10, 19, size=50)
group3 = np.random.randint(10, 19, size=50)

# Combine the data into a single array
data = np.concatenate([group1, group2, group3])

# Calculate the overall mean
overall_mean = np.mean(data)

# Calculate the Total Sum of Squares (SST)
sst = np.sum((data - overall_mean)**2)

# Calculate the group means
mean_group1 = np.mean(group1)
mean_group2 = np.mean(group2)
mean_group3 = np.mean(group3)

# Calculate the Explained Sum of Squares (SSE)
sse = len(group1) * (mean_group1 - overall_mean)**2 + \
      len(group2) * (mean_group2 - overall_mean)**2 + \
      len(group3) * (mean_group3 - overall_mean)**2

# Calculate the Residual Sum of Squares (SSR)
ssr = np.sum((group1 - mean_group1)**2) + \
      np.sum((group2 - mean_group2)**2) + \
      np.sum((group3 - mean_group3)**2)

# Calculate the degrees of freedom
df_total = len(data) - 1
df_groups = 3 - 1  # Number of groups minus 1
df_residual = df_total - df_groups

# Calculate the Mean Square for Groups (MSG) and Residual (MSE)
msg = sse / df_groups
mse = ssr / df_residual

# Calculate the F-statistic
f_statistic = msg / mse

# Calculate the p-value
p_value = 1 - stats.f.cdf(f_statistic, df_groups, df_residual)

# Print the results
print("Total Sum of Squares (SST):", sst)
print("Explained Sum of Squares (SSE):", sse)
print("Residual Sum of Squares (SSR):", ssr)
print("F-statistic:", f_statistic)
print("P-value:", p_value)

if f_statistic > p_value:
    print("Reject the Null hyoothesis")
else:
    print("Failed to reject the null hypothesis")