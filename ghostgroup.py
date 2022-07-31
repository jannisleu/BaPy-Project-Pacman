import pygame
from ghost import Ghost
from constants import *

class GhostGroup:

    def __init__(self):
        self.ghosts = [Ghost(RED), Ghost(BLUE), Ghost(PINK), Ghost(GREEN), Ghost(PURPLE), Ghost(ORANGE)]

    def move(self, map):
        for i in self.ghosts:
            i.move(i.validDirections(map.map))

    def resetPosition(self):
        for i in self.ghosts:
            i.resetPosition()

    def render(self, screen):
        for i in self.ghosts:
            i.render(screen)