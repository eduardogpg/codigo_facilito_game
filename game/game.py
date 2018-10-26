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

        self.font = pygame.font.match_font(FONT)

        self.dir = os.path.dirname(__file__)
        self.sound_dir = os.path.join(self.dir, 'sources/sounds')
        self.image_dir = os.path.join(self.dir, 'sources/images')

    def start(self):
        self.menu()
        self.new()

    def new(self):
        self.score = 0
        self.level = 1
        self.vel_x = WALL_SPEED
        self.playing = True
        self.win = False

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

        self.generate_walls()
        self.generate_coins()

    def generate_walls(self):
        las_position = WIDHT + 100

        if not self.exists_walls():

            for w in range(0, MAX_WALLS):

                pos_x = random.randrange(las_position + 100, las_position + 400)

                wall = Wall(pos_x, self.platform.rect.top)

                self.sprites.add(wall)
                self.walls.add(wall)

                las_position = wall.rect.right

    def generate_coins(self):
        las_position = WIDHT + 100

        for w in range(0, MAX_COINS):

            pos_x = random.randrange(las_position + 100, las_position + 300)

            coin = Coin(pos_x, 200)

            self.sprites.add(coin)
            self.coins.add(coin)

            las_position = coin.rect.right

    def exists_walls(self):
        return len(self.walls) > 0

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def draw(self):
        self.display.fill(BLACK)
        self.sprites.draw(self.display)

        self.draw_text()

        pygame.display.flip()

    def draw_text(self):
        if self.playing or self.win:
            self.display_text(self.score_format(), 30, WHITE, WIDHT / 2,10)
            self.display_text(self.level_format(), 30, WHITE, 60, 10)
        else:
            self.display_text('Perdistes!', 30, RED, WIDHT / 2, 10)
            self.display_text('Presiona r para comenzar de nuevo', 25, WHITE, WIDHT / 2, 30)

        if self.win:
            self.display_text('Feliciades!!!', 50, RED, WIDHT / 2, HEIGHT / 2)

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

        if keys[pygame.K_r] and not self.playing:
            self.new()

    def update(self):
        if not self.playing:
            return

        self.sprites.update()

        self.player.validate_platform(self.platform)

        self.update_elements(self.walls)
        self.update_elements(self.coins)

        coin = self.player.collide_with(self.coins)
        if coin:
            self.increment_score(coin.points)
            coin.kill()

        wall = self.player.collide_with(self.walls)
        if wall:
            if self.player.collide_bottom(wall):
                self.player.skid(wall)
            else:
                self.stop()

        self.change_next_level()

        if self.final_level():
            self.win = True
            self.stop()

    def update_elements(self, elements):
        for element in elements:
            element.set_vel_x(self.vel_x)

            if not element.visible():
                element.kill()

    def increment_score(self, points=1):
        self.score += points

    def change_next_level(self):
        if not self.exists_walls():
            self.next_level()
            self.generate_walls()
            self.generate_coins()

    def final_level(self):
        return self.level == FINAL_LEVEL

    def next_level(self):
        self.level += 1
        self.vel_x += 1

    def score_format(self):
        return "Score : {} ".format(self.score)

    def level_format(self):
        return "Level : {} ".format(self.level)

    def stop(self):
        self.vel_x = 0
        self.playing = False
        self.player.stop()

    def menu(self):
        pygame.mixer.music.load(os.path.join(self.sound_dir, 'Haggstrom.mp3'))
        pygame.mixer.music.play(loops=-1)

        self.display.fill(BLUE_LIGTH)

        self.display_text('FacilitoGames', 40, BLACK, WIDHT / 2, 50)
        self.display_text('Presiona una tecla para comenzar', 36, BLACK, WIDHT / 2, 300)

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
