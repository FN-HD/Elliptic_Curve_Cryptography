from Polynomial import Polynomial


poly1 = Polynomial({'x^3': 2, 'x^1': 2, 'y^1': 0, '1': 3})
poly2 = Polynomial({'x^2': 1, 'y^1': 2, '1': 1})


print(poly1)
print(poly2)
print(poly1 + poly2)
print(poly1 - poly2)
print(poly1 * poly2)
