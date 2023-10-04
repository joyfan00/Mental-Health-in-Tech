# packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
from scipy.stats import chi2_contingency
from scipy.stats import chi2

# 2014 data
data_2014 = pd.read_csv("2014surveyclean.csv")

# 2019 data
data_2019 = pd.read_csv("cleaning_data2019.csv")

# combined 2014 and 2019 data
data_combined = pd.concat([data_2014, data_2019], axis=0, ignore_index=True)

# Female: 134
# Male: 439

# CHI SQUARED + HEATMAPS
# Physical health consequence vs. gender 2014
# Contingency table + heatmap
physhealth_gender_2014 = pd.crosstab(data_2014['phys_health_consequence'],
                                       data_2014['gender'],
                                       margins = False)
sns.heatmap(physhealth_gender_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Physical Health Issue has Negative Consequences")
plt.xlabel("Gender")
plt.title("Physical Health Consequence vs. Gender 2014")
plt.show()

# Chi Squared Test
stat, p, dof, expected = chi2_contingency(physhealth_gender_2014)
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
print("Physical health consequence vs Gender")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")


# Mental health consequence vs. gender 2014
# Contingency table + heatmap
menthealth_gender_2014 = pd.crosstab(data_2014['mental_health_consequence'],
                                       data_2014['gender'],
                                       margins = False)
sns.heatmap(menthealth_gender_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Mental Health Issue has Negative Consequences")
plt.xlabel("Gender")
plt.title("Mental Health Consequence vs. Gender 2014")
plt.show()

# Chi Squared Test
stat, p, dof, expected = chi2_contingency(physhealth_gender_2014)
# interpret test-statistic
prob = 0.95
critical = chi2.ppf(prob, dof)
print("Mental health consequence vs Gender")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# Gender Physical Health Consequence
width = 0.3
plt.bar(['Yes', 'Maybe', 'No'], [8/134*100, 35/134*100, 91/134*100], align='edge', width=-width, color = '#009292') # Female
plt.bar(['Yes', 'Maybe', 'No'], [13/439*100, 70/439*100, 356/439*100], align='edge', width=width, color = '#6DB6FF') # Male
plt.title("Belief of Physical Health Issue Consequence Belief by Gender")
plt.ylabel("Percentage")
plt.xlabel("Belief there is a Consequence for Physical Health Issue")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
colors = {'Female': '#009292', 'Male': '#6DB6FF'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()

# Gender Mental Health Consequence
width = 0.3
plt.bar(['Yes', 'Maybe', 'No'], [33/134*100, 58/134*100, 43/134*100], align='edge', width=-width, color = '#009292') # Female
plt.bar(['Yes', 'Maybe', 'No'], [86/439*100, 163/439*100, 190/439*100], align='edge', width=width, color = '#6DB6FF') # Male
plt.title("Belief of Mental Health Issue Consequence Belief by Gender")
plt.ylabel("Percentage")
plt.xlabel("Belief there is a Consequence for Mental Health Issue")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
colors = {'Female': '#009292', 'Male': '#6DB6FF'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()