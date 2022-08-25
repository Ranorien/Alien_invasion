import sys
import pygame
from settings import Settings

class AlienInvasion():
    """main class"""

    def __init__(self):
        pygame.init()

        # Get settings
        self.settings = Settings()


        # set paramters of screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('My the first game - Alien Invasion')


    def run_game(self):
        """main loop on the screen"""
        while True:
            # Check events of keyboard and mouse
            for event in pygame.event.get():
                # print(event) shows events IDs in terminal
                if event.type == pygame.QUIT:
                    sys.exit()

            # Set default color
            self.screen.fill(self.settings.bg_color)

            # apply screen changes
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()

    # start window
    ai.run_game()