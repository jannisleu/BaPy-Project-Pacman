from asyncio.proactor_events import _ProactorDuplexPipeTransport
import pygame

#file which contains all constant values for the game

#colours
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PACMAN = 0
GHOST = 1

#directions
LEFT = -1
RIGHT = 1
UP = -2
DOWN = 2
STOP = 0

#screen
WIDTH = 19
HEIGHT = 25
TILESIZE = 25
SCREENWIDTH = WIDTH * TILESIZE
SCREENHEIGHT = HEIGHT * TILESIZE
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)


#Ghosts
red = pygame.image.load("Pictures/G1.png")
pink = pygame.image.load("Pictures/G2.png")
blue = pygame.image.load("Pictures/G3.png")
orange = pygame.image.load("Pictures/G4.png")
green = pygame.image.load("Pictures/G5.png")
purple = pygame.image.load("Pictures/G6.png")

RED = pygame.transform.scale(red, (TILESIZE, TILESIZE))
PINK = pygame.transform.scale(pink, (TILESIZE, TILESIZE))
BLUE = pygame.transform.scale(blue, (TILESIZE, TILESIZE))
ORANGE = pygame.transform.scale(orange, (TILESIZE, TILESIZE))
GREEN = pygame.transform.scale(green, (TILESIZE, TILESIZE))
PURPLE = pygame.transform.scale(purple, (TILESIZE, TILESIZE))

#Map
coin = pygame.image.load("Pictures/bonbon.png")
COIN = pygame.transform.scale(coin, (TILESIZE, TILESIZE))
brick = pygame.image.load("Pictures/dunkel-blau.png")
BRICK = pygame.transform.scale(brick, (TILESIZE, TILESIZE))
blank = pygame.image.load("Pictures/blank.png")
BLANK = pygame.transform.scale(blank, (TILESIZE, TILESIZE))
