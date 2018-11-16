from unittest import TestCase
from Mods.EC.Elliptic_Curve import EllipticCurve
from Mods.EC.Rational_Point_In_EC import RationalPointInEC
from Mods.Math.Rational_Number import RationalNumber


class TestRationalPointInEC(TestCase):
    def test(self):
        EllipticCurve.get_instance(0, -2)

        o = RationalPointInEC()
        p0 = RationalPointInEC(2, 2)
        p1 = RationalPointInEC(2, -2)
        p2 = RationalPointInEC(RationalNumber(9, 4), RationalNumber(-21, 8))
        p3 = RationalPointInEC(RationalNumber(12769, 7056), RationalNumber(900271, 592704))

        self.assertEqual(p0.pair, (2, 2))
        self.assertEqual(p1.pair, (2, -2))
        self.assertEqual((-p1).pair, (2, 2))
        self.assertEqual(p2.pair, (RationalNumber(9, 4), RationalNumber(-21, 8)))
        self.assertEqual(p3.pair, (RationalNumber(12769, 7056), RationalNumber(900271, 592704)))

        self.assertEqual(2 * p0, p2)
        self.assertEqual(3 * p0 + p1, p2)
        self.assertEqual(4 * p0, p3)
        self.assertEqual(2 * p0 + 2 * p0, p3)
        self.assertEqual(p0 + p1, o)
        self.assertEqual(p0 - p1, p2)

        EllipticCurve.remove_instance()
        EllipticCurve.get_instance(0, -2)

        r0 = RationalPointInEC(0, 0)
        r1 = RationalPointInEC(-1, 1)
        r2 = RationalPointInEC(2, 2)
        r3 = RationalPointInEC(RationalNumber(-8, 9), RationalNumber(-28, 27))
        r4 = RationalPointInEC(RationalNumber(-1, 169), RationalNumber(239, 2197))

        self.assertEqual(r0.pair, (0, 0))
        self.assertEqual(r1.pair, (-1, 1))
        self.assertEqual(r2.pair, (2, 2))
        self.assertEqual(r3.pair, (RationalNumber(-8, 9), RationalNumber(-28, 27)))
        self.assertEqual(r4.pair, (RationalNumber(-1, 169), RationalNumber(239, 2197)))

        self.assertEqual(r1 + r2, r3)
        self.assertEqual(r1 + 2 * r2, r4)

        with self.assertRaises(TypeError):
            RationalPointInEC(0, -1)

    def test_error(self):
        EllipticCurve.get_instance(0, -2)

        r1 = RationalPointInEC(-1, 1)
        r2 = r1 + r1
        o = r1 - r1

        EllipticCurve.remove_instance()

        EllipticCurve.get_instance(2, 1, 1)

        self.assertFalse(r1.is_in_the_EC())

        with self.assertRaises(TypeError):
            r1 + r1 == r2

        with self.assertRaises(TypeError):
            r1 + o == r1




