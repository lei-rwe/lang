from abc import ABCMeta, abstractmethod, abstractproperty

class Animal(object):
    __metaclass__ = ABCMeta

    def __init__(self, name):
        self._name = name

    @abstractmethod
    def eat(self):
        print(self._name, "Animal::eat")

    def getName(self):
        print("Animal::getName")
        return self._name
    def setName(self, value):
        print("Animal::setName")
        self._name = value
    def delName(self, value):
        print("Animal::delName")
        del self._name
    name = property(getName, setName, delName)

class Cat(Animal):
    def eat(self):
        super(Cat, self).eat()
        print(self._name, "Cat::eat")

if __name__ == "__main__":
    olivia = Cat("Olivia")
    olivia.eat()
    print(olivia.name)

    jack = Cat("Jack")
    jack.eat()
    print(jack.name)
