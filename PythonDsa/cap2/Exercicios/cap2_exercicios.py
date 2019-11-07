# Exercício 1 - Imprima na tela os números de 1 a 10. Use uma lista para armazenar os números.
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista_numeros)

# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela
lista_obj = ['valor1', 'valor2', 'valor3', 'valor4', 'valor5']
print(lista_obj)

# Exercício 3 - Crie duas strings e concatene as duas em uma terceira string
string1 = 'tudo'
string2 = 'bem'
string3 = string1+string2
print(string3)

# Exercício 4 - Crie uma tupla com os seguintes elementos: 1, 2, 2, 3, 4, 4, 4, 5 e depois utilize a função count do 
# objeto tupla para verificar quantas vezes o número 4 aparece na tupla
tup_num = (1, 2, 2, 3, 4, 4, 4, 5)
print(tup_num.count(4))

# Exercício 5 - Crie um dicionário vazio e imprima na tela
dic = {}
print(dic)

# Exercício 6 - Crie um dicionário com 3 chaves e 3 valores e imprima na tela
dic_exe6 = {'key1':1, 'key2':2, 'key3':3}
print(dic_exe6)

# Exercício 7 - Adicione mais um elemento ao dicionário criado no exercício anterior e imprima na tela
dic_exe6['key4'] = 4
print(dic_exe6)

# Exercício 8 - Crie um dicionário com 3 chaves e 3 valores. Um dos valores deve ser uma lista de 2 elementos numéricos. 
# Imprima o dicionário na tela.
dic_exe8 = {'a':1, 'b':[8, 9], 'c':3}
print(dic_exe8)

# Exercício 9 - Crie uma lista de 4 elementos. O primeiro elemento deve ser uma string, 
# o segundo uma tupla de 2 elementos, o terceiro um dcionário com 2 chaves e 2 valores e 
# o quarto elemento um valor do tipo float.
# Imprima a lista na tela.
list_exe9 = ['valor1', (1, 2), {'key1':3, 'key2':4}, 5.2]
print(list_exe9)

# Exercício 10 - Considere a string abaixo. Imprima na tela apenas os caracteres da posição 1 a 18.
frase = 'Cientista de Dados é o profissional mais sexy do século XXI'
print(frase[0:18])
