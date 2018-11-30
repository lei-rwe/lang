class Color:
    def __init__(self):
        print('Color.__init__')
        self.color = None

    def __get__(self, instance, owner):
        print('Color.__get__')
        print(self, instance, owner, sep='\n')
        return self.color

    def __set__(self, instance, value):
        print('Color.__set__')
        print(self, instance, value, sep='\n')
        self.color = value

class Toy:
    color = Color()

    def __init__(self):
        print('Toy.__init__')
        self.name = None
        self.owner = None

def main():
    print('Main')
    toy = Toy()
    toy.color = 'White'
    print(toy.color)


class Person: # Use (object) in 2.X
    def __init__(self, name):
        self._name = name

    class Name: # Use (object) in 2.X
        "name descriptor docs"
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name
        def __set__(self, instance, value):
            print('change...')
            instance._name = value
        def __delete__(self, instance):
            print('remove...')
            del instance._name

    name = Name() # Assign descriptor to attr

def main_2():
    bob = Person('Bob Smith') # bob has a managed attribute
    print(bob.name) # Runs Name.__get__
    bob.name = 'Robert Smith' # Runs Name.__set__
    print(bob.name)
    del bob.name # Runs Name.__delete__

    print('-'*20)
    sue = Person('Sue Jones') # sue inherits descriptor too
    print(sue.name)
    print(Person.Name.__doc__) # Or help(Name)

if __name__ == '__main__':
    main_2()

