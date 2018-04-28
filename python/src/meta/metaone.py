class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print("In MetaOne::__new__", meta, classname, supers, classdict)
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print("In MetaOne::__init__", classname, supers, classdict)
        print(Class.__dict__.keys())

def MetaFunc(classname, supers, classdict):
    print("MetaFunc:")
    print("classname:", classname)
    print("supers:", supers)
    print("classdict:", classdict)
    return type(classname, supers, classdict)

class MetaObj(type):
    def __call__(self, classname, supers, classdict):
        print('In MetaObj.call: ', classname, supers, classdict)
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class
    def __New__(self, classname, supers, classdict):
        print('In MetaObj.New: ', classname, supers, classdict)
        return type(classname, supers, classdict)
    def __Init__(self, Class, classname, supers, classdict):
        print('In MetaObj.Init:', classname, supers, classdict)
        print('...init class object:', list(Class.__dict__.keys()))

class Egg(object):
    pass

class Spam(Egg):
    __metaclass__ = MetaObj
    data = 1
    def method(self, arg):
        print(self.data, arg)

def test_1():
    x = Spam()
    x.method(15)

class M1(type): attr1 = 1
class M2(M1):
    attr2 = 2
class C1(object):
    attr3 = 3
class C2(C1):
    __metaclass__ = M2
    attr4 = 4

def test_2():
    I = C2()
    print(I.attr1, I.attr2, I.attr3, I.attr4)

    print(C2.attr1, C2.attr2, C2.attr3, C2.attr4)
    print(M2.attr1, M2.attr2)

if __name__ == "__main__":
    test_1()
