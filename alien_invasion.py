import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion():
    """main class"""

    def __init__(self):
        pygame.init()

        # Get settings
        self.settings = Settings()

        # set paramters of screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('My the first game - Alien Invasion')

        # create object type Ship
        self.ship = Ship(self)

    def __check_events(self):
            """Check events of keyboard and mouse"""
            for event in pygame.event.get():
                # print(event) #shows events IDs in terminal
                if event.type == pygame.QUIT:
                    sys.exit()

    def __update_screen(self):
        # Set default color
        self.screen.fill(self.settings.bg_color)

        # draw Ship on default position
        self.ship.blitme()

        # apply screen changes
        pygame.display.flip()
        
    def run_game(self):
        """main loop on the screen"""
        while True:
            self.__check_events()
            self.__update_screen()

            

if __name__ == '__main__':
    ai = AlienInvasion()

    # start window
    ai.run_game()
    

    