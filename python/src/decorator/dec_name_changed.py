# Decorator的副作用

# 被decorator的函数其实已经是另外一个函数了，
# 对于最前面那个hello.py的例子来说，如果你
# 查询一下foo.__name__的话，你会发现其输出
# 的是“wrapper”，而不是我们期望的“foo”，
# 这会给我们的程序埋一些坑。所以，Python的functool
# 包中提供了一个叫wrap的decorator来消除这样的副作用。
# 下面是我们新版本的hello.py。
from functools import wraps
def hello(fn):
    @wraps(fn)
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)
    return wrapper

@hello
def foo():
    '''foo help doc'''
    print("i am foo")

foo()
print(foo.__name__) #输出 foo
print(foo.__doc__)  #输出 foo help doc