# Imports
import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

fontsize = 14
ticklabelsize = 14

# Carregando o dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(len(df))
print(df.head())

# Imprima os valores numéricos da Variável target (o que queremos prever), 
# uma de 3 possíveis categorias de plantas: setosa, versicolor ou virginica
print(iris.target_names)

# Imprima os valores numéricos da Variável target (o que queremos prever), 
# uma de 3 possíveis categorias de plantas: 0, 1 ou 2
print(iris.target)

# Adicione ao dataset uma nova coluna com os nomes das espécies, pois é isso que vamos tentar prever (variável target)
df.insert(4, 'SVV', None)

# Inclua no dataset uma coluna com os valores numéricos da variável target
df_species = df.copy()
species = iris.target

df_species['target'] = species

# Extraia as features (atributos) do dataset e imprima
print(df_species)

# Calcule a média de cada feature para as 3 classes
