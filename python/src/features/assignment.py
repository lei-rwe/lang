# Chain assignment: 
def foo():
    return []

x = y = foo()
x.append(4)
print(x)
print(y)

a = foo()
b = foo()
a.append(3)
print(a)
print(b)

import random
u = v = random.random()
print(u)
print(v)

A = [1, 2, 3]
t = 2
t = A[t] = A.count(3)
print(A)
print(t)