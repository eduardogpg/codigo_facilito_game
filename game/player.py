import pygame
from pygame.math import Vector2 as vector
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( (40, 40) )
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.direction = ''

    def left(self):
        self.rect.left -= 5

    def right(self):
        self.rect.left += 5

    def jump(self):
        self.is_jump = True
        
    def fall(self):
        pass

    def update(self):
        self.fall()
