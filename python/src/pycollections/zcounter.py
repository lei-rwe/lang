# Counter: dict subclass for counting hashable objects
from collections import Counter

cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
l = Counter(words).most_common(10)
print(l)

c = Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

print(Counter('abracadabra').most_common(3))

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
print(c)

c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
print(c + d)
