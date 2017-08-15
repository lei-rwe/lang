'''
PEP 318
https://www.python.org/dev/peps/pep-0318/
'''
def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class MyClass:
    def foo(self, v):
        self.data = v

x = MyClass()
y = MyClass()

x.foo(100)
print x.data
print y.data



class Singleton(object):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton,cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):      
        if(self.__initialized): return
        self.__initialized = True
        print ("INIT")

a = Singleton()
b = Singleton()
print (a is b)


class Foo(object):
    pass

def foo_singleton_factory(_singleton = Foo()):
    return _singleton

a = foo_singleton_factory()
b = foo_singleton_factory()
print (a is b)


