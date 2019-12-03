import pygame


pygame.display.init()
pygame.display.set_mode()

# window and maze parameters
MATRIX_LENGTH = 15
MATRIX_SIZE = 30
WINDOW_SIZE = MATRIX_LENGTH * MATRIX_SIZE

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
