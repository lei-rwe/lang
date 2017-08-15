from __future__ import print_function

class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "does stuff")

    def __repr__(self):
        return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)

class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 50000)
    def work(self):
        print(self.name, "makes food")

class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 40000)
    def work(self):
        print(self.name, "interfaces with customer")

class PizzaRobot(Chef):
    def __init__(self, name):
        Chef.__init__(self, name)
    def work(self):
        print(self.name, "makes pizza")


class Customer:
    def __init__(self, name):
        self.name = name
    def order(self, server):
        print(self.name, "orders from", server)
    def pay(self, server):
        print(self.name, "pays for item to", server)
class Oven:
    def bake(self):
        print("oven bakes")
class PizzaShop:
    def __init__(self):
        self.server = Server('Pat') # Embed other objects
        self.chef = PizzaRobot('Bob') # A robot named bob
        self.oven = Oven()
    def order(self, name):
        customer = Customer(name) # Activate other objects
        customer.order(self.server) # Customer orders from server
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)

def test1():
    bob = PizzaRobot('bob') # Make a robot named bob
    print(bob) # Run inherited __repr__
    bob.work() # Run type-specific action
    bob.giveRaise(0.20) # Give bob a 20% raise
    print(bob); print()
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()

if __name__ == "__main__":
    scene = PizzaShop() # Make the composite
    scene.order('Homer') # Simulate Homer's order
    print('...')
    scene.order('Shaggy') # Simulate Shaggy's order

