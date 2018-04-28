class A(object):
    def __init__(self):
        self.value = 'A'

    def get_value(self):
        print(self.value)

class B(A):
    def __init__(self):
        self.value = 'B'

    def get_it(self):
        print(self.value)

class C(B):
    def __init__(self):
        self.value = 'C'

    def get_it(self):
        print(self.value)

class Foo(object):
    def __init__(self):
        self.a = 10

    def do_something(self):
        print(self.a)

class Bar(Foo):
    def __init__(self):
        Foo.__init__(self)
        self.b = 20


if __name__ == "__main__":
    a = A()
    b = B()
    c = C()

    print(dir(a))
    print(dir(b))
    print(dir(c))

    b.get_value()
    c.get_value()

    bar = Bar()
    bar.do_something()
