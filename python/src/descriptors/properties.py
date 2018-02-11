class Person: # Add (object) in 2.X
    def __init__(self, name):
        self._name = name
    def getName(self):
        print('fetch...')
        return self._name
    def setName(self, value):
        print('change...')
        self._name = value
    def delName(self):
        print('remove...')
        del self._name
    name = property(getName, setName, delName, "name property docs")


class properties(object):
    @property
    def age(self):
        print("property age")
        return self._age_

    @age.setter
    def age(self, v):
        print("set property age")
        self._age_ = v

if __name__ == '__main__':
    o = properties()
    o.age = 30
    print(o.age)

    bob = Person('Bob Smith') # bob has a managed attribute
    print(bob.name) # Runs getName
    bob.name = 'Robert Smith' # Runs setName
    print(bob.name)
    print(Person.name)        # This will print a <Property object>
    del bob.name # Runs delName

    print('-'*20)
    sue = Person('Sue Jones') # sue inherits property too
    print(sue.name)
    print(Person.name)        # This will print a <Property object>
    print(Person.name.__doc__) # Or help(Person.name)
