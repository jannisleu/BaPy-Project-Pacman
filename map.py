from constants import *
import numpy as np

class Map:

    def __init__(self, level):
        self.level = level
        self.map = self.loadLevel(level)

    def loadLevel(self, textfile):
        return np.loadtxt(textfile, dtype = int)

    
map = Map("1.txt")
print(map.map)

