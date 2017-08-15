def fibonacci(n, first=0, second=1):
    while n != 0:
            print(first) # side-effect
            n, first, second = n - 1, second, first + second # assignment
fibonacci(10)
