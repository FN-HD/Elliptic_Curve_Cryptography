from Elliptic_Curve import EC
from Elliptic_Curve import RationalPointInEC

# This test source for object which we will use.

ec = EC.get_instance(0, -2)

p = RationalPointInEC(2, 2)
q = RationalPointInEC(2, -2)

print(ec)

print(2*p)
print(3*p+q)
print(4*p)
print(2*p+2*p)
print(p+q)
print(p-q)
print()

