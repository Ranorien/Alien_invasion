import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class to descbibe alien"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.image.set_colorkey((255, 255, 255)) #прозрачный фон - transparent background
        self.rect = self.image.get_rect()

        # set default position of new alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # horizontal position of the alien
        self.x = float(self.rect.x)

    def update(self):
        """moving alien"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = int(round(self.x, 0))

    def check_edges(self):
        """True if alien located closely to border"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >=screen_rect.right or self.rect.left <= 0:
            return True
