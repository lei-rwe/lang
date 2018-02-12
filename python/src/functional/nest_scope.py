X = 99 # Global scope name: not used
def f1():
    X = 88 # Enclosing def local
    def f2():
        nonlocal X
        print(X) # Reference made in nested def
    f2()
f1() # Prints 88: enclosing def local