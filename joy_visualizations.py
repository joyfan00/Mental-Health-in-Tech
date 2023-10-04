# packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from scipy.stats import chi2
import matplotlib.ticker as mtick

# 2019 data
data_2019 = pd.read_csv("contingency_tables_2019.csv")

# 2014 data
data_2014 = pd.read_csv("contingency_tables_2014.csv")

# combined 2014 and 2019 data
data_combined = pd.concat([data_2014, data_2019], axis = 0, ignore_index = True)

# contingency table for 2014- benefits vs. supervisor
benefits_supervisor_2014 = pd.crosstab(data_2014['benefits'],
                                       data_2014['supervisor'],
                                       margins = False)

# heat map for 2014- benefits vs. supervisor
sns.heatmap(benefits_supervisor_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Knowledge of Mental Health Benefits")
plt.xlabel("Willing to Disclose to Supervisor")
plt.title("Knowledge of MH Benefits vs. Disclosing to Supervisor")
plt.show()

# chi squared test relating to 2019 benefits vs. supervisor
stat, p, dof, expected = chi2_contingency(benefits_supervisor_2014)
prob = 0.95
critical = chi2.ppf(prob, dof)
print("Mental health benefits vs. supervisors in 2014:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# contingency table for 2019- benefits vs. supervisor
benefits_supervisor_2019 = pd.crosstab(data_2019['benefits'],
                                       data_2019['supervisor'],
                                       margins = False)
# heat map for 2019- benefits vs. supervisor
sns.heatmap(benefits_supervisor_2019, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Knowledge of Mental Health Benefits")
plt.xlabel("Willing to Disclose to Supervisor")
plt.title("Knowledge of MH Benefits vs. Disclosing to Supervisor 2019")
plt.show()

# chi squared test relating to 2019 benefits vs. supervisor
stat, p, dof, expected = chi2_contingency(benefits_supervisor_2019)
critical = chi2.ppf(prob, dof)
print("Mental health benefits vs. disclosing to supervisors in 2019:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# contingency table for 2014- benefits vs. coworkers
benefits_coworkers_2014 = pd.crosstab(data_2014['benefits'],
                                      data_2014['coworkers'],
                                      margins = False)
# heat map for 2014- benefits vs. coworkers
sns.heatmap(benefits_coworkers_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Knowledge of Mental Health Benefits")
plt.xlabel("Willing to Disclose to Coworkers")
plt.title("Knowledge of MH Benefits vs. Disclosing to Coworkers")
plt.show()

# chi squared test relating to 2014 benefits vs. coworkers
stat, p, dof, expected = chi2_contingency(benefits_coworkers_2014)
critical = chi2.ppf(prob, dof)
print("Mental health benefits vs. disclosing to coworkers in 2014:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# contingency table for 2019- benefits vs. coworkers
benefits_coworkers_2019 = pd.crosstab(data_2019['benefits'],
                                      data_2019['coworkers'],
                                      margins = False)

# heat map for 2019- benefits vs. coworkers
sns.heatmap(benefits_coworkers_2019, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Knowledge of Mental Health Benefits")
plt.xlabel("Willing to Disclosing to Coworkers")
plt.title("Knowledge of MH Benefits vs. Disclosing to Coworkers 2019")
plt.show()

# chi squared test relating to 2019 benefits vs. coworkers
stat, p, dof, expected = chi2_contingency(benefits_coworkers_2019)
critical = chi2.ppf(prob, dof)
print("Mental health benefits vs. disclosing to coworkers in 2019:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# contingency table for 2019- anonymity vs. mental health emphasis
anonymity_mh_2019 = pd.crosstab(data_2019['anonymity'],
                                data_2019['mental_health'],
                                margins = False)

# heat map for 2019- anonymity vs. mental health emphasis
sns.heatmap(anonymity_mh_2019, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Anonymity of Employees")
plt.xlabel("Emphasis on Mental Health")
plt.title("Anonymity of Employees vs. Emphasis on Mental Health 2019")
plt.show()

# chi squared test relating to 2019 anonymity vs. mental health emphasis
stat, p, dof, expected = chi2_contingency(anonymity_mh_2019)
critical = chi2.ppf(prob, dof)
print("Anonymity vs. mental health emphasis in 2019:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# contingency table for 2014- gender vs. supervisors
gender_supervisor_2014 = pd.crosstab(data_2014['gender'],
                                     data_2014['supervisor'],
                                     margins = False)

# heat map for 2014- gender vs. supervisors
sns.heatmap(gender_supervisor_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Gender of Employee")
plt.xlabel("Willing to Disclose to Supervisor")
plt.title("Willing to Disclose to Supervisor vs. Gender of Employee 2014")
plt.show()

# chi squared test relating to 2014 gender vs. supervisors
stat, p, dof, expected = chi2_contingency(gender_supervisor_2014)
critical = chi2.ppf(prob, dof)
print("Gender vs. disclosing to supervisors in 2014:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# contingency table for 2019- gender vs. supervisors
gender_supervisor_2019 = pd.crosstab(data_2019['gender'],
                                     data_2019['supervisor'],
                                     margins = False)

# heat map for 2019- gender vs. supervisors
sns.heatmap(gender_supervisor_2019, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Gender of Employee")
plt.xlabel("Willing to Disclose to Supervisor")
plt.title("Willing to Disclose to Supervisor vs. Gender of Employee 2019")
plt.show()

# chi squared test relating to 2019 gender vs. supervisors
stat, p, dof, expected = chi2_contingency(gender_supervisor_2019)
critical = chi2.ppf(prob, dof)
print("Gender vs. disclosing to supervisors in 2019:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# contingency table for 2014- gender vs. coworkers
gender_coworkers_2014 = pd.crosstab(data_2014['gender'],
                                    data_2014['coworkers'],
                                    margins = False)
# heat map for 2014- gender vs. coworkers
sns.heatmap(gender_coworkers_2014, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Gender of Employee")
plt.xlabel("Willing to Disclose to Coworkers")
plt.title("Willing to Disclose to Coworkers vs. Gender of Employee 2014")
plt.show()

# chi squared test relating to 2014 gender vs. coworkers
stat, p, dof, expected = chi2_contingency(gender_coworkers_2014)
critical = chi2.ppf(prob, dof)
print("Gender vs. disclosing to coworkers in 2014:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# contingency table for 2019- gender vs. coworkers
gender_coworkers_2019 = pd.crosstab(data_2019['gender'],
                                    data_2019['coworkers'],
                                    margins = False)

# heat map for 2019- gender vs. coworkers
sns.heatmap(gender_coworkers_2019, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Gender of Employee")
plt.xlabel("Willing to Disclose to Coworkers")
plt.title("Willing to Disclose to Coworkers vs. Gender of Employee 2019")
plt.show()

# chi squared test relating to 2019 gender vs. coworkers
stat, p, dof, expected = chi2_contingency(gender_coworkers_2019)
critical = chi2.ppf(prob, dof)
print("Gender vs. disclosing to coworkers in 2019:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# combined gender vs. phys_health_interview
gender_phys_health_interview = pd.crosstab(data_combined['gender'],
                                           data_combined['phys_health_interview'],
                                           margins = False)

# heat map for gender vs. phys_health_interview
sns.heatmap(gender_phys_health_interview, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Gender of Employee")
plt.xlabel("Physical Health in Interview")
plt.title("Physical Health in Interview vs. Gender of Employee")
plt.show()

# chi squared test relating to gender vs. mental_health_interview
stat, p, dof, expected = chi2_contingency(gender_phys_health_interview)
critical = chi2.ppf(prob, dof)
print("Gender vs. disclosing physical health issues in interview combined data:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

# combined gender vs. mental_health_interview
gender_mental_health_interview = pd.crosstab(data_combined['gender'],
                                             data_combined['mental_health_interview'],
                                             margins = False)

# heat map for gender vs. mental_health_interview
sns.heatmap(gender_mental_health_interview, annot=True, fmt='.2f', vmin=0.0, vmax=100.0)
plt.ylabel("Gender of Employee")
plt.xlabel("Mental Health in Interview")
plt.title("Mental Health in Interview vs. Gender of Employee")
plt.show()

# chi squared test relating to gender vs. phys_health_interview
stat, p, dof, expected = chi2_contingency(gender_mental_health_interview)
critical = chi2.ppf(prob, dof)
print("Gender vs. disclosing mental health issues in interview combined data:")
if abs(stat) >= critical:
    print('Dependent (reject H0)')
else:
    print('Independent (fail to reject H0)')
print(f"Chi-squared value: {stat}")
print(f"P-value: {p}")

print(data_combined)

# bar chart for gender vs. disclosing physical health issues in interview
# filter data based on physical health interview response for bar graphs
phys_data_yes = data_combined.loc[data_combined["phys_health_interview"] == "Yes"]
phys_data_maybe = data_combined.loc[data_combined["phys_health_interview"] == "Maybe"]
phys_data_no = data_combined.loc[data_combined["phys_health_interview"] == "No"]

# frequency values
f_phys_health_interview_yes = phys_data_yes['gender'].value_counts()['F']/175*100
m_phys_health_interview_yes = phys_data_yes['gender'].value_counts()['M']/519*100
f_phys_health_interview_maybe = phys_data_maybe['gender'].value_counts()['F']/175*100
m_phys_health_interview_maybe = phys_data_maybe['gender'].value_counts()['M']/519*100
f_phys_health_interview_no = phys_data_no['gender'].value_counts()['F']/175*100
m_phys_health_interview_no = phys_data_no['gender'].value_counts()['M']/519*100

# female values
female = [f_phys_health_interview_yes, f_phys_health_interview_maybe, f_phys_health_interview_no]

# male values
male = [m_phys_health_interview_yes, m_phys_health_interview_maybe, m_phys_health_interview_no]

# set up bar graph
n = 3
ind = np.arange(n)
width = 0.3

# female bars
bar1 = plt.bar(ind - 0.15, female, width, color = '#009292')

# male bars
bar2 = plt.bar(ind + 0.15, male, width, color= '#6DB6FF')

# plot labels
plt.title("Willingness to Mention Physical Health Issues in Interview by Gender")
plt.ylabel("Percentage")
plt.xlabel("Willingness to Mention Physical Health Issues")
plt.xticks(ind,['Yes', 'Maybe', 'No'])
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
plt.legend((bar1, bar2), ('Female', 'Male') )
plt.show()

# bar chart for gender vs. disclosing mental health issues in interview
mental_data_yes = data_combined.loc[data_combined["mental_health_interview"] == "Yes"]
mental_data_maybe = data_combined.loc[data_combined["mental_health_interview"] == "Maybe"]
mental_data_no = data_combined.loc[data_combined["mental_health_interview"] == "No"]

# frequency values
f_mental_health_interview_yes = mental_data_yes['gender'].value_counts()['F']/175*100
m_mental_health_interview_yes = mental_data_yes['gender'].value_counts()['M']/519*100
f_mental_health_interview_maybe = mental_data_maybe['gender'].value_counts()['F']/175*100
m_mental_health_interview_maybe = mental_data_maybe['gender'].value_counts()['M']/519*100
f_mental_health_interview_no = mental_data_no['gender'].value_counts()['F']/175*100
m_mental_health_interview_no = mental_data_no['gender'].value_counts()['M']/519*100

# female values
female = [f_mental_health_interview_yes, f_mental_health_interview_maybe, f_mental_health_interview_no]

# male values
male = [m_mental_health_interview_yes, m_mental_health_interview_maybe, m_mental_health_interview_no]

# set up bar graph
n = 3
ind = np.arange(n)
width = 0.3

# female bars
bar1 = plt.bar(ind - 0.15, female, width, color = '#009292')

# male bars
bar2 = plt.bar(ind + 0.15, male, width, color= '#6DB6FF')

# plot labels
plt.title("Willingness to Mention Mental Health Issues in Interview by Gender")
plt.ylabel("Percentage")
plt.xlabel("Willingness to Mention Mental Health Issues")
plt.xticks(ind, ['Yes', 'Maybe', 'No'])
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
plt.legend((bar1, bar2), ('Female', 'Male') )
plt.show()

print(data_2014.shape)
print(data_2019.shape)

phys_data_yes_2014 = (len(data_2014.loc[data_2014["phys_health_interview"] == "Yes"]) / 580) * 100
phys_data_maybe_2014 = (len(data_2014.loc[data_2014["phys_health_interview"] == "Maybe"]) / 580) * 100
phys_data_no_2014 = (len(data_2014.loc[data_2014["phys_health_interview"] == "No"]) / 580) * 100
phys_data_yes_2019 = (len(data_2019.loc[data_2019["phys_health_interview"] == "Yes"]) / 126) * 100
phys_data_maybe_2019 = (len(data_2019.loc[data_2019["phys_health_interview"] == "Maybe"]) / 126) * 100
phys_data_no_2019 = (len(data_2019.loc[data_2019["phys_health_interview"] == "No"]) / 126) * 100
mental_data_yes_2014 = (len(data_2014.loc[data_2014["mental_health_interview"] == "Yes"]) / 580) * 100
mental_data_maybe_2014 = (len(data_2014.loc[data_2014["mental_health_interview"] == "Maybe"]) / 580) * 100
mental_data_no_2014 = (len(data_2014.loc[data_2014["mental_health_interview"] == "No"]) / 580) * 100
mental_data_yes_2019 = (len(data_2019.loc[data_2019["mental_health_interview"] == "Yes"]) / 126) * 100
mental_data_maybe_2019 = (len(data_2019.loc[data_2019["mental_health_interview"] == "Maybe"]) / 126) * 100
mental_data_no_2019 = (len(data_2019.loc[data_2019["mental_health_interview"] == "No"]) / 126) * 100

print(phys_data_yes_2014)
print(phys_data_yes_2019)
print(mental_data_yes_2014)
print(mental_data_yes_2019)

phys_2014 = [phys_data_yes_2014, phys_data_maybe_2014, phys_data_no_2014]
phys_2019 = [phys_data_yes_2019, phys_data_maybe_2019, phys_data_no_2019]
mental_2014 = [mental_data_yes_2014, mental_data_maybe_2014, mental_data_no_2014]
mental_2019 = [mental_data_yes_2019, mental_data_maybe_2019, mental_data_no_2019]

# set up bar graph
n = 3
ind = np.arange(n)
width = 0.3

# physical health interview in 2014
bar1 = plt.bar(ind - 0.15, phys_2014, width, color = '#1f77b4')

# physical health interview in 2019
bar2 = plt.bar(ind + 0.15, phys_2019, width, color = '#ff7f0e')

# plot labels
plt.title("Willingness to Mention Physical Health Issues in Interview 2014 vs. 2019")
plt.ylabel("Percentage")
plt.xlabel("Willingness to Mention Physical Health Issues")
plt.xticks(ind, ['Yes', 'Maybe', 'No'])
plt.legend((bar1, bar2), ('2014', '2019') )
plt.show()

# physical health interview in 2014
bar1 = plt.bar(ind - 0.15, mental_2014, width, color = '#1f77b4')

# physical health interview in 2019
bar2 = plt.bar(ind + 0.15, mental_2019, width, color = '#ff7f0e')

# plot labels
plt.title("Willingness to Mention Mental Health Issues in Interview 2014 vs. 2019")
plt.ylabel("Percentage")
plt.xlabel("Willingness to Mention Mental Health Issues")
plt.xticks(ind, ['Yes', 'Maybe', 'No'])
plt.legend((bar1, bar2), ('2014', '2019') )
plt.show()







