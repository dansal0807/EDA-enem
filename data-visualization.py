import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_topics = pd.read_csv("datasets/tópicos ordenados.csv", index_col=False)
topicos= df_topics.loc[:, ['Tópicos História', 'Tópicos Filosofia']]
print(topicos)


df_hist = pd.read_csv("datasets/tópicos de história.csv")
df_hist_int = df_hist.loc[:, "questões (numeros inteiros)"]
print(df_hist_int)



