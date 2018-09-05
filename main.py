from gamemanagement import gamemanagement
import numpy as np
from neuronalnet import NN
import tensorflow as tf
from collections import deque
import time
import random
import deap
from player import Player


def main():
    neuronalnet = NN()
    weights1 = np.random.rand(16,1)
    weights2 = np.random.rand(1,3)
    weights3 = np.random.rand(3,4)
    neuronalnet.setweights(weights1, weights2, weights3)
    player = Player(neuronalnet)
    #w1,w2,w3 = player.NN.getweights()
    #print(weights1)
    #print(w1)
    #print("---")
    #print(weights2)
    #print(w2)
    #print("---")
    #print(weights3)
    #print(w3)
    #print("---")
    player.play()
    #player.neuronplay()
if __name__ == '__main__':
    main()
    
    
        



