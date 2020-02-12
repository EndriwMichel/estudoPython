# Exemplo de LinearRegression
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

# Vamos chamar de X os dados de diâmetro da Pizza.
X = [[7], [10], [15], [30], [45]]

# Vamos chamar de Y os dados de preço da Pizza.
Y = [[8], [11], [16], [38.5], [52]]

modelo = LinearRegression()

modelo.fit(X, Y)

print("Uma pizza de 20 cm de diâmetro deve custar: R$%.2f" % modelo.predict([[20]]))

print('')

print('Coeficiente: ', modelo.coef_)

# MSE - Mean Square Error
print('MSE: %.2f' % np.mean((modelo.predict(X) - Y) ** 2))

print('Score de variação: %.2f'% modelo.score(X, Y))

print('')
print('Visualizando linha de regressão no scaterplot')

plt.scatter(X, Y, color='black')
plt.plot(X, modelo.predict(X), color='blue', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.xticks(())
plt.yticks(())
plt.show()