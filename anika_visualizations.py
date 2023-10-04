# packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from scipy.stats import chi2

# 2014 data
data_2014 = pd.read_csv("2014surveyclean.csv")

# 2019 data
data_2019 = pd.read_csv("cleaning_data2019.csv")

# combined 2014 and 2019 data
data_combined = pd.concat([data_2014, data_2019], axis=0, ignore_index=True)

# CHI SQUARED + HEATMAPS (2014 data only)
# Physical health consequence vs. supervisor
# Contingency table + heatmap
physhealth_supervisor_2014 = pd.crosstab(data_2014['phys_health_consequence'],
                                       data_2014['supervisor'],
                                       margins = False)
sns.heatmap(physhealth_supervisor_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Physical Health Issue has Negative Consequences")
plt.xlabel("Willing to Talk with Supervisor")
plt.title("Physical Health Consequence vs. Talking to Supervisor")
plt.show()

# Chi Squared Test
stat, p, dof, expected = chi2_contingency(physhealth_supervisor_2014)
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
print("Physical health consequence vs supervisor")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# Mental health consequence vs. supervisor
# Contingency table + heatmap
menthealth_supervisor_2014 = pd.crosstab(data_2014['mental_health_consequence'],
                                       data_2014['supervisor'],
                                       margins = False)
sns.heatmap(menthealth_supervisor_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Mental Health Issue has Negative Consequences")
plt.xlabel("Willing to Disclose to Supervisor")
plt.title("Mental Health Consequence vs. Talking to Supervisor")
plt.show()

# Chi Squared Test
stat, p, dof, expected = chi2_contingency(menthealth_supervisor_2014)
print("\nMental health consequence vs supervisor")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# Physical health consequence vs. coworkers
# Contingency table + heatmap
physhealth_coworker_2014 = pd.crosstab(data_2014['phys_health_consequence'],
                                       data_2014['coworkers'],
                                       margins = False)
sns.heatmap(physhealth_coworker_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Physical Health Issue has Negative Consequences")
plt.xlabel("Willing to Talk with Coworkers")
plt.title("Physical Health Consequence vs. Talking to Coworkers")
plt.show()

# Chi Squared Test
stat, p, dof, expected = chi2_contingency(physhealth_coworker_2014)
print("\nPhysical health consequence vs coworkers")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# Mental health consequence vs. coworkers
# Contingency table + heatmap
menthealth_coworker_2014 = pd.crosstab(data_2014['mental_health_consequence'],
                                       data_2014['coworkers'],
                                       margins = False)
sns.heatmap(menthealth_coworker_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Mental Health Issue has Negative Consequences")
plt.xlabel("Willing to Disclose to Coworkers")
plt.title("Mental Health Consequence vs. Talking to Coworkers")
plt.show()

# Chi Squared Test
stat, p, dof, expected = chi2_contingency(menthealth_coworker_2014)
print("\nMental health consequence vs coworkers")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# 2014 AND 2019
# Physical health interview vs. mental health interview
# Contingency table + heatmap
phys_ment_int = pd.crosstab(data_combined['phys_health_interview'],
                                       data_combined['mental_health_interview'],
                                       margins = False)
sns.heatmap(phys_ment_int, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Discuss Physical Health in Interview")
plt.xlabel("Discuss Mental Health in Interview")
plt.title("Discussing Physical Health vs. Mental Health in Interview")
plt.show()

# Chi Squared Test
stat, p, dof, expected = chi2_contingency(phys_ment_int)
print("\nDiscussing Physical Health vs. Mental Health in Interview")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")
