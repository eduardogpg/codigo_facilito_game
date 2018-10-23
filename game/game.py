import pygame

from .config import *

class Game:

    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode( (WIDHT, HEIGHT) )
        pygame.display.set_caption(TITLE)
        
        self.running = True

    def new(self):
        self.playing = True
        self.run()

    def run(self):
        while self.playing:
            self.draw()
            self.events()
            self.update()

    def draw(self):
        self.display.fill(BLACK)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        pass
