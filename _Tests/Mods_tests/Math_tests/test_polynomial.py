from unittest import TestCase
from Mods.Math.Polynomial import Polynomial


class TestPolynomial(TestCase):
    def test_init(self):
        poly = Polynomial({'x^3': 2, 'x^1': 2, 'x': 8, 'x^0': 22})

        self.assertEqual(poly, Polynomial({'x^3': 2, 'x^1': 10, '1': 22}))
        self.assertEqual(poly.get_differential_f('x'), Polynomial({'x^2': 6, '1': 10}))


