import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(
    [
    [100, 200],
    [120, 205],
    [130, 210],
    [140, 220],
    [150, 230],
    [160, 250],
    [170, 270],
    [180, 280],
    [190, 285],
    ],columns=['height', 'Footmm'])

print(df.head(10))
print(df.describe())
print(df.corr())
corr = df.corr()
sns.heatmap(data=corr)
plt.show()
#상관계수 파악 그래프
sns.barplot(x='height', y='Footmm', data=df)
plt.show()