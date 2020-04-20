# Utilizando variaveis com tf
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

# Criando um grafo computacional - variavel
node = tf.Variable(tf.zeros([2,2]))

with tf.Session() as sess:

    # Obrigatoriamente é necessário inicializar as variaveis
    sess.run(tf.global_variables_initializer())

    print('Tensor original: ', sess.run(node))

    # Aicionado element-wise no tensor
    node = node.assign(node + tf.ones([2, 2]))

    # Noe alterado
    print('Tensor depois da adição: ', sess.run(node))
