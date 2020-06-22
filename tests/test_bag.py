from pytest import fixture

from game.bag import Bag


@fixture()
def bag():
    bag = Bag()
    return bag

class TestBag:

    def test_generate_barrels(self, bag):
        assert len(bag.barrels) == 90

    def test_get_barrel(self, bag):
        barrel = bag.get_barrel()
        assert barrel in bag.barrels

    def test_remove_barrel(self, bag):
        barrel = 10
        bag.barrels.remove(barrel)
        assert barrel not in bag.barrels
