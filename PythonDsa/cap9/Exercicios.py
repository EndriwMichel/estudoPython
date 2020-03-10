""" Imports """
import time
import numpy as np
import pandas as pd
from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

fontsize = 14
ticklabelsize = 14

print('======= Extração e Transformação de Dados =======')
""" Carregando o dataset """
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(len(df))
# print(df.head())

""" 
Imprima os valores numéricos da Variável target (o que queremos prever), 
uma de 3 possíveis categorias de plantas: setosa, versicolor ou virginica 
"""
# print(iris.target_names)

""" 
Imprima os valores numéricos da Variável target (o que queremos prever), 
uma de 3 possíveis categorias de plantas: 0, 1 ou 2 
"""
# print(iris.target)

""" 
Adicione ao dataset uma nova coluna com os nomes das espécies, pois é isso que vamos tentar prever (variável target)
"""
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
# print(df.head())

""" 
Inclua no dataset uma coluna com os valores numéricos da variável target
"""
df['target'] = iris.target
# print(df.head())

""" 
Extraia as features (atributos) do dataset e imprima
"""
# print(df.columns)

"""
Calcule a média de cada feature para as 3 classes
"""
# print(df.groupby('target').mean())

print('')
print('======= Exploração de Dados =======')
print('')

"""
Imprima uma Transposta do dataset (transforme linhas e colunas e colunas em linhas)
"""
# print(df.transpose().T)

"""
Utilize a função Info do dataset para obter um resumo sobre o dataset
"""
# print(df.info())

"""
Faça um resumo estatístico do dataset
"""
# print(df.describe())

"""
Verifique se existem valores nulos no dataset
"""
# print(df.isnull().values.any())
# alterativa
# print(df.isnull().sum())

"""
Faça uma contagem de valores de sepal length
"""
# print(df['sepal length (cm)'].value_counts())

print('')
print('======= Plot =======')
print('')

"""
Crie um Histograma de sepal length
"""
# df['sepal length (cm)'].hist()
# plt.show()

"""
Crie um Gráficos de Dispersão (scatter Plot) da variável sepal length versus número da linha, 
colorido por marcadores da variável target
"""
# plt.scatter(
#     df['sepal length (cm)'],
#     [x for x in range(0, len(df['sepal length (cm)']))],
#     # c=df['target']
#     c=[x for x in range(0, len(df['sepal length (cm)']))]
# )
# plt.show()

"""
Crie um Scatter Plot de 2 Features (atributos)
"""
# plt.scatter(
#     df['sepal length (cm)'],
#     df['species'],
#     c=df['target']
# )
# plt.xlabel('sepal length (cm)')
# plt.ylabel('species')
# plt.title('sepal length (cm) x species')
# plt.show()

"""
Crie um Scatter Matrix das Features (atributos)
"""
# attributes = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
# scatter_matrix(df[attributes], alpha=0.2, figsize=(12, 9))
# plt.show()


"""
Crie um Histograma de todas as features
"""
# df.hist(figsize=(8, 8))
# plt.show()