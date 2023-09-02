# Q11. An educational researcher is interested in whether a new teaching method improves student test
# scores. They randomly assign 100 students to either the control group (traditional teaching method) or the
# experimental group (new teaching method) and administer a test at the end of the semester. Conduct a
# two-sample t-test using Python to determine if there are any significant differences in test scores
# between the two groups. If the results are significant, follow up with a post-hoc test to determine which
# group(s) differ significantly from each other.

import numpy as np
import scipy.stats as stats

# Generate sample data for the control group and experimental group
np.random.seed(42)  # For reproducibility
control_group = np.random.normal(loc=70, scale=10, size=100)  # Mean = 70, SD = 10
experimental_group = np.random.normal(loc=75, scale=10, size=100)  # Mean = 75, SD = 10

# Perform a two-sample t-test
t_statistic, p_value = stats.ttest_ind(control_group, experimental_group)

# Check if the result is significant
alpha = 0.05  # Significance level
if p_value < alpha:
    print("The two groups have significantly different test scores.")
else:
    print("There is no significant difference in test scores between the two groups.")


# If the two-sample t-test indicates a significant difference between the groups, you can follow up with post-hoc tests (e.g., Tukey's HSD, Bonferroni) to identify which group(s) differ significantly. However, since we're comparing only two groups in this example, there is no need for a post-hoc test; you can simply report the significant difference between the control and experimental groups.