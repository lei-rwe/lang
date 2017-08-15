from abc import ABCMeta, abstractmethod, abstractproperty

class animal:
    __metaclass__ = ABCMeta
    @abstractmethod
    def eat():
        pass

if __name__ == '__main__':
    obj = animal()
