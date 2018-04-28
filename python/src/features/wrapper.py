class Wrapper:
    def __init__(self, object):
        self.wrapped = object
    def __getattr__(self, attrname):
        print('Wrapper Trace: ' + attrname)
        return getattr(self.wrapped, attrname)

# https://docs.python.org/3/whatsnew/2.5.html
def my_decorator(f):
    import functools

    @functools.wraps(f)
    def wrapper(*args, **kwds):
        print 'Calling decorated function:', f.__name__
        print args
        print kwds
        return f(*args, **kwds)
    return wrapper

@my_decorator
def foo(i):
    pass

if __name__ == '__main__':
    x = Wrapper([1,2,3])
    x.append(5)
    print x

    foo(10)
