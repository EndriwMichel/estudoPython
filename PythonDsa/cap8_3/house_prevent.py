# Prevendo preços de casas

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

print('--- Prevendo preços de casas com o dataset boston ---')
boston = load_boston()

""" Visualizando o shape, 506 linhas por 13 colunas """
# print(boston.data.shape)

""" Visualizando a descrição do dataset """
# print(boston.DESCR)

""" Visualizando os atributos do dataset (colunas) """
# print(boston.feature_names)

# Visualizando os dados em um DataFrame Pandas 
df = pd.DataFrame(boston.data)
# print(df.head())

# Alterando o nome das colunas do DataFrame 
df.columns = boston.feature_names
# print(df.head()) 

# Visualizando a variavel target (preços das casas) 
print(boston.target)

# Incluindo o target no dataframe 
df['PRICE'] = boston.target
# print(df.head()) 

print('')

# Utilizando LinearRegresion para prever preço das casas 
print('--- Utilizando LinearRegresion para prever preço das casas ---')

# Removendo a coluna PRICE para poder utilizar ela no Y para analise preditiva, foi incluida anteriormente somente para visualização 
x = df.drop('PRICE', axis=1)
y = df.PRICE

""" Criação de plot para visualização geral de como estão os dados """
# plt.scatter(df.RM, y)
# plt.xlabel('Média de numeros de quartos por casa (RM)')
# plt.ylabel('Preço da casa')
# plt.title('Relação de numero de quartos e preços')
# plt.show()

# Criando o modelo
model = LinearRegression()

model.fit(x, y)

print('')
# Coeficientes
print('Coeficientes: ', model.intercept_)
print('Numero de coeficientes: ', len(model.coef_))
print('')

"""
Criando gráfico de relação preço real x preço previsto
Porém existem erros no gráfico, não faz sentido apresentar o 'x' para o modelo pois são dados que le ja conhece
"""
# plt.scatter(df.PRICE, model.predict(x))
# plt.xlabel('Preço original')
# plt.ylabel('Preço previsto')
# plt.title('Relação preço original x preço previsto')
# plt.show()

# Subtraindo o preço original do preço previsto para descobrir a taxa de erro
mse = np.mean((df.PRICE - model.predict(x)) ** 2)
# print(mse)


print('--- Separando os dados em treino e teste (Procedimento manual) ---')
print('')

# Pegando dados para treino e teste de x (dados treinados)
x_treino = x[:-50]
x_teste = x[-50:]

# Pegando dados para treino e teste de y (preços)

y_treino = df.PRICE[:-50]
y_teste = df.PRICE[-50:]

# Imprimindo o shape
# print('Shapes de x: ', x_treino.shape, x_teste.shape)
# print('Shapes de y: ', y_treino.shape, y_teste.shape)

print('')

print('--- Separando os dados em treino e teste (Procedimento automatico randomico) ---')
print('')

# Treinando com o train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(x, df.PRICE, test_size=0.30, random_state=5)
print('Shapes de x: ', x_treino.shape, x_teste.shape)
print('Shapes de y: ', y_treino.shape, y_teste.shape)

# Treinando um noo modelo com base no resultado do train_test_split
model_two = LinearRegression()

model_two.fit(x_treino, y_treino)

# Definindo os dados de treino e teste
pred_treino = model_two.predict(x_treino)
pred_teste = model_two.predict(x_teste)

""" Visualizando os dados """
# plt.scatter(model_two.predict(x_treino), model_two.predict(x_treino) - y_treino, c='b', s=40, alpha=0.5)
# plt.scatter(model_two.predict(x_teste), model_two.predict(x_teste) - y_teste, c='g', s=40, alpha=0.5)
# plt.hlines(y=0, xmin=0, xmax=50)
# plt.ylabel('Residuo')
# plt.title('Residual plot - Treino(Azul) Teste(Verde)')
# plt.show()