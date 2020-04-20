# Operações matematicas com tensor flow - adição
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

# Criando tensores de rank 0
const_a = tf.constant(5)
const_b = tf.constant(9)

# Obs.: Repare que o shape está () que significa o rank do tensor
# print(const_a)

# Efetuando uma soma
total = const_a + const_b

# Por enquanto está só criando um grafo... é a definição da operação e não a execução 
# print(total)

# Sessão TF
# with tf.Session() as sess:
#     print('\nA soma do no 1 com o no 1 é %i' % sess.run(total))
    

# ---- Outra Forma ----

# Utilizando a própria função add do tensorflow para fazer a adição
node1 = tf.constant(5, dtype=tf.int32) 
node2 = tf.constant(9, dtype=tf.int32)
node3 = tf.add(node1, node2)

# Criar a sessão TF
sess = tf.Session()

# Executar
print('A soma do node1 + node2 = ', sess.run(node3))

# Fechar a sessão
sess.close()