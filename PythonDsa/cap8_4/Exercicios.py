# Exercicios Python capitulo 8
import numpy as np
# Exercicio 1
# Crie um array NumPy com 1000000 e uma lista com 1000000.
# Multiplique cada elemento do array e da lista por 2 e calcule o tempo de execução com cada um dos objetos (use %time).
# Qual objeto oferece melhor performance, array NumPy ou lista?

import numpy as np
import time

list_arr = []
np_arr = np.arange(0, 1000000)

list_arr.extend(range(0, 1000000))

def returnNumpyPerform(np_list):
    start = time.time()
    new_np_arr = np.multiply(np_list, 2)    
    return print('numpy: ', time.time() - start)

def returnListPerfomr(list_list):
    start = time.time()
    new_list_arr = [x * 2 for x in list_list]
    return print('list: ', time.time() - start)

returnNumpyPerform(np_arr)
returnListPerfomr(list_arr)

print('R: Numpy tem melhor performance')
print('')

# Exercicio 2
# Crie um array de 10 elementos
# Altere o valores de todos os elementos dos índices 5 a 8 para 0
np_arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.where(np_arr2 >= 5, np.where(np_arr2 <= 8, 0, np_arr2), np_arr2))
# Segunda alternativa
# np_arr2[5:8] = 0
# print(np_arr2)


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

# Exercicio 6
# Considere os 3 arrays abaixo
# Retorne o valor do array xarr se o valor for True no array cond. Caso contrário, retorne o valor do array yarr.
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

valores = []

for x in range(0, len(cond)):
    if x == True:
        valores.append(xarr[x])
    else:
        valores.append(yarr[x])

# print(valores)

# Exercicio 7
# Crie um array A com 10 elementos e salve o array em disco com a extensão npy
# Depois carregue o array do disco no array B
# ???

# Exercicio 8
# Considerando a série abaixo, imprima os valores únicos na série
import pandas as pd
obj = pd.Series(['c', 'a', 'd', 'a', 'a', 'b', 'b', 'c', 'c', 'a', 'b'])
# print(obj[obj.duplicated(keep=False) == False])
# Resposta correta: obj.unique()

# Exercicio 9
# Considerando o trecho de código que conecta em uma url na internet, imprima o dataframe conforme abaixo.
import requests
import json
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
resp_j = json.loads(resp.content)

df = pd.DataFrame(resp_j)
# print(df.columns)

# Exercicio 10
# Crie um banco de dados no SQLite, crie uma tabela, insira registros, 
# consulte a tabela e retorne os dados em dataframe do Pandas
import sqlite3

def connect(file):
    return sqlite3.connect(file)

def insertCarros(con, carros_list):
    cursor = con.cursor()
    cursor.execute('DELETE FROM carros')    
    q_result = cursor.executemany('INSERT INTO carros (marca, nome_modelo, ano) VALUES (?, ?, ?)', carros_list)

    return q_result

carros = (
    ['Toyota', 'Corola', 2019],
    ['GM', 'Onyx', 2017],
    ['Honda', 'Fit', 2018],
    ['Honda', 'Civic', 2020],
    ['Fiat', 'Strada', 2015]
)

con = connect('db_carros.db')
result = insertCarros(con, carros)

sql_df = pd.read_sql_query('SELECT * FROM carros', con)
print(sql_df)

con.close()