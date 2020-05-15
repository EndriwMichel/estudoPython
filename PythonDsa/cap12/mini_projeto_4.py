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
