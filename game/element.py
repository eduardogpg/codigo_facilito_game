import pygame

from .config import *

class Element(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.vel_x = 0

    def update(self):
        self.rect.left -= self.vel_x
        
    def set_vel_x(self, vel_x):
        self.vel_x = vel_x

    def visible(self):
        return self.rect.right > 0
