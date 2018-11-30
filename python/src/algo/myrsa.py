import math
import unittest

class ZRSA:
    # This is to implement the basic RSA algorithm
    # https://www.youtube.com/watch?v=D_kMadCtKp8

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self._r = None

        self.verify()

    def verify(self):
        if self.a <= 0 or self.b <= 0:
            raise ValueError('Must be positive numbers')
        if self.a < self.b:
            self.a, self.b = self.b, self.a     # exchange a and b to make a the bigger one

    def gcd(self):
        a, b = self.a, self.b
        r = a % b
        while ( r > 0 ):
            a, b = b, r
            r = a % b
        print("a={}, b={}, r={}".format(a, b, r))
        self._r = b
        return b

    def relative_prime(self):
        if self._r == None:
            self.gcd()
        return self._r == 1

    @property
    def r(self):
        if self._r == None:
            self.gcd()
        return self._r

    @staticmethod
    def is_prime(a):
        if  a<=1:
            raise ValueError('Must be a positive number')

        for i in range(2, int(math.sqrt(a))+1):
            if a % i == 0:
                print('{} is not prime because it has factor {}'.format(a, i))
                return False
        return True

    @staticmethod
    def is_prime_1(n):
        if  n<=1:
            raise ValueError('Must be a positive number')

        from itertools import count, islice
        return all(n%i for i in islice(count(2), int(math.sqrt(n)-1)))

    # Miller-Rabin prime test algorith is based on Fermat's litte theorem
    # if p is a prime numbrer, then for any integer a
    #         a^p === a (mod p)
    # For example: 2^7 === 2 (mod 7): 126 = 7 x 18
    #
    # If a is not divisible by p, it is equivalent to
    #         a^(p-1) === 1 (mod p)
    # For example: 2^6 === 1 (mod 7): 63 = 7 x 9
    # Since p-1 is even, it can be writen as p-1 = 2^r * d
    #
    # Specifically, if p is a prime and q^2 === 1 (mod p), then
    #          (q + 1)(q -1 ) === 0 (mod p)
    # which means either p divides q+1 or q-1

    @staticmethod
    def is_prime_Miller_Rabin(p):
        d = p - 1
        r = 0

        while d % 2 == 0:
            d //= 2
            r += 1
        print('d={}, r={}'.format(d,r))

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.rsa1 = ZRSA(15, 8)
        self.rsa2 = ZRSA(15, 5)
        self.rsa3 = ZRSA(324, 24)
        self.rsa4 = ZRSA(153, 34)

    def test_gcd(self):
        assert self.rsa1.r == 1
        assert self.rsa2.r == 5
        assert self.rsa3.r == 12
        assert self.rsa4.r == 17

    def test_prime(self):
        self.assertTrue(ZRSA.is_prime(4567))
        self.assertTrue(ZRSA.is_prime(124567))
        self.assertTrue(ZRSA.is_prime(3214567))
        self.assertTrue(ZRSA.is_prime(23456789))
        self.assertTrue(ZRSA.is_prime(55566677))
        # self.assertTrue(ZRSA.is_prime(1234567894987654321))

        self.assertTrue(ZRSA.is_prime(2))
        self.assertTrue(ZRSA.is_prime(31))
        self.assertFalse(ZRSA.is_prime(49))
        self.assertTrue(ZRSA.is_prime(769))
        self.assertTrue(ZRSA.is_prime(65537))       # The last know Fermat Prime of 2^2^4+1
        self.assertFalse(ZRSA.is_prime(4294967297)) # The Fermat Prime of 2^2^5+1

        self.assertTrue(ZRSA.is_prime_1(2))
        self.assertTrue(ZRSA.is_prime_1(31))
        self.assertFalse(ZRSA.is_prime_1(49))
        self.assertTrue(ZRSA.is_prime_1(769))
        self.assertTrue(ZRSA.is_prime_1(65537))       # The last know Fermat Prime of 2^2^4+1
        self.assertFalse(ZRSA.is_prime_1(4294967297)) # The Fermat Prime of 2^2^5+1

    def test_MR(self):
        ZRSA.is_prime_Miller_Rabin(103)
        ZRSA.is_prime_Miller_Rabin(569)

if __name__ == '__main__':
    unittest.main()
