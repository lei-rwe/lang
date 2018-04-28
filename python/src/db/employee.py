class AttrDisplay:
    """
    Provides an inheritable display overload method that shows instances with their class names and a name=value pair for each attribute stored on the instance itself (but not attrs inherited from its classes). Can be mixed into any class, and will work on any instance.
    """
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

class Employee(AttrDisplay):
    count = 0
    def __init__(self, name, job=None, pay=0):
        Employee.count += 1
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Employee):
    def __init__(self, name, pay):
        Employee.__init__(self, name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        Employee.giveRaise(self, percent + bonus)

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

def test_1():
    bob = Employee('Bob Smith')
    sue = Employee('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager("Tom Jones", 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

    print('--All three--')
    for obj in (bob, sue, tom):
        obj.giveRaise(.10)
        print(obj)

def test_2():
    bob = Employee('Bob Smith', pay=50000)
    sue = Employee('Sue Jones', job='dev', pay=100000)
    tom = Manager('Tom Jones', 80000)
    development = Department(bob, sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
    print(Employee.count)

if __name__ == "__main__":
    test_2()
