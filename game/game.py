import pygame

from .config import *
from .platform import Platform
from .player import Player

class Game:

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode( (WIDHT, HEIGHT) )
        pygame.display.set_caption(TITLE)

        self.clock =  pygame.time.Clock()

        self.running = True

    def new(self):
        self.playing = True
        self.sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.elements()
        self.run()

    def elements(self):
        self.platform = Platform(0, HEIGHT - 40, WIDHT, 40, GREEN)
        self.player = Player(WIDHT / 5, self.platform.rect.top)

        p1 = Platform(500, HEIGHT - 80, 40, 40, BROWN)
        p2 = Platform(0, HEIGHT - 80, 40, 40, BROWN)

        self.sprites.add(self.player)
        self.sprites.add(self.platform)
        self.sprites.add(p1)
        self.sprites.add(p2)

        self.platforms.add(self.platform)
        self.platforms.add(p1)
        self.platforms.add(p2)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.draw()
            self.update()
            self.events()

    def draw(self):
        self.display.fill(BLACK)
        self.sprites.draw(self.display)

        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.sprites.update()

        if self.player.is_jump:
            self.player.rect.bottom += 2
            hits = pygame.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.validate_move(hits[0])


class Music:
    def __init__(self):
        pass
