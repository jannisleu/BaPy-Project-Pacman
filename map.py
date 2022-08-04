from constants import *
import numpy as np

class Map:
    """Class for a Map which contains the layout for the pacman maze"""

    def __init__(self, level, screen):
        """Create map object

        Args:
            level (textfile): textfile which contains the structure of the maze
            screen (Surface): pygame surface
        """
        self.level = level
        self.screen = screen
        self.map = self.loadLevel(level)
        self.createBoard(self.map, screen)

    def loadLevel(self, level):
        """Loads level textfile into a numpy array

        Args:
            level (textfile): textfile which contains the structure of the maze

        Returns:
            np.array: numpy array of the maze
        """
        return np.loadtxt(level, dtype = int)

    def createBoard(self, data, screen): 
        """Create and update the maze/board

        Args:
            data (numpy array): maze
            screen (Surface): pygame surface
        """
        rows,cols = np.shape(data)
        for j in range(cols):
            for i in range(rows):
                if data[i][j] == 0:
                    screen.blit(BRICK, (j*TILESIZE,i*TILESIZE))
                if data[i][j] == 1:
                    screen.blit(COIN, (j*TILESIZE,i*TILESIZE))
                if data[i][j] == 2:
                    screen.blit(BLANK, (j*TILESIZE,i*TILESIZE))
            
    def checkCoins(self):
        """check if there are still coins on the map

        Returns:
            bool: true if there are still coins
        """

        for j in range(WIDTH):
            for i in range(HEIGHT):
                if self.map[i][j] == 1:
                    return True
        return False

    def updateValues(self, row, col):
        """update a point in the maze

        Args:
            row (int): row of the maze array(from the current position)
            col (int): column of the maze array(from the current position)
        """
        self.map[row][col] = 2
        

    def render(self, screen):
        """Render map onto the screen

        Args:
            screen (Surface): pygame surface
        """
        self.createBoard(self.map, screen)





    

