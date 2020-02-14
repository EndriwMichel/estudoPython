import numpy as np

# Diâmetros (cm)
Diametros = [[7], [10], [15], [30], [45]]

# Preços (R$)
Precos = [[8], [11], [16], [38.5], [52]]


from sklearn.linear_model import LinearRegression

# Vamos chamar de X os dados de diâmetro da Pizza.
# X = [[7], [10], [15], [30], [45]]
X = [7, 10, 15, 30, 45]


# Vamos chamar de Y os dados de preço da Pizza.
# Y = [[8], [11], [16], [38.5], [52]]
Y = [8, 11, 16, 38.5, 52]

modelo = LinearRegression()

xy = list(zip(X, Y))

# print(type(modelo))

# re_x = np.array(X).reshape(1, -1) # X.reshape(1, -1)
# re_y = np.array(Y).reshape(1, -1)  #Y.reshape(1, -1)

modelo.fit(xy, [20, 0]).predict()
# modelo.fit(Y, X).predict([20][0])



# print("Uma pizza de 20 cm de diâmetro deve custar: R$%.2f" % modelo.predict([20][0]))

# import numpy as np
# from sklearn.linear_model import LinearRegression

# x = np.array([[1, 1], [1, 2], [2, 2], [2, 3]])

# y = np.dot(x, np.array([1, 2])) + 3

# reg = LinearRegression().fit(x, y)

# # print(reg.score(x, y))
# print(reg.predict(np.array([[3, 5]])))