# packages
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# 2014 data
data_2014 = pd.read_csv("2014surveyclean.csv")

# 2019 data
data_2019 = pd.read_csv("cleaning_data2019.csv")

# Bar charts
# Benefits 2014 vs 2019
benefits_yes2014 = data_2014['benefits'].value_counts()['Yes']/580
benefits_no2014 = data_2014['benefits'].value_counts()['No']/580
benefits_notsure2014 = data_2014['benefits'].value_counts()['Not sure']/580
benefits_yes2019 = data_2019['benefits'].value_counts()['Yes']/127
benefits_no2019 = data_2019['benefits'].value_counts()['No']/127
benefits_notsure2019 = data_2019['benefits'].value_counts()['Not sure']/127
benefits_na2019 = data_2019['benefits'].value_counts()['Not Applicable']/127
width = 0.3
plt.bar(['Yes', 'No', 'Not Sure', 'N/A'], [benefits_yes2014*100, benefits_no2014*100, benefits_notsure2014*100, 0], align='edge', width=-width)
plt.bar(['Yes', 'No', 'Not Sure', 'N/A'], [benefits_yes2019*100, benefits_no2019*100, benefits_notsure2019*100, benefits_na2019*100], align='edge', width=width)
plt.title("Mental Health Benefits Provided by Employer 2014 vs. 2019")
plt.ylabel("Percentage")
plt.xlabel("Benefits Provided by Employer")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
colors = {'2014': '#1f77b4', '2019': '#ff7f0e'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()

# Care options 2014 vs 2019
co_yes2014 = data_2014['care_options'].value_counts()['Yes']/580
co_no2014 = data_2014['care_options'].value_counts()['No']/580 + data_2014['care_options'].value_counts()['Not sure']/580
co_yes2019 = data_2019['care_options'].value_counts()['Yes']/127
co_no2019 = data_2019['care_options'].value_counts()['No']/127 + data_2019['care_options'].value_counts()['Not sure']/127
width = 0.3
plt.bar(['Yes', 'No'], [co_yes2014*100, co_no2014*100], align='edge', width=-width)
plt.bar(['Yes', 'No'], [co_yes2019*100, co_no2019*100], align='edge', width=width)
plt.title("Knowledge of Options for Mental Health Care 2014 vs. 2019")
plt.ylabel("Percentage")
plt.xlabel("Knowledge of Options for Mental Health Care")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
colors = {'2014': '#1f77b4', '2019': '#ff7f0e'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()

# Wellness program 2014 vs 2019
wp_yes2014 = data_2014['wellness_program'].value_counts()['Yes']/580
wp_no2014 = data_2014['wellness_program'].value_counts()['No']/580
wp_notsure2014 = data_2014['wellness_program'].value_counts()['Not sure']/580
wp_yes2019 = data_2019['wellness_program'].value_counts()['Yes']/127
wp_no2019 = data_2019['wellness_program'].value_counts()['No']/127
wp_notsure2019 = data_2019['wellness_program'].value_counts()['Not sure']/127
width = 0.3
plt.bar(['Yes', 'No', 'Not Sure'], [wp_yes2014*100, wp_no2014*100, wp_notsure2014*100], align='edge', width=-width)
plt.bar(['Yes', 'No', 'Not Sure'], [wp_yes2019*100, wp_no2019*100, wp_notsure2019*100], align='edge', width=width)
plt.title("Mental Health Discussions via Wellness Program 2014 vs. 2019")
plt.ylabel("Percentage")
plt.xlabel("Employer Discussion of Mental Health")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
colors = {'2014': '#1f77b4', '2019': '#ff7f0e'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()

# Supervisor 2014 vs 2019
sup_yes2014 = data_2014['supervisor'].value_counts()['Yes']/580 + data_2014['supervisor'].value_counts()['Some']/580
sup_no2014 = data_2014['supervisor'].value_counts()['No']/580
sup_yes2019 = data_2019['supervisor'].value_counts()['Yes']/127 + data_2019['supervisor'].value_counts()['Some']/127
sup_no2019 = data_2019['supervisor'].value_counts()['No']/127
width = 0.3
plt.bar(['Yes', 'No'], [sup_yes2014*100, sup_no2014*100], align='edge', width=-width)
plt.bar(['Yes', 'No'], [sup_yes2019*100, sup_no2019*100], align='edge', width=width)
plt.title("Willingness to Discuss Mental Health w/ Supervisor 2014 vs. 2019")
plt.ylabel("Percentage")
plt.xlabel("Comfortable Discussing Mental Health Issue with Supervisor")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
colors = {'2014': '#1f77b4', '2019': '#ff7f0e'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()

# Coworkers 2014 vs 2019
cow_yes2014 = data_2014['coworkers'].value_counts()['Yes']/580 + data_2014['coworkers'].value_counts()['Some']/580
cow_no2014 = data_2014['coworkers'].value_counts()['No']/580
cow_yes2019 = data_2019['coworkers'].value_counts()['Yes']/127 + data_2019['coworkers'].value_counts()['Some']/127
cow_no2019 = data_2019['coworkers'].value_counts()['No']/127
width = 0.3
plt.bar(['Yes', 'No'], [cow_yes2014*100, cow_no2014*100], align='edge', width=-width)
plt.bar(['Yes', 'No'], [cow_yes2019*100, cow_no2019*100], align='edge', width=width)
plt.title("Willingness to Discuss Mental Health w/ Coworkers 2014 vs. 2019")
plt.ylabel("Percentage")
plt.xlabel("Comfortable Discussing Mental Health Issue with Coworkers")
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(decimals=0))
colors = {'2014': '#1f77b4', '2019': '#ff7f0e'}
labels = list(colors.keys())
handles = [plt.Rectangle((0,0),1,1, color=colors[label]) for label in labels]
plt.legend(handles, labels)
plt.show()