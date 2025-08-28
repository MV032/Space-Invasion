import pygame

class Ship:
    #initializes player setup
    def __init__(self, space_game):
        self.screen = space_game.screen
        self.screen_rect = space_game.screen.get_rect()
        self.image = pygame.image.load("ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_left = False
        self.moving_right = False
        self.ship_speed = 1.5
        self.x = float(self.rect.x)      

    #updates player movement every frame
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.ship_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.ship_speed
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
