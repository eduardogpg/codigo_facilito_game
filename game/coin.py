import os
import pygame

from .element import Element
from .config import *

class Coin(Element):
    def __init__(self, pos_x, pos_y, sprite_dir):
        Element.__init__(self)

        #self.image = pygame.Surface( (20, 40) )
        self.image = pygame.image.load(os.path.join(sprite_dir, 'coin.png'))

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y - 40
        
        self.vel_x = 0

        self.points = 1
