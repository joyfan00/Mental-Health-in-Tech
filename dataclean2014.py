import pandas as pd

df = pd.read_csv('2014survey.csv')

# FILTER ENTRIES, REMOVE / RENAME COLUMNS
# timestamp - remove entries not in 2014
df = df[:-69]
df = df.drop('Timestamp', axis=1)
# age - must be between 0 and 100
df = df[df.Age > 0]
df = df[df.Age < 100]
# country - United States only
df = df[df.Country == 'United States']
df = df.drop('Country', axis=1)
# tech_company - only Yes values
df = df[df.tech_company == 'Yes']
df = df.drop('tech_company', axis=1)
# comments - remove column
df = df.drop('comments', axis=1)
# Rename columns
df.rename(columns={'Age': 'age', 'Gender': 'gender'}, inplace=True)

# REPLACE VALUES
# gender - F / M / NB
df['gender'] = df['gender'].replace(['Female', 'female', 'Femake', 'f', 'Female (cis)', 'Woman', 'Female ', 'Cis Female'], 'F')
df['gender'] = df['gender'].replace(['Male', 'male', 'maile', 'Mail', 'cis male', 'Cis Male', 'm', 'man', 'Male ', 'Male (CIS)', 'Make', 'Man', 'msle'], 'M')
df['gender'] = df['gender'].replace(['Male-ish', 'Trans-female', 'queer/she/they', 'non-binary', 'Nah', 'Genderqueer', 'Female (trans)'], 'NB')


# state - valid state abbreviation
df = df.dropna(subset=['state'])

# self_employed - Yes / No
# Fill nan values: self_employed
df = df.fillna(value={'self_employed': 'No', 'work_interfere': 'Never'})

# benefits - Yes / No / Not sure
df['benefits'] = df['benefits'].replace(["Don't know"], 'Not sure')

# wellness_program - Yes / No / Not sure
df['wellness_program'] = df['wellness_program'].replace(["Don't know"], 'Not sure')

# seek_help - Yes / No / Not sure
df['seek_help'] = df['seek_help'].replace(["Don't know"], 'Not sure')

# anonymity - Yes / No / Not sure
df['anonymity'] = df['anonymity'].replace(["Don't know"], 'Not sure')

# leave - Not sure / Very difficult / Somewhat difficult / Somewhat easy / Very easy
df['leave'] = df['leave'].replace(["Don't know"], 'Not sure')

# coworkers - Yes / No / Some
df['coworkers'] = df['coworkers'].replace(['Some of them'], 'Some')

# supervisor - Yes / No / Some
df['supervisor'] = df['supervisor'].replace(['Some of them'], 'Some')

# mental_vs_physical - Yes / No / Not sure
df['mental_vs_physical'] = df['mental_vs_physical'].replace(["Don't know"], 'Not sure')

# Send cleaned data to CSV
#df.to_csv('2014surveyclean.csv')

# contingency tables changing some to yes for supervisor and coworkers (some still means yes in this case)
df["supervisor"] = df["supervisor"].replace({"Some" : "Yes"})
df["coworkers"] = df["coworkers"].replace({"Some" : "Yes"})
df["benefits"] = df["benefits"].replace({"Not sure" : "No"})
df.to_csv('contingency_tables_2014.csv')