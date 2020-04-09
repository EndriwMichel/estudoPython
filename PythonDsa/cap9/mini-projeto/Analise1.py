# Analise 1 miniprojeto cap 9
# database: https://www.kaggle.com/orgesleka/used-cars-database
import pandas as pd
import zipfile
import os
import subprocess
import stat
import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

zip_cars = zipfile.ZipFile("PythonDsa/cap9/mini-projeto/autos.zip", 'r')
df = pd.read_csv(zip_cars.open('autos.csv'), encoding="latin-1")

"""
Crie um Plot com a Distribuição de Veículos com base no Ano de Registro
"""
# plt.hist(df.yearOfRegistration, density=True, histtype='stepfilled')
# plt.show()

"""
Crie um Boxplot para avaliar os outliers
"""
# df.boxplot(column=['price'], by=['vehicleType'], figsize=(8, 5), patch_artist=True)
# plt.show()

"""
Crie um Count Plot que mostre o número de veículos pertencentes a cada categoria
"""
vehicles_values = [x for x in df.groupby(['vehicleType'])['name'].count()]
vehicles_keys = [key for key, val in df.groupby(['vehicleType'])['name'].count().items()]

fig, ax = plt.subplots(figsize=(10,8))
ax.bar(vehicles_keys, vehicles_values)
plt.show()
