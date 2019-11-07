# Utilizando pandas para ler arquivos
import pandas as pd

filename = 'arquivos/binary.csv'

arq1 = pd.read_csv(filename)

print(arq1.head())

# Outro teste

print('')

filename = 'arquivos/salarios.csv'

arq1 = pd.read_csv(filename)

print(arq1.head())


