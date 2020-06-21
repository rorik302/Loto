from pytest import fixture

from card import Card


@fixture()
def card():
    return Card()


class TestCard:

    def test_set_numbers(self, card):
        assert len(card.numbers) == 15

    def test_create_card(self, card):
        assert len(card.card) == 3
        for row in card.card:
            assert len(row) == 9
