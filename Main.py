from Elliptic_Curve import EC
from Rational_Point_In_EC import RationalPointInEC

# This test source for object which we will use.

print(EC.get_instance(0, -2))

p0 = RationalPointInEC(2, 2)
p1 = RationalPointInEC(2, -2)

print()
print(2*p0)
print(3*p0+p1)
print(4*p0)
print(2*p0+2*p0)
print(p0+p1)
print(p0-p1)
print()

EC.remove_instance()
print(EC.get_instance(0, -1))

q0 = RationalPointInEC(1, 0)

