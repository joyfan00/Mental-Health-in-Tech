# import packages used for statistics
import pandas as pd
import numpy as np

# read csv file
data_2019 = pd.read_csv('2019survey.csv')

# columns that are not necessary for comparison purposes
data_2019 = data_2019.drop(['Is your primary role within your company related to tech/IT?',
                            'Would you feel more comfortable talking to your coworkers about your physical health or your mental health?',
                            'Have you ever discussed your mental health with your employer?',
                            'Describe the conversation you had with your employer about your mental health, including their reactions and what actions were taken to address your mental health issue/questions.',
                            'Have you ever discussed your mental health with coworkers?',
                            'Describe the conversation your coworker had with you about their mental health (please do not use names).',
                            'Do you have medical coverage (private insurance or state-provided) that includes treatment of mental health disorders?',
                            'Do you know local or online resources to seek help for a mental health issue?',
                            'If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to clients or business contacts?',
                            'If you have revealed a mental health disorder to a client or business contact, how has this affected you or the relationship?',
                            'If you have been diagnosed or treated for a mental health disorder, do you ever reveal this to coworkers or employees?',
                            'If you have revealed a mental health disorder to a coworker or employee, how has this impacted you or the relationship?',
                            'If yes, what percentage of your work time (time performing primary or secondary job functions) is affected by a mental health issue?',
                            '*Do you have previous employers?*',
                            'Was your employer primarily a tech company/organization?',
                            'Have your previous employers provided mental health benefits?',
                            'Were you aware of the options for mental health care provided by your previous employers?',
                            'Did your previous employers ever formally discuss mental health (as part of a wellness campaign or other official communication)?',
                            'Did your previous employers provide resources to learn more about mental health disorders and how to seek help?',
                            'Was your anonymity protected if you chose to take advantage of mental health or substance abuse treatment resources with previous employers?',
                            'Would you have felt more comfortable talking to your previous employer about your physical health or your mental health?',
                            'Would you have been willing to discuss your mental health with your direct supervisor(s)?',
                            'Did you ever discuss your mental health with your previous employer?',
                            'Describe the conversation you had with your previous employer about your mental health, including their reactions and actions taken to address your mental health issue/questions.',
                            'Would you have been willing to discuss your mental health with your coworkers at previous employers?',
                            'Did you ever discuss your mental health with a previous coworker(s)?',
                            'Describe the conversation you had with your previous coworkers about your mental health including their reactions.',
                            'Did you ever have a previous coworker discuss their or another coworker\'s mental health with you?',
                            'Describe the conversation your coworker had with you about their mental health (please do not use names).',
                            'Overall, how much importance did your previous employer place on physical health?',
                            'Overall, how much importance did your previous employer place on mental health?',
                            'Do you *currently* have a mental health disorder?',
                            'Have you ever been *diagnosed* with a mental health disorder?',
                            '*What disorder(s) have you been diagnosed with?*',
                            '*If possibly, what disorder(s) do you believe you have?*',
                            '*If so, what disorder(s) were you diagnosed with?*',
                            'Have you had a mental health disorder in the past?',
                            'Why or why not?',
                            'Why or why not?.1',
                            'Are you openly identified at work as a person with a mental health issue?',
                            'Has being identified as a person with a mental health issue affected your career?',
                            'How has it affected your career?',
                            'If they knew you suffered from a mental health disorder, how do you think that your team members/co-workers would react?',
                            'Have you observed or experienced an *unsupportive or badly handled response* to a mental health issue in your current or previous workplace?',
                            'Describe the circumstances of the badly handled or unsupportive response.',
                            'Have you observed or experienced a *supportive or well handled response* to a mental health issue in your current or previous workplace?',
                            'Describe the circumstances of the supportive or well handled response.',
                            'Overall, how well do you think the tech industry supports employees with mental health issues?',
                            'Briefly describe what you think the industry as a whole and/or employers could do to improve mental health support for employees.',
                            'If there is anything else you would like to tell us that has not been covered by the survey questions, please use this space to do so.',
                            'Would you be willing to talk to one of us more extensively about your experiences with mental health issues in the tech industry? (Note that all interview responses would be used _anonymously_ and only with your permission.)',
                            'What country do you *live* in?',
                            'What US state or territory do you *live* in?',
                            'What is your race?',
                            'Describe the conversation with coworkers you had about your mental health including their reactions.',
                            'Have you ever had a coworker discuss their or another coworker\'s mental health with you?',
                            'Describe the conversation your coworker had with you about their mental health (please do not use names)..1',
                            'How willing would you be to share with friends and family that you have a mental illness?',
                            'If you have a mental health disorder, how often do you feel that it interferes with your work *when being treated effectively?*',
                            'If you have a mental health disorder, how often do you feel that it interferes with your work *when* _*NOT*_* being treated effectively (i.e., when you are experiencing symptoms)?*'], axis=1)

# rename the columns to align more with the other dataset
data_2019.rename(columns = {'*Are you self-employed?*' : 'self_employed',
                            'How many employees does your company or organization have?' : 'no_employees',
                            'Is your employer primarily a tech company/organization?' : 'tech_company',
                            'Does your employer provide mental health benefits as part of healthcare coverage?' : 'benefits',
                            'Does your employer offer resources to learn more about mental health disorders and options for seeking help?' : 'seek_help',
                            'Is your anonymity protected if you choose to take advantage of mental health or substance abuse treatment resources provided by your employer?' : 'anonymity',
                            'Has your employer ever formally discussed mental health (for example, as part of a wellness campaign or other official communication)?' : 'wellness_program',
                            'If a mental health issue prompted you to request a medical leave from work, how easy or difficult would it be to ask for that leave?' : 'leave',
                            'Would you feel comfortable discussing a mental health issue with your direct supervisor(s)?' : 'supervisor',
                            'Would you feel comfortable discussing a mental health issue with your coworkers?' : 'coworkers',
                            'Overall, how much importance does your employer place on physical health?' : 'phys_health',
                            'Overall, how much importance does your employer place on mental health?' : 'mental_health',
                            'Do you believe your productivity is ever affected by a mental health issue?' : 'work_interfere',
                            'Have you ever sought treatment for a mental health disorder from a mental health professional?' : 'treatment',
                            'Do you have a family history of mental illness?' : 'family_history',
                            'Have your observations of how another individual who discussed a mental health issue made you less likely to reveal a mental health issue yourself in your current workplace?' : 'obs_consequence',
                            'Would you be willing to bring up a physical health issue with a potential employer in an interview?' : 'phys_health_interview',
                            'Would you bring up your *mental* health with a potential employer in an interview?' : 'mental_health_interview',
                            'What is your age?' : 'age',
                            'What is your gender?' : 'gender',
                            'What country do you *work* in?' : 'country',
                            'What US state or territory do you *work* in?' : 'state',
                            'Do you know the options for mental health care available under your employer-provided health coverage?' : 'care_options'}, inplace = True)
print(data_2019.columns)

# convert data_2019 to be a dataframe instead of a series
print(type(data_2019))

# tech company: standardizing of data, filtering for only tech company
data_2019["tech_company"] = data_2019["tech_company"].map({True : "Yes", False : "No", np.nan : "No"})

# filter the data: only United States of America, only tech company
data_2019 = data_2019[data_2019["country"] == "United States of America"]
data_2019 = data_2019[data_2019["tech_company"] == "Yes"]
data_2019 = data_2019.loc[(data_2019["age"] >= 1) & (data_2019["age"] <= 100)]

# self employment: standardizing of data
data_2019["self_employed"] = data_2019["self_employed"].map({True : 'Yes', False : 'No', np.nan: 'No'})  # Replace true/false with yes or no

# care options: standardizing of data values
data_2019["care_options"] = data_2019["care_options"].map({"Yes" : "Yes", "No" : "No", np.nan: "Not sure"})

# employee benefits: standardizing of data values
data_2019["benefits"] = data_2019["benefits"].map({"Yes" : "Yes", "No" : "No", "I don't know" : "Not sure", "Not eligible for coverage / NA" : "Not Applicable"})

# wellness program: standardizing of data values
data_2019["wellness_program"] = data_2019["wellness_program"].map({"Yes" : "Yes", "No" : "No", "I don't know" : "Not sure"})

# seek help: standardizing of data values
data_2019["seek_help"] = data_2019["seek_help"].replace({"Yes" : "Yes", "No" : "No", "I don't know" : "Not sure"})

# anonymity: standardizing of data values
data_2019["anonymity"] = data_2019["anonymity"].replace({"Yes" : "Yes", "No": "No", "I don't know" : "Not sure"})

# leave: standardizing of data values
data_2019["leave"] = data_2019["leave"].map({'Very easy' : 'Very easy',
                                             "I don't know" : "Not sure",
                                             'Somewhat difficult' : "Somewhat difficult",
                                             'Somewhat easy' : "Somewhat easy",
                                             'Neither easy nor difficult' : "Neither easy nor difficult",
                                             'Difficult' : "Difficult"})

# supervisor
data_2019["supervisor"] = data_2019["supervisor"].replace({"Maybe" : "Some"})

# coworkers
data_2019["coworkers"] = data_2019["coworkers"].replace({"Maybe" : "Some"})

# phys_health
# print(data_2019.phys_health.unique())

# mental_health

# work_interfere
print(data_2019.work_interfere.unique())
# data_2019["work_interfere"] = data_2019["work_interfere"].replace({"Yes": "Often", "Unsure" : "Sometimes"})

# treatment
data_2019["treatment"] = data_2019["treatment"].map({True : 'Yes', False : 'No', np.nan: 'No'})

# family_history
data_2019["family_history"] = data_2019["family_history"].replace({"I don't know" : "Not sure"})

# gender: split into three- male, female, gender minority
data_2019["gender"] = data_2019["gender"].replace(['Male', 'male', 'm', 'Let\'s keep it simple and say "male"',
                                                   'CIS Male', 'Cishet male', 'Cis Male', "M", "Man"], "M")
data_2019["gender"] = data_2019["gender"].replace(['female', 'Female', 'F', 'f', 'Female ', 'Female (cis)', 'Woman', 'cis woman'], "F")
data_2019["gender"] = data_2019["gender"].replace(["Agender trans woman", "Trans man", "None", "Trans non-binary/genderfluid", "Non-binary and gender fluid"], "NB")

# state
data_2019["state"] = data_2019["state"].replace({"Alabama" : "AL",
                                             "Alaska" : "AK",
                                             "Arizona" : "AZ",
                                             "Arkansas" : "AR",
                                             "California" : "CA",
                                             "Colorado" : "CO",
                                             "Connecticut" : "CT",
                                             "Delaware" : "DE",
                                             "Florida" : "FL",
                                             "Georgia" : "GA",
                                             "Hawaii" : "HI",
                                             "Idaho" : "ID",
                                             "Illinois" : "IL",
                                             "Indiana" : "IN",
                                             "Iowa" : "IA",
                                             "Kansas" : "KS",
                                             "Kentucky" : "KY",
                                             "Louisiana" : "LA",
                                             "Maine" : "ME",
                                             "Maryland" : "MD",
                                             "Massachusetts" : "MA",
                                             "Michigan" : "MI",
                                             "Minnesota" : "MN",
                                             "Mississippi" : "MS",
                                             "Missouri" : "MO",
                                             "Montana" : "MT",
                                             "Nebraska" : "NE",
                                             "Nevada" : "NV",
                                             "New Hampshire" : "NH",
                                             "New Jersey" : "NJ",
                                             "New Mexico" : "NM",
                                             "New York" : "NY",
                                             "North Carolina" : "NC",
                                             "North Dakota" : "ND",
                                             "Ohio" : "OH",
                                             "Oklahoma" : "OK",
                                             "Oregon" : "OR",
                                             "Pennsylvania" : "PA",
                                             "Rhode Island" : "RI",
                                             "South Carolina" : "SC",
                                             "South Dakota" : "SD",
                                             "Tennessee" : "TN",
                                             "Texas" : "TX",
                                             "Utah" : "UT",
                                             "Vermont" : "VT",
                                             "Virginia" : "VA",
                                             "Washington" : "WA",
                                             "West Virginia" : "WV",
                                             "Wisconsin" : "WI",
                                             "Wyoming" : "WY",})
data_2019.to_csv("cleaning_data2019.csv")

# contingency tables changing some to yes for supervisor and coworkers (some still means yes in this case)
data_2019["supervisor"] = data_2019["supervisor"].replace({"Some" : "Yes"})
data_2019["coworkers"] = data_2019["coworkers"].replace({"Some" : "Yes"})
data_2019["benefits"] = data_2019["benefits"].replace({"Not sure" : "No", "Not Applicable" : "No"})

# new csv file
data_2019.to_csv("contingency_tables_2019.csv")
