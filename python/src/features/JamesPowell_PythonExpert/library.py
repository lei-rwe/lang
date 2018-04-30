# You have no idea how this library code will be used by the users
# and you will have no way to modify users' code.
# How can you make sure that users using your library implemented
# the method that you call in the library?

class Base:
    def foo(self):
        print('In base.foo')
        return 'foo'

    def req(self):
        print('In base.req')
        return self.imp_by_user()   # How to make sure imp_by_user() is implemented by derived?

    # Python is a much much simper language than you can imagine
    # The following code are syntax correct
    # Pretty much every line of code is executable
    def junk(self):
        for _ in range(10):
            class Junk: pass

        class JJunk:
            for _ in range(10):
                def bar(self):
                    pass

# How to intersect the class construction process?
# Method 1: use __build_class__
# Method 2: use metaclass, see ep_meta.py
# Method 3: use __init_subclass__, see ep_is.py

def for_dis():
    class MyBase:
        pass

# python -i .\library.py
# >>> from dis import dis
# >>> dis(for_dis)
#  28           0 LOAD_BUILD_CLASS
#               2 LOAD_CONST               1 (<code object MyBase at 0x00000132D0284C90, file ".\library.py", line 28>)
#               4 LOAD_CONST               2 ('MyBase')
#               6 MAKE_FUNCTION            0
#               8 LOAD_CONST               2 ('MyBase')
#              10 CALL_FUNCTION            2
#              12 STORE_FAST               0 (MyBase)
#              14 LOAD_CONST               0 (None)
#              16 RETURN_VALUE

old_bc = __build_class__
def my_bc(func, name, base=None, **kwargs):
    print('my buildclas -> ', func, name, base, kwargs)
    if base is Base:
        print("Check if imp_by_user method defined")
    if base is not None:
        return old_bc(func, name, base, **kwargs)
    else:
        return old_bc(func, name, **kwargs)

import builtins
builtins.__build_class__ = my_bc

# If you run python -i user.py, you will get
# my buildclas ->  (<function Derived at 0x00000192855C3E18>, 'Derived', <class 'library.Base'>) {}
# In base.foo
# In base.req
# Derived.imp_by_user()

