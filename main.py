
# import pygame module in this program

import pygame
from pygame.locals import *
from classes import *
from contants import *


# activate the pygame library
pygame.init()

# create the display surface object of specific dimension i.e window_size
window = pygame.display.set_mode((window_size, window_size))

# window icon
window_icon = pygame.image.load(image_icon)
pygame.display.set_icon(window_icon)

# set the pygame window name
pygame.display.set_caption(window_title)

start_game = 1
while start_game:
    # loading the welcome window
    window.blit(welcome, (0, 0))

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
                choice = 0

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    play_home = 0
                    choice = 'maze'

    if choice != 0:
        # creating maze object
        level = Maze(choice)
        # calling maze generator method
        level.maze_generator()
        # calling display method
        level.display(window)
        # creating  player object
        mg = Player(level)

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

        window.blit(floor, (0, 0))
        level.display(window)
        window.blit(hero, (mg.x, mg.y))
        pygame.display.flip()

        # final destination
        if level.structure[mg.case_y][mg.case_x] == 'F':
            play_game = 0
