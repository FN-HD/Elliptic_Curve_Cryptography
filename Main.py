from Elliptic_Curve import EC
from Rational_Point_In_EC import RationalPointInEC

# This test source for object which we will use.

print(EC.get_instance(0, -2))

p = RationalPointInEC(2, 2)
q = RationalPointInEC(2, -2)

print(2*p)
print(3*p+q)
print(4*p)
print(2*p+2*p)
print(p+q)
print(p-q)

print()

EC.remove_instance()
print(EC.set_memento('0'))



