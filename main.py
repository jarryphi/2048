from gamemanagement import gamemanagement
import numpy as np
from neuronalnet import NN
import tensorflow as tf
from collections import deque
import time
import pygame
from pygame.locals import *
import sys

def main():
    game = gamemanagement()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT) :
                game.takeinput(event.key)
            if(game.checkloss() or game.checklossbychangedcounter):
                pygame.quit()
                sys.exit
if __name__ == '__main__':
    main()
    
    
        



