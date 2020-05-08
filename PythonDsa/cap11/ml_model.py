# Capitulo 11 dsa Machine Learning
# Criando um modelo de machine learning para prever com acuracia de 70% se uma pessoa pode possuir diabetes
# Coleta de dados

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

print('Recuperando valores missing: ')

print('Linhas no dataframe: ', len(df))
print('Linhas missing glucose_conc: ', len(df.loc[df['glucose_conc'] == 0]))
print('Linhas missing diastolic_bp: ', len(df.loc[df['diastolic_bp'] == 0]))
print('Linhas missing thickness: ', len(df.loc[df['thickness'] == 0]))
print('Linhas missing insulin: ', len(df.loc[df['insulin'] == 0]))
print('Linhas missing bmi: ', len(df.loc[df['bmi'] == 0]))
print('Linhas missing age: ', len(df.loc[df['age'] == 0]))


# Tratando os valores zero (valores missing ocultos) com Imputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer

# Seleção de variáveis preditoras (Feature Selection)
atributos = ['num_preg', 'glucose_conc', 'diastolic_bp', 'thickness', 'insulin', 'bmi', 'diab_pred', 'age']

# Variável a ser prevista
atrib_prev = ['diabetes']

# Criando objetos
X = df[atributos].values
Y = df[atrib_prev].values

# print(X)
# print(Y)

# Definindo a taxa de split
split_test_size = 0.30

# Criando dados de treino e de teste
X_treino, X_teste, Y_treino, Y_teste = train_test_split(X, Y, test_size = split_test_size, random_state = 42)

# Imprimindo os resultados
print("{0:0.2f}% nos dados de treino".format((len(X_treino)/len(df.index)) * 100))
print("{0:0.2f}% nos dados de teste".format((len(X_teste)/len(df.index)) * 100))

print("Original True : {0} ({1:0.2f}%)".format(len(df.loc[df['diabetes'] == 1]), 
                                               (len(df.loc[df['diabetes'] ==1])/len(df.index) * 100)))

print("Original False : {0} ({1:0.2f}%)".format(len(df.loc[df['diabetes'] == 0]), 
                                               (len(df.loc[df['diabetes'] == 0])/len(df.index) * 100)))
print("")
print("Training True : {0} ({1:0.2f}%)".format(len(Y_treino[Y_treino[:] == 1]), 
                                               (len(Y_treino[Y_treino[:] == 1])/len(Y_treino) * 100)))

print("Training False : {0} ({1:0.2f}%)".format(len(Y_treino[Y_treino[:] == 0]), 
                                               (len(Y_treino[Y_treino[:] == 0])/len(Y_treino) * 100)))
print("")
print("Test True : {0} ({1:0.2f}%)".format(len(Y_teste[Y_teste[:] == 1]), 
                                               (len(Y_teste[Y_teste[:] == 1])/len(Y_teste) * 100)))

print("Test False : {0} ({1:0.2f}%)".format(len(Y_teste[Y_teste[:] == 0]), 
                                               (len(Y_teste[Y_teste[:] == 0])/len(Y_teste) * 100)))

# Criando objeto
preenche_zero = Imputer(missing_values=0, strategy='mean', axis=0)

# Substituindo os valores iguais a zero
X_treino = preenche_zero.fit_transform(X_treino)
X_teste = preenche_zero.fit_transform(X_teste)

print(X_treino)

from sklearn.naive_bayes import GaussianNB

# Criando o modelo
modelo_v1 = GaussianNB()

print('--------------------- Treinando o modelo (Treino)---------------------')
modelo_v1.fit(X_treino, Y_treino.ravel())

# Verificando a exatidão
from sklearn import metrics

nb_predict_train = modelo_v1.predict(X_treino)
print('Exatidão: {0:.4f}'.format(metrics.accuracy_score(Y_treino, nb_predict_train)))

print('')
print('--------------------- Treinando o modelo (Teste)---------------------')
print('')

nb_predict_test = modelo_v1.predict(X_teste)
print('Exatidão: {0:.4f}'.format(metrics.accuracy_score(Y_teste, nb_predict_test)))

# A forma mais efetiva de medir a acuracia é com os dados de teste, pois são dados que o modelo nunca viu

print('')
print('--------------------- Metricas ---------------------')
print('')

print('Confusion Matrix')

print('{0}'.format(metrics.confusion_matrix(Y_teste, nb_predict_test, labels=[1, 0])))
print('')

print('Classification Report')
print(metrics.classification_report(Y_teste, nb_predict_test, labels=[1, 0]))

print('')
print('--------------------- Otimização com Random Forest ---------------------')
print('')

from sklearn.ensemble import RandomForestClassifier

modelo_v2 = RandomForestClassifier(random_state=42)
modelo_v2.fit(X_treino, Y_treino.ravel())

# Verificando os dados de treino
rf_predict_train = modelo_v2.predict(X_treino)
print('Exatidão: {0:.4f}'.format(metrics.accuracy_score(Y_treino, rf_predict_train)))
print('')

# Verificando os dados de teste
rf_predict_test = modelo_v2.predict(X_teste)
print('Exatidão: {0:.4f}'.format(metrics.accuracy_score(Y_teste, rf_predict_test)))
# Novamente notasse a importance de utilizar os dados de "teste" que s"ao dados que o modelo nunca viu e nunca validar a acuracia com base nos dados de "treino"

print('')
print('Confusion Matrix')

print('{0}'.format(metrics.confusion_matrix(Y_teste, rf_predict_test, labels=[1, 0])))
print('')

print('Classification Report')
print(metrics.classification_report(Y_teste, rf_predict_test, labels=[1, 0]))

print('')
print('--------------------- Regressão Logística ---------------------')
print('')
# Obs.: Regressão logistica é um modelo dentro da CLASSIFICAÇÃO e não pertence aos modelos de Regressão 

from sklearn.linear_model import LogisticRegression

# terceira versão do modelo usando Regressão Logistica    
modelo_v3 = LogisticRegression(C=0.7, random_state=42)
modelo_v3.fit(X_treino, Y_treino.ravel())
lr_predict_test = modelo_v3.predict(X_teste)

# Verificando os dados de teste
print('Exatidão: {0:.4f}'.format(metrics.accuracy_score(Y_teste, lr_predict_test)))

print('Classification Report')
print(metrics.classification_report(Y_teste, lr_predict_test, labels=[1, 0]))

# Resultado final

# Naive Bayes = 0.73
# Random Forest = 0.71
# Regressão Logistica = 0.74
import pickle

print("Salvando o modelo")

filename = 'modelo_treinado_v3.sav'
pickle.dump(modelo_v3, open(filename, 'wb'))
