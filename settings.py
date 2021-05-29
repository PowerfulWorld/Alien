class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """инициализируеет настройки игры"""
        # параметры экрана
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_speed = 1.5
