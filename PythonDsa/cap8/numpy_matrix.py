# Numpy trabalhando com matrizes
import numpy as np

# Primeira matriz em numpy
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)

# Verificando o shape da matriz, no exemplo ele ira imprimir uma matriz com duas linhas e tres colunas
print(matriz.shape)
print('')

# Criando matriz com numeros 1
matriz1 = np.ones((2, 3))
print(matriz1)
print('')

# Convertendo listas em matriz
lista = [[13, 81, 22], [0, 34, 89], [21, 48, 94]]

matriz2 = np.matrix(lista)

print(matriz2)
print('')

# Verificando o shape da matriz
# print(np.shape(matriz2)) --> outra forma de fazer
print(matriz2.shape)

# Verificando o tamanho da matriz, qtd de informações
print(matriz2.size)

# tipo da 'data' da matriz
print(matriz2.dtype)

# Verificar o tamanho que ira ficar na memoria
print(matriz2.itemsize)

# total de bytes da matriz
print(matriz2.nbytes)

# Imprimir elemento da matriz utilizando slice
print('')
print('Imprimindo valor da matriz: ')
print(matriz2[2, 1])

# Alterar o elemento da matriz
print('')
print('Alterar elemento da matriz: ')
matriz2[1, 0] = 100
print(matriz2)

print('')
print('Alterar tipos de dados: ')
# Tipos de dados
x = np.array([1, 2]) # Numpay automaticamente decide ser inteiro
y = np.array([1.0, 2.0]) # Numpay automaticamente decide ser float
z = np.array([1, 2], dtype=np.float64) # forçando a entender que é do tipo float 

print(x.dtype, y.dtype, z.dtype)

# Verificar dimensoes
print('')
print('Verificar diemnsoes: ')
print(matriz2.ndim)