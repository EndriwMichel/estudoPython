# Modulos e pacotes

# Math para operações matematicas
import math

# Mostra todos os modulos disponiveis para o pacote
dir(math)

# Calcular raiz quadrada
print(math.sqrt(25))

# Importando apenas uma função do pacote
from math import sqrt

print(sqrt(9))

# Ajuda sobre o pacote
print(help(sqrt))

# Random para operações randomicas
import random

print(random.choice(['maça', 'banana', 'laranja']))

print(random.sample(range(100), 10))

import statistics

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

# Apresentar a média dos valores
print(statistics.mean(dados))

# Calcular mediana
print(statistics.median(dados))


# Pacote OS
import os

# Verificar diretório atual do sistema operacional
print(os.getcwd())

# print(dir(os))

# Pacote Sys
import sys

print(sys.version)

# Pacote urllib
import urllib.request

resposta = urllib.request.urlopen('http://python.org')

print(resposta)

html = resposta.read()

print(html)