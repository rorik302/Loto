def int_option_validation(option):
    try:
        return int(option)
    except ValueError:
        raise ValueError('Нужно указать число!')


def validate_players_count(option):
    if option >= 2:
        return option
    raise ValueError('Должно быть не менее 2-х игроков')


def player_type_validation(option):
    if option == 1:
        return 'Человек'
    if option == 2:
        return 'Компьютер'
    raise ValueError('Неправильный вариант')


def action_validation(option):
    if option.lower() in ['д', 'н']:
        return option.lower()
    raise ValueError('Неправильный вариант')
