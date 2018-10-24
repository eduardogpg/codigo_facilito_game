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
        self.acc_y = ACC_Y

        self.vel_x = VEL_X

        print(self.rect.bottom)

    def left(self):
        self.acc_x -= self.speed_x
        self.direction = LEFT

    def right(self):
        self.acc_x += self.speed_x
        self.direction = RIGHT

    def validate_move(self, object):
        if self.is_jump:
            self.is_jump = False
            self.acc_y = ACC_Y
            self.rect.bottom = object.rect.top
            

    def jump(self):
        self.is_jump = True

    def left(self):
        self.rect.left -= self.vel_x

    def right(self):
        self.rect.right += self.vel_x

    def calculate_acc(self):
        if self.is_jump:
            F = (0.5 * self.mass * (self.acc_y * self.acc_y))
            if self.acc_y <= 0:
                F = F * -1

            self.rect.bottom = abs(self.rect.bottom - F)
            self.acc_y = self.acc_y - 1

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.jump()

        if keys[pygame.K_LEFT]:
            self.left()

        if keys[pygame.K_RIGHT]:
            self.right()

        self.calculate_acc()
