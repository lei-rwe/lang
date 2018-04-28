import math

for n in range(1, 100, 2):
    for x in range(2, int(math.sqrt(n))+1):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')