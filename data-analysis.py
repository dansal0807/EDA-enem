import pandas as pd
from PyPDF2 import PdfFileReader
import os
import re
import csv

#Dados do SAS (http://sasedu.co/raioxenem2021):

topicos_hist = ["Idade Contemporânea", "Brasil Colônia", "Brasil Império", "História política", 
"Patrimônio histórico-cultural e memória", "Primeira República", "Idade Moderna", "Idade Antiga",
"Identidade cultural", "Idade Média", "Brasil República", "Antropologia", "Direitos humanos", 'Questão indígena']

topicos_filo = ["Ética e justiça", "Filosofia antiga", "Filosofia contemporânea", "Natureza do conhecimento", "Filosofia moderna",
"Relações de poder", "Filosofia medieval", "Surgimento da Filosofia", "Intolerância"]

topicos_socio = ["Mundo do trabalho", "Cultura e indústria cultural", "Ideologia", 
"comunicação, tecnologia e cultura de massa", "Cidadania", "Movimentos sociais",
"Identidade de gênero", "Desigualdades sociais", 
"Organização científica do trabalho", "Conflito de terra e violência"]

quests_inteiras = ['64', '46', '41', '38', '28', '25', '23', '22', '19', '17', '13', '10', '9', '6', '29', '26', '19', '18', '18', '16', '12', '7', '5', '5', '34', '20', '18', 
'18', '16', '14', '12', '11', '8', '4']

quests_per = ['17.7', '12.7', '11.4', '10.5', '7.8', '6.9', '6.4', '6.1', '5.3', '4.7', '3.6', '2.8', '2.5', '1.7', '18.7', '16.8', '12.3', '11.6', '11.6', '10.3', '7.7', 
'4.5', '3.2', '3.2', '21.9', '12.9', '11.6', '11.6', '10.3', '9.0', '7.7', '7.1', '5.2', '2.6']

#equivalência dos dados para criação do data frame:
quests_inteiras = list(map(int, (quests_inteiras)))

#Dados de quantidade de questões inteiras por disciplina:
quests_inteiras_hist = []
for i in range(0, len(topicos_hist)):
    quests_inteiras_hist.append(quests_inteiras[i])

quests_inteiras_filo = []
for i in range(len(topicos_hist), len(topicos_hist) + len(topicos_filo)):
    quests_inteiras_filo.append(quests_inteiras[i])

quests_inteiras_socio = []
for i in range(len(topicos_hist) + len(topicos_filo) + 1, len(quests_inteiras)):
    quests_inteiras_socio.append(quests_inteiras[i])

#Dados de quantidade de questões por disciplina em porcentagem:
quests_per = list(map(float, (quests_per)))

quests_per_hist = []
for i in range(0, len(topicos_hist)):
    quests_per_hist.append(quests_per[i])

quests_per_filo = []
for i in range(len(topicos_hist), len(topicos_hist) + len(topicos_filo)):
    quests_per_filo.append(quests_per[i])

quests_per_socio = []
for i in range(len(topicos_hist) + len(topicos_filo) + 1, len(quests_inteiras)):
    quests_per_socio.append(quests_per[i])

#criando o data frame:
if not os.path.exists('datasets'):
    os.mkdir('datasets')

os.chdir('datasets')

#primeiro data set feito só de tópicos
dataset_topics = {'Tópicos História': topicos_hist, 'Tópicos Filosofia': topicos_filo, 'Tópicos Sociologia': topicos_socio}

for i in range(len(topicos_hist)):
    if len(topicos_filo) != len(topicos_hist):
        topicos_filo += 'x'
    
    if len(topicos_socio) != len(topicos_hist):
        topicos_socio += 'x'

df_topics = pd.DataFrame(dataset_topics)


with open('topicos ordenados.txt', 'w') as topicstxt:
    topicstxt.write(str(df_topics))

#Data set e porcentagens dos tópicos de história:

for quests in quests_per_hist:
    quests = str(quests) + '%'
    quests_per_hist.append(quests)

dataset_topics_hist = {'questões (numeros inteiros)': quests_inteiras_hist, 'questões (porcentagem)': quests_per_hist}

df_hist = pd.DataFrame(dataset_topics_hist, index = topicos_hist)

with open('estatisticas de história.txt', 'w') as topicstxt:
    topicstxt.write(str(df_hist))