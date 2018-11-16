from unittest import TestCase
from Mods.EC.Elliptic_Curve import EllipticCurve


class TestEllipticCurve(TestCase):
    def test(self):
        ec = EllipticCurve.get_instance(0, -2)
        terms = {'x^3': 1, 'x^2': 0, 'x^1': -2, 'y^2': -1, '1': 0}

        self.assertTrue(EllipticCurve.has_instance())

        for a in ec.terms.keys():
            self.assertEqual(ec.terms[a], terms[a])

        self.assertTrue(ec.includes(2, 2))
        self.assertTrue(ec.includes(-1, 1))

        EllipticCurve.remove_instance()
        self.assertFalse(EllipticCurve.has_instance())

        ec = EllipticCurve.get_instance(0, -1)
        terms = {'x^3': 1, 'x^2': 0, 'x^1': -1, 'y^2': -1, '1': 0}

        self.assertTrue(EllipticCurve.has_instance())

        for a in ec.terms.keys():
            self.assertEqual(ec.terms[a], terms[a])

        self.assertTrue(ec.includes(1, 0))
