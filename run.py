import pygame
from constants import *
from pacman import Pacman
from map import Map
from ghost import Ghost
from pygame.locals import (

    K_ESCAPE,
    QUIT,
    KEYDOWN
)

class Game:

    def __init__(self, level):
        """Create a Game object which manages the current game state

        Args:
            level (Textfile): Level that you want to play
        """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREENSIZE)
        self.background = pygame.surface.Surface(SCREENSIZE).convert()
        self.background.fill(BLACK)
        self.pacman = Pacman()
        self.ghost = Ghost(RED)
        self.map = Map(level, self.screen)

    def checkConditions(self):
        """Checks for certain keypresses to end the programm"""

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == QUIT:
                    exit()
                if event.key == K_ESCAPE:
                    exit()
        

    def render(self):
        """renders the object on the screen"""
        self.screen.blit(self.background, (0,0))
        self.map.render(self.screen)
        self.pacman.render(self.screen)
        self.ghost.render(self.screen)
        pygame.display.update()

    def update(self):
        """update the position etc. of our objects in the game"""
        self.clock.tick(30)
        direction = self.pacman.getDirection()
        col, row = self.pacman.position.asInt()
        if direction in self.pacman.validDirections(self.map.map):
            self.map.updateValues(int(row/TILESIZE), int(col/TILESIZE))
            self.pacman.move(direction)
        self.ghost.move(self.ghost.validDirections(self.map.map))
        self.render()
        self.checkConditions()

if __name__ == "__main__":
    #start game
    game = Game("1.txt")
    while True:
        game.update()
        