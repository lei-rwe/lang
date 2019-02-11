import inspect
import time
from functools import wraps

def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        ts = time.time()
        result = fn(*args, **kwargs)
        te = time.time()
        print("function      = {0}".format(fn.__name__))
        print("    arguments = {0} {1}".format(args, kwargs))
        print("    return    = {0}".format(result))
        print("    time      = %.6f sec" % (te-ts))
        return result
    return wrapper

@logger
def multipy(x, y):
    return x * y

@logger
def sum_num(n):
    s = 0
    for i in range(n+1):
        s += i
    return s

print(multipy(2, 10))
print(sum_num(100))
print(sum_num(10000000))

# 看一个更好一点的（带log level参数的）
def get_line_number():
    return inspect.currentframe().f_back.f_back.f_lineno

def logger(loglevel):
    def log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = fn(*args, **kwargs)
            te = time.time()
            print("function   = " + fn.__name__,)
            print("    arguments = {0} {1}".format(args, kwargs))
            print("    return    = {0}".format(result))
            print("    time      = %.6f sec" % (te-ts))
            if (loglevel == 'debug'):
                print("    called_from_line : " + str(get_line_number()))
            return result
        return wrapper
    return log_decorator


def advance_logger(loglevel):

    def get_line_number():
        return inspect.currentframe().f_back.f_back.f_lineno

    def _basic_log(fn, result, *args, **kwargs):
        print("function   = " + fn.__name__,)
        print("    arguments = {0} {1}".format(args, kwargs))
        print("    return    = {0}".format(result))

    def info_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            _basic_log(fn, result, args, kwargs)
        return wrapper

    def debug_log_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = fn(*args, **kwargs)
            te = time.time()
            _basic_log(fn, result, args, kwargs)
            print("    time      = %.6f sec" % (te-ts))
            print("    called_from_line : " + str(get_line_number()))
        return wrapper

    if loglevel is "debug":
        return debug_log_decorator
    else:
        return info_log_decorator