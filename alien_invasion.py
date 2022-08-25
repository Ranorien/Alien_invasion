from re import A
import sys
import pygame

class AlienInvasion():
    """main class"""

    def __init__(self):
        pygame.init()

        # set paramters of screen
        self.screen = pygame.display.set_mode((1280, 800))
        pygame.display.set_caption('My the first game - Alien Invasion')

    def run_game(self):
        """main loop on the screen"""
        while True:
            # Check events of keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Show last screen
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()

    # start window
    ai.run_game()