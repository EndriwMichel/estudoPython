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

# Quais são os principais interesses dos participantes da lista ?
# Principal interesse é desenvolvimento web (full-stack, front-end, back-end)
"""
# Definindo as quantidades
num = len(df.JobRoleInterest.value_counts().index)

# Criando a lista de cores
listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
labels = df.JobRoleInterest.value_counts().index
colors = ['OliveDrab', 'Orange', 'ORangeRed', 'DarkCyan', 'Salmon', 'Sienna', 'Maroon', 'LightSlateGrey', 'DimGray']

# Grafico de pizza
fatias, texto = plt.pie(df.JobRoleInterest.value_counts(), colors=listaRGB, startangle=90)
plt.axes().set_aspect('equal', 'datalim')
plt.legend(fatias, labels, bbox_to_anchor=(1.25, 1))
plt.title('Interesse Profissional')
plt.show()
"""

# Quais as áreas de negócio em que os participantes trabalham
# A maioria é desenvolimento de software e TI
"""
# Definindo as quantidades
num = len(df.EmploymentField.value_counts().index)

# Criando lista de cores
listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
labels = df.EmploymentField.value_counts().index

# Grafico de pizza
fatias, texto = plt.pie(df.EmploymentField.value_counts(), colors=listaRGB, startangle=90)
plt.axes().set_aspect('equal', 'datalim')
plt.legend(fatias, labels, bbox_to_anchor=(1.3, 1))
plt.title('Area de atuação')
plt.show()
"""

# Quais as principais preferencias de trabalho por idade ?
# A medida que a idade aumenta a preferencia por trabalhar como freelancer tbm aumenta
# Profissionais de 20 a 30 anos preferem startups 

df_agerange = df.copy()
bins = (0, 20, 30, 40, 50, 60, 100)

# Criando nova coluna...
df_agerange['AgeRange'] = pd.cut(df_agerange['Age'], bins, labels=['< 20', '20-30', '30-40', '40-50', '50-60', '< 60'])

"""
df2 = pd.crosstab(df_agerange.AgeRange, df_agerange.JobPref).apply(lambda r: r/r.sum(), axis=1)

# Definindo a quantidade
num = len(df_agerange.AgeRange.value_counts().index)

# Criando lista de cores
listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
labels = df_agerange.AgeRange.value_counts().index

# Grafico de barras
axl = df2.plot(kind='bar', stacked=True, color=listaRGB, title='Preferencia de trabalho por idade')
lines, labels = axl.get_legend_handles_labels()
axl.legend(lines, labels, bbox_to_anchor=(1.51, 1))
plt.show()
"""

# Qual o objetivo de realocação ?
# Quanto maior a idade , menos interesse me realocação
"""
df3 = pd.crosstab(df_agerange.AgeRange, df_agerange.JobRelocateYesNo).apply(lambda r: r/r.sum(), axis=1)

# Definindo a quantidade
num = len(df_agerange.AgeRange.value_counts().index)

# Criando lista de cores
listaHSV = [(x*1.0/num, 0.5, 0.5) for x in range(num)]
listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))

# Grafico de barras
axl = df3.plot(kind='bar', stacked=True, color=listaRGB, title='Realocação por idade')
lines, labels = axl.get_legend_handles_labels()
axl.legend(lines,['Não', 'Sim'], loc='best')
plt.show()
"""

# Qual a relação entre idade x horas de aprendizagem ?
"""
import warnings
warnings.filterwarnings('ignore')

# Criando subset de dados
df9 = df.copy()
df9 = df9.dropna(subset=['HoursLearning'])
df9 = df9[df['Age'].isin(range(0, 70))]

# Definino valores de x e y
x = df9.Age
y = df9.HoursLearning

# Gerando grafico
m, b = np.polyfit(x, y, 1)
plt.plot(x, y, '.')
plt.plot(x, m*x + b, '-', color='red')
plt.xlabel('Idade')
plt.ylabel('Horas de treinamento')
plt.title('Idade por horas de treinamento')
plt.show()
"""
