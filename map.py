from constants import *
import numpy as np

class Map:

    def __init__(self, level, screen):
        self.level = level
        self.screen = screen
        self.map = self.loadLevel(level)
        self.createBoard(self.map, screen)

    def loadLevel(self, level):
        return np.loadtxt(level, dtype = int)

    def createBoard(self, data, screen): 
        rows,cols = np.shape(data)
        for j in range(cols):
            for i in range(rows):
                if data[i][j] == 0:
                    screen.blit(BRICK, (j*25,i*25))
                if data[i][j] == 1:
                    screen.blit(COIN, (j*25,i*25))
                if data[i][j] == 2:
                    screen.blit(BLANK, (j*25,i*25))
            
            


    def render(self, screen):
        self.createBoard(self.map, screen)

#map = Map("1.txt", )




    

