from validators import player_type_validation


class Player:

    def __init__(self):
        self.number = None
        self.type = None

    def set_player_type(self, option):
        self.type = player_type_validation(option)
