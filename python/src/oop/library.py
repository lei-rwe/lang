import pdb
class Base:
    def __init_subclass__(self, *arg, **kw):
        print(arg, kw)
        return super().__init_subclass__(*arg, **kw)

    def foo(self):
        print("Base.foo")
        self.bar()
