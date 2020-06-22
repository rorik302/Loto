from pytest import raises
from random import randint

from game.validators import int_option_validation, validate_players_count

def test_int_option_validation():
    assert isinstance(int_option_validation(5), int)
    with raises(ValueError):
        assert not isinstance(int_option_validation('a'), int)

def test_validate_players_count():
    valid_option = randint(2, 10)
    assert validate_players_count(valid_option)

    invalid_option = randint(0, 1)
    with raises(ValueError):
        assert validate_players_count(invalid_option) in [0, 1]
