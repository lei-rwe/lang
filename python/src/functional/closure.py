import unittest

def maker(N):
    def action(X):      # Make and return action
        return X ** N   # action retains N from enclosing scope
    return action

def maker_lambda(N):
    return lambda X: X ** N

class ClosureTest(unittest.TestCase):
    def test_1(self):
        print("test_1")
        f = maker(2)
        print(f)
        print('f(3) is: {0}'.format(f(3)))
        print('f(4) is: {0}'.format(f(4)))

    def test_2(self):
        print("test_2")
        f = maker(2)
        g = maker(3)
        print('f(4) is: {0}'.format(f(4)))
        print('g(4) is: {0}'.format(g(4)))

    def test_3(self):
        print("test_3")
        f = maker_lambda(2)
        g = maker_lambda(3)
        print('f(4) is: {0}'.format(f(4)))
        print('g(4) is: {0}'.format(g(4)))

if __name__ == '__main__':
    unittest.main()