import pygame
from vector import Vector
from constants import *
import random as rand

class Ghost:
    """Class for one Ghost object"""

    def __init__(self, name):
        """initialize a ghost

        Args:
            name (constant): the image of the ghost(look in the constants file)
        """
        self.position = Vector(10*TILESIZE, 12*TILESIZE)
        self.directions = {STOP: Vector(), UP: Vector(0, -1), DOWN: Vector(0, 1), LEFT: Vector(-1, 0), RIGHT: Vector(1, 0)}
        self.direction = STOP
        self.speed = SPEED
        self.radius = 10
        self.name = name

    def move(self, directions):
        """moves the ghost 

        Args:
            directions (list): list of valid directions
        """
        #random movement into a valid direction
        self.direction = rand.choice(directions)
        self.position += self.directions[self.direction]*self.speed

    def validDirections(self, map):
        """Check surrounding fields whether they are valid for the next move

        Args:
            map (np array): array which contains the current map state

        Returns:
            list: list of valid directions for the next step
        """

        col, row = self.position.asInt()
        #check if we are exactly at an entry of our map array(not in between of two entries)
        if col % TILESIZE == 0 and row % TILESIZE == 0:
            col = int(col/TILESIZE)
            row = int(row/TILESIZE)
            valid = [STOP]
            #check every entry around the current one 
            if map[row][col - 1] != 0:
                valid.append(LEFT)
            if map[row][col + 1] != 0:
                valid.append(RIGHT)
            if map[row - 1][col] != 0:
                valid.append(UP)
            if map[row + 1][col] != 0:
                valid.append(DOWN)
            return valid
        #if we are not at a position where we can change direction(between two array entries): we move on
        valid = [self.direction]
        return valid

    def resetPosition(self):
        """reset to start position"""
        self.position = Vector(10*TILESIZE, 12*TILESIZE)

    def render(self, screen):
        """Render Ghost onto the screen

        Args:
            screen (Surface): pygame surface 
        """
        x, y = self.position.asInt()
        pygame.draw.circle(screen, BLACK, (x + 12.5, y + 12.5), self.radius)
        screen.blit(self.name, (x, y))