# Analise 2 miniprojeto cap 9
# database: https://www.kaggle.com/orgesleka/used-cars-database
import pandas as pd
import zipfile
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

zip_cars = zipfile.ZipFile("PythonDsa/cap9/mini-projeto/autos.zip", 'r')
df = pd.read_csv(zip_cars.open('autos.csv'), encoding="latin-1")

"""
Crie um Plot que mostre o número de veículos pertencentes a cada marca
"""
# brand_count = df.groupby(['brand'])['name'].count()

# b_plot = brand_count.plot(kind='barh', figsize=(14, 10), color='#C70039')
# b_plot.set_xlabel('Count of Vehicles', labelpad=20, weight='bold', size=10)
# b_plot.set_ylabel('Brand', labelpad=20, weight='bold', size=10)
# plt.show()

"""
Crie um Plot com o Preço médio dos veículos com base no tipo de veículo, bem como no tipo de caixa de câmbio
"""

# price_by_type = [[x, y] for x, y in df.groupby(['vehicleType', 'gearbox'])['price'].mean().items()]
# price_by_type = df.groupby(['vehicleType', 'gearbox'])['price'].mean()

price_by_type = df.groupby(['vehicleType', 'gearbox'])['price'].mean()
vehicles_keys = [key for key, val in df.groupby(['vehicleType'])['name'].count().items()]

# for x in vehicles_keys:
#     print(price_by_type[x]['manuell'])

ax = plt.subplot(111)

for x in vehicles_keys:
    ax.bar(x-0.1, price_by_type[x], width=0.1, color='b', align='center')
    ax.bar(x, price_by_type[x], width=0.1, color='g', align='center')
    ax.bar(x+0.1, price_by_type[x], width=0.1, color='r', align='center')
    # print(price_by_type[x]['manuell'])

plt.show()
