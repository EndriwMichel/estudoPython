# Capitulo 9 Analise de dados
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import colorsys
plt.style.use('seaborn-talk')
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('Dados-Pesquisa.csv', sep=',', low_memory=False)

print(df)

print(df.describe())

# Bins é a quantidade de "colunas" do histograma
"""
df.Age.hist(bins=60)
plt.xlabel('Idade')
plt.ylabel('Numero de profissionais')
plt.title('Distribuiçõ de idade')
plt.show()
"""
# Com base na pesquisa a maioria dos programadores possuem idade entre 20 e 30 anos
"""
# Definindo as quantidades
labels = df.Gender.value_counts().index
num = len(df.EmploymentField.value_counts().index)

# Criando lista de cores
listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

# Grafio de Pizza
fatias, texto = plt.pie(df.Gender.value_counts(), colors=listaRGB, startangle=90)
plt.axes().set_aspect('equal', 'datalim')
plt.legend(fatias, labels, bbox_to_anchor=(1.05, 1))
plt.title('Sexo')
plt.show()
"""
