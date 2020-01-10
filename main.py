#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from classes import *
from constants import *
from items import *


def main():
    """The main function"""

    # activate the pygame library
    pygame.init()

    # create the display surface object of specific dimension i.e window_size
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # window icon
    window_icon = pygame.image.load(IMAGE_ICON)
    pygame.display.set_icon(window_icon)

    # set the pygame window name
    pygame.display.set_caption(WINDOW_TITLE)
    window.blit(WELCOME, (0, 0))

    start_game = 1
    while start_game:

        # update the display using flip
        pygame.display.flip()

        # setting the following variables for each loop
        play_game = 1
        play_home = 1

        while play_home:

            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                # if event object type is QUIT ,KEY DOWN and K_ESCAPE then quitting the pygame and program both

                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    play_home = 0
                    play_game = 0
                    start_game = 0
                    maze_choice = 0

                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        play_home = 0
                        maze_choice = 'maze'

        if maze_choice != 0:
            # creating maze object
            level = Maze(maze_choice)
            # calling maze generator method
            level.maze_generator()
            # calling display method
            level.display(window)
            # creating  player object
            mg = Player(level)
            item_1, item_2, item_3 = prep_items(level.structure)
            item_count = 0

        while play_game:

            # tracking number of frames
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    play_game = 0
                    start_game = 0

                elif event.type == KEYDOWN:
                    # if user press escape we come back to the menu
                    if event.key == K_ESCAPE:
                        play_game = 0

                    # movement of the player
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

            pygame.display.flip()

            # final destination
            if level.structure[mg.case_x][mg.case_y] == 'F' and item_count == 3:
                window.blit(WIN, (0, 0))
                pygame.display.flip()
                play_game = 0
                play_home = 1
            elif level.structure[mg.case_x][mg.case_y] == 'F' and item_count != 3:
                window.blit(LOSS, (0, 0))
                play_game = 0
                play_home = 1
    # Quit the game
    pygame.quit()


if __name__ == '__main__':
    main()
