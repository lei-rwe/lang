class Squares_1:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop: raise StopIteration
        self.value += 1
        return self.value ** 2
    next = __next__

class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        # __iter__ + yield generator
        # __next__ is automatic/implied
        for value in range(self.start, self.stop + 1):
            yield value ** 2
            print("Finished Value:", value)


def test_1():
    for i in Squares(1,5):
        print(i)

    it = iter(range(0, 10))
    print(zip(it, it))

def test_2():
    S = Squares(1, 3)
    for i in S: # Each for calls __iter__
        for j in S:
            print('%s:%s' % (i, j))

if __name__ == '__main__':
    import sys
    sys.exit(test_2())
