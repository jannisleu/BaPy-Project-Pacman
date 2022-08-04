import pygame
from ghost import Ghost
from constants import *

class GhostGroup:
    """Class to manage a group of Ghosts"""

    def __init__(self):
        """initialize the GhostGroup (see constants file)
        """
        self.ghosts = [Ghost(RED), Ghost(BLUE), Ghost(PINK), Ghost(GREEN), Ghost(PURPLE), Ghost(ORANGE)]

    def move(self, map):
        """move the whole group on the map

        Args:
            map (Map): Map object 
        """
        for i in self.ghosts:
            i.move(i.validDirections(map.map))

    def resetPosition(self):
        """reset the whole Group to the start position"""
        for i in self.ghosts:
            i.resetPosition()

    def render(self, screen):
        """render the whole group onto the screen"""
        for i in self.ghosts:
            i.render(screen)