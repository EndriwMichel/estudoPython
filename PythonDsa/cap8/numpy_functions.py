# Numpy funções
import numpy as np

# Cria um array de acordo com um range
vetor2 = np.arange(0., 4.5, .5)
print(vetor2)

# Verificar o tipo de 'data' do array
print(vetor2.dtype)

# Criar arrays de zeros
print(np.zeros(10))

# exemplo de possiblidades de array com numpy
z = np.eye(6)
print(z)

d = np.diag([1, 2, 3, 4, 5, 6])
print(d)

# Numerações complexas
c = np.array([1+2j, 3+4j, 5+6*1j])
print(c)

# Arrays de numeros booleanos
b = np.array([True, True, False, True])
print(b)

# Array de strings
s = np.array(['Python', 'R', 'J'])
print(s)

# Metodo linspace retorna um numero de valores igualmente distribuidos em um intervalo especifico
print(np.linspace(0, 10))