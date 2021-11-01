import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df_topics = pd.read_csv("datasets/tópicos ordenados.csv", index_col=False)
topicos= df_topics.loc[:, ['Tópicos História', 'Tópicos Filosofia']]

#seção de história:
df_hist = pd.read_csv("datasets/tópicos de história.csv")
questoes_hist = df_hist['questões (numeros inteiros)'].values.tolist()
topicos_hist = df_hist['Unnamed: 0'].values.tolist()
questoes2_hist = df_hist['questões em %'].values.tolist()

sns.set_style('darkgrid')
sns.barplot(questoes_hist, topicos_hist)
plt.show()

sns.set_style('darkgrid')
sns.barplot(questoes2_hist, topicos_hist)
plt.show()

#seção de filosofia:
df_filo = pd.read_csv("datasets/tópicos de filosofia.csv")
questoes_filo = df_filo['questões (numeros inteiros)'].values.tolist()
topicos_filo = df_filo['Unnamed: 0'].values.tolist()
questoes2_filo = df_filo['questões em %'].values.tolist()

sns.set_style('darkgrid')
sns.barplot(questoes_filo, topicos_filo)
plt.show()

sns.set_style('darkgrid')
sns.barplot(questoes2_filo, topicos_filo)
plt.show()

#seção de sociologia:
df_socio = pd.read_csv("datasets/tópicos de sociologia.csv")
questoes_socio = df_socio['questões (numeros inteiros)'].values.tolist()
topicos_socio = df_socio['Unnamed: 0'].values.tolist()
questoes2_socio = df_socio['questões em %'].values.tolist()

sns.set_style('darkgrid')
sns.barplot(questoes_socio, topicos_socio)
plt.show()

sns.set_style('darkgrid')
sns.barplot(questoes2_socio, topicos_socio)
plt.show()


