import pygame

from .config import *

class Platform(pygame.sprite.Sprite):
    def __init__(self, posx, posy, widht, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( (widht, height) )
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
