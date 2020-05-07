# Capitulo 11 dsa Machine Learning
# Criando um modelo de machine learning para prever com acuracia de 70% se uma pessoa pode possuir diabetes

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('prima-data.csv')

# Visualizando o shape, 768 linas por 10 colunas (variaveis)
print(df.shape)

# Visualizando as primeiras linhas do dataset
print(df.head(5))

# Visualizando as ultimas colunas do dataset
print(df.tail(5))

"""
Obs.: A ultima coluna é a variavel 'target' ou a variavel que queremos prever, no caso diates = True/False
"""

# Verificando valores nulos
print(df.isnull().values.any())

print('')

# Identificando a correlação entre as variaveis
def plot_corr(df, size=10):
    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    ax.matshow(corr)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.show()

""" Visualização de correlação em gráfico """
# plot_corr(df)

# Coeficiente da correlação:
# +1 forte correlação positiva
#  0 não há correlação
# -1 forte correlação negativa

""" Visualização de correlação em tabela """
print(df.corr())

print('')

# definindo as classe, no caso se está ou não (True/False) 
# Obs.: O modelo não entende string, ou seja, True e False não resolvem, então covertemos para 1/0
diabetes_map = {True: 1, False: 0}

# Aplicando o mapeamento ao dataset
df['diabetes'] = df['diabetes'].map(diabetes_map)

# Visualizando como ficou o dataset
print(df.head(5))

# Verificando a distribuição dos dados
# True = 268
# False = 500
num_true = len(df.loc[df['diabetes'] == 1])
num_false = len(df.loc[df['diabetes'] == 0])
print('Casos verdadeiros: ', num_true)
print('Casos false: ', num_false)
