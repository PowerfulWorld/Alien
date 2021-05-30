class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """инициализируеет настройки игры"""
        # параметры экрана
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_speed = 5
        self.ship_limit = 3

        # настройки снаряда
        self.bullet_speed = 4
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 влево
        self.fleet_direction = 1
