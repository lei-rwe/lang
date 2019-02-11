def cache(f):
    mem = {}
    def wrap(arg):
        if arg in mem:
            print("find {} -> {}".format(arg, mem[arg]))
            return mem[arg]
        else:
            v = f(arg)
            mem[arg] = v
            return v
    return wrap

@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    print(fib(10))

