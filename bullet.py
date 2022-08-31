import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class for control bullets shooted from the ship"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # creation of bullet in position (0, 0) and set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)


    def update(self):
        """moving bullet up"""

        self.y -= self.settings.bullet_speed
        self.rect.y = int(round(self.y, 0))

    def draw_bullet(self):
        """draw bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)