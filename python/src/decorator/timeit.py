'''
Created on Jul 3, 2017

@author: lzhang938
'''

import time

def timeit(f):
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', f.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print('%r  %2.2f ms' % (f.__name__, (te - ts) * 1000))
        return result
    return timed

@timeit
def foo(n):
    for i in range(n):
        time.sleep(0.5)
        print(i)

if __name__ == '__main__':
    foo(5)