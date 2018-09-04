from neuronalnet import NN
from gamemanagement import gamemanagement
import pygame
import sys
import numpy as np
from pygame.locals import *

class Player():
    def __init__(self, neuronalnet):
        self.NN = neuronalnet
        self.game = gamemanagement()
        self.lost = 0
    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN and (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT) :
                    self.game.setinput(event.key)
                    i , j = np.where(self.game.getgrid() == 0)
                    print(i)
                    print(j)
                    #weights1 = np.random.rand(16,1)
                    #weights2 = np.random.rand(1,3)
                    #weights3 = np.random.rand(3,4)
                    #self.NN.setweights(weights1, weights2, weights3)
                    #w1,w2,w3 = self.NN.getweights()
                        
                    #action, _ = neuronalnet.predict(game.getgrid())
                    #game.takeinput(action)
                    self.lost, grid, reward = self.game.getoutput(0)
                if(self.lost):
                    print("lost")
                    print(self.game.getgrid())
                    pygame.quit()
                    sys.exit()
                    return True