# Função reduce
# Função utilizada para 'reduzir' uma lista por exemplo até chegar a um unico valor, como por exemplo somar todos os itens de uma lista de numeros 

from functools import reduce

lista = [47, 11, 42, 13]

def soma(a, b):
    return a + b

print(reduce(soma, lista))

# Outro exemplo
lst = [47, 11, 42, 13]

print(reduce(lambda x, y: x + y, lst))

# Atribuindo a uma variavel

max_find = lambda x, y: x if (x > y) else y

# PRovando que é uma função
print(type(max_find))

print(reduce(max_find, lst))