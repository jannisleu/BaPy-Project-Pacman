import pygame

#file which contains all constant values for the game

#colours
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

PACMAN = 0
GHOST = 1
SPEED = 2

#directions
LEFT = -1
RIGHT = 1
UP = -2
DOWN = 2
STOP = 0

#screen
WIDTH = 19
HEIGHT = 25
TILESIZE = 24
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

#Pacman
pacman_right = pygame.image.load("Pictures/pac right.png")
pacman_right_open = pygame.image.load("Pictures/pac right open.png")
pacman_left = pygame.image.load("Pictures/pac left.png")
pacman_left_open = pygame.image.load("Pictures/pac left open.png")
pacman_up = pygame.image.load("Pictures/pac up.png")
pacman_up_open = pygame.image.load("Pictures/pac up open.png")
pacman_down = pygame.image.load("Pictures/pac down.png")
pacman_down_open = pygame.image.load("Pictures/pac down open.png")

PACMAN_RIGHT = pygame.transform.scale(pacman_right, (TILESIZE, TILESIZE))
PACMAN_RIGHT_OPEN = pygame.transform.scale(pacman_right_open, (TILESIZE, TILESIZE))
PACMAN_LEFT = pygame.transform.scale(pacman_left, (TILESIZE, TILESIZE))
PACMAN_LEFT_OPEN = pygame.transform.scale(pacman_left_open, (TILESIZE, TILESIZE))
PACMAN_UP = pygame.transform.scale(pacman_up, (TILESIZE, TILESIZE))
PACMAN_UP_OPEN = pygame.transform.scale(pacman_up_open, (TILESIZE, TILESIZE))
PACMAN_DOWN = pygame.transform.scale(pacman_down, (TILESIZE, TILESIZE))
PACMAN_DOWN_OPEN = pygame.transform.scale(pacman_down_open, (TILESIZE, TILESIZE))


#Map
coin = pygame.image.load("Pictures/bonbon.png")
COIN = pygame.transform.scale(coin, (TILESIZE, TILESIZE))
brick = pygame.image.load("Pictures/dunkel-blau.png")
BRICK = pygame.transform.scale(brick, (TILESIZE, TILESIZE))
blank = pygame.image.load("Pictures/blank.png")
BLANK = pygame.transform.scale(blank, (TILESIZE, TILESIZE))
