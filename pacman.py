from constants import *
import pygame
import numpy as np
from vector import Vector
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_UP
)

class Pacman:
    """Class for a Pacman object"""

    def __init__(self):
        """Create a Pacman"""
        self.position = Vector(9*TILESIZE, 16*TILESIZE)
        self.directions = {STOP: Vector(), UP: Vector(0, -1), DOWN: Vector(0, 1), LEFT: Vector(-1, 0), RIGHT: Vector(1, 0)}
        self.direction = STOP
        self.speed = 1
        self.radius = 10
        self.color = YELLOW
        self.name = PACMAN

    def getDirection(self):
        """get direction after pressing a key

        Returns:
            constant: one of the directions of the self.directions dictionary
        """
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            return LEFT 
        if keys[K_RIGHT]:
            return RIGHT
        if keys[K_UP]:
            return UP
        if keys[K_DOWN]:
            return DOWN
        return STOP

    def move(self, direction):
        """Moves the pacman

        Args:
            direction (key): key for the self.directions dictionary
        """
        self.position += self.directions[self.direction]*self.speed
        self.direction = direction
        print(self.position)

    def render(self, screen):
        """Render Pacman onto the screen

        Args:
            screen (Surface): pygame surface 
        """
        x, y = self.position.asInt()
        pygame.draw.circle(screen, YELLOW, (x + 12.5, y + 12.5), self.radius)