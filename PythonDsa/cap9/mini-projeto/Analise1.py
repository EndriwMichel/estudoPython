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

zip_cars = zipfile.ZipFile("autos.zip", 'r')
df = pd.read_csv(zip_cars.open('autos.csv'), encoding="latin-1")

"""
Crie um Plot com a Distribuição de Veículos com base no Ano de Registro
"""
# plt.hist(df.yearOfRegistration, density=True, histtype='stepfilled')
# plt.show()

"""
Crie um Boxplot para avaliar os outliers
"""
fig1, ax1 = plt.subplots()
ax1.set_title('Basic Plot')
ax1.boxplot([df.price, df.vehicleType])
plt.show()
# print(df)
# cd .\Documents\estudoPython\PythonDsa\cap9\mini-projeto\