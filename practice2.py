import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os, ssl
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv('https://raw.githubusercontent.com/cranberrygame/data_analysis/master/StudentsPerformance.csv')

print(df.head(df['gender'].count()))
print(df.describe())
print(df.info())

sns.pairplot(df)
plt.show()

df['average'] = (df['math score'] + df['reading score'] + df['writing score'])
print(df.head())

sns.catplot(x='lunch', y='math score', data=df, hue='gender', kind='box')
plt.show()