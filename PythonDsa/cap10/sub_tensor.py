# Operações matematicas com tensor flow - subtração e divisão
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

print('---- Subtração ----')
print('')

rand_a = tf.random_normal([3], 2.0)
rand_b = tf.random_uniform([3], 1.0, 4.0)
# print(rand_a)
# print(rand_b)

# Para efetuar a subtração
diff = tf.subtract(rand_a, rand_b)

with tf.Session() as sess:
    print('Tenor rand_a: ', sess.run(rand_a))
    print('Tenor rand_b: ', sess.run(rand_b))
    print('')
    print('Subtração entre 2 tensores: ', sess.run(diff))


print('')
print('---- Divisão ----')
print('')

node1 = tf.constant(21, dtype=tf.int32)
node2 = tf.constant(7, dtype=tf.int32)

# Para efetuar a divisão
div = tf.div(node1, node2)

with tf.Session() as sess:
    print('Divisão entre os 2 tensores: ', sess.run(div))


    