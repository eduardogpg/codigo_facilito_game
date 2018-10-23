import pygame

from .config import *
from .platform import Platform
from .player import Player

class Game:

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode( (WIDHT, HEIGHT) )
        pygame.display.set_caption(TITLE)

        self.running = True

    def new(self):
        self.playing = True
        self.sprites = pygame.sprite.Group()

        self.elements()
        self.run()

    def elements(self):
        self.player = Player(WIDHT / 5, HEIGHT / 3)
        self.platform = Platform(0, HEIGHT - 40, WIDHT, 40)

        self.sprites.add(self.player)
        self.sprites.add(self.platform)

    def run(self):
        while self.playing:
            self.draw()
            self.events()
            self.update()

    def draw(self):
        self.display.fill(BLACK)
        self.sprites.draw(self.display)

        pygame.display.flip()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.sprites.update()
