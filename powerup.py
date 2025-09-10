import pygame

class Powerup:
    def __init__(self, game):
        self.settings = game.settings
        self.reset_power_ups()
        
    def draw_power_up(self, num, pos):
        image
        if num == 1: 
            image = "speed.png" 
        elif num == 2: 
            image = "ammo.png" 
        elif num == 3: 
            image = "super_bullet.png"
            
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x, self.y = pos

    def update(self):
        self.y -= 5
        self.rect.y = self.y

    def reset_power_ups(self):
        self.settings.player_speed = 3
        self.settings.bullets_allowed = 3
        self.settings.bullet_width = 3
        self.settings.bullet_height = 15

    def activate_power_up(self, num):
        if num == 1: #speed
            self.settings.player_speed = 8
        elif num == 2: #ammo
            self.settings.bullets_allowed = 10
        elif num == 3: #super bullet
            self.settings.bullet_width = 9
            self.settings.bullet_height = 45