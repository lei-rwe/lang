# In python 2, classes derived from object are New Style Classes; otherwise
# they are classic classes.
# In python 3, every class is default to New Style Class model
# For New Style Class, the attribute fetch call is like "type(obj).__X__(obj, args);
# while for classic classes, it is like "obj.__X__(args)".
# Reason: 1) Performance; 2) call pattern issue
class A:
    def __add__(self, v):
        return 100 + v

class B(object):
    def __add__(self, v):
        return 1000 + v

if __name__ == '__main__':
    a = A()
    b = B()

    a.__add__ = lambda t : 50 + t
    b.__add__ = lambda t : 500 + t

    print(a + 1)
    print(b + 1)