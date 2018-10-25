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

        #All moves will validate first with pos_x and pos_y
        self.vel_y = 0
        self.pos_y = self.rect.bottom
        self.acc_y = PLAYER_GRAV

        self.vel_x = 0
        self.pos_x = self.rect.left
        self.acc_x = 0

        self.can_jump = False

    def is_falling(self):
        return self.vel_y > 0

    def is_running(self):
        return self.vel_x > 0

    def left(self):
        self.acc_x = - 0.5

    def right(self):
        self.acc_x = 0.5

    def jump(self):
        if self.can_jump:
            self.vel_y -= 20
            self.can_jump = False

    def validate_border(self):
        if self.pos_x <= 0:
            self.pos_x = 0
            self.vel_x = 0
            self.acc_x = 0

    def validate_jump(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.can_jump = True

    def validate_landing(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.pos_y = hits[0].rect.top
            self.vel_y = 0

    def validate_acc_x(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            print("Auch!")

    def update(self):
        self.vel_y += self.acc_y #Siempre en caida
        self.pos_y += self.vel_y + 0.5 * self.acc_y

        self.acc_x += self.vel_x * PLAYER_FRICTION

        self.vel_x += self.acc_x
        self.pos_x += self.vel_x + 0.5 * self.acc_x

        self.acc_x = 0

        self.rect.left = self.pos_x
        self.rect.bottom = self.pos_y
