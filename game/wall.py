import pygame

from .config import *
from .element import Element

class Wall(Element):
    def __init__(self, pos_x, pos_y):
        Element.__init__(self)

        self.image = pygame.Surface( (40, 100) )
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y - 100
