import pygame.font

class Lives:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.font = pygame.font.Font("press_start_2p_font.ttf", 28)
        self.prep_lives()

    def prep_lives(self):
        #lives title
        self.title_image = self.font.render("LIVES", True, (225,255,255), self.settings.bg_color)
        self.title_rect = self.title_image.get_rect()
        self.title_rect.left = self.screen_rect.left + 20
        self.title_rect.top = 20

        #lives number
        lives_str = str(self.stats.ships_left)
        self.lives_image = self.font.render(lives_str, True, self.settings.score_color, self.settings.bg_color)
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = self.screen_rect.left + 20
        self.lives_rect.top = 60

    def show_lives(self):
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.lives_image, self.lives_rect)