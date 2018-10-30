import os
import pygame

from pygame.math import Vector2 as vector
from .config import *

class Player(pygame.sprite.Sprite):
    def __init__(self, left, bottom, sprite_dir):
        pygame.sprite.Sprite.__init__(self)

        self.images = ( pygame.image.load(os.path.join(sprite_dir, 'player1.png')),
                        pygame.image.load(os.path.join(sprite_dir, 'jump.png'))
                       )

        self.image = self.images[0]

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom

        self.vel_y = 0
        self.pos_y = self.rect.bottom

        self.can_jump = False
        self.jumpping = False
        self.playing = True

    def jump(self):
        if self.can_jump:
            self.vel_y = PLAYER_VEL_Y
            self.jumpping = True
            self.can_jump = False

    def validate_platform(self, platform):
        collide = pygame.sprite.collide_rect(self, platform)
        if collide:
            self.vel_y = 0
            self.pos_y = platform.rect.top
            self.can_jump = True
            self.jumpping = False
            self.image = self.images[0]

    def collide_with(self, sprites):
        hits = pygame.sprite.spritecollide(self, sprites, False)
        if hits:
            return hits[0]

    def collide_bottom(self, wall):
        return self.rect.colliderect(wall.surface)

    def skid(self, wall):
        self.pos_y = wall.rect.top
        self.vel_y = 0
        self.can_jump = True
        self.image = self.images[0]

    def stop(self):
        self.playing = False

    def update_pos(self):
        self.vel_y += PLAYER_GRAV #always falling
        self.pos_y += self.vel_y + 0.5 * PLAYER_GRAV

        if not self.can_jump:
            self.image = self.images[1]

    def update(self):
        if self.playing:
            self.update_pos()
            self.rect.bottom = self.pos_y
