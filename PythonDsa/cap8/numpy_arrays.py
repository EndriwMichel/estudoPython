import numpy as np

# Verificando a versão do numpy
print(np.__version__)
print('')

# Executando o comando help para mostrar informações do pacote
# print(help(np.array))

# declarando um array
vetor1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

print(vetor1)

# Verificando o tipo do array
#print(type(vetor1))

# Utilizando metodos de array, cumsum é o metodo para calcular
print(vetor1.cumsum())

# alterando elemento
vetor1[0] = 100

print(vetor1)

# Não é possivel mudar ou incluir elemento de outro tipo de valor
# vetor1[0] = 'novo elemento'

# Função shape traz a dimensão e a quantidade de posições do array 
print(vetor1.shape)