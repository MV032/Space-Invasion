import pygame

class Ship:
    #initializes player setup
    def __init__(self, space_game):
        self.settings = space_game.settings
        self.screen = space_game.screen
        self.screen_rect = space_game.screen.get_rect()
        self.image =  pygame.image.load("ship.png")
        self.rect = self.image.get_rect()
        self.rect.y = self.screen.get_height() - 100
        self.moving_left = False
        self.moving_right = False
        self.ship_speed = 3
        self.x = (self.screen.get_width() / 2) - self.rect.width / 2

    #updates player movement every frame
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
