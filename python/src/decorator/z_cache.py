import urllib.request
from functools import lru_cache

def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    with urllib.request.urlopen(url) as f:
        page = f.read()
        saved[url] = page
    return page

@lru_cache(maxsize=None)
def web_lookup_1(url):
    with urllib.request.urlopen(url) as f:
        return f.read()

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# To clear the cache
# fib.cache_clear()

def mycache(func):
    saved = {}
    def newfunc(*args):
        print(args, saved)
        if args in saved:
            return saved[args]
        result = func(*args)
        saved[args] = result
        return result
    return newfunc

@mycache
def mycached_fib(n):
    if n < 2:
        return n
    return mycached_fib(n-1) + mycached_fib(n-2)

if __name__ == '__main__':
    print([mycached_fib(n) for n in range(8)])
    
    # print(web_lookup_1('https://en.wikipedia.org/wiki/Financial_endowment'))