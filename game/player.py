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
        print("Si")

        if self.direction == LEFT:
            self.rect.left = object.rect.right

        if self.direction == RIGHT:
            self.rect.right = object.rect.left

        self.direction = ''


    def jump(self):
        self.is_jump = True

    def left(self):
        self.rect.left -= self.vel_x
        self.direction = LEFT

    def right(self):
        self.rect.right += self.vel_x
        self.direction = RIGHT

    def calculate_acc(self):
        if self.is_jump:
            pass

    def calculdate_fall(self):
        self.rect.bottom += 4

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.jump()

        if keys[pygame.K_LEFT]:
            self.left()

        if keys[pygame.K_RIGHT]:
            self.right()

        self.calculate_acc()
        self.calculdate_fall()
