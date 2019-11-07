# função zip
# zip é utilizado para unir duas listas de valores e retornar uma tupla desta união, porém retorna sempre com base no menor valor

x = [1, 2, 3]
y = [4, 5, 6]

print(list(zip(x, y)))

print('')
# Retorna o numero de valores de acordo com o menor numero
print(list(zip('ABCD', 'xy')))

a = [1, 2, 3]
b = [4, 5, 6, 7, 8]

print(list(zip(a, b)))

print('')
# Exemplo com dicionario, unindo chaves
d1 = {'a':1, 'b':2}
d2 = {'c':4, 'd':5}

print('União de chaves: ')
print(list(zip(d1, d2)))
print('')
# Unindo as chaves de d1 com valores de d2
print('União de valores: ')
print(list(zip(d1, d2.values())))

