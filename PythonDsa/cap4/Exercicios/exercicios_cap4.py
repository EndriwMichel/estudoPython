# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
print('=========Exercicio 1=========')
lista = [2, 3, 4]
calcPotencia = lambda x: x ** 3
print(list(map(calcPotencia, lista)))

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
# palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
# resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
# for i in resultado:
#     print(i)
print('')
print('=========Exercicio 2=========')
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()

def loadString(valor):
    resultado = [valor.upper(), valor.lower(), len(valor)]
    return print(resultado)

list(map(loadString, palavras))


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]
print('')
print('=========Exercicio 3=========')
vet1 = []
vet2 = []
aux = []

for x, y in matrix:
    vet1.append(x)
    vet2.append(y)

aux.append(vet1)
aux.append(vet2)

for i in aux:
    print(i)


# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]
print('')
print('=========Exercicio 4=========')

calc_square = lambda num: num**2

calc_cube = lambda num: num**3

calc = [calc_square, calc_cube]

for x in calc:
    print(list(map(x, lista)))

# Exercício 5 - Abaixo você encontra duas listas. Faça com que cada elemento da listaA seja elevado 
# ao elemento correspondente na listaB.
listaA = [2, 3, 4]
listaB = [10, 11, 12]
print('')
print('=========Exercicio 5=========')

for x, y in zip(listaA, listaB):
    print(x**y)

# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.
range(-5, 5)    
print('')
print('=========Exercicio 6=========')

def verify_negative(num):
    if num < 0:
        return True
    else:
        return False

print(list(filter(verify_negative, range(-5, 5))))

# Exercício 7 - Usando a função filter(), encontre os valores que são comuns às duas listas abaixo.
a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print('')
print('=========Exercicio 7=========')

print(list(filter(lambda x: x in a, b)))

# Exercício 8 - Considere o código abaixo. Obtenha o mesmo resultado usando o pacote time. 
# Não conhece o pacote time? Pesquise!
print('')
print('=========Exercicio 8=========')
import datetime
import time

print (datetime.datetime.now().strftime("%d/%m/%Y %H:%M"))
print(time.strftime('%d/%m/%Y %H:%M'))

# Exercício 9 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}
print('')
print('=========Exercicio 9=========')

# dict3 = [{x, y} for x, y in zip(dict1.keys(), dict2.values())]
dict3 = {}
for x, y in zip(dict1.keys(), dict2.values()):
    dict3[x] = y

print(dict3)

# Exercício 10 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('')
print('=========Exercicio 10=========')

for k, v in enumerate(lista):
    if k > 5:
        print(v)