'''
Created on Jul 4, 2017
@author: lzhang938

To illustration that the derived class method
will SHADOW the base class method, even for
the constructor-like __init__() method
'''

class Foo(object):
    def __init__(self):
        self.a = 10

    def do_something(self):
        print(self.a)

class Bar(Foo):
    def __init__(self):
        self.b = 20

if __name__ == '__main__':
    bar = Bar()
    bar.do_something() 