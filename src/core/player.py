# src/core/player.py

"""
    This class is responsible for the player.
"""
import os.path

from src.core.paths import image_dir
from src.core.utils import TILE_SIZE, pygame, screen


class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = None
        self.speed = 5
        self.score = 0
        self.rect = pygame.Rect(self.x, self.y, TILE_SIZE, TILE_SIZE)
        self.set_image("pac-man.png")

    def set_image(self, file_name:str):
        image_path = os.path.join(image_dir, file_name)
        self.image = pygame.image.load(image_path)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
