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
