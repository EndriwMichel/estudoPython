# Numpy statistica
import numpy as np
import matplotlib.pyplot as plt

A = np.array([15, 23, 63, 94, 75])
print('')

# Calcular media
print('Calcular media')
print(np.mean(A))
print('')

# Calcular desvio
print('Calcular desvio')
print(np.std(A))
print('')

# Calcular Variancia
print('Calcular variancia')
print(np.var(A))
print('')

# --- Arrange ----

# Cria um array
d = np.arange(1, 10)

print('Array de valores')
print(d)
print('')

# Soma os valores do array para calcular frequencia
d_sum = np.sum(d)
print('Calculo de soma, para poder calcular frequencia')
print(d_sum)
print('')

# Caclular produto
print('Caclular produto')
print(np.prod(d))
print('')

# Caclular soma acumulada
print('Caclular soma acumulada - fibonasi')
print(np.cumsum(d))
print('')

print('Caclular media de valores randomicos')
a = np.random.randn(400, 2)
m = np.mean(0)
print(m, m.shape)

plt.plot(a[:,0], a[:,1], 'o', markersize=5, alpha=0.50)
plt.plot(m[0], m[1], 'ro', markersize=10)
plt.show()

