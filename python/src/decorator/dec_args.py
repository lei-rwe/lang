# 用Decorator设置函数的调用参数

# 你有三种方法可以干这个事：

# 第一种，通过 **kwargs，这种方法decorator会在kwargs中注入参数

def decorate_A(function):
    def wrap_function(*args, **kwargs):
        kwargs['str'] = 'Hello!'
        return function(*args, **kwargs)
    return wrap_function

@decorate_A
def print_message_A(*args, **kwargs):
    print(kwargs['str'])

print_message_A()

# 第二种，约定好参数，直接修改参数

def decorate_B(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        return function(str, *args, **kwargs)
    return wrap_function

@decorate_B
def print_message_B(str, *args, **kwargs):
    print(str)

print_message_B()

# 第三种，通过 *args 注入

def decorate_C(function):
    def wrap_function(*args, **kwargs):
        str = 'Hello!'
        #args.insert(1, str)
        args = args +(str,)
        return function(*args, **kwargs)
    return wrap_function

class Printer:
    @decorate_C
    def print_message(self, str, *args, **kwargs):
        print(str)

p = Printer()
p.print_message()