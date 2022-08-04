from time import sleep
import pygame
from constants import *
from ghostgroup import GhostGroup
from pacman import Pacman
from map import Map
from pygame.locals import (

    K_ESCAPE,
    QUIT,
    KEYDOWN
)

class Game:
    """class which contains the main game loop and manages the game state"""

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
        self.font = pygame.font.Font(pygame.font.get_default_font(), 36)
        self.pacman = Pacman()
        self.ghosts = GhostGroup()
        self.map = Map(level, self.screen)

    def checkConditions(self):
        """Checks for certain keypresses to end the programm"""

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == QUIT:
                    exit()
                if event.key == K_ESCAPE:
                    exit()

        #check whether all coins are collected and print a message 
        if self.map.checkCoins() == False:
            text = self.font.render("You Won!", True,  BLACK)
            pygame.draw.rect(self.screen, WHITE, (SCREENWIDTH/3, SCREENHEIGHT/2 - 7.5, 165, 50))
            self.screen.blit(text, (SCREENWIDTH/3, SCREENHEIGHT/2))
            pygame.display.update()
            sleep(5)
            exit()
        

        #check for collision and if pacman is still alive
        for i in self.ghosts.ghosts:
            if self.pacman.collision(i):
                self.pacman.looseLife()
                if self.pacman.alive():
                    self.pacman.resetPosition()
                    self.ghosts.resetPosition()
                else: 
                    text = self.font.render("Game Over!", True,  BLACK)
                    pygame.draw.rect(self.screen, WHITE, (SCREENWIDTH/3, SCREENHEIGHT/2 - 7.5, 215, 50))
                    self.screen.blit(text, (SCREENWIDTH/3, SCREENHEIGHT/2))
                    pygame.display.update()
                    sleep(5)
                    exit()
                

        

    def render(self):
        """renders the object on the screen"""
        self.screen.blit(self.background, (0,0))
        self.map.render(self.screen)
        self.pacman.render(self.screen)
        self.ghosts.render(self.screen)
        pygame.display.update()

    def update(self):
        """update the position etc. of our objects in the game"""
        self.clock.tick(30)
        direction = self.pacman.getDirection()
        col, row = self.pacman.position.asInt()

        #position of pacman and the map only get updated if pacman moves into a valid direction
        if direction in self.pacman.validDirections(self.map.map):
            self.map.updateValues(int(row/TILESIZE), int(col/TILESIZE))
            self.pacman.move(direction)
            
        self.ghosts.move(self.map)
        self.render()
        self.checkConditions()


if __name__ == "__main__":
    #start game
    game = Game("1.txt")
    while True:
        game.update()
        