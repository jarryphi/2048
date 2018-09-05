import numpy as np
import random
import pygame
from pygame.locals import *
from pygame.constants import KEYDOWN, K_RIGHT
import math

pygame.init()

class grid():
    
    def __init__(self):
        self.grid = np.zeros((4,4))
        self.changed = 1;
        self.reward = 0
        self.indrow, self.indcolumn = np.where(self.grid == 0)
        for i in range(0,2):
            pos = self.generaterand()
            rand = np.random.choice([2,4])
            self.grid[pos[0]][pos[1]] = rand         
    def addrand(self):
        pos = self.generaterand()
        self.grid[pos[0]][pos[1]] = 2
      
    def generaterand(self):
        index = random.randint(0,np.size(self.indrow)-1)
        rand = np.array([self.indrow[index], self.indcolumn[index]])
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
        self.indrow = []
        self.indcolumn = []
        if (key == K_RIGHT or key == K_LEFT):
            for i in range(0,4):
                row = self.grid[i,:]
                refrow = row
                row = self.shrinkline(row)
                if(key == K_RIGHT):
                    for j in range(0,4-np.size(row)):
                        self.indrow.append(i)
                        self.indcolumn.append(j)
                    row = np.pad(row,(4-np.size(row),0),'constant', constant_values = 0)
                else:
                    for j in range(0,4-np.size(row)):
                        self.indrow.append(i)
                        self.indcolumn.append(np.size(row)+j)
                    row = np.pad(row,(0,4-np.size(row)),'constant', constant_values = 0)                    
                if (np.array_equal(refrow,row) == False):
                    self.changed = 1                
                self.grid[i,:] = row

        else:
            for i in range(0,4):
                column = self.grid[:,i]
                refcolumn = column
                column = self.shrinkline(column)
                if(key == K_UP):
                    for j in range(0,4-np.size(column)):
                        self.indrow.append(np.size(column)+j)
                        self.indcolumn.append(i)
                    column = np.pad(column,(0,4-np.size(column)),'constant', constant_values = 0)
                else:
                    for j in range(0,4-np.size(column)):
                        self.indrow.append(j)
                        self.indcolumn.append(i)
                    column = np.pad(column,(4-np.size(column),0),'constant', constant_values = 0)
                if (np.array_equal(refcolumn,column) == False):
                    self.changed = 1
                self.grid[:,i] = column
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