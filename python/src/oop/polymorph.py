class Animal(object):
    from abc import ABCMeta, abstractmethod, abstractproperty
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, name):
        print("Animal.__init__")
        print(self)
        self._name_ = name

    @abstractmethod
    def eat(self):
        print("Animal.eat")

    @property
    def name(self):
        return self._name_

    def tryme(self):
        print(self._name_)

class Dog(Animal):
    def __init__(self, name):
        print("Dog.__init__")
        print(self)
        Animal.__init__(self, name)

    def eat(self):
        print("Dog.eat")
        Animal.eat(self)

if __name__ == "__main__":
    obj = Dog("Terry")
    obj.eat()
    print(obj.name)
    obj.tryme()
