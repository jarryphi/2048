from gamemanagement import gamemanagement
import numpy as np
from neuronalnet import NN
import tensorflow as tf
from collections import deque
import time

from player import Player
def main():
    neuronalnet = NN()
    player = Player(neuronalnet)
    player.play()
if __name__ == '__main__':
    main()
    
    
        



