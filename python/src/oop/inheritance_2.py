'''
This is to show the difference of the new-style
class definition from the classic class definition.
In the new style, attributes are fetched at
class level, not instance level.
In other words, the attribute fetch
    for classic class: obj.__X__
    for new-style: type(obj).__X__(obj, args)

Two reasons:
    1. performance: new style searches one level less
    2. call pattern issue:

Note: this needs to be tested in python 2. In python 3,
all classes are default to new style classes
'''
class A:
    def __add__(self, v):
        return 100 + v

class B(object):
    def __add__(self, v):
        return 1000 + v

class C(object):
    data = 'spam'
    def __getattr__(self, name):
        print('getattr: ' + str(name))
        return getattr(self.data, str(name))

class A1(A):
    pass

class B1(B):
    pass

if __name__ == '__main__':
    a = A()
    b = B()

    a.__add__ = lambda t  : 50 + t
    b.__add__ = lambda t  : 500 + t

    print(a + 1)
    print(b + 1)

    print("Now testing derived class ...")
    a1 = A1()
    b1 = B1()

    a1.__add__ = lambda t  : 30 + t
    b1.__add__ = lambda t  : 300 + t

    print(a1 + 1)
    print(b1 + 1)

    print("Now testing class for __getattr__...")
    c = C()
    print(c.__add__('eggs'))
    print(c.upper())
    print(c + 'eggs')