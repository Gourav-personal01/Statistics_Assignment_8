# Q10. A company wants to know if there are any significant differences in the average time it takes to
# complete a task using three different software programs: Program A, Program B, and Program C. They
# randomly assign 30 employees to one of the programs and record the time it takes each employee to
# complete the task. Conduct a two-way ANOVA using Python to determine if there are any main effects or
# interaction effects between the software programs and employee experience level (novice vs.
# experienced). Report the F-statistics and p-values, and interpret the results.

# Answer - 

import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Create a sample dataset
data = {
    'Software': ['A', 'B', 'C'] * 10,
    'Experience': ['Novice', 'Experienced'] * 15,
    'CompletionTime': [20, 25, 22, 28, 24, 30, 18, 21, 19, 26,
                       23, 29, 17, 20, 18, 25, 22, 28, 16, 19,
                       27, 24, 30, 17, 21, 19, 26, 23, 29, 16]
}

df = pd.DataFrame(data)

# Fit a two-way ANOVA model
model = ols('CompletionTime ~ Software + Experience + Software:Experience', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA results
print(anova_table)


# The ANOVA table will provide F-statistics and p-values for the main effects of software, experience, and their interaction effect. You can interpret the results as follows:

# If the p-value for the main effect of software is significant (typically < 0.05), it suggests that there are significant differences in completion times between the software programs.

# If the p-value for the main effect of experience is significant, it suggests that there are significant differences in completion times between novice and experienced employees.

# If the p-value for the interaction effect (Software:Experience) is significant, it suggests that the effect of software on completion times varies depending on employee experience level.

# Remember to adjust the significance level (e.g., Bonferroni correction) if you're conducting multiple hypothesis tests.