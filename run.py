import pygame
from constants import *
from pacman import Pacman
from map import Map
from pygame.locals import (

    K_ESCAPE,
    QUIT,
    KEYDOWN
)

class Game:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.clock.tick(30)
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)
        self.pacman = Pacman()
        self.map = Map("1.txt", self.screen)

    def checkConditions(self):

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == QUIT:
                    exit()
                if event.key == K_ESCAPE:
                    exit()
        

    def render(self):
        self.screen.blit(self.background, (0,0))
        self.map.render(self.screen)
        self.pacman.render(self.screen)
        pygame.display.update()

    def update(self):
        self.pacman.move()
        self.render()
        self.checkConditions()

if __name__ == "__main__":
    game = Game()
    while True:
        game.update()
        