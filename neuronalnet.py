import tensorflow as tf
import numpy as np
from numpy import int32
from tensorflow.examples.tutorials.mnist.mnist import loss

class NN():
    
    def __init__(self):
        np.random.seed(123)
        self.g = tf.Graph()
        with self.g.as_default():
            self.w_1 = tf.get_variable("w_1", shape=[16, 1],
                                       initializer=tf.contrib.layers.xavier_initializer())
            self.w_2 = tf.get_variable("w_2", shape=[1, 3],
                                      initializer=tf.contrib.layers.xavier_initializer())
            self.w_3 = tf.get_variable("w_3", shape=[3, 4],
                                      initializer=tf.contrib.layers.xavier_initializer())
            self.entry = tf.placeholder("float", shape = [1,16])
            self.output_target = tf.placeholder("float", shape = [1,4])
            
            self.yhat = self.forwardprop(self.entry, self.w_1, self.w_2, self.w_3)
            self.prediction = tf.argmax(self.yhat, axis = 1)
            self.cost = tf.reduce_sum(tf.square(self.output_target-self.yhat))
            self.trainer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
            self.updateModel = self.trainer.minimize(loss=self.cost)
            self.init = tf.global_variables_initializer()
        self.sess = tf.Session(graph = self.g)
        self.sess.run(self.init)

    def predict(self, grid):
        feed = {self.entry: grid.reshape((1,16))}
        action, Q_Values = self.sess.run([self.prediction, self.yhat], feed_dict = feed)
        return action, Q_Values
    
    def forwardprop(self,X, w_1, w_2, w_3):
        h1 = tf.nn.sigmoid(tf.matmul(X, w_1))
        h2 = tf.nn.sigmoid(tf.matmul(h1, w_2))
        yhat = tf.matmul(h2, w_3)
        return yhat
    
    def train(self, grid, target):
        feed = {self.entry: grid.reshape((1,16)), self.output_target: target}
        self.sess.run([self.updateModel, self.w_1, self.w_2], feed_dict = feed)
        
    def setweights(self, wL_1, wL_2, wL_3):
        with self.g.as_default():
            self.w_1 = tf.assign(self.w_1,wL_1, validate_shape = True)
            self.w_2 = tf.assign(self.w_2,wL_2, validate_shape = True)
            self.w_3 = tf.assign(self.w_3,wL_3, validate_shape = True)
            self.init = tf.global_variables_initializer()
        self.sess = tf.Session(graph = self.g)
        self.sess.run(self.init)
          
    def getweights(self):
        return self.sess.run(self.w_1) , self.sess.run(self.w_2) ,self.sess.run(self.w_3)