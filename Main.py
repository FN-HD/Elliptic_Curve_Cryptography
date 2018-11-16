from Elliptic_Curve import EC
from Rational_Point_In_EC import RationalPointInEC
from Rational_Number import RationalNumber

# This test source for object which we will use.

print(EC.get_instance(0, -2))

p0 = RationalPointInEC(2, 2)
p1 = RationalPointInEC(2, -2)

print(p0)
print(2*p0)
print(3*p0+p1)
print(4*p0)
print(2*p0+2*p0)
print(p0+p1)
print(p0-p1)

EC.remove_instance()
print()
print(EC.get_instance(0, -1))

q0 = RationalPointInEC(1, 0)
q1 = RationalPointInEC(-1, 0)
q2 = RationalPointInEC(RationalNumber(1, 23), RationalNumber(1, 5))

print(q0)
print(q1)

EC.remove_instance()
print()
print(EC.get_instance(0, -2))

r0 = RationalPointInEC(0, 0)
r1 = RationalPointInEC(-1, 1)
r2 = RationalPointInEC(2, 2)

print(r0)
print(r1)
print(r2)

print(r1 + r2)
print(r1 + 2*r2)




