class GameStats():
    """saving of game stats"""

    def __init__(self, ai_game):
        """init stats"""
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

    def reset_stats(self):
        """init stats"""
        self.ships_left = self.settings.ship_limit