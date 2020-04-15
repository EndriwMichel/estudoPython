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
Calcule a média de preço por marca e por veículo
"""
vehicles_by_price = df.groupby(['brand', 'vehicleType'])['price'].mean()
