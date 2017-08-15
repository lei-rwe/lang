'''
By assigning a sequence of string attribute names to
a special __slots__ class attributes,
we can enable new-style class to both limit the set of
legal attributes that instances of the class will have,
and optimize memory usage and possibly program speed.

To quote the manual, slots "best reserved for rare cases
where there are large numbers of instances in a
memory critical application". In other words,
this is yet another feature that should be used
only if clearly warranted.

Slots and namespace dictionaries
To be clear: this is a major incompatibility with the
traditional class model.

__slots__ means no __dict__ by default. But we can still
accommodate extra attributes by
including __dict__ explicitly in __slots__:
'''
class D:
    __slots__ = ['a', 'b', '__dict__']  # Name __dict__ to include one too
    c = 3                               # Class attrs work normally
    def __init__(self):
        self.d = 4                      # d stored in __dict__, a is a slot

obj = D()
print(obj.d)
print(obj.c)
print(obj.__dict__)


class Slotful:
    __slots__ = ['a', 'b', '__dict__']
    def __init__(self, data):
        self.c = data
s = Slotful(3)
print(dir(s))
l = [x for x in dir(s) if not x.startswith('__')]
print(l)
