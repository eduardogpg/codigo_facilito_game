import pygame

from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( (40, 40) )
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
