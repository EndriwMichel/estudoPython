# Analise 2 miniprojeto cap 9
# database: https://www.kaggle.com/orgesleka/used-cars-database
import zipfile
import os
import subprocess
import stat
import numpy as np
import pandas as pd
# import seaborn as sns
import matplotlib as mat
import matplotlib.pyplot as plt
from datetime import datetime

plt.rcParams["figure.figsize"] = [12, 8]

zip_cars = zipfile.ZipFile("PythonDsa/cap9/mini-projeto/autos.zip", 'r')
df = pd.read_csv(zip_cars.open('autos.csv'), encoding="latin-1")

"""
Calcule a média de preço por marca e por veículo
"""
vehicles_by_price = df.groupby(['brand', 'vehicleType'])['price'].mean()

values_count = [key for key, val in df.groupby(['brand', 'vehicleType'])['vehicleType'].count().items()]

arr = [[vehicles_by_price[x[0]][x[1]], x[0], x[1]] for x in values_count]

df_vehicles = pd.DataFrame(arr, columns=['avgPrice', 'brand', 'vehicleType'])

# print(df_vehicles)

"""
Crie um Heatmap com Preço médio de um veículo por marca, bem como tipo de veículo
"""

df_vehicles = df_vehicles.pivot(index='brand', columns='vehicleType', values='avgPrice')

print(df_vehicles)
plt.pcolor(df_vehicles)
plt.yticks(np.arange(1.5, len(df_vehicles.index), 1), df_vehicles.index)
plt.xticks(np.arange(1.5, len(df_vehicles.columns), 1), df_vehicles.columns)
plt.title('Preço médio de um veículo por marca e tipo de veículo')
plt.ylabel('Marcas')
plt.xlabel('Tipos de Veiculos')

plt.show()
