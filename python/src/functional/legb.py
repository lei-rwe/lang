X = 10
def foo():
    print(X)    # Here it will throw exception
    X = 11
    print(X)

def bar():
    global y
    y = 100

def bar1():
    print(y)

if __name__ == '__main__':
    bar()
    y = 1000
    bar1()