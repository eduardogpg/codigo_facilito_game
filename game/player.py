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

        #acceleration x
        self.speed_x = SPEED_X
        self.pos_x = self.rect.right
        self.vel_x = 0
        self.acc_x = 0

    def left(self):
        self.acc_x -= self.speed_x
        self.direction = LEFT

    def right(self):
        self.acc_x += self.speed_x
        self.direction = RIGHT

    def validate_move(self, object):

        if self.direction == LEFT:
            self.rect.left = object.rect.right

        if self.direction == RIGHT:
            self.rect.right = object.rect.left

        self.pos_x = self.rect.right
        self.vel_x = 0

    def calculate_acc(self):
        #fricction
        self.acc_x += self.vel_x * PLAYER_FRICTION

        self.vel_x += self.acc_x
        self.pos_x += self.vel_x + 0.5 * self.acc_x

    def update(self):
        self.acc_x = 0
        
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.left()

        if keys[pygame.K_RIGHT]:
            self.right()

        self.calculate_acc()
        self.update_rect()

    def update_rect(self):
        self.rect.right = self.pos_x
