# PythonDecorators/my_decorator.py
class my_decorator(object):
    def __init__(self, f):
        print("inside my_decorator.__init__()")
        # f() # Prove that function definition has completed
        self.f = f
    def __call__(self, *args):
        print("inside my_decorator.__call__()")
        self.f(*args)

@my_decorator
def aFunction(x):
    print("inside aFunction()" + str(x))

aFunction(22)
print("Finished decorating aFunction()")
