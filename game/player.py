from game.validators import player_type_validation


class Player:

    def __init__(self):
        self.number = None
        self.type = None

    def __str__(self):
        return f'Игрок №{self.number}'

    def set_player_type(self, option):
        self.type = player_type_validation(option)
