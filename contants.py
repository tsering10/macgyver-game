import pygame


pygame.display.init()
pygame.display.set_mode()

# window and maze parameters
matrix_length = 15
matrix_size = 30
window_size = matrix_length * matrix_size

# setting window title and icon
window_title = "Mcgver  Labyrinthe"
image_icon = "images/hero.png"


# setting image  parameters
wall = pygame.image.load('images/wall.png').convert()
depart = pygame.image.load('images/start.png').convert()
destination = pygame.image.load('images/destination.png').convert_alpha()
welcome = pygame.image.load('images/home.jpg').convert()
floor = pygame.image.load('images/floor.jpg').convert()
hero = pygame.image.load('images/hero.png').convert()
