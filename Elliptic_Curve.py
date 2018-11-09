from Rational_Number import RationalNumber
from Polynomial import Polynomial

# Elliptic Curve
class EC(Polynomial):
    def __init__(self, a, b=0, c=0):
        if 'internal_access' in dir(EC):
            if EC.internal_access:
                EC.internal_access = False
            else:
                raise TypeError('you are wrong')
        else:
            raise TypeError('you are wrong')

        super().__init__(
            {
                'y^2': -1, 'x^3': 1, 'x^2': RationalNumber(a),
                'x^1': RationalNumber(b), '1': RationalNumber(c)
             }
        )

    # we can check whether this function includes point(x, y).
    def includes(self, x, y):
        if isinstance(x, (RationalNumber, int)) and isinstance(y, (RationalNumber, int)):
            return (super().input(x, 'x')).input(y, 'y')['1'] == 0
        else:
            return False

    # method about check multiple root of x.
    def has_multiple_root_of_x(self):
        return 0 == self.get_discriminant_value_of_x()

    # We can get Discriminant of self equation.(f(x)=0,y=0)
    def get_discriminant_value_of_x(self):
        a = self[2]
        b = self[1]
        c = self[0]

        return -4*(a**3)*(c**3) + (a**2)*(b**2) + 18*a*b*c - 4*(b**3) - 27*(c**2)

    # The following functions are special methods.
    def __add__(self, other):
        if isinstance(other, EC):
            return EC(
                (self[2]+other[2])/2, (self[1]+other[1])/2, (self[0]+other[0])/2
            )
        else:
            return NotImplemented

    # We can get a coefficient of x, which has key index.
    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 == item:
                item = '1'
            elif 0 < item < 4:
                item = 'x^' + str(item)

        return super().__getitem__(item)

    # The following functions are singleton methods.
    # We can get instance.
    # We cannot use default constructor.
    @staticmethod
    def get_instance(a=0, b=0, c=0):
        if EC.has_instance():
            return EC.instance
        else:
            EC.internal_access = True
            EC.instance = EC(a, b, c)
            return EC.instance

    # Whether Ec is created.
    @staticmethod
    def has_instance():
        return 'instance' in dir(EC)

    # We can remove EC.
    @staticmethod
    def remove_instance():
        if EC.has_instance():
            del EC.instance

class RationalPointInEC:
    def __init__(self, x0=0, x1=None):
        if not EC.has_instance():
            raise TypeError('EC does not exist')

        self.ec = EC.get_instance()

        if self.ec.has_multiple_root_of_x():
            raise TypeError('EC has multiple root for f(x)')

        if x0 is None or x1 is None:
            # pair = (0, None) is a point at infinity.
            # because the point at infinity in elliptic curve is x = 0. (x^3=0)
            x0 = 0
            x1 = None
        else:
            x0 = RationalNumber(x0, 1)
            x1 = RationalNumber(x1, 1)

        if self.ec.includes(x0, x1) or x1 is None:
            self.pair = (x0, x1)
        else:
            raise TypeError('EC does not have this point')

    # We can get slope of self and other.
    def get_slope(self, other):
        if isinstance(other, RationalPointInEC):
            d = 0

            if self == other:
                for a in self.ec.get_differential_f('x'):
                    if a[0] == '1':
                        d += a[1]
                        continue

                    d += a[1] * (self.x ** int(a[0].split('^')[1]))

                d = d / (2 * self.y)
            else:
                d = (self.y - other.y) / (self.x - other.x)

            return d
        else:
            return NotImplemented

    # boolean method
    # Whether self is a point at infinity.
    def is_a_point_at_infinity(self):
        return self.y is None

    # Whether self is in EC.
    def is_in_EC(self):
        if self.is_a_point_at_infinity():
            return True
        else:
            return self.ec.includes(self.x, self.y)

    # Special method.
    # It is a method for addition.
    def __add__(self, other):
        if isinstance(other, RationalPointInEC):
            return -(self*other)
        else:
            return NotImplemented

    # It is a method for equivalent.
    def __eq__(self, other):
        if isinstance(other, RationalPointInEC):
            if self.is_a_point_at_infinity():
                return other.is_a_point_at_infinity()
            else:
                return self.x == other.x and self.y == other.y
        else:
            return NotImplemented

    # It is a method for item.
    def __getattr__(self, item):
        if item == 'x':
            return self.pair[0]
        elif item == 'y':
            return self.pair[1]
        else:
            raise AttributeError(item)

    # It is a method for inverse of addition.
    def __neg__(self):
        if self.is_a_point_at_infinity():
            return self
        else:
            return RationalPointInEC(self.x, -self.y)

    # It is a method for int mul or to get cross point
    def __mul__(self, other):
        if isinstance(other, RationalPointInEC):
            return self.__mul_with_point(other)
        elif isinstance(other, int):
            return self.__mul_with_int(other)
        else:
            return NotImplemented

    # It is a method for commutative mul.
    def __rmul__(self, other):
        return self*other

    # It is a method for subtraction.
    def __sub__(self, other):
        return self + (other.__neg__())

    # It is a method for string.
    def __str__(self):
        if self.is_a_point_at_infinity():
            return 'O'
        else:
            return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # The following method is a method for special method.
    # It is a method for getting cross point of ec and line, which has self and other.
    def __mul_with_point(self, other):
        if not isinstance(other, RationalPointInEC):
            return NotImplemented

        if self.is_a_point_at_infinity():
            return other
        elif other.is_a_point_at_infinity():
            return self
        elif self == -other:
            return RationalPointInEC()

        d = self.get_slope(other)
        x = -self.x-other.x-(self.ec[2]-d**2)/self.ec[3]
        y = d*(x-self.x)+self.y

        return RationalPointInEC(x, y)

    # It is a method for mul with integer.
    def __mul_with_int(self, other):
        if not isinstance(other, int):
            return NotImplemented

        if other > 1:
            return self * (other - 1) + self
        elif other == 1:
            return self
        elif other == 0:
            return self - self
        else:
            return -(self * (-other))
