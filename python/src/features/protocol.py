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