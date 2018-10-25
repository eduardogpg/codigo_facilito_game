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

        self.vel_y = 0
        self.pos_y = 0

        self.can_jump = False

    def left(self):
        pass

    def right(self):
        pass

    def jump(self):
        if self.can_jump:
            self.vel_y -= 20
            self.can_jump = False

    def validate_jump(self, platforms):
        self.rect.y -= 1

        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.can_jump = True

        self.rect.y += 1

    def is_falling(self):
        return self.vel_y > 0

    def validate_landing(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.pos_y = hits[0].rect.top
            self.vel_y = 0

    def update(self):
        self.vel_y += PLAYER_GRAV
        self.pos_y += self.vel_y + 0.5 * PLAYER_GRAV

        self.rect.bottom = self.pos_y
