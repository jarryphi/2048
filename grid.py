import numpy as np
import random
import pygame
from pygame.locals import *
from pygame.constants import KEYDOWN, K_RIGHT
import math

pygame.init()

class grid():
    
    def __init__(self):
        self.gridoccupied = np.zeros((4,4))
        self.grid = np.zeros((4,4))
        self.changed = 1;
        self.reward = 0
        for i in range(0,2):
            pos = self.generaterand()
            rand = np.random.choice([2,4])
            if not self.gridoccupied[pos[0],pos[1]]:
                self.grid[pos[0]][pos[1]] = rand
                self.gridoccupied[pos[0]][pos[1]] = 1         
    def addrand(self):
        pos = self.generaterand()
        if self.gridoccupied[pos[0],pos[1]]==1:
            self.addrand()
        else:
            self.grid[pos[0]][pos[1]] = 2
            self.gridoccupied[pos[0]][pos[1]] = 1
      
    def generaterand(self):
        
        randx = random.randint(0,3)
        randy = random.randint(0,3)
        rand = np.array([randx, randy])
     
        return rand
        
    def checkchanged(self):
        return self.changed
    
    def losshandler(self,key):
        numbercount = 0;
        if (key == K_RIGHT or key == K_LEFT):
            for i in range(0,4):
                line = self.grid[i,:]
                line = self.shrinkline(line)
                numbercount += np.size(line)
        else:
            for i in range(0,4):
                line = self.grid[:,i]
                line = self.shrinkline(line)
                numbercount += np.size(line)
        return (numbercount == 16)
    
    def normalizegrid(self):
        return np.where(np.log2(self.grid) < 0, 0, np.log2(self.grid))
        
        
    def keyevent(self,key):
        self.changed = 0;
        if (key == K_RIGHT or key == K_LEFT):
            for i in range(0,4):
                line = self.grid[i,:]
                refline = line
                line = self.shrinkline(line)
                if(key == K_RIGHT):
                    line = np.pad(line,(4-np.size(line),0),'constant', constant_values = 0)
                else:
                    line = np.pad(line,(0,4-np.size(line)),'constant', constant_values = 0)
                if (np.array_equal(refline,line) == False):
                    self.changed = 1                
                self.grid[i,:] = line
                line[line > 0] = 1
                self.gridoccupied[i,:] = line

        else:
            for i in range(0,4):
                row = self.grid[:,i]
                refrow = row
                row = self.shrinkline(row)
                if(key == K_UP):
                    row = np.pad(row,(0,4-np.size(row)),'constant', constant_values = 0)
                else:
                    row = np.pad(row,(4-np.size(row),0),'constant', constant_values = 0)
                if (np.array_equal(refrow,row) == False):
                    self.changed = 1
                self.grid[:,i] = row
                row[row > 0] = 1
                self.gridoccupied[:,i] = row
        if(self.changed):
            self.addrand()
    def summelements(self, arr):
        l = 0
        result = []
        while( l < np.size(arr)):
            if(l != np.size(arr)-1 and arr[l]==arr[l+1]):
                result = np.append(result, arr[l]*2)
                self.reward +=arr[l]
                l += 2
            elif (l != np.size(arr)-1):
                result = np.append(result, arr[l])
                l += 1
            else:
                result = np.append(result, arr[l])
                l += 1

        return result
    def shrinkline(self, line):
        line = line[line !=0]
        resultline = self.summelements(line)
        return  resultline