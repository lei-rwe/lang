# There are two ways to force the constraint from base to derived
# 1. meta-class: A class that derives from "type", which allow you
#    to intercept the construction of derived types

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('BaseMeta.__new__', cls, name, bases, body)
        import pdb; pdb.set_trace()
        if name != 'Base' and not 'bar' in body:
            raise TypeError('bad user class implementation')
        return super().__new__(cls, name, bases, body)

class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

class Derived(Base):
    def bar(self):
        print('Derived.bar')
        return 'bar'

# Run above code:
# python -i ep_meta.py
# BaseMeta.__new__ <class '__main__.BaseMeta'> Base () {'__module__': '__main__', '__qualname__': 'Base', 'foo': <function Base.foo at 0x000002604D37F0D0>}
# BaseMeta.__new__ <class '__main__.BaseMeta'> Derived (<class '__main__.Base'>,) {'__module__': '__main__', '__qualname__': 'Derived', 'bar': <function Derived.bar at 0x000002604D37F1E0>}
