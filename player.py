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
                    self.lost, grid, reward = self.game.getoutput(0)
                if(self.lost):
                    pygame.quit()
                    sys.exit()
                    return True
    def neuronplay(self):
        while True:
            action, _ = self.NN.predict(self.game.getgrid())
            self.game.setinput(action)
            self.lost, grid, reward = self.game.getoutput(100)
            if(self.lost):
                pygame.quit()
                sys.exit()
                return True
            