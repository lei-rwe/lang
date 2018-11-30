import time

def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('Method %r ran %2.2f ms' % (f.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def foo(n):
    for i in range(n):
        time.sleep(0.5)
        print(i)

if __name__ == '__main__':
    foo(5)