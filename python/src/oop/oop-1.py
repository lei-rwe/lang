class A(object):
    def foo(self):
        print "A::foo"

class B(A):
    def foo1(self):
        print "B::foo"

class C(A):
    def foo(self):
        print "C::foo"

class D(B, C):
    def test(self):
        self.foo()

obj = D()
obj.test()
