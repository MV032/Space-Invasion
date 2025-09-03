# @name: Christopher Dougherty
# @date: 8-2025
# @title: Space Invasion
# @desc: Simple recreation of Space Invaders in python

import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class SpaceInvasionGame:
    #initializes game setup
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Space Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    #runs the game and updates at 60 fps
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            self.aliens.update()
            self._update_screen()
            self.clock.tick(60)

    #check for keyboard inputs
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    #update bullets and ship every frame
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        pygame.display.flip()

    #check which key is pressed and associate that to an event
    def _check_key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()

    #check when a key is released to stop player movement
    def _check_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    #creates a new bullet and adds it to the bullets group
    def _fire_bullet(self):
        if len(self.bullets) < 3: #no more than 3 bullets at a time
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    #spawns aliens in a grid style, keeping them on screen and above player
    def _create_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - (3 * alien_height)):
            while current_x < (self.settings.screen_width - (2 * alien_width)):
                self._make_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_y += 2 * alien_height
            current_x = alien_width
    
    #creates an alien and adds it to the alien group
    def _make_alien(self, x, y):
        new_alien = Alien(self)
        new_alien.x = x
        new_alien.rect.x = x
        new_alien.rect.y = y 
        self.aliens.add(new_alien)

if __name__ == "__main__":
    game = SpaceInvasionGame()
    game.run_game()
