import pygame
import sys

class SpaceInvasionGame:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((640, 480))
        # rest of settings

    def run_game(self):
        while True:
            self.check_events()
            self.update_objects()
            self.new_method()
            self.clock.tick(60)

    def new_method(self):
        self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_objects(self):
        pass

    def update_screen(self):
        pass

if __name__ == "__main__":
    game = SpaceInvasionGame()
    game.run_game()
