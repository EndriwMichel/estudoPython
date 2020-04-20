# Operações matematicas com tensor flow - multiplicação
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

tensor_a = tf.constant([[4., 2.]])
tensor_b = tf.constant([[3.], [7.]])
# tensor_b = tf.constant([[3.], [7.]])
# print(tensor_a)
# print(tensor_b)

# Efetua multiplicação
prod = tf.multiply(tensor_a, tensor_b)

with tf.Session() as sess:
    print('Tensor_a: ', sess.run(tensor_a))
    print('Tensor_b: ', sess.run(tensor_b))
    print('Produto Element-wise entre tensores: ', sess.run(prod))


print('')
print('Outro exemplo de multiplicação')
print('')

mat_a = tf.constant([[2, 3], [9, 2], [4, 5]])
mat_b = tf.constant([[6, 4, 5], [3, 7, 2]])
# print(mat_a)
# print(mat_b)

# Multiplicação de multiplas matrizes
mat_prod = tf.matmul(mat_a, mat_b)

with tf.Session() as sess:
    print('Tensor mat_a: ', sess.run(mat_a))
    print('Tensor mat_b: ', sess.run(mat_b))
    print('Produto Element-wise entre tensores (matrizes): ', sess.run(mat_prod))