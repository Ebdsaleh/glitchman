# src/core/utils.py

"""
    This is a collection of constants and definitions used throughout the program
"""
import os.path

import pygame
from src.core.paths import image_dir, font_dir
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TILE_SIZE = 30

# Program screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

font_path = os.path.join(font_dir, "ka1.ttf")
font = pygame.font.Font(str(font_path), 24)
