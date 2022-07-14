
from this import d
import pygame

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PACMAN = 0

LEFT = -1
RIGHT = 1
UP = -2
DOWN = 2
STOP = 0

SCREENWIDTH = 475
SCREENHEIGHT = 625
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)
TILESIZE = 25

#Map
COIN = pygame.image.load("Pictures/bonbon.png")
COIN = pygame.transform.scale(COIN, (TILESIZE, TILESIZE))
BRICK = pygame.image.load("Pictures/dunkel-blau.png")
BRICK = pygame.transform.scale(BRICK, (TILESIZE, TILESIZE))
BLANK = pygame.image.load("Pictures/blank.png")
BLANK = pygame.transform.scale(BLANK, (TILESIZE, TILESIZE))

print(BRICK)
