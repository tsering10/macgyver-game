#!/usr/bin/env python3
import pygame
from pygame.locals import *
from constants import *


class Maze:
    """This is a class for  creating a maze"""

    def __init__(self, filename):
        self.filename = filename
        self.structure = 0

    def maze_generator(self):

        # Opening of file
        with open(self.filename, "r") as f:
            structure_level = []
            for line in f:
                line_level = []
                for sprite in line:
                    if sprite != '\n':
                        line_level.append(sprite)
                structure_level.append(line_level)
            self.structure = structure_level

    def display(self, window):
        num_line = 0
        for line in self.structure:
            num_case = 0
            for sprite in line:
                x = num_case * MATRIX_SIZE
                y = num_line * MATRIX_SIZE
                if sprite == 'm':  # m = wall
                    window.blit(WALL, (x, y))
                elif sprite == 'd':  # d = start
                    window.blit(DEPART, (x, y))
                elif sprite == 'F':  # F = destination
                    window.blit(DESTINATION, (x, y))
                num_case += 1
            num_line += 1


class Player:
    """ This is a class for creating player in the game """

    def __init__(self, level):
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.level = level

    def control(self, direction):

        # right movement
        if direction == 'right':
            # not go over the screen
            if self.case_x < (MATRIX_LENGTH - 1):
                # check the destination is not a wall
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                    # move over one step
                    self.case_x += 1
                    self.x = self.case_x * MATRIX_SIZE

        # left movement
        if direction == 'left':
            if self.case_x > 0 and self.level.structure[self.case_y][self.case_x - 1] != 'm':
                self.case_x -= 1
                self.x = self.case_x * MATRIX_SIZE

        # up movement
        if direction == 'up':
            if self.case_y > 0 and self.level.structure[self.case_y - 1][self.case_x] != 'm':
                self.case_y -= 1
                self.y = self.case_y * MATRIX_SIZE

        # down movement
        if direction == 'down':
            if self.case_y < (MATRIX_LENGTH  - 1) and self.level.structure[self.case_y + 1][self.case_x] != 'm':
                self.case_y += 1
                self.y = self.case_y * MATRIX_SIZE


class Items:
    pass
