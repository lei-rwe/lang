from time import sleep
from time import time

def timer(func):
    def f(*args, **kwargs):
        before = time()
        rv = func(*args, **kwargs)
        after = time()
        print('Elapsed: ', after - before)
        return rv
    return f

def add1(x, y):
    return x + y

class Adder:
    def __call__(self, x, y):
        return x + y
add2 = Adder()

print('add1(10, 20)', add1(10, 20))
print('add2(10, 20)', add2(10, 20))

@timer
def compute():
    rv = []
    for i in range (10):
        sleep(.5)
        rv.append(i)
    return rv

class Compute:
    def __call__(self):
        rv = []
        for i in range (10):
            sleep(.5)
            rv.append(i)
        return rv
# comp = Compute()
# print(comp())

# How can we enhance the class to iterator once with one call?
class ComputeIter:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        if self.last >= 10:
            raise StopIteration()
        sleep(.5)
        rv = self.last
        self.last += 1
        return rv

for x in ComputeIter():
    print(x)
