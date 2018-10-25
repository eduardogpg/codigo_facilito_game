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

        self.acc_w = WALL_SPEED

        self.jumped = False

    def update(self):
        self.rect.left -= self.acc_w

    def stop(self):
        self.acc_y = 0
