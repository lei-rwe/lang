# pronounced "deck", in short of "double-ended queue"

from collections import deque

d = deque('ghi')
for elem in d:
    print(elem.upper())

d.append('j')
d.appendleft('f')
print(d)

d.pop()
d.popleft()
print(list(d))

print(list(reversed(d)))
print('h' in d)

d.extend('jkl')
print(d)

d.rotate(1)
print(d)

d.rotate(-1)
print(d)

d = deque(reversed(d))
print(d)

# d.clear()
# d.pop()

d.extendleft('abc')
print(d)
