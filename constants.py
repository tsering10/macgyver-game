#!/usr/bin/env python3
# -*- coding: Utf-8 -*

"""constants for the game macgyver-game"""

import pygame

pygame.display.init()
pygame.display.set_mode()

# Window and maze parameters
MATRIX_LENGTH = 15
MATRIX_HEIGHT = 16
SPRITE_SIZE = 32
SCREEN_WIDTH = MATRIX_LENGTH * SPRITE_SIZE
SCREEN_HEIGHT = MATRIX_HEIGHT * SPRITE_SIZE

# Setting window title and icon
WINDOW_TITLE = "Mcgver  Labyrinthe"
IMAGE_ICON = "images/hero.png"

# Setting images parameters
WALL = pygame.image.load('images/wall.png').convert()
DEPART = pygame.image.load('images/start.png').convert()
DESTINATION = pygame.image.load('images/destination.png').convert_alpha()
WELCOME = pygame.image.load('images/home.jpg').convert()
FLOOR = pygame.image.load('images/floor.jpg').convert()
HERO = pygame.image.load('images/hero.png').convert_alpha()
WIN = pygame.image.load('images/you_win.jpg').convert()
LOSS = pygame.image.load('images/you_lost.jpg').convert()

# Setting item parameters

NEEDLE = pygame.image.load('images/needle.jpg').convert_alpha()
TUBE = pygame.image.load('images/tube.jpg').convert_alpha()
ETHER = pygame.image.load('images/ether.jpg').convert_alpha()
