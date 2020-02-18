import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_train = pd.DataFrame([
        ['A01', 2, 1, 60, 139, 'country', 0, 3],
        ['A02', 3, 2, 80, 148, 'country', 0, 5],
        ['A03', 3, 4, 50, 149, 'country', 0, 7],
        ['A04', 5, 5, 40, 151, 'country', 0, 10],
        ['A05', 7, 5, 35, 154, 'city', 0, 12],
        ['A06', 2, 5, 45, 149, 'country', 0, 7],
        ['A07',8, 9, 40, 155, 'city', 1, 13],
        ['A08', 9, 10, 70, 155, 'city', 3, 13],
        ['A09', 6, 12, 55, 154, 'city', 0, 12]
    ], columns=['ID', 'hour', 'attendance', 'weight', 'iq', 'region', 'library', 'score'])


#print(df_train.info())print(df_train.head())
#print(df_train.tail(10)) #전체 데이터
#print(df_train.shape) #튜플형태로 나타냄
#print(df_train.info())
#print(df_train.describe())
#sns.boxplot(x='hour', data = df_train)
#plt.show()
#print(df_train['attendance'].describe())
print(df_train['iq'].sum()/9)
print(df_train['iq'].sum()/df_train['iq'].count())
print(df_train.corr())
print(df_train.isnull())
df_train['score'] = 8
print(df_train.head(10)) #데이터 추가하는 방식