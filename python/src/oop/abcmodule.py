from abc import ABC, ABCMeta, abstractmethod

class animal:
    __metaclass__ = ABCMeta
    @abstractmethod
    def eat(self):
        print('animal.eat()')

class shape(ABC):
    @abstractmethod
    def draw(self):
        print('shape.draw')

class circle(shape):
    def draw(self):
        print('circle.draw')

class base(ABC):
    @abstractmethod
    def abmthd(self):
        pass

if __name__ == '__main__':
    obj = animal()
    obj.eat()

    try:
        obj = shape()
    except TypeError as ex:
        print(ex)

    obj = circle()
    obj.draw()

    try:
        obj = base()
    except TypeError as ex:
        print(ex)
