import pygame
from pygame.sprite import Sprite
from stats import Stats

class Alien(Sprite):
    #initializes an alien
    def __init__(self, game):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.stats = game.stats
        self.image = pygame.image.load("alien.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    #updates the aliens position based on their speed and direction
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.alien_direction) * (self.stats.round * 0.2)
        self.rect.x = self.x

    #checks if the alien has reached the edge of a screen, if it does change it's direction
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    #checks if the alien has reached the bottom and "landed"
    def check_bottom(self):
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom > screen_rect.bottom)