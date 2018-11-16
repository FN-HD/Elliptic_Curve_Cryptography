from Mods.EC.Elliptic_Curve import EllipticCurve
from Mods.EC.Rational_Point_In_EC import RationalPointInEC
from Mods.Math.Polynomial import Polynomial

print(EllipticCurve.get_instance(0, -2))

o = RationalPointInEC(0, 0)
r1 = RationalPointInEC(-1, 1)
r2 = RationalPointInEC(2, 2)

print('show value')
print('o = ' + str(o))
print('r1 = '+str(r1))
print('r2 = '+str(r2))

print('show calculation')
print('r1 + o = '+str(r1 + o))
print('r2 + r1 = '+str(r2 + r1))
print('2 * r1 = '+str(2*r1))
print('\'4*r1 == 3*r1 + r1\' is ' + str(4*r1 == 3*r1 + r1))
