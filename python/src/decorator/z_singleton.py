def singleton(cls): # On @ decoration
    instances = {}
    def getinstance(*args, **kwargs): # On instance creation
        nonlocal instances
        if cls not in instances: # One dict entry per class
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getinstance

@singleton
class Person:
    def __init__(self, name, hour, rate):
        print("Person.__init__")
        self.name = name
        self.hour = hour
        self.rate = rate
    def pay(self):
        return self.rate * self.hour

if __name__ == '__main__':
    bob = Person('Bob', 40, 10)
    print(bob.name, ': ', bob.pay())

    # This will not create another instance
    sue = Person('Sue', 40, 10)
    print(sue.name, ': ', sue.pay())