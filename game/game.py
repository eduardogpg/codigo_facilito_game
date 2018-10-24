import pygame

from .config import *
from .platform import Platform
from .player import Player
from .obstacle import Obstacle

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
        self.platform = Platform()
        self.player = Player(WIDHT / 6, self.platform.rect.top)

        p1 = Obstacle(500, HEIGHT - 80, 40, 40)

        self.sprites.add(self.player)
        self.sprites.add(self.platform)
        self.sprites.add(p1)

        self.platforms.add(p1)
        self.platforms.add(self.platform)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def draw(self):
        self.display.fill(BLACK)
        self.sprites.draw(self.display)

        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.left()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.right()

        if keys[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        self.sprites.update()
