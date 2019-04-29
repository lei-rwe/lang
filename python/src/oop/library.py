import pdb
class Base:
    def __init_subclass__(self, *arg, **kw):
        print(arg, kw)
        return super().__init_subclass__(*arg, **kw)

    def foo(self):
        print("Base.foo")
        self.bar()


old_bc = __build_class__

def my_bc(func, name, base=None, **kw):
    pdb.set_trace()
    print("my buildclass ->", kw)
    if base is Base:
        print("check if bar() defined")
        assert hasattr(Base, "bar"), "You break it, fool"
    if base is not None:
        return old_bc(func, name, base, **kw)
    return old_bc(func, name, **kw)

import builtins
builtins.__build_class__ = my_bc
