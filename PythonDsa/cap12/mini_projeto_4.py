# Mini-Projeto 4 - Modelo de deep learning
import os
import sys
import inspect
import numpy as np
# import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib as mat
# from modulos import utils
from datetime import datetime
from tensorflow.python.framework import ops
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_recall_fscore_support
import sklearn as sk
import warnings
import tensorflow.compat.v1 as tf

tf.compat.v1.disable_eager_execution()

warnings.filterwarnings('ignore')
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
ops.reset_default_graph()
np.random.seed(123456789)

FLAGS = tf.flags.FLAGS
tf.flags.DEFINE_string('data_dir', 'https://raw.githubusercontent.com/dsacademybr/PythonFundamentos/master/Cap12/dataset/', 'Caminho para diretorio de dados de treino e teste')
tf.flags.DEFINE_string('logs_dir', 'modelo/', 'Caminho para diretorio onde será gravado modelo')
tf.flags.DEFINE_string('mode', 'https://raw.githubusercontent.com/dsacademybr/PythonFundamentos/master/Cap12/dataset/train.csv', 'mode: train (efault)/ test')

# Hyperparametros
BATCH_SIZE = 128        # Tamanho do conjunto de dados de cada "passada"
LEARNING_RATE = 1e-3    # Vai definir como o gradiente será aplicado para os pesos
MAX_ITERATIONS = 1000   # Limite de iterações
REGULARIZATION = 1e-3
IMAGE_SIZE = 48         # Tamanho da imagem
NUM_LABELS = 7
VALIDATION_PERCENT = 7  # Percentual de validação
  
# Funções Auxiliares

def add_to_regularization_loss(W, b):
    tf.add_to_collection('lossess', tf.nn.l2_loss(W))
    tf.add_to_collection('lossess', tf.nn.l2_loss(b))

def weight_variable(shape, stddev=0.02, name=None):
    initial = tf.truncated_normal(shape, stddev=stddev)
    if name is None:
        return tf.Variable(initial)
    else:
        return tf.get_variable(name, initializer=initial)

def bias_variable(shape, name=None):
    initial = tf.constant(0.0, shape=shape)
    if name is None:
        return tf.Variable(initial)
    else:
        return tf.get_variable(name, initializer=initial)

def emotionCNN(dataset):
    
    # Camada de Convolução 1
    with tf.name_scope("conv1") as scope:
        tf.summary.histogram("W_conv1", weights['wc1'])
        tf.summary.histogram("b_conv1", biases['bc1'])
        conv_1 = tf.nn.conv2d(dataset, weights['wc1'], strides=[1, 1, 1, 1], padding="SAME")
        h_conv1 = tf.nn.bias_add(conv_1, biases['bc1'])
        h_1 = tf.nn.relu(h_conv1)
        h_pool1 = tf.nn.max_pool(h_1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
        add_to_regularization_loss(weights['wc1'], biases['bc1'])

    # Camada de Convolução 2
    with tf.name_scope("conv2") as scope:
        tf.summary.histogram("W_conv2", weights['wc2'])
        tf.summary.histogram("b_conv2", biases['bc2'])
        conv_2 = tf.nn.conv2d(h_pool1, weights['wc2'], strides=[1, 1, 1, 1], padding="SAME")
        h_conv2 = tf.nn.bias_add(conv_2, biases['bc2'])
        h_2 = tf.nn.relu(h_conv2)
        h_pool2 = tf.nn.max_pool(h_2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")
        add_to_regularization_loss(weights['wc2'], biases['bc2'])

    # Camada Totalmente Conectada 1
    with tf.name_scope("fc_1") as scope:
        prob = 0.5
        image_size = IMAGE_SIZE // 4
        h_flat = tf.reshape(h_pool2, [-1, image_size * image_size * 64])
        tf.summary.histogram("W_fc1", weights['wf1'])
        tf.summary.histogram("b_fc1", biases['bf1'])
        h_fc1 = tf.nn.relu(tf.matmul(h_flat, weights['wf1']) + biases['bf1'])
        h_fc1_dropout = tf.nn.dropout(h_fc1, prob)
        
    # Camada Totalmente Conectada 2
    with tf.name_scope("fc_2") as scope:
        tf.summary.histogram("W_fc2", weights['wf2'])
        tf.summary.histogram("b_fc2", biases['bf2'])
        pred = tf.matmul(h_fc1_dropout, weights['wf2']) + biases['bf2']

    return pred


#  Pesos e Bias do Modelo
weights = {
    'wc1': weight_variable([5, 5, 1, 32], name="W_conv1"),
    'wc2': weight_variable([3, 3, 32, 64],name="W_conv2"),
    'wf1': weight_variable([int((IMAGE_SIZE // 4) * (IMAGE_SIZE // 4)) * 64, 256],name="W_fc1"),
    'wf2': weight_variable([256, NUM_LABELS], name="W_fc2")
}

biases = {
    'bc1': bias_variable([32], name="b_conv1"),
    'bc2': bias_variable([64], name="b_conv2"),
    'bf1': bias_variable([256], name="b_fc1"),
    'bf2': bias_variable([NUM_LABELS], name="b_fc2")
}    

def loss(pred, label):
    cross_entropy_loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=pred, labels=label))
    tf.summary.scalar('Entropy', cross_entropy_loss)
    reg_losses = tf.add_n(tf.get_collection("losses"))
    tf.summary.scalar('Reg_loss', reg_losses)
    return cross_entropy_loss + REGULARIZATION * reg_losses

def train(loss, step):
    return tf.train.AdamOptimizer(LEARNING_RATE).minimize(loss, global_step=step)

def get_next_batch(images, labels, step):
    offset = (step * BATCH_SIZE) % (images.shape[0] - BATCH_SIZE)
    batch_images = images[offset: offset + BATCH_SIZE]
    batch_labels = labels[offset:offset + BATCH_SIZE]
    return batch_images, batch_labels

# Listas para resultados de treinamento
train_error_list = []
train_step_list = []

# Listas para resultados de validação
valid_error_list = []
valid_step_list = []


def main(argv=None):
    
    # Carrega os dados
    train_images, train_labels, valid_images, valid_labels, test_images = utils.read_data(FLAGS.data_dir)
    
    print("\nTamanho do Dataset de Treino: %s" % train_images.shape[0])
    print('Tamanho do Dataset de Validação: %s' % valid_images.shape[0])
    print("Tamanho do Dataset de Teste: %s" % test_images.shape[0])

    global_step = tf.Variable(0, trainable=False)
    dropout_prob = tf.placeholder(tf.float32)
    input_dataset = tf.placeholder(tf.float32, [None, IMAGE_SIZE, IMAGE_SIZE, 1], name="input")
    input_labels = tf.placeholder(tf.float32, [None, NUM_LABELS])

    pred = emotionCNN(input_dataset)
    output_pred = tf.nn.softmax(pred, name="output")
    loss_val = loss(pred, input_labels)
    train_op = train(loss_val, global_step)

    summary_op = tf.summary.merge_all()
    init_op = tf.global_variables_initializer()

    with tf.Session() as sess:
        sess.run(init_op)
        summary_writer = tf.summary.FileWriter(FLAGS.logs_dir, sess.graph)
        saver = tf.train.Saver()
        ckpt = tf.train.get_checkpoint_state(FLAGS.logs_dir)
        if ckpt and ckpt.model_checkpoint_path:
            saver.restore(sess, ckpt.model_checkpoint_path)
            print("Modelo Restaurado!")

        for step in range(MAX_ITERATIONS):
            batch_image, batch_label = get_next_batch(train_images, train_labels, step)
            feed_dict = {input_dataset: batch_image, input_labels: batch_label}

            sess.run(train_op, feed_dict=feed_dict)
            if step % 10 == 0:
                train_loss, summary_str = sess.run([loss_val, summary_op], feed_dict=feed_dict)
                summary_writer.add_summary(summary_str, global_step=step)
                train_error_list.append(train_loss)
                train_step_list.append(step)
                print("Taxa de Erro no Treinamento: %f" % train_loss)

            if step % 100 == 0:
                valid_loss = sess.run(loss_val, feed_dict={input_dataset: valid_images, input_labels: valid_labels})
                valid_error_list.append(valid_loss)
                valid_step_list.append(step)
                print("%s Taxa de Erro na Validação: %f" % (datetime.now(), valid_loss))
                saver.save(sess, FLAGS.logs_dir + 'model.ckpt', global_step=step)
        
        # Plot do erro durante o treinamento
        plt.plot(train_step_list, train_error_list, 'r--', label='Erro no Treinamento Por Iteração', linewidth=4)
        plt.title('Erro no Treinamento Por Iteração')
        plt.xlabel('Iteração')
        plt.ylabel('Erro no Treinamento')
        plt.legend(loc='upper right')
        plt.show()

        # Plot do erro durante a validação
        plt.plot(valid_step_list, valid_error_list, 'r--', label='Erro na Validação Por Iteração', linewidth=4)
        plt.title('Erro na Validação Por Iteração')
        plt.xlabel('Iteração')
        plt.ylabel('Erro na Validação')
        plt.legend(loc='upper right')
        plt.show()  

print(train_error_list) 
print(valid_error_list)

if __name__ == "__main__":
    tf.app.run()
    print("Treinanento concluído")
