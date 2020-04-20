# Utilizando placeholders com tf
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

# Criando os nodes de grafo computacional
a = tf.placeholder(tf.int32 , shape=(3, 1))
b = tf.placeholder(tf.int32 , shape=(1, 3))
c = tf.matmul(a, b)

with tf.Session() as sess:
    # feed_dict = dicionario de alimentacao, usado para alimentar os valores dos placeholders
    print(sess.run(c, feed_dict={a: [[3], [2], [1]], b:[[3, 2, 1]]}))
    