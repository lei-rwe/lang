def onexit(f):
    import atexit
    atexit.register(f)
    return f

@onexit
def myexit():
    print("In function myexit")

def foo():
    print("In function foo")
    raise Exception("I manually raised an exception")

foo()
