from Rational_Number import RationalNumber
from Polynomial import Polynomial
from Caretaker import Caretaker
from Memento import Memento


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

        a = RationalNumber(a)
        b = RationalNumber(b)
        c = RationalNumber(c)

        if -4*(a**3)*(c**3) + (a**2)*(b**2) + 18*a*b*c - 4*(b**3) - 27*(c**2) == 0:
            raise TypeError('this poly has multiple root. ')
        else:
            super().__init__({'y^2': -1, 'x^3': 1, 'x^2': a, 'x^1': b, '1': c})

    # we can check whether this function includes point(x, y).
    def includes(self, x, y):
        if isinstance(x, (RationalNumber, int)) and isinstance(y, (RationalNumber, int)):
            return (super().input(x, 'x')).input(y, 'y')['1'] == 0
        else:
            return False

    # We can get Discriminant of self equation.(f(x)=0,y=0)
    def get_discriminant_value_of_x(self):
        a = self[2]
        b = self[1]
        c = self[0]

        return -4*(a**3)*(c**3) + (a**2)*(b**2) + 18*a*b*c - 4*(b**3) - 27*(c**2)

    # We can get a coefficient of x, which has key index.
    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 == item:
                item = '1'
            elif 0 < item < 4:
                item = 'x^' + str(item)

        try:
            return super().__getitem__(item)
        except AttributeError:
            pass

        if isinstance(item, str):
            return 0
        else:
            raise AttributeError(item)

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
    def remove_instance(name=''):
        if EC.has_instance():
            ct = Caretaker.get_instance()
            ec = EC.get_instance()
            ct.set(name, [ec[0], ec[1], ec[2]])

            del EC.instance

    # Method for memento.
    @staticmethod
    def get_memento(key):
        return Caretaker.get_instance()[key]

    @staticmethod
    def set_memento(key):
        if isinstance(key, Memento):
            return EC.get_instance(key.a, key.b, key.c)
        elif isinstance(key, str):
            return EC.set_memento(EC.get_memento(key))


