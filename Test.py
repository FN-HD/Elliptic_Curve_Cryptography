from Polynomial import Polynomial
from Rational_Number import RationalNumber
import math


poly = Polynomial({'y^2': -1, 'x^3': 1, 'x^1': 1})

for d in range(1, 10000):
    for n in range(2, 10000):
        if math.gcd(n,d) != 1:
            continue
        a = RationalNumber(d, n)**3 - RationalNumber(d, n)
        a0 = a.num
        if a0 < 0:
            continue

        if a0 == int( math.sqrt(a0) ) ** 2:
            a1 = a.den
            print(d)
            print('-')
            print(n)
            print(a)
            print('success 1')
            if a1 == int(math.sqrt(a1)) ** 2:
                print(d)
                print('-')
                print(n)
                print(a)
                print('success 2')
                break

print('finish')

