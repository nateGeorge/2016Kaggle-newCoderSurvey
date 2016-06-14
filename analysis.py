import pandas as pd
import seaborn as sns

surveyData = pd.read_csv('2016-FCC-New-Coders-Survey-Data.csv',
                          usecols=['EmploymentStatus', 'ExpectedEarning', 'Income', 'IsUnderEmployed', 
                                    'MoneyForLearning', 'MonthsProgramming', 'SchoolMajor', 'BootcampName',
                                  'BootcampFullJobAfter', 'BootcampRecommend']
                        )

GV = surveyData[surveyData['BootcampName']=='Galvanize']

sns.barplot(x=["No", "Yes"], y=GV.BootcampRecommend.value_counts())

plt.ylabel("Recommended Galvanize")

sns.distplot(GV[GV.Income.notnull()], bins = 12)

plt.show()

'''sns.barplot(x=surveyData.BootcampName, y=surveyData.BootcampRecommend, hue=surveyData.BootcampRecommend.value_counts())

plt.ylabel("Recommended Galvanize")

BCs = surveyData.groupby('BootcampName')

BCs.BootcampRecommend.value_counts()'''

BCDF = surveyData.groupby('BootcampName').filter(lambda x: len(x)>10)

BCDF = BCDF[BCDF.BootcampName!='Free Code Camp is not a bootcamp - please scroll up and change answer to "no"']

sns.barplot(x=BCDF.BootcampName.unique(), y = BCDF.BootcampName.value_counts())

sns.factorplot(x='BootcampName', y='BootcampRecommend', hue='BootcampFullJobAfter', data = BCDF, kind='bar', size=6)

locs, labels = plt.xticks()
plt.setp(labels, rotation = 90, ha = 'center')
plt.subplots_adjust(bottom = 0.2, right = 0.9)
plt.show()

sns.barplot(x=surveyData.BootcampName[surveyData.BootcampName.notnull()].unique(), y=surveyData.BootcampName.value_counts())

sns.barplot(x=surveyData.BootcampName[surveyData.BootcampName.notnull()].unique(), y=surveyData.BootcampName.value_counts())

