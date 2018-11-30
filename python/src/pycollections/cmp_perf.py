# https://stackoverflow.com/questions/6256983/how-are-deques-in-python-implemented-and-when-are-they-worse-than-lists
# How deque is implemented?

import time
from collections import deque

num = 100000

def append(c):
    for i in range(num):
        c.append(i)

def appendleft(c):
    if isinstance(c, deque):
        for i in range(num):
            c.appendleft(i)
    else:
        for i in range(num):
            c.insert(0, i)
def pop(c):
    for i in range(num):
        c.pop()

def popleft(c):
    if isinstance(c, deque):
        for i in range(num):
            c.popleft()
    else:
        for i in range(num):
            c.pop(0)

for container in [deque, list]:
    for operation in [append, appendleft, pop, popleft]:
        c = container(range(num))
        start = time.time()
        operation(c)
        elapsed = time.time() - start
        print("Completed %s/%s in %.2f seconds: %.1f ops/sec" % (container.__name__,
                operation.__name__, elapsed, num / elapsed))
