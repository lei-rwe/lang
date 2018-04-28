def fib(n):
    a, b = 0, 1
    while (a < n):
        print(a)
        a, b = b, a+b

def fib_gen(n):
    a, b = 0, 1
    while ( a < n ):
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    # fib(1000)
    print([x for x in fib_gen(1000)])

