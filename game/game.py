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
        self.obstacles = pygame.sprite.Group()

        self.elements()
        self.run()

    def elements(self):
        self.platform = Platform()
        self.player = Player(WIDHT / 5, self.platform.rect.top)

        p1 = Obstacle(500, HEIGHT - 80, 40, 40)
        p2 = Obstacle(0, HEIGHT - 80, 40, 40)

        self.sprites.add(self.player)
        self.sprites.add(self.platform)
        self.sprites.add(p1)
        self.sprites.add(p2)

        self.obstacles.add(p1)
        self.obstacles.add(p2)

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

        #collide with platform
        hit = pygame.sprite.collide_rect(self.player, self.platform)
        if hit:
            self.player.rect.bottom = self.platform.rect.top

        hits = pygame.sprite.spritecollide(self.player, self.obstacles, False)
        if(hits):
            self.player.validate_move(hits[0])

class Music:
    def __init__(self):
        pass
