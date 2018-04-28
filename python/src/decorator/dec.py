class ctracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("call #{0} of function {1}".format(self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

calls = 0
def ftracer(func):
    def onCall(*args, **kwargs):
        global calls
        calls += 1
        print("call #{0} of function {1}".format(calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

class Person:
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    @ftracer
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    @ctracer
    def lastName(self):
        return self.name.split()[-1]

@ctracer
def spam(a, b, c):
    print(a + b + c)

if __name__ == "__main__":
    spam(1, 2, 3)
    spam(a=4, b=5, c=6)

    bob = Person('Bob Smith', 50000)
    jack = Person('Jack Lin', 160000)
    Person.giveRaise(bob, .25)
    Person.giveRaise(jack, .25)

    bob.giveRaise(.10)
