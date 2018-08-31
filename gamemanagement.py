from itertools import cycle
import sys
from grid import grid
import math
import numpy as np
import pygame
from pygame.locals import *
from pygame.constants import KEYDOWN, K_RIGHT
from visualization import visualization


class gamemanagement():
    def __init__(self):
        self.grid = grid()
        self.__vis = visualization(self.grid.grid)
        self.changedcounter = 0
        self.iteration_counter = 0
        self.reward_in = 0
        self.filled_before= np.count_nonzero(self.grid.grid)
    def takeinput(self, action):
        if (action == 0 or action == K_LEFT):
            key = K_LEFT
            self.progressgame(key)
        elif (action == 1 or action == K_UP):
            key = K_UP
            self.progressgame(key)
        elif (action == 2 or action == K_RIGHT):
            key = K_RIGHT
            self.progressgame(key)
        elif (action == 3 or action == K_DOWN):
            key = K_DOWN
            self.progressgame(key)
        self.printgrid()  
        return self.calculatereward()
    def checkloss(self):
        lost = 0
        if (np.count_nonzero(self.grid) == 16):
            lost = max(lost, self.grid.losshandler(K_LEFT))
            lost = max(lost, self.grid.losshandler(K_RIGHT))
            lost = max(lost, self.grid.losshandler(K_UP))
            lost = max(lost, self.grid.losshandler(K_DOWN))
        if lost:
            return True
        else:
            return False
    def checklossbychangedcounter(self):
        lost = 0
        if (self.changedcounter == 10):
            lost = 1
        if lost:
            return True
        else:
            return False
        
    def getgrid(self):
        return self.grid.grid
    
    def getreward(self):
        return self.calculatereward()

    def progressgame(self,key):
        self.checkloss()
        self.grid.keyevent(key)
        if(self.grid.checkchanged()):  
            self.changedcounter +=0
        else:
            self.changedcounter +=1
        
    def calculatereward(self):
        
        if (self.iteration_counter%5 == 0):
            actual_reward = self.grid.reward*5
            if(self.grid.checkchanged() == False):
                actual_reward += -2
            self.grid.reward = 0
            self.iteration_counter = 1
            return actual_reward
        else:
            self.filled_before = np.sum(self.grid.gridoccupied)
            self.iteration_counter +=1
            if(self.grid.checkchanged() == False):    
                return -2
            else:
                return 0
    def printgrid(self):
        self.__vis.printgrid(self.grid.grid)