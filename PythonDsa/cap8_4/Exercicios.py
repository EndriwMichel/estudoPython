# Exercicios Python capitulo 8
import numpy as np

# Exercicio 2
# Crie um array de 10 elementos
# Altere o valores de todos os elementos dos índices 5 a 8 para 0
np_arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(np.where(np_arr2 >= 5, np.where(np_arr2 <= 8, 0, np_arr2), np_arr2))

# Exercicio 3
# Crie um array de 3 dimensões e imprima a dimensão 1
np_arr3 = np.array([[1,2,3], [4,5,6], [4,5,6]])
# print(np_arr3[0])

# Exercicio 4
# Crie um array de duas dimensões (matriz).
# Imprima os elementos da terceira linha da matriz
# Imprima todos os elementos da primeira e segunda linhas e segunda e terceira colunas
np_arr4 = np.array([[1,2,3],[4,5,6]])
new_arr = np.array([np_arr4[x][-2:] for x in range(0, len(np_arr4))])
# print(new_arr)

# Exercicio 5
# Calcule a transposta da matriz abaixo
arr = np.arange(15).reshape((3, 5))
# print(np.transpose(arr))

# Considere os 3 arrays abaixo
# Retorne o valor do array xarr se o valor for True no array cond. Caso contrário, retorne o valor do array yarr.
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

