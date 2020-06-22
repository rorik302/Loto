from random import randint, sample


class Card:

    def __init__(self):
        self.numbers = self.set_numbers()
        self.card = []
        self.create_card()

    @staticmethod
    def generate_number():
        return randint(1, 90)

    def set_numbers(self):
        numbers = []
        while len(numbers) < 15:
            number = self.generate_number()
            if number not in numbers:
                numbers.append(number)
            else:
                return self.set_numbers()
        return numbers

    def create_card(self):
        self.card = [
            sample(self.numbers[i:i + 5] + [0] * 4, 9) for i in range(0, len(self.numbers), 5)
        ]

    def print_card(self, player):
        print(f'Карточка игрока №{player.number} ({player.type})'.center(40, '-'))
        for row in self.card:
            str_row = []
            for number in row:
                if number == 0:
                    number = ''
                str_row.append(str(number).rjust(2))
            print(('|' + ' '.join(str_row) + '|').center(40))
        print('-'*40)

    def is_number_exists(self, number):
        return number in self.numbers

    def cross(self, number):
        self.card = [['--' if num == number else num for num in row] for row in self.card]
        self.numbers.remove(number)
