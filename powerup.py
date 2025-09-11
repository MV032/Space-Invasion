import pygame

class Powerup(pygame.sprite.Sprite):
    def __init__(self, game, num=1, x=0, y=0):
        super().__init__()
        self.settings = game.settings
        self.screen = game.screen
        self.num = num
        self._load_image(num)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.reset_power_ups()
        
    def _load_image(self, num):
        image = "ammo.png"
        if num == 1: 
            image = "speed.png" 
        elif num == 2: 
            image = "ammo.png" 
        elif num == 3: 
            image = "super_bullet.png"
        self.image = pygame.image.load(image)

    def update(self):
        self.y += 1
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