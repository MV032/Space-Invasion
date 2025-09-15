import pygame

class Bullet(pygame.sprite.Sprite):
    #initialize a bullet
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0, 0, game.settings.bullet_width, game.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    #moves bullet upwards
    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    
    #creates the visual bullet
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)