class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""
    def __init__(self, ai_game):
        """инициализация статистики"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0

        # Игра запускается в неактивном режиме
        self.game_active = False

    def reset_stats(self):
        """Инициализирует статистику изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
