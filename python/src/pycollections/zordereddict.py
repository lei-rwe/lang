from collections import OrderedDict

# Ordered dictionaries are just like regular dictionaries
# but they remember the order that items were inserted.
# When iterating over an ordered dictionary, the items
# are returned in the order their keys were first added.

# Since an ordered dictionary remembers its insertion order,
# it can be used in conjunction with sorting to make a sorted dictionary:

# regular unsorted dictionary
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
o = OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print(o)

# dictionary sorted by value
p = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
print(p)

# dictionary sorted by length of the key string
q = OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
print(q)

# The new sorted dictionaries maintain their sort order
# when entries are deleted. But when new keys are added,
# the keys are appended to the end and the sort is not maintained.