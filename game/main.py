import os
from time import sleep

from bag import Bag
from card import Card
from player import Player
from validators import int_option_validation, validate_players_count, action_validation


def wrong_option(option, players, player, barrel):
    if option == 'д':
        print(f'\nЧисла {barrel} нет на карточке. {player} проиграл')
    else:
        print(f'\nЧисло {barrel} есть на карточке. {player} проиграл')
    players.remove(player)
    sleep(2)


def main():
    players_list = []
    winners = []

    players_count_option = int_option_validation(
        input('Укажите количество игроков: ')
    )
    players_count = validate_players_count(players_count_option)

    for player_number in range(1, players_count + 1):
        player = Player()
        player.number = player_number
        player_type_option = int_option_validation(
            input('-'*40 + '\n'
                           f'Укажите тип игрока №{player.number}:\n'
                           '1. Человек.\n'
                           '2. Компьютер.\n'
                           'Вариант: ')
        )
        player.set_player_type(player_type_option)

        player.card = Card()

        players_list.append(player)

    print('\nНачинаем игру!')

    bag = Bag()

    while len(bag.barrels) > 0 and len(winners) == 0:
        if len(players_list) == 1:
            winners.append(players_list[0])
            break

        barrel = bag.pull()

        for player in players_list:
            card = player.card
            card.print_card(player)

        for player in players_list:
            card = player.card
            number_exists = card.is_number_exists(barrel)

            if player.type == 'Человек':
                action_option = action_validation(
                    input(f'\n{player}, зачеркнуть число? (д/н): ')
                )
                if action_option == 'д':
                    if number_exists:
                        card.cross(barrel)
                    else:
                        wrong_option(action_option, players_list, player, barrel)
                if action_option == 'н':
                    if number_exists:
                        wrong_option(action_option, players_list, player, barrel)

            if player.type == 'Компьютер':
                if number_exists:
                    card.cross(barrel)
                else:
                    continue

            if len(card.numbers) == 0:
                winners.append(player)

    for winner in winners:
        print(f'\n{winner} победил.')


if __name__ == '__main__':
    if 'script' in os.environ:
        if os.environ['script'] == 'test':
            os.system('pytest')
    else:
        main()
