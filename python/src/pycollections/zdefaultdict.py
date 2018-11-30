from collections import defaultdict
# defaultdict is a subclass of the built-in dict class.
# It overrides one method and adds one writable instance variable.
# The remaining functionality is the same as for the dict
# class and is not documented here.

# Using list as the default_factory, it is easy to group a sequence
# of key-value pairs into a dictionary of lists:
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d.items())

s = 'mississippi'
d = defaultdict(int)
print(d.items())
for k in s:
    d[k] += 1
print(d.items())
