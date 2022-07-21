import pygame
from ghost import Ghost
from constants import *

class GhostGroup:

    def __init__(self):
        self.red = Ghost(RED)
        self.blue = Ghost(BLUE)
        self.pink = Ghost(PINK)
        self.green = Ghost(GREEN)
        self.purple = Ghost(PURPLE)
        self.orange = Ghost(ORANGE)
        self.group = [self.red, self.blue, self.pink, self.green, self.purple, self.orange]

    def move(self, map):
        for i in self.group:
            i.move(i.validDirections(map.map))

    def render(self, screen):
        for i in self.group:
            i.render(screen)