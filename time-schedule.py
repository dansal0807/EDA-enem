import datetime
import calendar
import holidays
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#aqui a necessidade é descobrir quantas horas de aula terei em 2022 e distribuir eles proporcionalmente entre esses horários.
#1- descobrir quantidade de horas de aulas em 2022, lembrando que as aulas de filosofia e sociologia são juntas às segundas-feiras e as aulas de história são às terças-feiras.


def weekday_count(start, end):
  #formatando as datas:
  start_date  = datetime.datetime.strptime(start, '%d/%m/%Y')
  end_date = datetime.datetime.strptime(end, '%d/%m/%Y')
  week = {}
  #contabilizando a quantidade de dias da função:
  for i in range((end_date - start_date).days):
    day = calendar.day_name[(start_date + datetime.timedelta(days=i+1)).weekday()]
    week[day] = week[day] + 1 if day in week else 1
  return week

print(weekday_count("01/02/2022", "31/12/2022"))
#teremos 47 segundas e terças-feiras.

#quantas delas serão feriados?
count_seg = 0
count_ter = 0
print("\nferiados de segunda:")
for data in holidays.Brazil(years=2022).items():
    novadata = data[0]
    feriados = novadata.weekday()
    if feriados == 1:
        count_seg += 1
        print(novadata)

print("\nferiados de terça:")
for data in holidays.Brazil(years=2022).items():
    novadata = data[0]
    feriados = novadata.weekday()
    if feriados == 2:
        count_ter += 1
        print(novadata)

print('\n')
print(count_ter, count_seg)

#feriados de segunda:(2022, 11, 15), 'Proclamação da República'; (datetime.date(2022, 3, 1), 'Carnaval'): 2 feriados
#feriados de terça: feriados de terça: (2022, 9, 7), 'Independência do Brasil'; (2022, 10, 12), 'Nossa Senhora Aparecida'; (2022, 11, 2), 'Finados'; (2022, 3, 2), 'Quarta-feira de cinzas (Início da Quaresma)'
#feriados de terça: 4

#assim, totalizamos:
#segundas-feiras: 47 - 2 = 45 segundas feiras válidas.
#terças-feiras: 47 - 4 = 43 terças-feiras válidas.

#2- após a descoberta de horas, aplicar essas horas à proporção das questões dos últimos arquivos.

#Nesta parte, escolhi por aplicar a proporção em % para os dias.

##SEÇÃO DE HISTÓRIA:
df_hist = pd.read_csv("datasets/tópicos de história.csv")
topicos_hist = df_hist['Unnamed: 0'].values.tolist()
questoes2_hist = df_hist['questões em %'].values.tolist()

#aplicando a proporção dos dias e as matérias devidas:
diasaplicados = []
for porcentagem in questoes2_hist:
    daysoftopics = (43*round(porcentagem, 0))/100
    daysoftopics = round(daysoftopics, 0)
    diasaplicados.append(daysoftopics)

#dicionário com as proporções devidas: tópicos por porcentagem aplicada a quantidade total de dias (terça-feira)
proportion_hist = {topicos_hist[i]: diasaplicados[i] for i in range(len(topicos_hist))}

#transformando em uma visualização:
keys = list(proportion_hist.keys())
vals = list(proportion_hist.values())
sns.set_style('darkgrid')
sns.barplot(x=vals, y=keys)
plt.show()

##SEÇÃO DE FILOSOFIA / SOCIOLOGIA:
df_filo = pd.read_csv("datasets/tópicos de filosofia.csv")
questoes2_filo = df_filo['questões em %'].values.tolist()
topicos_filo = df_filo['Unnamed: 0'].values.tolist()

df_socio = pd.read_csv("datasets/tópicos de sociologia.csv")
questoes2_socio = df_socio['questões em %'].values.tolist()
topicos_socio = df_socio['Unnamed: 0'].values.tolist()



#aplicando a proporção dos dias e as matérias devidas:
##Aqui existe uma pequena diferença em relação a aplicação de historia; como segunda-feira é um dia tanto para filosofia como sociologia, resolvo dividir pela metade os dias para cada disciplina.
##Dessa forma, divido 22 dias para cada um, deixando 1 dia para revisão de ambas as matérias.
diasaplicados_filo = []
for porcentagem in questoes2_filo:
    daysoftopics = (22*round(porcentagem, 0))/100
    daysoftopics = round(daysoftopics, 0)
    diasaplicados.append(daysoftopics)

#dicionário com as proporções devidas: tópicos por porcentagem aplicada aos 22 dias.
proportion_filo = {topicos_filo[i]: diasaplicados[i] for i in range(len(topicos_filo))}

#Aplicando para sociologia:
diasaplicados_socio = []
for porcentagem in questoes2_socio:
    daysoftopics = (22*round(porcentagem, 0))/100
    daysoftopics = round(daysoftopics, 0)
    diasaplicados.append(daysoftopics)

#dicionário com as proporções devidas: tópicos por porcentagem aplicada aos 22 dias.
proportion_socio = {topicos_socio[i]: diasaplicados[i] for i in range(len(topicos_socio))}

#transformando em uma visualização (filo):
keys = list(proportion_filo.keys())
vals = list(proportion_filo.values())
sns.set_style('darkgrid')
sns.barplot(x=vals, y=keys)
plt.show()

#transformando em uma visualização (socio):
keys = list(proportion_socio.keys())
vals = list(proportion_socio.values())
sns.set_style('darkgrid')
sns.barplot(x=vals, y=keys)
plt.show()

