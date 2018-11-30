def onexit(f):
    import atexit
    atexit.register(f)
    return f

@onexit
def func():
    print("in func")

if __name__ == '__main__':
    print('main')