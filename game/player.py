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
        self.speed_x = SPEED_X

    def left(self):
        self.rect.x -= self.speed_x
        self.direction = LEFT

    def right(self):
        self.rect.x += self.speed_x
        self.direction = RIGHT

    def validate_move(self, object):
        if self.direction == LEFT:
            self.rect.left = object.rect.right

        if self.direction == RIGHT:
            self.rect.right = object.rect.left

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.left()

        if keys[pygame.K_RIGHT]:
            self.right()
