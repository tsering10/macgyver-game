#!/usr/bin/env python3
import pygame
from pygame.locals import *
from constants import *
import random
import os


class Maze:
    """This is a class for creating a maze"""

    def __init__(self, filename):
        """
        The constructor for Maze class.

        Parameters:
        filename : maze file in a text file format.
        """
        self.filename = filename
        self.structure = 0

    def maze_generator(self):
        """ Method to read the maze file and creates a list with contains a list per line"""

        # Opening of file
        try:
            with open(self.filename, "r") as file_maze:
                structure_level = []
                # loop through the lines in the file
                for line in file_maze:
                    line_level = []
                    # loop through the sprites or characters in the file
                    for sprite in line:
                        # ignore the "\ n" at the end of the line
                        if sprite != '\n':
                            # append the sprite to the line_level list
                            line_level.append(sprite)
                    # append the lines to the list structure_level
                    structure_level.append(line_level)
                    # assign or save to structure
                self.structure = structure_level
        except IOError:
            print("Not able to open the file {}.txt".format(self.filename))
            os.exit(1)

    def display(self, window):
        """
        Method for displaying the maze  according the the list resturn by the previous function


        Parameters:
           window: This function will create a display Surface. The arguments passed in are requests for a display type
        """
        num_line = 0
        for line in self.structure:
            num_case = 0
            # loop through the lines
            for sprite in line:
                # calculate the real position in pixel
                x = num_case * MATRIX_SIZE
                y = num_line * MATRIX_SIZE
                if sprite == 'm':  # m = Wall
                    window.blit(WALL, (x, y))
                elif sprite == 'd':  # d = Start
                    window.blit(DEPART, (x, y))
                elif sprite == 'F':  # F = Destination
                    window.blit(DESTINATION, (x, y))
                elif sprite == '0':
                    window.blit(FLOOR, (x, y))  # 0 = Floor
                num_case += 1
            num_line += 1


class Player:
    """
        This is a class for creating character in the game.


     """

    def __init__(self, level):
        """
        The constructor for Player class.

        Parameters:
        level : list
        """
        # player position in boxes and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        self.level = level

    def control(self, direction):
        """
                The method is use to control the movement of the player character .

                Parameters:
                    direction: constants (from pygame.localspygame constants) used to represent keyboard keys.


         """

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
            if self.case_y < (MATRIX_LENGTH - 1) and self.level.structure[self.case_y + 1][self.case_x] != 'm':
                self.case_y += 1
                self.y = self.case_y * MATRIX_SIZE


class Items:
    """
        This is a class for creating items in the game.


    """
    def __init__(self, structure):
        """
        The constructor for Items  class.

        Parameters:
                  structure : list.
        """
        # Initialising  item  position in boxes and pixels
        self.structure = structure
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0

    def items_position(self):
        """
        The method to set item positions on the maze.


        """
        while self.structure[self.case_y][self.case_x] != "0":
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
        self.x = self.case_x * MATRIX_SIZE
        self.y = self.case_y * MATRIX_SIZE
