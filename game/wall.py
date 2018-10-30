import os
import pygame

from .config import *
from .element import Element

class Wall(Element):
    def __init__(self, left, bottom, sprite_dir):
        Element.__init__(self)

        self.image = pygame.image.load(os.path.join(sprite_dir, 'wall.png'))

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.surface = pygame.Rect(self.rect.x + 100, self.rect.y, self.rect.width, 1)

    def update(self):
        Element.update(self)

        self.surface.x = self.rect.x
        self.surface.y = self.rect.y
