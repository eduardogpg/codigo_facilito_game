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

        self.is_jump = False
        self.mass = MASS
        self.speed_y = SPEED_Y

    def left(self):
        self.acc_x -= self.speed_x
        self.direction = LEFT

    def right(self):
        self.acc_x += self.speed_x
        self.direction = RIGHT

    def validate_move(self, object):
        print("Siii")
        if self.is_jump:
            self.is_jump = False
            self.speed_y = SPEED_Y
            self.rect.bottom = object.rect.top + 2

    def jump(self):
        self.is_jump = True

    def calculate_acc(self):
        if self.is_jump:
            F = (0.5 * self.mass * (self.speed_y * self.speed_y))
            if self.speed_y <= 0:
                F = F * -1

            self.rect.y = self.rect.y - F
            self.speed_y = self.speed_y - 1

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.jump()

        self.calculate_acc()
