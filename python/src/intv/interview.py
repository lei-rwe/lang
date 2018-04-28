def print_directory(dir):
    import os
    for item in os.listdir(dir):
        path = os.path.join(dir, item)
        if os.path.isdir(path):
            print_directory(path)
        else:
            print path


def test_list_comp():
    A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    A1 = range(10)
    A2 = sorted([i for i in A1 if i in A0])
    A3 = sorted([A0[s] for s in A0])
    A4 = [i for i in A1 if i in A3]
    A5 = {i:i*i for i in A1}
    A6 = [[i,i*i] for i in A1]

    print A0
    print A1
    print A2
    print A3
    print A4
    print A5
    print A6

def test_default_args():
    def f(x,l=[]):
        for i in range(x):
            l.append(i*i)
        print(l)
    f(2)
    f(3,[3,2,1])
    f(3)


def test_default_args_ref():
    l_mem = []

    l = l_mem           # the first call
    for i in range(2):
        l.append(i*i)

    print(l)            # [0, 1]

    l = [3,2,1]         # the second call
    for i in range(3):
        l.append(i*i)

    print(l)            # [3, 2, 1, 0, 1, 4]

    l = l_mem           # the third call
    for i in range(3):
        l.append(i*i)

    print(l)            # [0, 1, 0, 1, 4]


def test_args():
    def f(*args,**kwargs): print(args, kwargs)

    l = [1,2,3]
    t = (4,5,6)
    d = {'a':7,'b':8,'c':9}

    f()
    f(1,2,3)                    # (1, 2, 3) {}
    f(1,2,3,"groovy")           # (1, 2, 3, 'groovy') {}
    f(a=1,b=2,c=3)              # () {'a': 1, 'c': 3, 'b': 2}
    f(a=1,b=2,c=3,zzz="hi")     # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
    f(1,2,3,a=1,b=2,c=3)        # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}

    f(*l,**d)                   # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
    f(*t,**d)                   # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
    f(1,2,*t)                   # (1, 2, 4, 5, 6) {}
    f(q="winning",**d)          # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    f(1,2,*t,q="winning",**d)   # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

    def f2(arg1,arg2,*args,**kwargs): print(arg1,arg2, args, kwargs)

    f2(1,2,3)                       # 1 2 (3,) {}
    f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
    f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
    f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
    f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}

    f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
    f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
    f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
    f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

def test_overloading():
    def f(b):
        print "Only one argument: ", b
    def f(a, b=3, c=1):
        print "three arguments: ", a, b, c

    f(5)
    f(4, 3)

def frange(start, stop, step):
    i = start
    while i < stop - step / 1000.0:
        yield i
        i += step

def test_frange():
    print [i for i in frange(0.5, 1.0, 0.1)]

if __name__ == "__main__":
    # import sys
    # print_directory(sys.argv[1])
    test_list_comp()
    test_default_args()
    test_default_args_ref()
    test_args()
    test_overloading()
    test_frange()
