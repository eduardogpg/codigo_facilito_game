import pygame
from pygame.math import Vector2 as vector
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface( (40, 40) )
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.vel_y = 0
        self.pos_y = self.rect.bottom
        self.acc_y = PLAYER_GRAV

        self.can_jump = False
        self.playing = True

    def jump(self):
        if self.can_jump:
            self.vel_y = -25
            self.can_jump = False

    def validate_platform(self, platform):
        collide = pygame.sprite.collide_rect(self, platform)
        if collide:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True

    def collide_with(self, sprites):
        hits = pygame.sprite.spritecollide(self, sprites, False)
        if hits:
            return hits[0]

    def stop(self):
        self.playing = False

    def update_pos(self):
        self.vel_y += self.acc_y #always falling
        self.pos_y += self.vel_y + 0.5 * self.acc_y

    def update(self):
        if self.playing:
            self.update_pos()
            self.rect.bottom = self.pos_y
