# Construindo um modelo de regresão linear com Tensor Flow
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

# Definindo hyperparametros
# Para configurar o modelo
learning_Rate = 0.01
training_epochs = 2000
display_step = 200

# Dataset de treino
# Obs.: Considerar train_X = tamanho de casas e train_y = preço de casas
train_X = np.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_y = np.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]
 
# Dataset de teste
test_X = np.asarray([6.83, 4.668, 8.9, 7.91, 5.7, 8.7, 3.1, 2.1])
test_y = np.asarray([1.84, 2.273, 3.2, 2.831, 2.92, 3.24, 1.35, 1.03])

# Placeholders para as variáveis preditoras (X) e para  variável target (y)
X = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)
 
# Pesos e bias do modelo
W = tf.Variable(np.random.randn(), name="weight")
b = tf.Variable(np.random.randn(), name="bias")

# Construindo o modelo de regressão linear
# Formula: y = w*X + b
linear_model = W * X + b

# Calculo de erro
cost = tf.reduce_sum(tf.square(linear_model - y)) / (2*n_samples)

# Otimização com Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_Rate).minimize(cost)

# Iniciando as variaves
# init = tf.global_variable_initializer()

with tf.compat.v1.Session() as sess:
    # Iniciando as variaveis
    sess.run(tf.global_variables_initializer())
    # sess.run()

    # Treinando o modelo
    for epoch in range(training_epochs):

        # Otimização com Gradient Descent
        sess.run(optimizer, feed_dict={X: train_X, y:train_y})

        # Display de cada epoch
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, y: train_y})
            print("Epoch: {0:6} \t Cost:{1:10.4} \t W:{2:6.4} \t b:{3:6.4}".format(epoch+1, c, sess.run(W), sess.run(b)))

        # Imprimindo os paremostr finais do modelo
        print('\nOtimização Concluida')
        trainig_cost = sess.run(cost, feed_dict={X: train_X, y: train_y})
        print("Custo Final do Treinamento: ", trainig_cost, " - W final: ", sess.run(W), " - b final: ", sess.run(b), '\n')

        # Visualizando o resultado
        plt.plot(train_X, train_y, 'ro', label='Dados Originais')
        plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Linha de Regressão')
        plt.legend()
        plt.show()

        # Testando o modelo
        testing_cost = sess.run(tf.reduce_sum(tf.square(linear_model - y)) / (2 * test_X.shape[0]), feed_dict={X: test_X, y: test_y})

        print('Custo final em teste: ', testing_cost)
        print('Diferença Média Quadrada Absoluta: ', abs(trainig_cost - testing_cost))

        # Display em teste
        plt.plot(test_X, test_y, 'bo', label='Dado e teste')
        plt.plot(train_X, sess.run(W) * train_X + sess.run(b), label='Linha de REgressão')
        plt.legend()
        plt.show()

sess.close()
