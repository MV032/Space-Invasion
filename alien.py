import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = Settings()
        self.screen = game.screen
        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed
        self.rect.x = self.x