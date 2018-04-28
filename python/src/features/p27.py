import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point: ' + str(self.__dict__)

def add(a, b):
    return Point(a.x+b.x, a.y+b.y)

def sub(a, b):
    return Point(a.x-b.x, a.y-b.y)

def wrapper(func):
    def checker(a, b):
        if a.x < 0 or a.y < 0:
            a = Point(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        if b.x < 0 or b.y < 0:
            b = Point(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        ret = func(a, b)
        if ret.x < 0 or ret.y < 0:
            ret = Point(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
        return ret

    return checker


class Counter:
    Count = 0 # This represents the count of objects of this class
    def __init__(self, name):
        self.name = name
        print(name, 'created')
        Counter.Count += 1
    def __del__(self):
        print(self.name, 'deleted')
        Counter.Count -= 1
        if Counter.Count == 0:
            print('Last Counter object deleted')
        else:
            print(Counter.Count, 'Counter objects remaining')

if __name__ == '__main__':
    one = Point(100, 200)
    two = Point(300, 400)
    print(add(one, two))
    x = Counter("First")
    # del x
