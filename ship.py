import pygame

class Ship():
    """Class for Space Ship"""

    def __init__(self, ai_game):
        """Init Ship a set default position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.image.set_colorkey((255, 255, 255)) #прозрачный фон - transparent background
        self.rect = self.image.get_rect()

        # set default position
        # self.rect.midbottom = self.screen_rect.midbottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """draw ship in current position"""
        self.screen.blit(self.image, self.rect)