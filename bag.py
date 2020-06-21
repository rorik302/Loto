from random import choice


class Bag:

    def __init__(self):
        self.barrels = self.generate_barrels()

    def generate_barrels(self):
        return [barrel for barrel in range(1, 91)]

    def get_barrel(self):
        return choice(self.barrels)

    def remove_barrel(self, barrel):
        self.barrels.remove(barrel)

    def print_barrel(self, barrel):
        print(f'\nНовый бочонок: {barrel} (осталось {len(self.barrels)})')

    def pull(self):
        barrel = self.get_barrel()
        self.remove_barrel(barrel)
        self.print_barrel(barrel)
        return barrel
