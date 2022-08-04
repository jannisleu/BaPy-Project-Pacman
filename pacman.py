from constants import *
import pygame
import numpy as np
from vector import Vector
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_DOWN,
    K_UP
)

class Pacman:
    """Class for a Pacman object"""

    def __init__(self):
        """Create a Pacman"""
        self.position = Vector(9*TILESIZE, 16*TILESIZE)
        self.directions = {STOP: Vector(), UP: Vector(0, -1), DOWN: Vector(0, 1), LEFT: Vector(-1, 0), RIGHT: Vector(1, 0)}
        self.direction = STOP
        self.speed = SPEED
        self.radius = 10
        self.color = YELLOW
        self.name = PACMAN_RIGHT
        self.lives = 3
        self.iterations = 0

    def getDirection(self):
        """get direction after pressing a key

        Returns:
            constant: one of the directions of the self.directions dictionary
        """
        keys = pygame.key.get_pressed()

        col, row = self.position.asInt()
        if col % TILESIZE == 0 and row % TILESIZE == 0:

            if keys[K_LEFT]:
                return LEFT 
            if keys[K_RIGHT]:
                return RIGHT
            if keys[K_UP]:
                return UP
            if keys[K_DOWN]:
                return DOWN
            return STOP

        return self.direction


    def validDirections(self, map):
        """Check surrounding fields whether they are valid for the next move

        Args:
            row (int): row of the maze array(from the current position)
            col (int): column of the maze array(from the current position)

        Returns:
            _list: list of valid directions for the next step
        """

        col, row = self.position.asInt()
        if col % TILESIZE == 0 and row % TILESIZE == 0:
            col = int(col/TILESIZE)
            row = int(row/TILESIZE)
            valid = [STOP]
            if map[row][col - 1] != 0:
                valid.append(LEFT)
            if map[row][col + 1] != 0:
                valid.append(RIGHT)
            if map[row - 1][col] != 0:
                valid.append(UP)
            if map[row + 1][col] != 0:
                valid.append(DOWN)
            return valid
        valid = [self.direction]
        return valid

    def move(self, direction):
        """Moves the pacman

        Args:
            direction (key): key for the self.directions dictionary
        """
        self.direction = direction
        self.position += self.directions[self.direction]*self.speed
        
        self.iterations += 1
        if self.iterations > 2:
            self.iterations = 0
            
            #update pacman image to the new direction
            if self.checkForOpenMouth():
                if direction == RIGHT:
                    self.name = PACMAN_RIGHT
                if direction == LEFT:
                    self.name = PACMAN_LEFT
                if direction == UP:
                    self.name = PACMAN_UP
                if direction == DOWN:
                    self.name = PACMAN_DOWN

            else:
                if direction == RIGHT:
                    self.name = PACMAN_RIGHT_OPEN
                if direction == LEFT:
                    self.name = PACMAN_LEFT_OPEN
                if direction == UP:
                    self.name = PACMAN_UP_OPEN
                if direction == DOWN:
                    self.name = PACMAN_DOWN_OPEN


    def checkForOpenMouth(self):
         
        if  self.name == PACMAN_RIGHT_OPEN:
            return True 
        if  self.name == PACMAN_LEFT_OPEN:
            return True
        if  self.name == PACMAN_DOWN_OPEN:
            return True
        if  self.name == PACMAN_UP_OPEN:
            return True
        return False

    def collision(self, other):
        helper = self.position - other.position
        distance = helper.squaredLength()
        if distance < 100:
            return True
        return False
 
    def looseLife(self):
        self.lives -= 1

    def alive(self):
        if self.lives < 0:
            return False
        return True

    def resetPosition(self):
        self.position = Vector(9*TILESIZE, 16*TILESIZE)

    def render(self, screen):
        """Render Pacman onto the screen

        Args:
            screen (Surface): pygame surface 
        """
        x, y = self.position.asInt()
        pygame.draw.circle(screen, BLACK, (x + 12.5, y + 12.5), self.radius)
        screen.blit(self.name, (x, y))