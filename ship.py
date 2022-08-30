import pygame

class Ship():
    """Class for Space Ship"""

    def __init__(self, ai_game):
        """Init Ship a set default position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.image.set_colorkey((255, 255, 255)) #прозрачный фон - transparent background
        self.rect = self.image.get_rect()

        # set default position
        self.rect.midbottom = self.screen_rect.midbottom

        # moving right flag
        self.moving_right = False

        # moving left flag
        self.moving_left = False

        # position of the ship
        self.x = float(self.rect.x)

    def blitme(self):
        """draw ship in current position"""
        self.screen.blit(self.image, self.rect)

    def update_after_screen_change(self, ai_game):
        """update ship position after screen resolution changes"""

        self.screen_rect = ai_game.screen.get_rect()
        self.settings.screen_width = self.screen_rect.width
        self.settings.screen_height = self.screen_rect.height
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.screen_rect.width / 2

    def update(self):
        """updating of the ship position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # set position of ship
        self.rect.x = int(round(self.x,0))
  
