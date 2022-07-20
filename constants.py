import pygame

#file which contains all constant values for the game

#colours
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
PACMAN = 0

#directions
LEFT = -1
RIGHT = 1
UP = -2
DOWN = 2
STOP = 0

#screen
WIDTH = 19
HEIGHT = 25
TILESIZE = 30
SCREENWIDTH = WIDTH * TILESIZE
SCREENHEIGHT = HEIGHT * TILESIZE
SCREENSIZE = (SCREENWIDTH, SCREENHEIGHT)

#Map
COIN = pygame.image.load("Pictures/bonbon.png")
COIN = pygame.transform.scale(COIN, (TILESIZE, TILESIZE))
BRICK = pygame.image.load("Pictures/dunkel-blau.png")
BRICK = pygame.transform.scale(BRICK, (TILESIZE, TILESIZE))
BLANK = pygame.image.load("Pictures/blank.png")
BLANK = pygame.transform.scale(BLANK, (TILESIZE, TILESIZE))
