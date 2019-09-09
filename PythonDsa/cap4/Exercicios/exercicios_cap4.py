# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.

# lista = [2, 3, 4]
# calcPotencia = lambda x: x ** 3
# print(list(map(calcPotencia, lista)))

# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
# palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()
# resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
# for i in resultado:
#     print (i)

palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil'.split()

    print(type(valor))
def loadString(valor):
    for i in valor:
        resultado = [i.upper(), i.lower(), len(i)]
    return resultado

print(palavras[2])
print(list(map(loadString, palavras)))