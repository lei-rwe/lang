class Empty:
    def __init__(self):
        # self.name = "Empty"       # This will call __setattr__ !!!
        pass

    def __getattr__(self, item):
        if item == "age":
            return 40
        else:
            raise AttributeError("Not defined")

    def __setattr__(self, key, value):
        if key == "age":
            self.__dict__[key] = value + 10
        else:
            raise AttributeError("Not defined")

class Person(object):
    """
    managed attributes
    """
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

def test1():
    X = Empty()
    print(X.age)

    X.age = 30
    print(X.age)

def test2():
    bob = Person('Bob Smith')
    print(bob.name)
    bob.name = 'Robert Smith'
    print(bob.name)

if __name__ == '__main__':
    test2()
