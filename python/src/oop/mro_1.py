class X(object):
    def who_am_i(self):
        print("I am a A")

class Y(object):
#   def who_am_i(self):
#       print("I am a B")
    pass

class A(X, Y):
    def who_am_i(self):
        print("I am a C")

class B(X, Y):
#   def who_am_i(self):
#       print("I am a D")
    pass

class C(A, B):
    pass

if __name__ == "__main__":
    pass
