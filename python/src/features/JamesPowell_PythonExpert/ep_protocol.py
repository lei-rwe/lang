#
# Python datamodel: protocol view, protocol oriented datamodel
#
# From "What Does It Take To Be An Export At Python?
# From PyData Presentation at Microsoft by James Power
# https://www.youtube.com/watch?v=7lmCu8wz8ro
# The above video is downloaded by RealPlayer

# dunder methods: (double underscore methods)
# Some behavior that I want to implement -> write some __ function__
# top-level function or top-level syntax -> corresponding __method__

# https://docs.python.org/3/reference/datamodel.html

class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return 'Polynomial {!r}'.format(self.coeffs)

    def __add__(self, other):
        return Polynomial( *(a+b for (a, b) in zip(self.coeffs, other.coeffs)) )

    def __len__(self):
        return len(self.coeffs)

p1 = Polynomial(1, 3, 2)
p2 = Polynomial(2, 3, 1)
p3 = p1 + p2
import pdb; pdb.set_trace()