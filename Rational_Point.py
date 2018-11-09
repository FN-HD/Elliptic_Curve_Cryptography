from Rational_Number import RationalNumber


class RationalPoint:
    def __init__(self, arg):
        if isinstance(arg, list):
            pass
        elif isinstance(arg, (int, RationalNumber)):
            arg = [arg]
        else:
            raise TypeError('you should input list or RationalNumber')

        k = 0

        while k < len(arg):
            arg[k] = RationalNumber(arg[k])
            k = k + 1

        self.pair = tuple(arg[k])

    def __add__(self, other):
        if isinstance(other, RationalNumber):
            if len(self) == len(other):
                return NotImplemented

            new_list = []

            for i, x in enumerate(self):
                new_list[i] = x + other[i]

            return RationalPoint(new_list)
        else:
            return NotImplemented

    def __getattr__(self, item):
        if item == 'list':
            return list(self.pair)
        else:
            raise AttributeError(item)

    def __getitem__(self, item):
        if isinstance(item, int):
            if 0 <= item < len(self.pair):
                return self.pair[item]
            raise TypeError('out of list')
        else:
            raise AttributeError(item)

    def __len__(self, other):
        return len(self.pair)
