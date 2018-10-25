import pygame
import random

from .config import *
from .player import Player
from .platform import Platform
from .wall import Wall

class Game:

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode( (WIDHT, HEIGHT) )
        pygame.display.set_caption(TITLE)

        self.clock =  pygame.time.Clock()

        self.running = True
        self.score = 0
        self.vel_x = WALL_SPEED

    def new(self):
        self.playing = True

        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.generate_fonts()
        self.update_text()

        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200)

        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()

        self.sprites.add(self.player)
        self.sprites.add(self.platform)

        self.las_position_wall = WIDHT + 200

        self.generate_walls()

    def generate_walls(self):
        if len(self.walls) < 6:

            pos_x = random.randrange(self.las_position_wall + 200,
                                     self.las_position_wall + 500)

            wall = Wall(pos_x, self.platform.rect.top)

            self.sprites.add(wall)
            self.walls.add(wall)
            self.las_position_wall = wall.rect.right

    def generate_fonts(self):
        font = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font, 28)

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def draw(self):
        self.display.fill(BLACK)
        self.display.blit(self.text, self.text_rect)

        self.sprites.draw(self.display)

        pygame.display.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        self.sprites.update()

        self.player.validate_platform(self.platform)

        self.update_text()
        self.update_walls()

        if self.player.collide_with(self.walls):
            self.stop()

    def update_walls(self):
        for wall in self.walls:
            wall.set_vel_x(self.vel_x)

            if not wall.visible():
                wall.kill()

        self.generate_walls()

    def update_score(self):
        self.score += 1

    def update_text(self):
        self.text = self.font.render(self.score_text(), True, WHITE)

        self.text_rect = self.text.get_rect()
        self.text_rect.midtop = (WIDHT / 2, 10)

    def score_text(self):
        return "Score : {} ".format(self.score)

    def stop(self):
        self.vel_x = 0
        self.player.stop()
