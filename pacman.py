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
        self.directions = {STOP: Vector(), UP: Vector(0, -1), DOWN: Vector(0, 1), LEFT: Vector(-1, 0), RIGHT: Vector(1, 0)}
        self.direction = STOP
        self.speed = 0.1
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
        return STOP

    def move(self):
        self.position += self.directions[self.direction]*self.speed 
        self.direction = self.getDirection()


    def render(self, screen):
        p = self.position.asInt()
        pygame.draw.circle(screen, YELLOW, p, self.radius)