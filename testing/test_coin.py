from unittest import TestCase


class TestCoin(TestCase):
    def test_reset_pos(self):
        from game import Coin
        c = Coin()
        self.assertEquals(c.center_x, 0)
        c.update()
