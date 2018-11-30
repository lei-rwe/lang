from collections import namedtuple

# Basic example
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)     # instantiate with positional or keyword arguments
print(p[0] + p[1])      # indexable like the plain tuple (11, 22)

x, y = p                # unpack like a regular tuple
print(x, y)

print(p.x + p.y)        # fields also accessible by name
print(p)                # readable __repr__ with a name=value style

# Since a named tuple is a regular Python class, it is easy to
# add or change functionality with a subclass. Here is how to
# add a calculated field and a fixed-width print format:

class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Point(3, 4), Point(14, 5/7):
    print(p)

# Subclassing is not useful for adding new, stored fields.
# Instead, simply create a new named tuple type from the _fields attribute:

Point3D = namedtuple('Point3D', Point._fields + ('z',))