# Numpay Metodos e Operações
import numpy as np
import matplotlib.pyplot as plt
import os

# Utilizando random com numpy
print(np.random.rand(10))

# Criando graficos
# plt.show(plt.hist(np.random.rand(1000)))

# Criando heatmap
#imagem = np.random.rand(30, 30)
#plt.imshow(imagem, cmap=plt.cm.hot)
#plt.colorbar()


# Transformar arquivo csv em array com numpay
filename = os.path.join('iris.csv')

arquivo = np.loadtxt(filename, delimiter=',', usecols=(0, 1, 2, 3), skiprows=1)
print(arquivo)

# plotando direto do arquivo csv
var1, var2 = np.loadtxt(filename, delimiter=',', usecols=(0, 1), skiprows=1, unpack=True)
plt.show(plt.plot(var1 , var2, 'o', markersize=8, alpha=0.75))