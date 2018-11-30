import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n %i for i in range(3, int(math.sqrt(n))+1, 2))

# Find prime numbers that are 1 away from being divisible by 5
o = list(filter(lambda x: (not (x+1)%5 or not (x-1)%5) and is_prime(x), range(1, 10**4)))
print(o)
