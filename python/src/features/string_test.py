import unittest

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

class FirstClass: # Define a class object
    def __init__(self, value): # Define class's methods
        self.data = value # self is the instance
    def display(self):
        print(self.data) # self.data: per instance

def gensquares(N):
    for i in range(N):
        yield i ** 2
        print('{}-{}'.format(i, i**2))

class StringTest(unittest.TestCase):
    def test_translate(self):
        for i in gensquares(5):
            print(i, end=' : ')

    def test_class(self):
        obj = FirstClass(30)
        obj.display()

    def test_a1(self):
        bob = Person('Bob Smith') # Test the class
        sue = Person('Sue Jones', job='dev', pay=100000) # Runs __init__ automatically
        print(bob.name, bob.pay) # Fetch attached attributes
        print(sue.name, sue.pay) # sue's and bob's attrs differ


if __name__ == '__main__':
    unittest.main()