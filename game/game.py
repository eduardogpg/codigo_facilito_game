import os
import pygame
import random

from .config import *
from .player import Player
from .platform import Platform
from .wall import Wall
from .coin import Coin

class Game:

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode( (WIDHT, HEIGHT) )
        pygame.display.set_caption(TITLE)

        self.clock =  pygame.time.Clock()

        self.running = True
        self.score = 0

        self.font = pygame.font.match_font('arial')

        self.dir = os.path.dirname(__file__)
        self.sound_dir = os.path.join(self.dir, 'sources/sounds')

    def start(self):
        self.menu()
        self.new()

    def new(self):
        self.playing = True
        self.level = 1
        self.vel_x = WALL_SPEED

        self.generate_elements()
        self.run()

    def generate_elements(self):
        self.platform = Platform()
        self.player = Player(100, self.platform.rect.top - 200)

        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()

        self.sprites.add(self.player)
        self.sprites.add(self.platform)

        self.las_position_wall = WIDHT + 200
        self.las_position_coin = WIDHT + 100

        self.generate_walls()
        self.generate_coins()

    def generate_coins(self):
        if len(self.coins) < 10:

            pos_x = random.randrange(self.las_position_coin + 200,
                                     self.las_position_coin + 400)
            coin = Coin(pos_x, 200)

            self.sprites.add(coin)
            self.coins.add(coin)
            self.las_position_coin = coin.rect.right

    def generate_walls(self):
        if len(self.walls) < 6:

            pos_x = random.randrange(self.las_position_wall + 200,
                                     self.las_position_wall + 500)

            wall = Wall(pos_x, self.platform.rect.top)

            self.sprites.add(wall)
            self.walls.add(wall)
            self.las_position_wall = wall.rect.right

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def draw(self):
        self.display.fill(BLACK)

        self.draw_text()
        self.sprites.draw(self.display)

        pygame.display.flip()

    def draw_text(self):
        if self.playing:
            self.display_text(self.score_text(), 30, WHITE, WIDHT / 2,10)
        else:
            self.display_text('Perdiste!!!', 30, RED, WIDHT / 2, 10)

    def display_text(self, text, font_size, color, pos_x, pos_y):
        font = pygame.font.Font(self.font, font_size)

        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)

        self.display.blit(text, rect)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.player.jump()

    def update(self):
        self.sprites.update()

        self.player.validate_platform(self.platform)

        self.update_elements(self.walls)
        self.update_elements(self.coins)

        coin = self.player.collide_with(self.coins)
        if coin:
            self.update_score(coin.points)
            coin.kill()

        wall = self.player.collide_with(self.walls)
        if wall:
            if self.player.collide_bottom(wall):
                self.player.skid(wall)
            else:
                self.stop()

        self.generate_walls()
        self.generate_coins()

    def update_elements(self, elements):
        for element in elements:
            element.set_vel_x(self.vel_x)

            if not element.visible():
                element.kill()

    def update_score(self, points=1):
        self.score += points

    def update_text_final(self):
        return self.final_font.render("Perdiste!!", True, RED)

    def score_text(self):
        return "Score : {} ".format(self.score)

    def stop(self):
        self.vel_x = 0
        self.playing = False
        self.player.stop()

    def menu(self):
        pygame.mixer.music.load(os.path.join(self.sound_dir, 'Haggstrom.mp3'))
        pygame.mixer.music.play(loops=-1)

        self.display.fill(BLUE_LIGTH)

        self.display_text('Facilito Game', 40, BLACK, WIDHT / 2, 50)
        self.display_text('Press a key to play', 36, BLACK, WIDHT / 2, HEIGHT * 3 / 4)

        pygame.display.flip()

        self.wait()

        pygame.mixer.music.fadeout(1000)

    def wait(self):
        wait = True

        while wait:
            self.clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.running = False

                if event.type == pygame.KEYUP:
                    wait = False
