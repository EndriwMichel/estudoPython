# matplot lib
import matplotlib as mpl
import matplotlib.pyplot as plt

print(mpl.__version__)

# Primeiro plot, hello plot
print('First plot')
"""
plt.plot([1, 3, 5], [2, 5, 7])
plt.show()
"""
print('')

# Construindo gráfico
print('Construindo gráfico')
x = [1, 4, 5]
y = [3, 7, 2]

"""
plt.plot(x, y)
plt.xlabel('Variavel 1')
plt.ylabel('Variavel 2')
plt.title('Teste Plot')
plt.show()
"""
print('')

# Outro exemplo
print('Segundo exemplo')
x2 = [1, 2, 3]
y2 = [11, 12, 15]

plt.plot(x2, y2, label='Primeira linha')
plt.legend()
plt.show()