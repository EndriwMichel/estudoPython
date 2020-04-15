# Analise 2 miniprojeto cap 9
# database: https://www.kaggle.com/orgesleka/used-cars-database
import zipfile
import os
import subprocess
import stat
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mat
import matplotlib.pyplot as plt
from datetime import datetime

zip_cars = zipfile.ZipFile("PythonDsa/cap9/mini-projeto/autos.zip", 'r')
df = pd.read_csv(zip_cars.open('autos.csv'), encoding="latin-1")

"""
Crie um Barplot com o Preço médio do veículo por tipo de combustível e tipo de caixa de câmbio
"""
# vehicles_by_price = df.groupby(['fuelType', 'gearbox'])['price'].mean()
# vehicles_keys = [key for key, val in df.groupby(['fuelType'])['name'].count().items()]

# manuell = [vehicles_by_price[x]['manuell'] for x in vehicles_keys]
# automatik = [vehicles_by_price[x]['automatik'] for x in vehicles_keys]
# unspecified = [vehicles_by_price[x]['Unspecified'] for x in vehicles_keys]

# new_df = pd.DataFrame(
#     {
#         'manuell': manuell,
#         'automatik': automatik,
#         'unspecified': unspecified
#     },
#     index=vehicles_keys
# )

# ax = new_df.plot.bar()
# plt.show()


"""
Crie um Barplot com a Potência média de um veículo por tipo de veículo e tipo de caixa de câmbio
"""
vehicles_by_price = df.groupby(['vehicleType', 'gearbox'])['powerPS'].mean()
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
plt.show()