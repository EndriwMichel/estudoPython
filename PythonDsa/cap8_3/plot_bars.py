# matplot bars
import matplotlib as mpl
import matplotlib.pyplot as plt

# Primeiro grafico de barras
print('Grafico de barras')
x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]
"""
plt.bar(x, y, label="Barras", color='r')
plt.legend()
plt.show()
"""
print('')

# Segundo exemplo
print('Segundo exemplo')
x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 2, 4, 2]

"""
plt.bar(x, y, label='Barras1', color='r')
plt.bar(x2, y2, label='Barras2', color='y')
plt.legend()
plt.show()
"""
print('')

# Terceiro exemplo
print('Terceiro exemplo')
idades = [22,65,45,55,21,22,34,42,41,4,99,101,120,122,130,111,115,80,75,54,44,64,13,18,48]

ids = [x for x in range(len(idades))]
"""
plt.bar(ids, idades)
plt.show()
"""
print('')

# Exemplo com histograma
print('Exemplo com histograma')
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]
"""
plt.hist(idades, bins, histtype='stepfilled', rwidth=0.8)
plt.show()
"""
print('')

# Scatterplot
print('Scatterplot')
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,5,6,8,4,8]
"""
plt.scatter(x, y, label='Pontos', color='r', marker='o', s=100)
plt.legend()
plt.show()
"""
print('')

# Stackplot
print('Stackplot')

dias = [1,2,3,4,5]
dormir = [7,8,6,77,7]
comer = [2,3,4,5,3]
trabalhar = [7,8,7,2,2]
passear = [8,5,7,8,13]
"""
plt.stackplot(dias, dormir, comer, trabalhar, passear, colors=['y', 'c', 'r', 'k', 'b'])
plt.show()
"""
print('')

# Pie chart
print('Pie Chart')
fatias = [7, 2, 2, 13]
atividades = ['dormir', 'comer', 'trabalhar', 'passear']
colunas = ['c', 'm', 'r', 'k']

plt.pie(fatias, labels=atividades, colors=colunas, startangle=90, shadow=True, explode=(0,0.1,0,0))
plt.show()