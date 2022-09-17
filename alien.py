from re import S
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class to descbibe alien"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # load alien image
        self.image = pygame.image.load('images/alien.bmp')
        self.image.set_colorkey((255, 255, 255)) #прозрачный фон - transparent background
        self.rect = self.image.get_rect()

        # set default position of new alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # horizontal position of the alien
        self.x = float(self.rect.x)
