class time_5:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args):
        return self.func(*args) * 5

def add_3(F):
    def wrapper(*args):
        print("In decorator add_3")
        return F(*args) + 3
    return wrapper

@add_3
@time_5
def func(x, y):
    return x * y

def tracer(func): # State via enclosing scope and nonlocal
    calls = 0 # Instead of class attrs or global
    def wrapper(*args, **kwargs): # calls is per-function, not global
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c): # Same as: spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y): # Same as: eggs = tracer(eggs)
    print(x ** y)

if __name__ == '__main__':
    print(func(10, 20))

    spam(1, 2, 3) # Really calls wrapper, bound to func
    spam(a=4, b=5, c=6) # wrapper calls spam
    eggs(2, 16) # Really calls wrapper, bound to eggs
    eggs(4, y=4) # Nonlocal calls _is_ per-decoration here
