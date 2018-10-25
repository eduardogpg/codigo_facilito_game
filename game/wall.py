import pygame

from .config import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( (40, 100) )
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y - 100

        self.vel_x = 0

    def update(self):
        self.rect.left -= self.vel_x

    def set_vel_x(self, vel_x):
        self.vel_x = vel_x

    def visible(self):
        return self.rect.right > 0
