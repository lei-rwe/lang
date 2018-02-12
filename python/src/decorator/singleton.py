from ctypes.test.test_pickling import name
from audioop import ratecv
def singleton(aClass): # On @ decoration
    instances = {}
    def onCall(*args, **kwargs): # On instance creation
        nonlocal instances
        if aClass not in instances: # One dict entry per class
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall

@singleton
class Person:
    def __init__(self, name, hour, rate):
        self.name = name
        self.hour = hour
        self.rate = rate
    def pay(self):
        return self.rate * self.hour

@singleton
class Spam:
    def __init__(self, val):
        self.attr = val

if __name__ == '__main__':
    bob = Person('Bob', 40, 10)
    print(bob.name, ': ', bob.pay())

    sue = Person('Sue', 40, 10)
    print(sue.name, ': ', sue.pay())