'''
When calling base class method and pass
'self', which object self refers to?
'''
class B(object):
    def __init__(self):
        self.m = 20

    def foo(self):
        print(self.m)

class D(B):
    def __init__(self):
        self.m = 30

    def foo(self):
        B.foo(self)

d = D()
d.foo()

