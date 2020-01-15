#!/usr/bin/python3
# -*- coding: Utf-8 -*
"""
The main function or the start point of the  macgyver-game

Python scripts:  main.py, items.py, classes.py, constants.py,

Files: maze, .gitignore and images files



"""

import pygame
from pygame.locals import *
from classes import *
from constants import *
from items import *


def main():
    """The main function"""

    # Activate the pygame library
    pygame.init()

    # Create the display surface object of specific dimension i.e window_size
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Window icon
    window_icon = pygame.image.load(IMAGE_ICON)
    pygame.display.set_icon(window_icon)

    # Set the pygame window name
    pygame.display.set_caption(WINDOW_TITLE)
    window.blit(WELCOME, (0, 0))

    start_game = 1
    while start_game:

        # Update the full display Surface to the screen
        pygame.display.flip()

        # Setting the following variables for each loop
        play_game = 1
        play_home = 1

        while play_home:

            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                # If the  event object type is QUIT ,KEY DOWN and K_ESCAPE then quitting the pygame and program both
                #  We set the loop variables to 0
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    play_home = 0
                    play_game = 0
                    start_game = 0
                    maze_choice = 0

                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        play_home = 0   # Quit the home page
                        maze_choice = 'maze'     # Assign the selected maz to maze_choice

        if maze_choice != 0:
            # Creating the maze object
            level = Maze(maze_choice)
            # Calling maze generator method
            level.maze_generator()
            # Calling the display method
            level.display(window)
            # Creating  player object  = mg
            mg = Player(level)
            item_1, item_2, item_3 = prep_items(level.structure)
            item_count = 0

        while play_game:

            # Tracking number of frames
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    play_game = 0
                    start_game = 0

                elif event.type == KEYDOWN:
                    # If user press escape we come back to the menu
                    if event.key == K_ESCAPE:
                        play_game = 0

                    # Movement of the player
                    elif event.key == K_RIGHT:
                        mg.control('right')
                    elif event.key == K_LEFT:
                        mg.control('left')
                    elif event.key == K_UP:
                        mg.control('up')
                    elif event.key == K_DOWN:
                        mg.control('down')

                if mg.case_x == item_1.case_x and mg.case_y == item_1.case_y:
                    item_1.case_x = 0
                    item_1.case_y = 15
                    item_count += 1
                if mg.case_x == item_2.case_x and mg.case_y == item_2.case_y:
                    item_2.case_x = 1
                    item_2.case_y = 15
                    item_count += 1
                if mg.case_x == item_3.case_x and mg.case_y == item_3.case_y:
                    item_3.case_x = 2
                    item_3.case_y = 15
                    item_count += 1

            # window.blit(FLOOR, (0, 0))
            level.display(window)
            window.blit(HERO, (mg.x_value, mg.y_value))

            window.blit(NEEDLE, (item_1.case_x * MATRIX_SIZE, item_1.case_y * MATRIX_SIZE))
            window.blit(TUBE, (item_2.case_x * MATRIX_SIZE, item_2.case_y * MATRIX_SIZE))
            window.blit(ETHER, (item_3.case_x * MATRIX_SIZE, item_3.case_y * MATRIX_SIZE))

            # Update the full display Surface to the screen
            pygame.display.flip()

            # Final destination or Win
            if level.structure[mg.case_x][mg.case_y] == 'F' and item_count == 3:
                window.blit(WIN, (0, 0))
                pygame.display.flip()
                play_game = 0
                play_home = 1
            # Lost and return to the home page
            elif level.structure[mg.case_x][mg.case_y] == 'F' and item_count != 3:
                window.blit(LOSS, (0, 0))
                play_game = 0
                play_home = 1
    # Quit the game
    pygame.quit()


if __name__ == '__main__':
    # Start the main function
    main()
