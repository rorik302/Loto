from random import choice


class Bag:

    def __init__(self):
        self.barrels = [barrel for barrel in range(1, 91)]

    def pull(self):
        barrel = choice(self.barrels)
        self.barrels.remove(barrel)
        print(f'\nНовый бочонок: {barrel} (осталось {len(self.barrels)})')
        return barrel
