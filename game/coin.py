import pygame

from .element import Element
from .config import *

class Coin(Element):
    def __init__(self, pos_x, pos_y):
        Element.__init__(self)

        self.image = pygame.Surface( (20, 40) )
        self.image.fill(YELLOW)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y - 40

        self.acc_w = WALL_SPEED

        self.vel_x = 0
