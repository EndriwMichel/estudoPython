# Função Filter
# Filtrar todos os elementos de uma lista por exemplo e retornar um booleano, true or false

def verifica_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Retorna somente os valores que derem True
print(list(filter(verifica_par, lista)))

# Utilizando lambda
print(list(filter(lambda x: x % 2 == 0, lista)))

print(list(filter(lambda num: num > 8, lista)))