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

        self.ship_speed = 1.2 #speed of ship's moving
