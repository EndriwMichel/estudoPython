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
Crie um Plot que mostre o número de veículos pertencentes a cada marca
"""
# brand_count = df.groupby(['brand'])['name'].count()

# b_plot = brand_count.plot(kind='barh', figsize=(14, 10), color='#C70039')
# b_plot.set_xlabel('Count of Vehicles', labelpad=20, weight='bold', size=10)
# b_plot.set_ylabel('Brand', labelpad=20, weight='bold', size=10)
# plt.title('Número de veículos pertencentes a cada marca')
# plt.show()

"""
Crie um Plot com o Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio
"""
vehicles_by_price = df.groupby(['vehicleType', 'gearbox'])['price'].mean()
vehicles_keys = [key for key, val in df.groupby(['vehicleType'])['name'].count().items()]

manuell = [vehicles_by_price[x]['manuell'] for x in vehicles_keys]
automatik = [vehicles_by_price[x]['automatik'] for x in vehicles_keys]
unspecified = [vehicles_by_price[x]['Unspecified'] for x in vehicles_keys]

new_df = pd.DataFrame(
    {
        'manuell': manuell,
        'automatik': automatik,
        'unspecified': unspecified
    },
    index=vehicles_keys
)

ax = new_df.plot.bar()
plt.title('Preço médio dos veículos com base no tipo de veículo e tipo de caixa de câmbio')
plt.show()
