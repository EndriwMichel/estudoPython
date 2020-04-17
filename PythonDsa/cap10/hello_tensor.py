# Hello TensorFlow, primeiro código de execução de um TensorFlow
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

# Visualizar a versão
print(tf.__version__)

# Crar um tensor
# Este tensor é adicionado a um nó no grafo
hello = tf.constant('Hello TensorFlWord')
print(hello)
print('')

# Iniciar a sessão tensorflow
sess = tf.Session()
print(sess)
print('')
# Executa o grafo computacional
print(sess.run(hello))