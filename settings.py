import tkinter

class Settings():
    """saved settings for project"""

    def __init__(self):
        """init settings"""

        # screen settings group:
        # self.screen_width = 1280
        # self.screen_height = 800

        self.tk = tkinter.Tk()
        self.screen_width = self.default_screen_width = self.tk.winfo_screenwidth()
        self.screen_height = self.default_screen_height = self.tk.winfo_screenheight()
        self.screen_full = False


        self.bg_color = (204, 229, 255) # default screen background color

        # ship settings
        self.ship_limit = 3
        
        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 5

        # aliens settings
        self.fleet_drop_speed = 10
         
        # pace game
        self.speedup_scale = 1.1

        # pace scores
        self.score_scale = 1.5

        # init dymanic settings
        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Init settings that changed during the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.1
        self.fleet_direction = 1 #-1 - left direction

        self.alien_points = 50


    def increase_speed(self):
        """increase speed"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(round(self.alien_points * self.score_scale,0))