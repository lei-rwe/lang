import math

def primes():
    for n in range(1, 100, 2):
        for x in range(2, int(math.sqrt(n))+1):
            if n % x == 0:
                print(n, 'equals', x, '*', n/x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

def prime_gen(m):
    for n in range(2, m):
        # print("Checking ", n)
        for p in range(2, int(math.sqrt(n))+1):
            if n % p == 0:
                break
        else:
            # print("Found ", n)
            yield n

if __name__ == '__main__':
    print(tuple(prime_gen(500)))
