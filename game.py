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
from scoreboard import Scoreboard
from stats import Stats
from lives import Lives
from time import sleep

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
        self.stats = Stats(self)
        self.lives = Lives(self)
        self.scoreboard = Scoreboard(self)
        self._create_fleet()

    #runs the game and updates at 60 fps
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._check_fleet_edges()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _ship_hit(self):
        self.bullets.empty()
        self.aliens.empty()
        self.stats.ships_left -= 1
        if self.stats.ships_left == 0:
            self.stats.reset_stats()
            self.scoreboard.prep_score()
        self.lives.prep_lives()
        self._create_fleet()
        self.ship.x = (self.screen.get_width() / 2) - self.ship.rect.width / 2
        sleep(.5)

    def _update_aliens(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit() 
        self.aliens.update()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet()
                break

    def _change_fleet(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop
        self.settings.alien_direction *= -1

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
        self.scoreboard.show_score()
        self.lives.show_lives()
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

    #checks for collisions and when to remove bullets
    def _update_bullets(self):
        for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            self.stats.score += 100
            self.scoreboard.prep_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

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