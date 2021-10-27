import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_topics = pd.read_csv("datasets/tópicos ordenados.csv")
print(df_topics)

df_hist = pd.read_csv("datasets/tópicos de história.csv")
df_hist = df_hist(index=False)

sns.set_theme(style="whitegrid")
ax  = sns.barplot(data=df_hist)
plt.show()

