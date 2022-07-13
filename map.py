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
        for rows in range(data.shape[0]):
            for cols in range(data.shape[1]):
                if data[rows][cols] == 0:
                    screen.blit(BRICK, (rows, cols))

    def render(self, screen):
        self.createBoard(self.map, screen)

#map = Map("1.txt", )




    

