from constants import *
import pygame
from vector import Vector
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_UP
)

class Pacman:

    def __init__(self):
        self.position = Vector(200, 200)
        self.direction = STOP
        self.radius = 10
        self.color = YELLOW
        self.name = PACMAN

    def getDirection(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT]:
            return LEFT 
        if keys[K_RIGHT]:
            return RIGHT
        if keys[K_UP]:
            return UP
        if keys[K_DOWN]:
            return DOWN

        def move(self):
            pass


    def render(self, screen):
        pygame.draw.circle(screen, YELLOW, self.position, self.radius)