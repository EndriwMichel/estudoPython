# Analise 1 miniprojeto cap 9
import pandas as pd
import zipfile

zip_cars = zipfile.ZipFile("autos.zip", 'r')
df = pd.read_csv(zip_cars.open('autos.csv'), encoding="latin-1")

print(df)