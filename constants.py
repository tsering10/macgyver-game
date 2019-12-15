#!/usr/bin/env python3
"""constants for the game macgyver-game"""

import pygame
pygame.display.init()
pygame.display.set_mode()

# window and maze parameters
MATRIX_LENGTH = 15
MATRIX_HEIGHT = 16
MATRIX_SIZE = 32
SCREEN_WIDTH = MATRIX_LENGTH * MATRIX_SIZE
SCREEN_HEIGHT = MATRIX_HEIGHT * MATRIX_SIZE

# setting window title and icon
WINDOW_TITLE = "Mcgver  Labyrinthe"
IMAGE_ICON = "images/hero.png"


# setting images parameters
WALL = pygame.image.load('images/wall.png').convert()
DEPART = pygame.image.load('images/start.png').convert()
DESTINATION = pygame.image.load('images/destination.png').convert_alpha()
WELCOME = pygame.image.load('images/home.jpg').convert()
FLOOR = pygame.image.load('images/floor.jpg').convert()
HERO = pygame.image.load('images/hero.png').convert()
WIN = pygame.image.load('images/you_win.jpg').convert()
LOSS = pygame.image.load('images/you_lost.jpg').convert()

# setting item parameters

NEEDLE = pygame.image.load('images/needle.jpg').convert()
TUBE = pygame.image.load('images/tube.jpg').convert()
ETHER = pygame.image.load('images/ether.jpg').convert()
