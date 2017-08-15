class A(object):
    def __init__(self, id):
        print("A::__init__")
        self.id = id
    def __del__(self):
        print("A::__del__ with id: ", self.id)

def test1():
    a = A(1)

def test2():
    a = A(2)

if __name__ == "__main__":
    test1()
    test2()
