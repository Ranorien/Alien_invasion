import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion():
    """main class"""

    def __init__(self):
        pygame.init()

        # Get settings
        self.settings = Settings()

        # set paramters of screen
        self.screen = pygame.display.set_mode((self.settings.default_screen_width, self.settings.default_screen_height))
        pygame.display.set_caption('My the first game - "Alien Invasion" - for my son Vlad with love')

        # create stats
        self.stats = GameStats(self)

        # create object type Ship
        self.ship = Ship(self)

        # create group of bullets
        self.bullets = pygame.sprite.Group()

        # create group of aliens
        self.aliens = pygame.sprite.Group()
        self.__create_fleet()

        # create button Play
        self.play_button = Button(self, 'Play')

    def __update_after_screen_change(self):
        """change setting after screen resolution change"""
        self.ship.update_after_screen_change(self)
        self.aliens.empty()
        self.bullets.empty()
        self.__create_fleet()
        self.stats.reset_stats()

    def __check_keydown_events(self, event):
        """key down events"""
        match event.key:
            case pygame.K_ESCAPE:
                sys.exit()

            case pygame.K_q:
                sys.exit()

            case pygame.K_f:
                if self.settings.screen_full:
                    self.settings.screen_full = False
                    self.screen = pygame.display.set_mode((self.settings.default_screen_width, self.settings.default_screen_height))
                else:
                    self.settings.screen_full = True
                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

                self.__update_after_screen_change()

            case pygame.K_r:
                if not self.stats.game_active:
                    self.__start_game()


            case pygame.K_RIGHT:
                self.ship.moving_right = True

            case pygame.K_LEFT:
                self.ship.moving_left = True

            case pygame.K_SPACE:
                self.__fire_bullet()


    def __check_keyup_events(self, event):
        """keyup events"""
        match event.key:
            case pygame.K_RIGHT:
                self.ship.moving_right = False

            case pygame.K_LEFT:
                self.ship.moving_left = False

    def __mouse_button_click(self):
        """mouse button click events"""
        mouse_pos = pygame.mouse.get_pos()
        self.__check_play_button(mouse_pos)

    def __check_events(self):
            """Check events of keyboard and mouse"""
            for event in pygame.event.get():
                # print(event) #shows events IDs in terminal
                match event.type:
                    case pygame.QUIT:
                        sys.exit()

                    case pygame.KEYDOWN:
                        self.__check_keydown_events(event)

                    case pygame.KEYUP:
                        self.__check_keyup_events(event)

                    case pygame.MOUSEBUTTONDOWN:
                        self.__mouse_button_click()

    def __check_play_button(self, mouse_pos):
        """Start new game"""
        if self.play_button.rect.collidepoint(mouse_pos) and not self.stats.game_active:
            self.__start_game()
            

    def __start_game(self):
        """start game"""
        self.stats.reset_stats()
        self.stats.game_active = True

        self.aliens.empty()
        self.bullets.empty()

        self.__create_fleet()
        self.ship.center_ship()

        # hide mouse
        pygame.mouse.set_visible(False)

    def __fire_bullet(self):
        """create new bullet and add it to bullet's group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def __create_fleet(self):
        """creation of aliens fleet"""
        SHIFT_WIDTH = 2 #int
        SHIFT_HEIGHT = 2 #int

        alien = Alien(self) #create first alien to calculate alien.rect
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (SHIFT_WIDTH * alien_width)
        number_aliens_x = available_space_x // (SHIFT_WIDTH * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (2 * alien_height) - ship_height
        number_rows = available_space_y // (SHIFT_HEIGHT * alien_height)

        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.__create_alien(alien_number, row_number, SHIFT_WIDTH, SHIFT_HEIGHT)



    def __create_alien(self, alien_number, row_number, shift_width, shift_height):
        """create alien"""

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + shift_width * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + shift_height * alien_height * row_number
        self.aliens.add(alien)

    
    def __update_screen(self):
        """update screen"""
        # Set default color
        self.screen.fill(self.settings.bg_color)

        # draw Ship
        self.ship.blitme()

        # draw all bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # draw aliens
        self.aliens.draw(self.screen)

        # show button Play if game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()

        # apply screen changes
        pygame.display.flip()

    def __update_bullets(self):
        """update bullets in game control"""
        self.bullets.update()

        # delete inactive bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self.__check_bullet_alien_collisions()

        

    def __check_bullet_alien_collisions(self):
        """check collisions"""

        # check if bullet hit alien
        # if so, delete both
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if not self.aliens: 
            # if no more aliens, delete all bullets (if it was not deleted)
            self.bullets.empty()
            # create fleet again
            self.__create_fleet()


    def __update_aliens(self):
        """update position of all aliens"""
        self.__check_fleet_edges()
        self.aliens.update()

        # check collisions alien - ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.__ship_hit()

        self.__check_aliens_bottom()

    def __check_aliens_bottom(self):
        """check if fleet in on the bottom"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.__ship_hit()
                break

    def __ship_hit(self):
        """when ship is hit"""
        
        if self.stats.ships_left > 0:
            # decrease ships
            self.stats.ships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self.__create_fleet()
            self.ship.center_ship()

            sleep(1.5) #sleep 1.5 seconds
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def __check_fleet_edges(self):
        """check all aliens in fleet"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.__change_fleet_direction()
                break
                
    
    def __change_fleet_direction(self):
        """changes direction and sets down the fleet"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        
        self.settings.fleet_direction *= -1
        
    def run_game(self):
        """main loop on the screen"""
        while True:
            self.__check_events()

            if self.stats.game_active:
                self.ship.update()
                self.__update_bullets()
                self.__update_aliens()
                
            self.__update_screen()


def main():
    ai = AlienInvasion()

    # start window
    ai.run_game()


if __name__ == '__main__':
    main()