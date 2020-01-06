# Aray slicing
import numpy as np

# Criando array com opçao diag de diagonal
print('Criando array diagonal')
a = np.diag(np.arange(3))
print(a)

print('Slicing de linhas e colunas')
print(a[1,1])
print(a[1])
print('')

# Especificando range de elementos para slicing
print('Especificando range de elementos para slicing')
b = np.arange(10)
print('')
print('Array com range 0 a 10')
print(b)

print('')
# start:step:end
print('start:step:end')
print(b[2:9:3])
print('')

# Verificar se dois arrays são iguais
a = [1, 2, 3, 4]
b = [4, 2, 3, 4]

print('Verificar se dois arrays sao iguais')
print(np.array_equal(a, b))
print('')

print('Verificar minimo')
print(np.min(a))
print('')

print('Verificar maximo')
print(np.max(a))
print('')

# Somar valores ao array
print(np.array([1, 2, 3]) + 1.5)
print('') 

# Usando around para arredondar
print('Arrendondamento')
a = np.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
print(np.around(a))
print('')

# Copiando array
B = np.array([1, 2, 3, 4])
print(B)
C = B.flatten()
print(C)
print('')

# Adicionando dimensoes ao array
print('Adicionando dimensoes ao array')
v = np.array([1, 2, 3])

print(v[:, np.newaxis], v[:, np.newaxis].shape, v[np.newaxis,:].shape)
print('')

# Repeir elementos de array
print('Repetino elementos de um array')
print(np.repeat(v, 3))
print('')

# Repeir elementos com tile, obs: existe diferença
print('Repetino elementos de um array - com tile')
print(np.tile(v, 3))
print('')

# Concatenar elementos de um array
print('Concatenar array')
w = np.array([4, 5])
print(np.concatenate((v, w)))
print('')

# Copiar um array
print('copiar array - com copy')
w = np.array(v)
print(w)
print('')