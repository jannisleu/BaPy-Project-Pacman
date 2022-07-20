import pygame
from vector import Vector
from constants import *
import random as rand

class Ghost:

    def __init__(self, name):
        self.position = Vector(10*TILESIZE, 12*TILESIZE)
        self.directions = {STOP: Vector(), UP: Vector(0, -1), DOWN: Vector(0, 1), LEFT: Vector(-1, 0), RIGHT: Vector(1, 0)}
        self.direction = STOP
        self.speed = 1
        self.radius = 10
        self.name = name

    def move(self, directions):
    
        self.direction = rand.choice(directions)
        self.position += self.directions[self.direction]*self.speed

    def validDirections(self, map):
        """Check surrounding fields whether they are valid for the next move

        Args:
            row (int): row of the maze array(from the current position)
            col (int): column of the maze array(from the current position)

        Returns:
            _list: list of valid directions for the next step
        """

        col, row = self.position.asInt()
        if col % TILESIZE == 0 and row % TILESIZE == 0:
            col = int(col/TILESIZE)
            row = int(row/TILESIZE)
            valid = [STOP]
            if map[row][col - 1] != 0:
                valid.append(LEFT)
            if map[row][col + 1] != 0:
                valid.append(RIGHT)
            if map[row - 1][col] != 0:
                valid.append(UP)
            if map[row + 1][col] != 0:
                valid.append(DOWN)
            return valid
        valid = [self.direction]
        return valid

    def render(self, screen):
        """Render Pacman onto the screen

        Args:
            screen (Surface): pygame surface 
        """
        x, y = self.position.asInt()
        pygame.draw.circle(screen, WHITE, (x + 12.5, y + 12.5), self.radius)
        screen.blit(self.name, (x, y))