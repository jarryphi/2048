import font
import pygame
from pygame.locals import *
from font import text_to_screen

class visualization():
    def __init__(self, grid):
        self.screenwidth = 420
        self.screenheight = 510
        pygame.init()
        pygame.display.set_caption('2048')
        self.screen = pygame.display.set_mode((self.screenwidth, self.screenheight))    
        self.screen.fill((209,238,238))
        text_to_screen(self.screen, 'Score:' , 100, 440, 30, (0,0,0))
        pygame.font.init()
        self.printgrid(grid)
        pygame.display.update()
    def printgrid(self, grid):
        posx = 10
        posy = 10
        for i in range(0,4):
            for j in range(0,4):
                score = int(grid[i][j])
                self.printrectbyscore(score, posx, posy)
                posx += 10
                posy +=30
                if score != 0:
                    text_to_screen(self.screen, score , posx, posy, 30, (255,255,255))
                posx += 90
                posy -= 30
            posx = 10
            posy += 100
        pygame.display.update() 
    def printrectbyscore(self,score, posx, posy):
        if (score == 0):
            color = (135,206,250)
        else:
            color = (98, 0, 0)    
        self.screen.fill(color,pygame.draw.rect(self.screen,(0,0,0), (posx,posy,100,100), 4))
        pygame.draw.rect(self.screen,(0,0,0), (posx,posy,100,100), 4)