# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

# lista = [2, 3, 4]
# calcPotencia = lambda x: x ** 3
# print(list(map(calcPotencia, lista)))

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
# palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
# resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
# for i in resultado:
#     print(i)

# palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()

# def loadString(valor):
#     resultado = [valor.upper(), valor.lower(), len(valor)]
#     return print(resultado)

# list(map(loadString, palavras))


# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matrix = [[1, 2],[3,4],[5,6],[7,8]]

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

# print(aux)
